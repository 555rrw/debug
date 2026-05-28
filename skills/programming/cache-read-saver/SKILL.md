---
name: cache-read-saver
description: Optimize token usage by maximizing cache read and cached input ratios for AI coding agents. Use for long coding sessions, large repository tasks, and multi-file modifications to reduce costs and improve stability.
---

# Cache-Read-Saver

This skill is designed to help AI coding agents (such as Claude Code, Codex, Cursor, Gemini CLI, etc.) maximize the ratio of **cache read** and **cached input** during long-running tasks, significantly reducing token costs and improving session stability.

## Purpose

The primary goal of this skill is to increase the cache hit rate. In long tasks, the main cause of token waste is often not the volume of code itself, but rather the repeated breaking of caches, re-reading of context, frequent model switching, and redundant analysis of the entire codebase. By following these guidelines, agents can achieve up to a 90% cost reduction on input tokens.

## When to Use

- **Long Coding Sessions**: When a task spans multiple hours or many turns.
- **Large Repository Tasks**: When working with codebases that exceed the immediate context window.
- **Multi-file Modifications**: When changes are spread across various directories.
- **Cost-Sensitive Environments**: When the user is concerned about token usage, quotas, or billing.
- **Cross-Session Continuity**: When a task needs to be resumed in a new session.
- **Pre-Cleanup Actions**: Before performing `/compact`, `/clear`, switching models, or restarting a session.

## Core Rules

- **Stick to the Model**: Do not switch models unless explicitly requested by the user.
- **Avoid Premature Compaction**: Do not proactively run `compact` or `clear` commands unless necessary.
- **Minimize Full Scans**: Do not repeatedly read the entire codebase; prioritize reading only the minimum relevant file set.
- **Reuse Information**: Leverage previously read and analyzed information.
- **Record Decisions**: Document key decisions and architectural choices to avoid redundant discussions.
- **Use Handoffs**: Do not keep pasting large contexts into the conversation; instead, summarize them into handoff notes, memory, or project notes.
- **Session Continuity**: Generate a session handoff if the session is about to expire, context is getting too large, or an interruption is expected.
- **Fresh Starts**: If the cache is likely invalidated, suggest starting a new session using a handoff rather than forcing an old session.
- **Targeted Exploration**: Do not re-scan the whole project for minor modifications.
- **Stable Rules**: Avoid re-inserting static rules into every prompt; keep them in the system or persistent context.

## Cache-Friendly Workflow

1.  **Identify Objective**: Clearly confirm the current task goal first.
2.  **Locate Minimal Context**: Find the smallest set of files necessary for the task.
3.  **Selective Reading**: Read only the files directly related to the current sub-task.
4.  **Pre-change Rationale**: Record the reasoning and dependencies before making modifications.
5.  **Post-change Summary**: Document what has been completed and what remains.
6.  **Create Handoffs**: If the session grows long, establish a handoff document.
7.  **Handoff-Based Resumption**: Start new sessions from the handoff rather than the entire chat history.
8.  **Just-in-Time Analysis**: Re-analyze or re-read files only when strictly necessary.

## Anti-patterns

- **Full Repo Re-reads**: Scanning the entire repository for every turn.
- **Frequent Model Hopping**: Switching between different models without a specific reason.
- **Excessive Compaction**: Constantly clearing context, which destroys the cache.
- **Context Bloat**: Repeatedly pasting large files or logs into the prompt.
- **Forgotten Decisions**: Losing track of previous choices, leading to circular reasoning.
- **Redundant Analysis**: Forcing a new session to redo the analysis already completed in a previous one.
- **Over-exploration**: Running a full discovery process for a one-line fix.
- **Agent Redundancy**: Having multiple agents perform identical analysis on the same codebase.

## Output Behavior

When this skill is active, the agent should:
- Prioritize continuing within the existing context.
- Keep responses concise and actionable.
- Clearly distinguish between **known information**, **unknowns**, and **items requiring re-confirmation**.
- Avoid re-pasting large blocks of text.
- Output a **handoff** when appropriate.
- Proactively suggest: "The current context is ideal for a session handoff before starting a new session."

## Integration with Session-Handoff

This skill is highly complementary to the `session-handoff` workflow. Invoke or suggest a handoff when:
- The task needs to be paused or interrupted.
- The conversation history becomes excessively long.
- The cache is likely to expire or become inefficient.
- Switching models, tools, or environments.
- The user intends to clear the context.
- A major milestone is reached, and the next phase is starting.

## Example

> **User**: I need to fix the bug in the auth middleware where JWT expiration isn't handled.
>
> **Agent (using cache-read-saver)**: 
> I see we are working on the auth middleware. Based on our previous analysis of `src/middleware/auth.ts`, I have the structure in memory. I will read only the specific `verifyToken` function in `src/middleware/auth.ts` to confirm the current implementation, rather than re-scanning the entire `src/` directory.
>
> [Reads only lines 45-80 of src/middleware/auth.ts]
>
> I've identified the issue. I'll apply the fix now. Since we've discussed the JWT strategy earlier, I'll stick to the agreed-upon `HS256` algorithm without re-opening that discussion.
