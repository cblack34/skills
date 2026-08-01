---
name: implement-build-pack
description: Lead implementation from an approved strategic build pack using rolling, one-slice-at-a-time planning. Use only when the human explicitly invokes this skill or explicitly asks to begin or resume implementation from a build pack. Propose one slice for approval, preserve a durable high-level slice plan, use GitHub issues as the execution tracker, delegate code writing to the least expensive capable agents, and prepare a reviewed green PR for the human to merge to main. Do not invoke merely because a build pack or implementation work is mentioned.
disable-model-invocation: true
---

# Implement Build Pack

Act as the implementation lead for an approved strategic build pack. Understand the complete strategy, but plan and execute only one slice at a time. Keep the primary context focused on requirements, decisions, routing, integration, and concise evidence; delegate bounded code writing and noisy execution work.

This is an explicitly invoked workflow. Do not treat installing the plugin, discovering this skill, discussing a build pack, or encountering implementation work as permission to run it.

## Authority

- The active strategic pack owns the intended outcome, scope, non-negotiables, architecture boundaries, research gates, deliberate deferrals, risks, and final acceptance.
- The human approves each proposed slice, material plan amendments, external actions beyond recorded authority, scope changes, and every merge to `main`.
- The implementation lead selects one slice, maintains its high-level plan, creates and manages its GitHub issues, routes bounded work, reviews results, integrates authorized non-`main` work, and prepares the final PR.
- Execution agents implement only their assigned GitHub issue and return evidence. They do not broaden scope, redesign the slice, or merge to `main`.
- Shipped code and tests own current-state facts. Archived plans and issue history are evidence, not active authority.

## Read first

Read these files completely before acting:

1. `references/kickoff-checklist.md`
2. `references/slice-plan-audit.md`
3. `references/delegation-routing.md`

Use `assets/slice-plan-template.md` when materializing an approved slice. Follow the repository's `AGENTS.md` family and active workflow documents when they are stricter. Surface contradictions instead of silently choosing one authority.

## Determine whether work is new or in progress

Inspect the repository before changing anything:

- `AGENTS.md` and every active strategic document in its specified order;
- relevant production code, tests, manifests, lockfiles, CI, and verification commands;
- Git branch, worktree, and diff state;
- live GitHub issues, PRs, reviews, and checks related to the build pack;
- durable slice-plan documents already present in the repository.

If an approved slice is already in progress, follow **Resume an active slice**. Otherwise follow **Propose the next slice**.

## Resume an active slice

Reconstruct state from the durable slice plan, its linked GitHub issues, the live repository, Git history, PRs, and checks. Do not depend on a prior agent's chat transcript.

Audit the plan with `references/slice-plan-audit.md`:

- If it remains valid, do not rewrite or re-approve it. Continue from the next unfinished actionable GitHub issue and surface any blocker recorded on the critical path.
- Put progress, assignments, checklists, blockers, and verification evidence in GitHub issues, not the plan.
- Amend the plan only for a material invalidation. Present the evidence and minimal proposed amendment to the human before editing the plan or redirecting work.

## Propose the next slice

Understand the entire strategic outcome, then select only the single best next slice. A useful slice is coherent, reviewable, preserves shipped behavior, and produces working behavior or decision-shaping evidence. A research or feasibility slice is valid when an unresolved gate prevents responsible implementation.

Present only this slice for discussion. Include:

- outcome and why it should come next;
- strategic scope and final-acceptance criteria it advances;
- precise in-scope and out-of-scope boundaries;
- hard dependencies, research gates, and sequencing recommendations, clearly distinguished;
- affected architecture seams and public contracts;
- expected high-level approach without prematurely fixing discoverable code details;
- required tests, verification, and manual evidence;
- risks, stop conditions, and decisions requiring human input;
- proposed slice-plan path and GitHub issues for this slice only;
- proposed branch and PR shape under the repository's recorded topology;
- proposed execution-agent assignments and capability tiers.

Do not plan future slices in execution-level detail or create a complete roadmap, milestone, story hierarchy, or issue backlog.

### Approval gate

Before the human approves the proposed slice, do not:

- edit files or write code;
- create or update issues, branches, commits, or PRs;
- delegate implementation work;
- change external state.

Research and read-only inspection needed to make the proposal are allowed. Stop after presenting the slice and wait for explicit approval.

## Materialize an approved slice

After approval, create only the tactical artifacts needed for this slice:

1. Create the slice plan from `assets/slice-plan-template.md` at the approved path. Prefer the repository's established location; otherwise use `docs/implementation/slices/<slice-name>.md`.
2. Create only the authorized GitHub issues for this slice. Each issue is an execution-sized tracker with its own task checklist, dependencies, verification, and completion evidence.
3. Link every issue to the slice-plan path. Add an issue register to the plan with each issue's number, title, purpose, and dependency relationship.
4. Treat this issue-linking pass as initial plan materialization. After it, keep the plan stable and use issues for live work.
5. Establish the approved branch or feature-spine state according to the repository workflow.

The slice plan records the high-level **what** and **why**. GitHub issues record the execution **how**, WIP, ownership, checklists, blockers, and evidence. Do not duplicate issue checklists into the plan.

## Route execution work

Use `references/delegation-routing.md` for every assignment.

- Size the issue independently of the primary agent's model and reasoning effort.
- Select the least expensive model and lowest effort that can complete the work reliably.
- Inspect the current harness's available models, effort levels, agent types, and delegation controls. Do not invent model identifiers or claim a routing configuration that cannot be verified.
- Delegate production code and test writing by default. The implementation lead retains the user conversation, scope decisions, sequencing, issue management, integration, and final verification.
- If capable delegation is unavailable, stop and tell the human. Do not silently consume the primary agent for implementation.
- Parallelize independent read-heavy work when useful. Serialize coupled or overlapping write-heavy work unless isolated branches or worktrees make ownership unambiguous.
- Give each execution agent a minimal complete packet and require a concise return receipt. Review its diff and evidence before accepting the issue.

Do not automatically reuse an expensive primary configuration for bounded implementation, review, or review-addressing. Escalate model capability or effort only when ambiguity, risk, coupling, or failed evidence justifies it.

## Execute and track the slice

For each issue:

1. Confirm its prerequisites and branch ownership.
2. Record or communicate the chosen execution-agent tier, effort, and rationale.
3. Delegate the bounded assignment.
4. Review the returned diff against the issue, slice plan, strategic pack, repository rules, and affected tests.
5. Run or independently verify the required checks.
6. Update the GitHub issue with decisions, evidence, commits or PRs, and remaining blockers.
7. Integrate only through the repository's authorized non-`main` workflow.

When evidence reveals a wider issue, stop the affected assignment. Update the issue with the evidence, then decide whether it is an issue-level adjustment, a material slice-plan amendment requiring human approval, or a strategic conflict requiring human resolution.

## Prepare the slice PR

When all slice issues are complete:

1. Reconcile the implementation with the strategic pack and final acceptance it advances.
2. Run the repository's complete required verification on the proposed final head.
3. Open or update the PR with scope, issue links, verification evidence, risks, and deviations.
4. Fill the slice plan's delivery record with the outcome, deviations, unresolved gates, issue links, and final PR link, then push that documentation update to the PR. This is a completion record, not WIP tracking.
5. Re-run checks affected by the delivery-record update.
6. Complete the repository-defined independent review and address-review loop. Prefer the repository's recorded reviewer. Do not invoke an unrelated review or publishing skill unless the human explicitly requests it or `AGENTS.md` requires it for this stage.
7. Require green CI, no genuine unresolved review findings, and review evidence that matches the current PR head.

## Human-only merge to `main`

The human must physically perform every merge to `main` in GitHub. This authority cannot be delegated or inferred from broad instructions to finish, integrate, or keep going.

The implementation lead and every execution agent must never:

- run a merge command for a PR whose base is `main`;
- call a merge API or automate the GitHub merge UI;
- enable auto-merge or add the PR to a merge queue;
- push commits directly to `main`;
- ask another agent or service to perform the merge.

After the PR is reviewed, green, and ready, stop and give the human the PR link plus concise merge-readiness evidence. Authorized leaf-to-spine merges remain allowed only when the recorded repository workflow explicitly grants that authority and the target is not `main`.

Do not start the next slice until the human has merged the current slice to `main` and the resulting repository state is confirmed. After confirmation, inspect the updated repository, propose one next slice, and repeat.

## Hard rules

- One approved slice at a time; no upfront execution backlog for the whole feature.
- Strategic scope and final acceptance always outrank tactical plans and issue text.
- Keep the slice plan stable; issues are the execution tracker.
- Preserve the shipped MVP unless the approved slice explicitly changes it.
- Distinguish hard causal dependencies from preferred sequence.
- Delegate bounded code work using the least expensive capable model and effort.
- Never claim checks, review, routing, or integration that were not verified.
- Never merge, auto-merge, queue, automate, delegate, or push directly to `main`.
