# Skills Index

This directory is the central index for agent skills in this repository.

## Purpose

Use this file to list every skill under `skills/` so ChatGPT, Codex, Claude Code, OpenCode, and other coding agents can discover and maintain them without needing directory listing support.

## Current Skills

> Add each skill here when created or imported.

| Skill | Path | Purpose | Status |
|---|---|---|---|
| _TBD_ | _TBD_ | _TBD_ | draft |

## Recommended Skill Layout

Each skill should usually follow this structure:

```text
skills/<skill-name>/SKILL.md
skills/<skill-name>/README.md      # optional
skills/<skill-name>/examples/      # optional
```

## Maintenance Rules

- Keep this index updated whenever a skill is added, renamed, moved, or deleted.
- Prefer concise `SKILL.md` files over long explanations.
- Put reusable behavior rules in `SKILL.md`.
- Put background notes, examples, and rationale in optional README or examples files.
- When adapting a skill for multiple agents, keep the core rules agent-neutral unless the skill is explicitly agent-specific.
