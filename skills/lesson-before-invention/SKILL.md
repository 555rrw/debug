---
name: precedent-first
description: Research-before-design protocol for AI coding agents. Search external projects, web sources, and MCP/tool docs first; use the current repo only for narrow boundary checks before editing.
---

# Precedent-First / 前車之鑑

Do not invent first. Find working external precedent, extract the pattern, then do a narrow local boundary check before editing.

## Activation

Activate when the user says or implies:

- Precedent-First
- 前車之鑑
- 不要自己亂想
- 參考別人的
- 有成功案例就借鑑
- Don't reinvent the wheel
- Find precedent first
- How do other projects handle this?
- What's best practice for this?
- Follow established patterns

Also activate for:

- designing a new system, module, API, protocol, CLI, workflow, or agent skill
- selecting frameworks, libraries, architecture, or integration patterns
- adding a new abstraction, file format, command format, plugin system, or protocol
- integrating unfamiliar services, APIs, MCP servers, routers, workers, or tools
- any structural decision that will be hard to reverse
- naming, wording, schema, config, CLI, prompt, agent behavior, error handling, permission, sandbox, retry, or MCP/tool contract decisions that shape future usage

## One-Line Rule

Learn first, then design.

## When This Skill Applies, External Search Is Mandatory

Precedent means evidence outside the current repository. When this skill applies, search at least one external channel before proposing a design or change:

1. external projects or mature repositories
2. web sources such as official docs, source, tests, examples, issues, PRs, discussions, or credible engineering posts
3. MCP/tool docs or MCP server examples when tools, agents, integrations, or protocols are involved

The current repository can only answer what hard boundary this change must not break. It cannot satisfy the precedent requirement.

## Research Depth

- Full precedent: use for new systems, APIs, workflows, protocols, MCP servers, skills, or hard-to-reverse structural decisions.
- Light precedent: use for smaller decisions about names, formats, commands, prompts, tool schemas, failure handling, or agent behavior. Keep the summary short, but still look outside the current project. Do not satisfy it by scanning this repo for conventions.
- Skip: single-line small fixes, clear bug fixes with an obvious cause and patch, pure translation or explanation, and small tasks where the user already provided a complete implementation plan and only wants execution.

## Required Flow

1. Classify the task and the correct external search domain.
2. Do not search the current repository for conventions as precedent.
3. Define what counts as good or bad precedent.
4. Search external projects or mature repositories outside the current workspace.
5. Search web sources: official docs, source, tests, examples, config, issues, PRs, discussions, or credible engineering posts.
6. Search MCP/tool documentation or MCP server examples when the task involves tools, agents, integrations, or protocols.
7. Review at least 2 independent external sources for structural decisions.
8. Read beyond README: source, tests, examples, config, docs, issues, or PRs.
9. Do a narrow local boundary check only for touched files or integration points.
10. Decide what to adopt, adapt, or reject.
11. Propose a solution only after the research summary is complete.

## Strict Gate

Do not propose architecture or write code until the precedent research summary is complete when strict mode is enabled or when the task is structural.

Stop if:

- local boundary check was skipped before editing code or files
- fewer than 2 independent external/web/MCP sources were reviewed for a structural decision
- sources are README-only
- sources solve a different class of problem
- sources are outdated, abandoned, or unverifiable
- the agent cannot explain what to adopt, adapt, and reject
- the solution is novel without explaining why mature precedents do not apply
- a touched file already has a partial solution that should be extended instead of replaced

Blocked output:

```text
STOP: Precedent gate failed.

Reason:
- ...

What must be researched next:
- ...
```

## Research Summary Template

```text
## Precedent Research: [Task Name]

### Task Classification
This is a [category] problem. I searched for precedents in [domain].

### Local Boundary Check
- Files / docs checked: [...]
- Hard constraints found: [...]
- Local conventions intentionally ignored as precedent: [...]

### Precedent Criteria
Useful precedent must: [...]
Reject precedent if: [...]

### Sources Reviewed
| Project / Source | Evidence Read | Approach | Strengths | Weaknesses | Decision |
|-----------------|---------------|----------|-----------|------------|----------|
| ...             | source/tests/docs/issues | ... | ... | ... | adopt/adapt/reject |

### Patterns to Adopt Directly
- [Pattern]: [Why it fits this project without modification]

### Patterns That Need Adjustment
- [Pattern]: [What differs in this context and why adjustment is needed]

### Options Rejected
- [Option]: [Reason for exclusion]

### Proposed Solution
[Only after the above is complete]
```

## Source Reading Standard

README-only research is insufficient for implementation decisions. Inspect at least one of:

- source code
- configuration files
- tests
- examples
- issues or pull requests explaining design decisions
- official documentation for the exact behavior being reused
- release notes or migration docs when behavior may have changed

## Forbidden Behaviors

Do not:

- skip local boundary checks before editing
- treat the current repository as enough precedent for structural design
- fake research from memory
- accept README-only summaries as implementation evidence
- use a single source for structural decisions
- cite unverifiable or stale sources
- copy without understanding
- replace hard local integration points without strong reason
- invent new protocols, config formats, or abstractions when proven ones fit

## Final Principle

Use creativity where it matters: adapting proven solutions safely to the current project.
