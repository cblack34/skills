# Slice-plan audit

The slice plan is a durable high-level charter and historical artifact. It is deliberately less detailed and less mutable than the linked GitHub issues.

## Valid-plan test

An active plan remains valid when all of these are true:

- Its outcome still advances the active strategic pack and final acceptance.
- Its scope and exclusions still preserve non-negotiables and deliberate deferrals.
- Its assumptions and research gates remain supported or explicitly unresolved with safe stop conditions.
- Its architecture seams and public-contract boundaries still match repository reality.
- Its verification can still demonstrate the slice outcome.
- Its branch and issue structure can still deliver the slice safely.
- No later repository change has made the approach unsafe or impossible.

When these hold, keep the plan unchanged. New implementation detail, a different code preference, ordinary task discovery, estimate drift, assignment changes, and routine blockers belong in GitHub issues.

## Material invalidation

Consider an amendment only when evidence shows at least one of these:

- The plan conflicts with strategic scope, a non-negotiable, architecture boundary, deliberate deferral, or final acceptance.
- A relied-upon assumption is false or a required research or feasibility gate failed.
- A previously unknown hard dependency changes the slice outcome or makes it unsafe to proceed.
- The planned approach requires an unapproved public-contract, data-model, migration, security, or material risk change.
- The slice cannot satisfy its verification or preserve shipped behavior as approved.
- A material repository change makes the approved outcome or delivery approach impossible or unsafe.

A more elegant design, a preferred library, ordinary refactoring opportunity, or alternate issue ordering is not material invalidation by itself.

## Amendment procedure

1. Stop only the affected work; preserve unrelated safe evidence.
2. Record the discovery and its evidence in the relevant GitHub issue.
3. Explain which plan statement is invalid and the effect on outcome, scope, risk, or verification.
4. Propose the smallest possible amendment. Do not rewrite history or silently replace the original plan.
5. Obtain explicit human approval before editing the plan or redirecting the slice.
6. Append a dated amendment containing the previous assumption, new evidence, approved change, and affected issues.
7. Update issue checklists and dependencies to implement the amendment.

If the evidence challenges the strategic pack rather than the tactical plan, stop for a strategic decision. A slice-plan amendment cannot redefine strategic authority.

## Initial and final edits that are not replanning

The plan may change during initial materialization to add the GitHub issue register after issue creation. It may receive one delivery-record update when the final PR is ready, recording results, deviations, unresolved gates, and links. Neither edit should turn the plan into a status board.

## Historical integrity

- Keep the document in the repository after completion.
- Preserve approved outcome, rationale, boundaries, and amendment history.
- Keep closed issue and PR links so future developers can recover detailed execution evidence.
- Do not replace the plan with a retrospective. Record concise delivery facts in its designated section.
- Do not update issue status, assignment, or checklist state in the plan.
