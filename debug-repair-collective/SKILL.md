---
name: debug-repair-collective
description: Find, reproduce, diagnose, fix, and verify software bugs using a consolidated workflow built from mattpocock/skills and trailofbits/skills. Use when code is broken, tests fail, behavior regresses, security bugs may exist, logs show errors, or user asks to debug, repair, triage, diagnose, scan, review, fuzz, or harden a codebase.
---

# Debug Repair Collective

Use this skill to move from symptom to verified fix. Do not only explain. Inspect files, run commands, build a feedback loop, patch code when appropriate, and verify result.

## Source Corpus

Full copied source skills live in:

- `references/source-skills/mattpocock-skills/`
- `references/source-skills/trailofbits-plugins/`
- `references/source-skills/trailofbits-codex-skills/`

Load source files only when needed. Start with this skill, then pull exact upstream instructions for specialized cases.

Useful source entrypoints:

- General diagnosis: `references/source-skills/mattpocock-skills/engineering/diagnose/SKILL.md`
- Test-driven fixes: `references/source-skills/mattpocock-skills/engineering/tdd/SKILL.md`
- Code review: `references/source-skills/mattpocock-skills/in-progress/review/SKILL.md`
- Triage: `references/source-skills/mattpocock-skills/engineering/triage/SKILL.md`
- Architecture follow-up: `references/source-skills/mattpocock-skills/engineering/improve-codebase-architecture/SKILL.md`
- Static analysis: `references/source-skills/trailofbits-plugins/static-analysis/skills/semgrep/SKILL.md`
- CodeQL: `references/source-skills/trailofbits-plugins/static-analysis/skills/codeql/SKILL.md`
- SARIF parsing: `references/source-skills/trailofbits-plugins/static-analysis/skills/sarif-parsing/SKILL.md`
- Property tests: `references/source-skills/trailofbits-plugins/property-based-testing/skills/property-based-testing/SKILL.md`
- Mutation tests: `references/source-skills/trailofbits-plugins/mutation-testing/skills/mutation-testing/SKILL.md`
- Coverage analysis: `references/source-skills/trailofbits-plugins/testing-handbook-skills/skills/coverage-analysis/SKILL.md`
- Fuzz harness writing: `references/source-skills/trailofbits-plugins/testing-handbook-skills/skills/harness-writing/SKILL.md`
- Sanitizers: `references/source-skills/trailofbits-plugins/testing-handbook-skills/skills/address-sanitizer/SKILL.md`
- C review: `references/source-skills/trailofbits-plugins/c-review/skills/c-review/SKILL.md`
- False-positive checks: `references/source-skills/trailofbits-plugins/fp-check/skills/fp-check/SKILL.md`
- Supply-chain risk: `references/source-skills/trailofbits-plugins/supply-chain-risk-auditor/skills/supply-chain-risk-auditor/SKILL.md`
- Insecure defaults: `references/source-skills/trailofbits-plugins/insecure-defaults/skills/insecure-defaults/SKILL.md`
- Git cleanup: `references/source-skills/trailofbits-plugins/git-cleanup/skills/git-cleanup/SKILL.md`
- GitHub CLI: `references/source-skills/trailofbits-codex-skills/gh-cli/SKILL.md`

## Core Loop

1. Capture symptom.
   - Record exact command, error, URL, log line, failing test, screenshot, or user-visible behavior.
   - Confirm current working tree state before edits.
   - Prefer `rg`, test runner output, logs, process state, HTTP checks, and config files over guesses.

2. Build fast feedback.
   - First choice: failing test at correct behavior seam.
   - Next: focused CLI, HTTP request, fixture replay, Playwright flow, trace replay, or small harness.
   - For flakes: loop many times, raise reproduction rate, pin time/seed where possible.
   - Do not fix until there is a pass/fail signal unless impossible; if impossible, document what artifact is missing.

3. Reproduce.
   - Run feedback loop and prove it matches user symptom.
   - Save key output path or command.
   - If multiple failures appear, isolate primary failure before changing code.

4. Hypothesize.
   - Make 3 ranked, falsifiable causes.
   - Test one variable at a time.
   - Use targeted probes only. Tag temporary logs as `[DEBUG-<shortid>]`.

5. Fix.
   - Make smallest code/config change that addresses proven cause.
   - Preserve user changes and unrelated work.
   - Prefer existing project patterns and public interfaces.
   - Add or update regression tests when a correct seam exists.

6. Verify.
   - Re-run original repro.
   - Run focused regression tests.
   - Run broader nearby tests or static checks when blast radius warrants.
   - Remove `[DEBUG-...]` probes and throwaway files unless explicitly kept.

7. Report.
   - State root cause, changed files, verification commands, residual risk.
   - If no correct test seam exists, say so and suggest architecture follow-up.

## Tool Selection

- Unknown repo: inspect structure, package files, test commands, and recent changes before patching.
- Test failure: use project test runner first; narrow after first failure.
- Runtime service bug: check process, ports, health endpoint, logs, env, config, dependency state.
- Frontend bug: use browser automation/screenshots, console logs, network responses, responsive viewport checks.
- Security concern: load Semgrep/CodeQL/source-specific security skills; get explicit approval before large scans.
- C/C++/Rust memory issue: prefer sanitizer, coverage, harness, fuzzing source skills.
- Dependency or build issue: inspect lockfiles, package manager, compiler output, PATH/tool versions.
- Kubernetes/service outage: load relevant ops/debug source skill and start with pod status, events, logs, resources.

## Stop Conditions

Stop and ask only when:

- Credentials, destructive operations, paid services, or irreversible migrations are required.
- Reproduction needs unavailable external access or a missing artifact from the user.
- Multiple valid fixes have materially different product behavior.

Otherwise keep using tools until issue is fixed or a concrete blocker is proven.
