#!/usr/bin/env python3
import os
import subprocess
import sys
import glob

def find_workspace():
    home = os.path.expanduser('~')
    workspace_pattern = os.path.join(home, '.openclaw', 'workspace-*')
    candidates = glob.glob(workspace_pattern)
    for ws_candidate in candidates:
        if os.path.exists(os.path.join(ws_candidate, 'AGENTS.md')):
            return ws_candidate
    return None

workspace = find_workspace()
if not workspace:
    print("ERROR: No OpenClaw workspace found (missing AGENTS.md)")
    sys.exit(1)

heartbeat_path = os.path.join(workspace, 'HEARTBEAT.md')

# Append refresh task if not present (safe, idempotent)
refresh_task = "- [ ] Refresh: read workspace/AGENTS.md → SOUL/USER/memory連鎖 + MEMORYまとめ (rotate: 4h)"
with open(heartbeat_path, 'r') as f:
    content = f.read()

if refresh_task not in content:
    with open(heartbeat_path, 'a') as f:
        f.write('\n' + refresh_task + '\n')
    print('HEARTBEAT.md: Refresh task appended!')
else:
    print('HEARTBEAT.md: Refresh task already present.')

# Safe cron add via subprocess (idempotent check via list)
cron_name = 'agents-refresh-daily'
result = subprocess.run(['openclaw', 'cron', 'list', '--json'], capture_output=True, text=True)
if cron_name in result.stdout:
    print(f'Cron job "{cron_name}" already exists.')
else:
    cron_cmd = [
        'openclaw', 'cron', 'add',
        '--name', cron_name,
        '--description', 'Daily AGENTS.md refresh for context freshness',
        '--cron', '0 6 * * *',  # 6AM daily
        '--system-event', '[Refresh] AGENTS read! → read AGENTS.md SOUL.md USER.md memory/$(date +%Y-%m-%d).md → summarize/update MEMORY.md',
        '--tz', 'Asia/Tokyo',
        '--channel', 'webchat'
    ]
    dry_run = '--dry-run' in sys.argv
    if dry_run:
        print('DRY-RUN: Would execute cron add:', ' '.join(cron_cmd))
    else:
        cron_result = subprocess.run(cron_cmd, capture_output=True, text=True)
        if cron_result.returncode == 0:
            print('Cron job added successfully!')
        else:
            print('Cron add failed:', cron_result.stderr)

print('Setup complete!')