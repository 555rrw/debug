# debug

AI agent skills collection for coding, research, debugging, game development, and execution-control workflows.

本倉庫用來集中管理可被 AI Agent / Codex / Claude Code / Cursor / Manus 類工具讀取的 Skills。  
所有正式技能都放在小寫 `skills/` 目錄下，每個技能以獨立資料夾管理，主要入口通常為 `SKILL.md`；若是大型技能包，則可使用資料夾內 README 或多個子技能作為索引。

## Repository Structure

```text
.
├── README.md
├── .gitignore
└── skills/
    ├── agent-miranda/
    ├── ai-regression-guard/
    ├── cache-read-saver/
    ├── claude-400pro-mode/
    ├── code-extreme-refiner/
    ├── code-logic-refiner/
    ├── debug-repair-collective/
    ├── game-development/
    ├── lesson-before-invention/
    ├── tw-legal-rag-researcher/
    └── twinkle-hub-mcp-researcher/
```

## Skills Overview

| Folder | Skill Name | Purpose |
| --- | --- | --- |
| `skills/agent-miranda/` | `right-to-silence` | Silent execution mode. Stop over-explaining, act directly, ask only when blocked, and report final results. |
| `skills/ai-regression-guard/` | `ai-regression-guard` | Prevent regression bugs when fixing, refactoring, reviewing, or adding features in existing codebases. |
| `skills/cache-read-saver/` | `cache-read-saver` | Preserve cache-read / cached-input efficiency during long AI coding sessions and large repository tasks. |
| `skills/claude-400pro-mode/` | `claude-400pro-mode` | Hardcore analysis mode combining Jensen Huang's public scrutiny and Elon Musk's 5-step algorithm for rigorous decision-making. |
| `skills/code-extreme-refiner/` | `code-extreme-refiner` | Refine code aggressively while preserving correctness, reducing redundancy, clearing technical debt, and improving readability. |
| `skills/code-logic-refiner/` | `code-logic-refiner` | Perform deep three-stage code logic review for correctness, technical-debt avoidance, and concise high-quality implementation. |
| `skills/debug-repair-collective/` | `debug-repair-collective` | Reproduce, diagnose, patch, verify, review, fuzz, harden, and report software bugs through a systematic workflow. |
| `skills/game-development/` | Game Development Skills | Converted Claude Code Game Studios skill pack for game-development workflows, slash-command style skills, and specialist roles. |
| `skills/lesson-before-invention/` | `precedent-first` | Research-before-design protocol. Search successful precedents before inventing new solutions. |
| `skills/tw-legal-rag-researcher/` | `tw-legal-rag-researcher` | Taiwan legal judgment retrieval and citation-grounded legal research through TW Legal RAG. |
| `skills/twinkle-hub-mcp-researcher/` | `twinkle-hub-mcp-researcher` | Twinkle Hub MCP integration for Taiwan public datasets, government records, company data, statistics, and citation-grounded research. |

## Skill Categories

### Execution Control

- `agent-miranda` / `right-to-silence`  
  Makes the agent stop narrating and start executing. Best for tasks where the user wants action instead of explanation.

### Hardcore Analysis and Decision Making

- `claude-400pro-mode`  
  Combines Jensen Huang's extreme co-design and Elon Musk's ruthless algorithm to strip away fluff and find the core essence of a problem.

### Research Before Design

- `lesson-before-invention` / `precedent-first`  
  Forces the agent to look for working examples, proven patterns, and external precedents before designing from scratch.

### Debugging and Code Safety

- `debug-repair-collective`  
  Main bug-fixing and verification workflow.

- `ai-regression-guard`  
  Prevents the common AI failure mode of fixing one bug while breaking existing behavior.

### Code Refinement

- `code-logic-refiner`  
  Deep logic review for correctness, edge cases, and maintainability.

- `code-extreme-refiner`  
  Stronger cleanup/refactor mode for reducing redundancy and technical debt while keeping behavior intact.

### Token / Cache Efficiency

- `cache-read-saver`  
  Helps long coding sessions preserve cache hits, reduce repeated context loading, and avoid token waste.

### Game Development

- `game-development`  
  Converted game-development skill pack from Claude Code Game Studios. It includes `ccgs-*` workflow skills and `ccgs-agent-*` specialist roles.

### Taiwan Research and Retrieval

- `tw-legal-rag-researcher`  
  Uses TW Legal RAG for Taiwan judgment retrieval and citation-grounded legal research. It should not fabricate legal records or citations.

- `twinkle-hub-mcp-researcher`  
  Uses Twinkle Hub MCP for Taiwan-specific public datasets, government records, company data, statistics, and grounded research.

## Usage Philosophy

These skills are designed around several practical rules:

1. **Do not invent blindly**  
   Before designing a new solution, search for working precedents and reuse proven patterns when appropriate.

2. **Act, do not narrate endlessly**  
   For execution tasks, minimize filler, avoid unnecessary planning text, and focus on completing the task.

3. **Debug through feedback loops**  
   Reproduce the issue, inspect evidence, patch carefully, and verify the result instead of only giving advice.

4. **Avoid regression loops**  
   When modifying an existing codebase, preserve current behavior unless the user explicitly asks to change it.

5. **Keep context and cache stable**  
   In long coding sessions, avoid needless re-reading, model switching, and context churn.

6. **Use external retrieval when facts matter**  
   For Taiwan legal, public-data, government, company, or statistical claims, use grounded retrieval tools and cite results instead of hallucinating.

## Recommended Activation Examples

| User Intent | Recommended Skill |
| --- | --- |
| 「直接做，不要解釋」 | `agent-miranda` |
| 「用黃仁勳和馬斯克模式幫我分析」 | `claude-400pro-mode` |
| 「參考別人的成功案例」 | `lesson-before-invention` |
| 「修 bug / 測試失敗 / 幫我 debug」 | `debug-repair-collective` |
| 「不要修 A 壞 B」 | `ai-regression-guard` |
| 「幫我把程式碼邏輯檢查到很嚴」 | `code-logic-refiner` |
| 「幫我把程式碼精煉到極致」 | `code-extreme-refiner` |
| 「長任務省 token / 保快取」 | `cache-read-saver` |
| 「做遊戲開發流程或角色分工」 | `game-development` |
| 「查台灣判決 / 法律 RAG」 | `tw-legal-rag-researcher` |
| 「查台灣政府資料 / 公司資料 / 統計資料」 | `twinkle-hub-mcp-researcher` |

## Maintenance Rules

- Keep all official skills under `skills/`.
- Use lowercase folder name `skills`, not `skill`, `Skills`, or root-level duplicate folders.
- Each normal skill folder should contain a primary `SKILL.md`.
- Large converted skill packs may include multiple sub-skills and an internal README.
- Do not leave duplicate skill folders at the repository root.
- Keep this root `README.md` as the single overall index.
- Avoid maintaining a second general index at `skills/README.md`; it becomes stale easily.
- If a skill is copied or converted from another source, preserve useful attribution or reference notes inside that skill folder.
- Prefer concise, operational instructions over long theory.

## Current Status

This repository currently acts as a personal skill sandbox and reusable AI-agent workflow library.  
The main focus is practical coding assistance, debugging, regression prevention, code refinement, research grounding, game-development workflows, cache efficiency, and reducing unnecessary agent chatter.
