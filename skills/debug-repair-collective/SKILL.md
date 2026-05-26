# debug-repair-collective

Use this skill when a bug, regression, failing test, broken workflow, or unclear runtime error needs systematic repair instead of one-shot guessing.

## Goal

Coordinate one or more agents to diagnose, patch, verify, and document a fix while avoiding repeated blind attempts.

## When to Use

Trigger this skill when any of these are true:

- A test, build, script, workflow, or command fails.
- A previous fix attempt did not solve the problem.
- The cause is unclear and may involve multiple files.
- The task benefits from separating investigation, repair, and review.
- The user asks for debug, repair, triage, root cause, or regression handling.

## Core Protocol

1. **Collect evidence first**
   - Capture the exact error, command, stack trace, failing test, log, or user-reported symptom.
   - Identify what changed recently if available.
   - Do not patch before there is at least one plausible root-cause hypothesis.

2. **Localize the fault**
   - Find the smallest relevant files, functions, config entries, tests, or workflow steps.
   - Prefer existing project patterns over inventing a new architecture.
   - Separate symptom files from likely cause files.

3. **Form repair hypotheses**
   - Write the top likely cause in one short sentence.
   - If there are multiple likely causes, rank them by evidence.
   - Avoid broad rewrites unless the evidence demands it.

4. **Apply the smallest safe fix**
   - Patch only the necessary scope.
   - Preserve public behavior unless the bug is caused by that behavior.
   - Add or adjust tests when practical.

5. **Verify**
   - Run the narrowest relevant check first.
   - Then run broader checks only if needed.
   - If verification fails, update the hypothesis instead of repeating the same fix style.

6. **Report concisely**
   - State root cause, changed files, verification result, and remaining risk.
   - Do not include long narratives unless requested.

## Multi-Agent Roles

If multiple agents or models are available, split work like this:

- **Investigator**: reads logs, traces failing path, proposes root cause.
- **Repairer**: makes the smallest code/config/test change.
- **Reviewer**: checks scope, regressions, style, and whether the verification is meaningful.
- **Commander**: decides when to stop, retry, escalate, or ask the user.

A single agent may perform all roles, but should still keep the phases distinct.

## Anti-Patterns

Do not:

- Guess and patch without reading the error.
- Rewrite large sections before locating the fault.
- Run expensive full checks before narrow checks when a narrow check exists.
- Repeat failed fixes without changing the hypothesis.
- Hide verification failures.
- Claim a fix is complete without evidence.

## Escalation Rules

Ask the user or stop for confirmation only when:

- The fix requires destructive actions.
- Credentials, secrets, payments, deployments, or production data are involved.
- The correct behavior is ambiguous and cannot be inferred from tests, docs, or local patterns.
- The repair would significantly change architecture or user-facing behavior.

Otherwise, proceed with the smallest safe repair and report the result.

## Output Format

Use this final report format:

```text
Root cause: <one sentence>
Changed: <files or components>
Verified: <commands/checks and result>
Remaining risk: <none / short note>
```
