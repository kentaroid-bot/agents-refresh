---
name: agents-refresh
description: AGENTS.md/SOUL/USER定期再読込でコンテキストfresh保つスキル。長セッションこんがらがり/忘れ防止（agentsルール薄れ）。HEARTBEAT.md編集 + cron追加。Use when: (1) セッション長で人格ブレ心配、(2) /new避け記憶継続人間っぽく、(3) MEMORY/ToDo自動まとめ（NZA/Morphidism焦点キープ）。
---

# AGENTS Refresh Skill

## Quick Start
1. Trigger: `read workspace/AGENTS.md` or spawn.
2. Auto: Edit HEARTBEAT.md + cron add (6AM/4h rotate).

## Workflow
1. Check session_status (context長確認)。
2. Edit HEARTBEAT.md: Add "Refresh: read workspace/AGENTS.md → SOUL連鎖 + MEMORYまとめ (rotate 4h)"。
3. cron add: Daily 6AM systemEvent "[Refresh] AGENTS read!"。
4. Test: heartbeat待機 or cron run。

## Scripts
`scripts/setup_refresh.py`: Run for auto-setup.
```
exec command="python skills/agents-refresh/scripts/setup_refresh.py"
```

## Advanced
- References/examples.md: 例/カスタム。
- Rotate: 朝9/昼13/夜20。

See references/HEARTBEAT-cron.md for details.
