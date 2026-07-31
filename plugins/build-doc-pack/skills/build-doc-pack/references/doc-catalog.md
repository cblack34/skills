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
