# Delegation and model-routing guide

The implementation lead owns decisions and integration. Execution agents own bounded work. Route each assignment independently so an expensive primary configuration does not become the accidental default for every task.

## Size the assignment

Assess these dimensions before choosing an agent:

| Dimension | Lower demand | Higher demand |
| --- | --- | --- |
| Ambiguity | Exact mechanical outcome | Competing interpretations or missing evidence |
| Breadth | One known seam | Cross-cutting architecture or many interacting systems |
| Risk | Easy rollback, no durable data | Security, migrations, concurrency, money, privacy, or data loss |
| Novelty | Existing repository pattern | New domain, API, or architectural pattern |
| Verification | Deterministic focused check | Emergent behavior or difficult manual evidence |
| Coupling | Independent files and contracts | Shared state, overlapping writes, or sequencing constraints |
| Context | Small issue packet | Large strategic or repository context required |

Split work only along real ownership boundaries. Do not manufacture tiny agents whose coordination costs more than their work, but do not keep code writing in the implementation-lead context merely to avoid making a clear assignment.

## Choose the least expensive capable tier

Use capability tiers as the durable contract. Model names and effort labels are runtime facts and may change.

### Light

Use for narrow read-only discovery, documentation edits, mechanical transformations, isolated tests, formatting, or repetitive changes with exact examples.

- Prefer an efficient model.
- Use low or medium effort when the harness offers it.
- Provide exact files, pattern, output, and checks.

### Standard

Use for bounded features and bug fixes with known architecture seams, moderate implementation judgment, or review work that requires tracing ordinary edge cases.

- Prefer a balanced coding model.
- Start at medium effort; use high when logic or verification warrants it.
- Keep scope bounded to one issue and require tests.

### Heavy

Use for ambiguous cross-cutting design, difficult causal debugging, migrations, concurrency, security-sensitive behavior, irreversible data changes, or work whose failure has a large blast radius.

- Use the strongest appropriate model available.
- Use high or greater effort only while the difficult reasoning remains necessary.
- Consider a separate read-only investigator before assigning writes.
- Return strategic or scope ambiguity to the implementation lead instead of letting the worker decide it.

Escalate after concrete evidence: failed attempts, unexplained behavior, missed edge cases, or newly discovered coupling. Do not escalate merely because the primary agent is expensive or the task is important to the project.

## Harness-adaptive routing

At runtime:

1. Inspect the harness's available models, effort levels, subagent types, and per-invocation controls.
2. Map the selected capability tier to an available configuration.
3. Request the model and effort explicitly when the harness supports per-agent routing.
4. Verify the effective configuration when the harness exposes it.
5. If routing is unavailable, restricted, or unverifiable, state that limitation in the assignment or issue. Do not claim savings that were not achieved.

Current harnesses use different mechanisms:

- Claude Code can define or select a subagent model and effort. Prefer stable aliases or runtime-discovered identifiers rather than embedding a dated full model ID in the plan.
- Codex can route subagents by model and reasoning effort. An efficient model at medium or high effort often fits bounded scans, implementation, and review; reserve the strongest model at very high effort for genuinely demanding work.
- Grok exposes models, effort, agent types, and independent child sessions, but the available per-child override may depend on the installed version. Inspect the live controls and report when only session-level selection is possible.

These are routing examples, not promises about a future catalog. Never fail an otherwise valid slice merely because an example model is unavailable.

## Keep the primary context lean

The implementation lead should retain:

- the human conversation and approvals;
- strategic and slice-level decisions;
- issue decomposition and dependency management;
- integration review and final verification;
- concise execution-agent receipts.

Execution agents should absorb:

- targeted codebase exploration needed for their issue;
- code and test writing;
- focused test loops, logs, stack traces, and debugging output;
- mechanical documentation updates tied to their implementation.

Return summaries and evidence, not raw transcripts. Do not preload the entire strategic pack when the issue needs only named constraints and links.

## Assignment packet

Give every execution agent:

- **Outcome:** one sentence describing the completed behavior or evidence.
- **Authority links:** slice-plan path and GitHub issue.
- **Scope:** exact files, components, or contracts it may change, plus explicit exclusions.
- **Constraints:** relevant non-negotiables, architecture boundaries, compatibility promises, and repository rules.
- **Known context:** entry points and facts already established by the implementation lead.
- **Verification:** exact automated and manual checks it must run.
- **Ownership:** branch or worktree and whether any other agent may touch overlapping files.
- **Stop conditions:** discoveries that must return to the implementation lead.
- **Return format:** changed files, checks and results, decisions, assumptions, surprises, and commit or diff reference.

Do not ask an execution agent to reinterpret the whole strategic pack or choose the next slice.

## Review and review-addressing

Keep independent review separate from authorship. Review and review-addressing are bounded tasks and normally should not inherit the implementation lead's most expensive configuration.

- Use a standard tier with enough effort to trace behavior, tests, and edge cases.
- Escalate for security, concurrency, migrations, subtle data invariants, or evidence that the first review missed real defects.
- Give a reviewer the PR diff, relevant strategic constraints, acceptance criteria, and verification evidence—not the entire implementation transcript.
- Give a review-addressing agent the exact unresolved threads, current PR head, issue boundaries, and required checks.
- The implementation lead evaluates dispositions, ensures replies and resolutions are complete, and confirms review matches the final head.

Follow the repository's recorded reviewer precedence. Do not invoke an installed or available skill merely because it could help; explicit human instruction or applicable repository instructions must authorize it.

## Parallelism

Parallelize independent read-only research, test execution, or non-overlapping worktree assignments when it reduces latency. Default to serial execution when agents would modify the same files, depend on uncommitted outputs, or compete over shared external state.

The implementation lead owns conflict avoidance. Agents must not resolve non-trivial integration conflicts by guessing or force-pushing.

## Return receipt

Require a concise receipt containing:

1. Outcome achieved or precise blocker.
2. Files changed and public behavior affected.
3. Tests and verification run, with results.
4. Decisions, assumptions, and unexpected findings.
5. Commit, branch, PR, or diff reference.
6. Follow-up work, if any, that remains inside the issue.

The receipt is evidence for the implementation lead. Durable progress and verification belong in the GitHub issue.
