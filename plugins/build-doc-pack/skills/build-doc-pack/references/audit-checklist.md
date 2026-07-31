# Audit Checklist

Run after generation and before delivery. Fix findings, then re-run affected checks. Surface decisions that cannot be resolved from user input, repository evidence, or authoritative research as explicit open gates.

## A. Cold-read integrity

- [ ] A fresh agent can understand the product or feature, intended users, active scope, and final outcome without conversation history.
- [ ] No names or assumptions from unrelated projects, repositories, organizations, teams, or people leaked into the pack.
- [ ] No past-verification claim is borrowed from another context. Procedures not verified in this repository say so.
- [ ] Repository slugs, URLs, account identifiers, tool availability, and workflow claims come from this repository or the user.
- [ ] Optional tools or skills are “if available” and have a self-contained fallback.
- [ ] Every unresolved placeholder is removed or surfaced in delivery as an explicit user decision or research gate.

## B. Reference integrity

- [ ] Every relative link resolves inside the pack or current repository.
- [ ] Every generated document appears in the pack's reading order; every listed document exists.
- [ ] No document points to an appendix, plan, task list, or artifact that was omitted.
- [ ] Existing-repository packs follow the repository's active navigation and do not revive archived instructions.

## C. Cross-document consistency

- [ ] Verification commands are character-identical everywhere they appear.
- [ ] Non-negotiables agree in substance across agent instructions, brief, design, and acceptance.
- [ ] Scope is consistent: nothing is both active and deferred.
- [ ] Stack names, contracts, constants, data ownership, and architecture boundaries agree across documents.
- [ ] Research conclusions and open gates do not conflict with adopted design decisions.
- [ ] Any priority rule resolves otherwise-conflicting instructions.

## D. Strategic coverage

- [ ] The pack states the complete intended product- or feature-level outcome, not merely a first coding increment.
- [ ] Every in-scope capability has at least one final acceptance item, and every final acceptance item traces to scope.
- [ ] Every non-negotiable has a verification path or an explicit human-review method.
- [ ] Architecture boundaries identify ownership and external seams without mandating discoverable file layouts.
- [ ] Material research findings include useful provenance; assumptions, inferences, and unresolved gates are distinguishable.
- [ ] Material risks and failure modes have a mitigation, a detection path, or an explicit accepted-risk decision.
- [ ] Known dependencies describe genuine causal constraints and explain why they exist.
- [ ] Nontrivial scope includes a short, high-level suggested implementation approach with rationale.

## E. Strategic/tactical boundary

For the default strategic mode:

- [ ] The pack contains no execution-sized slices, milestone/story hierarchy, implementation task list, issue backlog, branch plan, or PR sequence.
- [ ] Any suggested implementation order stays at broad capability or decision-gate level, explains its rationale, and is labeled non-binding.
- [ ] The implementation agent is explicitly allowed to reorder the suggestion when live code, tests, or unforeseen constraints justify it.
- [ ] Final acceptance remains project- or feature-level and is not folded into per-task acceptance.
- [ ] The handoff tells the implementation agent to inspect the current repository, propose slices and order to the user, and obtain agreement before creating execution artifacts or coding.
- [ ] Authority is clear: the strategic agent sets direction, the implementation lead owns tactical planning and integration, and execution sub-agents receive bounded concrete assignments.
- [ ] Exactly one delivery topology is active: human-merge-each-PR to `main`, or agent-merge leaves to a spine with human merge of the final spine PR to `main`.
- [ ] Only a human may merge to `main`; the agent's merge authority, if any, is limited to clean leaf PRs targeting the spine.
- [ ] The workflow retains self-verification, CI, review, reply/resolve, re-request-until-clean, clean-HEAD review, documentation, and stop gates without preassigning feature scope to PRs.
- [ ] Reviewer precedence is explicit: GitHub Copilot first when available, `review-pr` fallback, then a fresh bounded review sub-agent; author self-review never substitutes for independent review.
- [ ] PR mechanics retain base synchronization, Conventional Commits titles, verification evidence, protected-branch safety, and issue closure only through a PR to `main`.

If the user explicitly requested a tactical addendum:

- [ ] The request is recorded, and the addendum is separate and labeled as revisable execution planning.
- [ ] Every execution item traces to strategic scope and final acceptance; none expands or redefines them.
- [ ] GitHub issues, branches, PRs, or other external state are created only with separate authorization.

## F. Lean pass

Ask of every paragraph: *Is this a user-owned decision, decision-shaping evidence, durable constraint, meaningful risk, or final acceptance fact that a capable implementation agent could not cheaply infer?* Cut what fails. Keep examples few and short, commands exact, and root agent instructions well under 150 lines. It is normal for this pass to shrink the pack.
