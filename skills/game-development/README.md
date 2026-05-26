# Game Development Skills

This folder packages the converted Claude Code Game Studios skills for game-development workflows.

Source: https://github.com/Donchitos/Claude-Code-Game-Studios.git
Source commit inspected: 984023ddac0d5e27624f2baacde6105e45de375f

Layout:
- `ccgs-*`: converted slash-command skills.
- `ccgs-agent-*`: converted Claude agent roles as Codex skills.

Notes:
- Claude-specific frontmatter fields such as model, allowed-tools, hooks, memory, and disallowedTools were omitted during conversion.
- Existing non-game skills remain in `skills/`.
- The old repository-root `debug-repair-collective/` duplicate was removed; keep `skills/debug-repair-collective/` as the installable skill copy.
