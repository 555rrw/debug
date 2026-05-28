---
name: ai-regression-guard
description: A guardrail skill to prevent regression bugs in medium to large-scale projects by enforcing strict coding and testing practices, reducing rework and token waste. This skill is triggered when an AI agent is assigned to fix bugs, refactor code, or implement new features in an existing codebase.
license: Complete terms in LICENSE.txt
---

# AI Regression Guard

This skill provides a set of strict guidelines and checks for AI agents working on codebases to prevent "fixing A, breaking B" regression loops, minimize repeated fixes, and optimize token usage. It enforces disciplined development practices to ensure code stability and maintainability.

## When to Use This Skill

This skill MUST be activated whenever an AI agent is tasked with:

-   **Bug Fixing:** Addressing reported defects in existing functionality.
-   **Feature Implementation:** Adding new features or modifying existing ones.
-   **Code Refactoring:** Restructuring existing code without changing its external behavior.
-   **Code Review:** Reviewing changes made by other agents or developers.

## Inapplicable Scenarios

This skill is NOT intended for:

-   **Greenfield Projects:** Starting a project from scratch where no existing codebase or regression risk exists.
-   **Minor Text/Documentation Changes:** Simple updates that do not involve code logic or functionality.
-   **Exploratory Prototyping:** Rapid experimentation where stability is not the primary concern.

## Core Principles & Directives

### 1. Session Start Check

-   **Directive:** Upon session initiation for any code modification task, ALWAYS perform a `git status` and `git log --oneline -5` to understand the current repository state and recent changes. Report any uncommitted changes or divergent history immediately.

### 2. Git State Verification

-   **Directive:** Before making ANY code changes, ensure the working directory is clean (`git status` shows no uncommitted changes) and the current branch is up-to-date with the designated base branch (e.g., `main`, `develop`). If not, STOP and report the discrepancy.

### 3. Recent Fix History Review

-   **Directive:** Review the last 5-10 commits related to the affected files or modules. Identify patterns of recurring bugs or areas of frequent modification. This informs potential high-risk zones.

### 4. High-Risk File Identification

-   **Directive:** A file is considered high-risk if it:
    -   Has a high commit frequency or recent changes.
    -   Is part of a shared state or critical data flow.
    -   Contains complex business logic or integration points.
    -   Is frequently involved in bug reports.
-   **Action:** If a task requires modifying a high-risk file, escalate the risk level and proceed with extreme caution.

### 5. Regression Test Requirement

-   **Directive:** EVERY bug fix MUST be accompanied by a new, specific regression test that fails before the fix and passes after. This test MUST cover the exact scenario of the bug.
-   **Prohibition:** NEVER skip tests or use `--no-verify` flags to bypass CI/CD checks. Ensure all tests pass locally before committing.

### 6. Single Responsibility Principle

-   **Directive:** Focus on one responsibility per change. If a bug fix reveals a separate refactoring opportunity or a new feature idea, create a separate task for it. DO NOT combine unrelated changes.

### 7. No Unrelated Changes

-   **Prohibition:** ABSOLUTELY DO NOT make 
unrelated changes or 
“drive-by refactorings” while working on a specific task. This includes formatting, minor optimizations, or renaming variables that are outside the immediate scope of the task. If such changes are truly necessary, they MUST be proposed as separate, atomic changes.

### 8. High-Risk Situation Protocol

-   **Directive:** If any of the following high-risk situations are encountered, STOP immediately and report to the user for guidance:
    -   Modification of shared state without clear understanding of all dependencies.
    -   Mixing UI, business logic, and refactoring within a single change.
    -   Discovery of business rules embedded directly in UI components or API endpoints.
    -   Encountering a bug that has been reported and "fixed" multiple times previously.
-   **Action:** Provide a detailed explanation of the high-risk situation, potential consequences, and proposed mitigation strategies.

### 9. Final Report Format

Upon completion of any task, a `final_report.md` MUST be generated with the following sections:

1.  **Task Summary:** Brief description of the task performed.
2.  **Changes Made:** List of files modified and a summary of changes.
3.  **Regression Tests:** Details of new or modified regression tests, including how to run them.
4.  **Risk Assessment:** Re-evaluation of any high-risk files or situations encountered and how they were addressed.
5.  **Verification Steps:** Clear instructions for manual verification, if applicable.
6.  **Lessons Learned:** Any insights gained or recommendations for future improvements.

## Prohibitions (Key Anti-Patterns to Avoid)

-   **Shared State Modification:** NEVER modify shared state (e.g., global variables, singleton instances, shared database tables) without a thorough understanding of all downstream impacts and explicit approval.
-   **Mixed Concerns:** AVOID intertwining UI logic, core business logic, and refactoring efforts in a single commit or change set. Each should be an independent, atomic change.
-   **Business Logic in UI/Endpoint:** DO NOT embed critical business rules directly within frontend UI components or API endpoint handlers. Business logic MUST reside in a dedicated, testable layer.
-   **Repeated Bug Fixes:** If a bug appears to be a recurrence of a previously "fixed" issue, STOP and investigate the root cause thoroughly. A simple patch is insufficient.
-   **Test Evasion:** NEVER intentionally skip tests, disable test suites, or use flags like `--no-verify` to bypass quality gates. All changes MUST pass all relevant tests.

By adhering to these directives, the AI agent will significantly reduce the likelihood of introducing regressions and improve the overall quality and stability of the codebase.
