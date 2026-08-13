# Document Catalog

Choose the smallest document set that preserves the strategic contract. Distinguish **constitution** documents (how agents work), **strategic spec** documents (what must be true and why), **descriptive design** documents (current or intended architecture, updated when code changes), and optional **execution plans** (revisable tactical decomposition). Strategic mode is the default.

## Greenfield core

| File | Species | Purpose |
| --- | --- | --- |
| `AGENTS.md` | constitution | Operating manual, strategic-to-tactical handoff, verification, non-negotiables, authority boundaries, and reading order. Target well under 150 lines. Use `assets/templates/AGENTS-template.md`. |
| `CLAUDE.md` | constitution | Portable bridge to `AGENTS.md` and the brief. Copy `assets/CLAUDE.md`. |
| `docs/build-brief.md` | strategic spec | Product outcome, scope, directives, non-negotiables, architecture boundaries, research gates, risks, known dependencies, high-level suggested implementation approach, and definition of done. Use `assets/templates/build-brief-template.md`. |
| `docs/acceptance.md` | strategic spec | Stable, final project-level behavioral and verification contract. Use `assets/templates/acceptance-template.md`. |
| `docs/engineering/workflow.md` | constitution | Handoff from strategic pack to user-approved tactical planning plus company-wide branch/PR topology, CI, review, merge authority, verification, and stop conditions. Copy the static asset and fill marked blocks. |
| `docs/engineering/code-quality.md` | constitution | Universal core plus project-specific code rules. Copy the static asset and fill marked blocks. |

## Greenfield conditional documents

| File | Add when… | Skip when… |
| --- | --- | --- |
| `docs/ui-spec.md` (+ optional `docs/ui-layout.svg`) | Layout, interaction, accessibility, responsive behavior, or visual constraints materially affect acceptance. | The product has no UI or the user delegates presentation details. |
| `docs/tech-stack.md` | Choices, vetting rules, licenses, runtime limits, or interoperability constraints are strategically significant. Include a short rationale and status for each choice. | The implementation agent may choose within rules already stated in the brief. |
| `docs/data-model.md` | Domain concepts, canonical representations, persistence ownership, migrations, or serialization boundaries are nontrivial. | The model is trivial or still blocked by research; record the gate instead of inventing a schema. |
| `docs/architecture.md` | Layering, ownership, contracts, trust boundaries, or extension seams would surprise an agent familiar with the stack. Mark shipped structure as descriptive: code wins, and the doc changes with it. | Framework convention plus the brief is sufficient. |
| `docs/research.md` | Multiple sourced findings materially constrain standards, dependencies, architecture, licensing, or feasibility. Record conclusions, provenance, confidence, and unresolved gates—not a search diary. | Findings fit clearly in the brief or design. |
| `docs/risks.md` | Risks, tradeoffs, mitigations, or fallback decisions are numerous or cross-cutting enough to need a register. | A compact brief section is sufficient. |
| `docs/<capability>.md` | One complex capability needs its own behavioral contract, algorithm constraints, or caveats. | The brief and acceptance already specify it clearly. |
| `docs/api-contract.md` | An external API or integration has fixed contracts the implementation agent must not invent. | No fixed external contract exists. |

## Feature pack for an existing repository

Place it in `docs/features/<feature-name>/` or the repository's active spec location.

| File | Purpose |
| --- | --- |
| `brief.md` | Problem, users, complete feature outcome, in/out of scope, directives, non-negotiables, risks, and final success boundary. |
| `design.md` | Non-obvious architecture boundaries, touched ownership domains, contracts, data semantics, research conclusions or gates, alternatives, known causal dependencies, and a high-level suggested implementation approach. Omit only when genuinely trivial. Label suggested order non-binding; do not turn it into slices or tasks. |
| `research.md` | Optional source-backed findings when standards, licenses, providers, or feasibility materially shape the feature and do not fit cleanly in `design.md`. |
| `acceptance.md` | Stable feature-level done criteria plus repository verification that must remain green. Keep separate from execution planning. |

Feature packs do not duplicate constitution content. If the repository lacks usable agent instructions or verification guidance, flag that gap and offer a separate constitution update.

## Starting the next pack after delivery

Use this transition when the pack that currently defines the work has been delivered and accepted, and a new product horizon or substantial feature needs its own strategic contract. The goal is a clean cold read: one obvious active entry point, durable living references, and completed contracts preserved as history.

### 1. Prove the prior pack is complete

- Cold-read the prior strategic pack and final acceptance; current code and tests; CI and verification commands; living architecture, data, stack, and integration references; roadmap and active decisions; root navigation; and delivery history around the claimed completion.
- Compare its final acceptance with shipped code, tests, CI, and required human or live evidence.
- Reconcile stale checkboxes or status text from real evidence. Keep missing evidence explicit; do not mark an item complete because implementation merely appears present.
- If material scope remains undelivered, keep the pack active or record an explicit scope decision before archiving it. Archiving must not hide unfinished work.

### 2. Classify documents by role and current truth

Do not archive by filename alone. A data model or tech-stack document may be a living reference in one repository and a milestone-specific historical record in another.

| Document role | Default treatment |
| --- | --- |
| Constitution: root agent instructions, workflow, code quality, durable delivery governance | Keep active. Update navigation or current governance without copying it into the archive. |
| Living descriptive/reference docs: current architecture, data model, stack, integration contracts | Keep active and reconcile with shipped code. If only one completed milestone still needs the content, archive it and make the historical status explicit. |
| Completed strategic specs: brief, final acceptance, milestone-specific research or design | Move to `docs/archive/<milestone>/` or the repository's established archive location. |
| Completed execution records: slice plans, milestone plans, completed tactical addenda | Move with the completed pack when they provide useful delivery or verification history. |
| Roadmap and active decision records | Keep active when they still govern selection, deferrals, or prohibited directions. Remove or mark decisions that no longer have active force. |

Move completed files rather than copying them. In a Git repository, history preserves their former paths; duplicate copies risk looking like two active contracts. Make only narrow historical-status annotations and link repairs inside archived material so the original contract and evidence remain intelligible.

### 3. Create the archive boundary

Default to a stable milestone or release name such as `docs/archive/<milestone>/`; follow an established local convention when one exists. Add `README.md` from `assets/templates/archive-README-template.md` stating:

- what outcome the directory records and its completion or acceptance status;
- what contract, verification, and optional execution records it contains;
- that it is historical evidence, not an active build specification;
- where active work begins now; and
- that active documents and current code/tests win on conflict.

A Git tag or release may add provenance, but it does not replace a repository-contained archive that a cold reader can discover.

### 4. Establish the new active entry point

- Put the new feature pack in `docs/features/<feature-name>/` or the repository's established spec location.
- Use a roadmap as the entry point only when it carries real selection/status information across multiple outcomes. Otherwise point directly to the selected feature pack.
- Keep active deferred or superseded directions in a decision record when a future agent might otherwise revive them from the archive or issue history.
- Update root agent instructions and any small navigation bridges so their prime directive and reading order lead to active docs first. List the archive separately and say when it is appropriate to read.
- Repair and verify every moved relative link, active-document list, root README pointer, and workflow reference. Remove stale statements that still describe the completed pack as future work.

For later feature transitions, follow the repository's established delivered-feature convention. A completed feature pack may move under the archive or remain in place with an explicit delivered status, but it must leave the active reading order and cannot remain co-equal with the next pack.

## Optional tactical addendum — explicit request only

Use the repository's established planning location and vocabulary. A separate `execution-plan.md` or `tasks.md` may contain proposed slices, order, dependencies, per-slice checks, and delivery mechanics only when the user explicitly requests tactical planning. Label it **revisable; strategic specs and shipped code win on conflict**.

Do not create this addendum merely because implementation is next. The future implementation agent should normally cold-read the strategic pack and current code, discuss decomposition with the user, then create the plan. Creating GitHub issues, branches, or PRs is a separate state-changing action that requires authorization.

## Suggested implementation approach in strategic mode

For nontrivial scope, include a compact advisory order of broad capability areas or decision gates. Explain the dependency or risk rationale for the recommendation. State that the implementation agent should use it as context, inspect the live repository, and revise the order when new evidence warrants. This section must not name execution-sized slices, tasks, issues, branches, or PRs.

## Final acceptance style

- Group criteria by user-visible capability or strategic invariant.
- Use event → observable outcome phrasing where behavior is conditional.
- Mark automated checks with the expected assertion, not just “add tests.”
- Cover scope bidirectionally: every active capability has acceptance; every criterion traces to active scope.
- Keep final acceptance independent of optional per-slice checks so replanning cannot weaken the contract.
