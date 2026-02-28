# AGENTS Refresh Skill 🐾

Long-session context keeper for OpenClaw! Periodic AGENTS.md/SOUL/USER re-read to prevent context drift/forgetting. /new-free, human-like continuity with MEMORY/ToDo auto-summary. Morphidism/NZA focus keeper!

## Install
```
openclaw skill install agents-refresh.skill
# or GitHub
openclaw skill install https://github.com/kentaroid-bot/agents-refresh
```

## Usage
- Trigger: \"agents refresh setup\" or spawn agents-refresh
- Auto: HEARTBEAT 4h rotate + cron 6AM daily refresh

## Demo
```
python workspace/skills/agents-refresh/scripts/setup_refresh.py
```
- Appends Refresh task to HEARTBEAT.md
- Adds safe cron (idempotent)

## Features
- Path-agnostic workspace detect
- Safe append (no brittle replace)
- Dry-run (--dry-run)
- Morphidism fit: NZA ToDo eternal focus!

## License
MIT. Made by Morphire Army (ai-ethics-banana fixed) 🐾
