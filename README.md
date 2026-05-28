# debug

AI agent skills collection for coding, research, debugging, and execution-control workflows.

本倉庫用來集中管理可被 AI Agent / Codex / Claude Code / Cursor 類工具讀取的 Skills。  
所有正式技能都放在小寫 `skills/` 目錄下，每個技能以獨立資料夾管理，主要入口為 `SKILL.md`。

## Repository Structure

```text
.
├── README.md
├── .gitignore
└── skills/
    ├── agent-miranda/
    │   └── SKILL.md
    ├── debug-repair-collective/
    │   └── SKILL.md
    ├── lesson-before-invention/
    │   └── SKILL.md
    └── twinkle-hub-mcp-researcher/
        └── SKILL.md
```

## Skills Overview

| Folder | Skill Name | Purpose |
| --- | --- | --- |
| `skills/lesson-before-invention/` | `precedent-first` | Research-before-design protocol. Search external successful precedents before inventing new solutions. |
| `skills/agent-miranda/` | `right-to-silence` | Silent execution mode. Stop over-explaining, act directly, ask only when blocked, and report final results. |
| `skills/debug-repair-collective/` | `debug-repair-collective` | Bug reproduction, diagnosis, repair, verification, security review, fuzzing, and hardening workflow. |
| `skills/twinkle-hub-mcp-researcher/` | `twinkle-hub-mcp-researcher` | Twinkle Hub MCP integration guide for Taiwan-specific datasets, public records, company data, statistics, and citation-grounded research. |

## Usage Philosophy

These skills are designed around four main principles:

1. **Do not invent blindly**  
   Before designing a new solution, search for working precedents and reuse proven patterns when appropriate.

2. **Act, do not narrate endlessly**  
   For execution tasks, the agent should minimize filler, avoid unnecessary planning text, and focus on completing the task.

3. **Debug through feedback loops**  
   Reproduce the issue, inspect evidence, patch carefully, and verify the result instead of only giving advice.

4. **Use external retrieval when facts matter**  
   For Taiwan-specific public data or factual research, use Twinkle Hub MCP or other grounded tools instead of hallucinating.

## Skill Details

### `lesson-before-invention` / `precedent-first`

Use when the task requires design, architecture, protocol writing, skill creation, or implementation strategy.  
The agent should first look for successful existing examples, extract their patterns, then adapt them to the current repo.

Typical triggers:

- 「參考別人的」
- 「不要自己亂想」
- 「有成功案例就借鑑」
- “Find precedent first”
- “Don't reinvent the wheel”

### `agent-miranda` / `right-to-silence`

Use when the user wants the agent to stop explaining and directly execute.  
The agent should avoid verbose narration, avoid unnecessary permission-checking, and only ask questions when genuinely blocked.

Typical triggers:

- 「直接做」
- 「不要說明」
- 「緘默權」
- “silent mode”
- “no talk just do”

### `debug-repair-collective`

Use when software is broken, tests fail, regressions appear, logs show errors, or the user asks for debugging, repair, triage, review, fuzzing, or hardening.

Core workflow:

1. Clarify or infer the failure.
2. Reproduce the issue.
3. Inspect code and evidence.
4. Patch the smallest safe fix.
5. Run verification.
6. Report what changed and what remains uncertain.

### `twinkle-hub-mcp-researcher`

Use for Taiwan-specific data retrieval and grounded research through Twinkle Hub MCP.

Typical use cases:

- Taiwan government records
- Taiwan company or business data
- Taiwan public datasets
- Taiwan statistics
- Citation-grounded factual research

Important rule: never fabricate retrieved records, statistics, government data, company data, or citations.

## Maintenance Rules

- Keep all official skills under `skills/`.
- Use lowercase folder name `skills`, not `skill` or `Skills`.
- Each skill folder should contain a primary `SKILL.md`.
- Do not leave duplicate skill folders at the repository root.
- If a skill is copied from another source, preserve useful attribution or reference notes inside that skill.
- Prefer concise, operational instructions over long theory.

## Current Status

This repository currently acts as a personal skill sandbox and reusable AI-agent workflow library.  
The main focus is practical coding assistance, debugging, research grounding, and reducing unnecessary agent chatter.
