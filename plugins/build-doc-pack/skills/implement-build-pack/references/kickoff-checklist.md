# Kickoff and resume checklist

Use this checklist before proposing a new slice or resuming an active one. Read only material relevant to the active strategic scope, but do not skip an authoritative document in the pack's stated reading order.

## Establish authority

- [ ] Read the applicable `AGENTS.md` family from repository root to the working directory.
- [ ] Identify the active strategic pack and read every listed document in order.
- [ ] Separate active authority from archived plans, closed issues, and historical evidence.
- [ ] Record final acceptance, non-negotiables, architecture boundaries, deliberate deferrals, research gates, and human approval boundaries.
- [ ] Confirm that only the human may physically merge to `main`.

When sources conflict, do not average them. Shipped code and tests describe current behavior; the active strategic pack describes intended outcomes and constraints; the human resolves material contradictions.

## Inspect repository reality

- [ ] Check the current branch, worktree, status, diff, remotes, and recent relevant history.
- [ ] Inspect production entry points, affected architecture seams, tests, manifests, lockfiles, and generated artifacts.
- [ ] Read CI workflows and exact repository verification commands.
- [ ] Identify public contracts, persisted data, compatibility promises, and migration risks.
- [ ] Inspect live issues, PRs, reviews, checks, and branch relationships for the active scope.
- [ ] Verify unfamiliar or drift-prone external APIs against current official sources when they affect the slice decision.

## Detect active tactical work

Search established planning locations and repository history for a durable slice-plan document. Confirm that a candidate plan:

- identifies the strategic pack it serves;
- records human approval or otherwise has clear evidence of approval;
- links the active GitHub issues;
- describes the same branch, PR, and code state now present;
- has not already been completed or superseded.

If more than one slice appears active, stop and ask the human which one owns current implementation. Do not merge their scopes yourself.

## Resume path

When an active approved slice exists:

1. Read the plan for the high-level what and why.
2. Read every linked issue for task state, assignments, blockers, and evidence.
3. Inspect referenced commits, PRs, reviews, and checks rather than trusting prose summaries.
4. Audit plan validity with `slice-plan-audit.md`.
5. If valid, continue the next actionable issue without rewriting the plan.
6. If materially invalid, stop and propose the smallest amendment supported by evidence.

## New-slice path

When no slice is active:

1. Reconcile completed work with the entire strategic outcome.
2. Identify unresolved hard gates and the smallest coherent outcome that advances acceptance.
3. Select one slice, not the full remaining roadmap.
4. Define clear exclusions so future work is not accidentally pulled in.
5. Derive verification from strategic acceptance and current repository behavior.
6. Propose the slice, its issues, delivery shape, and delegation tiers without creating them.
7. Stop for explicit human approval.
