<!-- TEMPLATE: docs/build-brief.md. Resolve and delete every template comment. Keep only non-obvious strategic content. -->

# Build Brief

_Read this first, then follow the active-pack order in `AGENTS.md`. This document defines the complete strategic outcome; the implementation agent will inspect the repository and propose the tactical plan with the user._

_Code, types, schemas, and file layouts are **illustrative guidance, not mandated implementation**. Described behavior, architecture contracts, non-negotiables, and [`acceptance.md`](acceptance.md) are authoritative._

## Product outcome

<!-- State the product or feature, intended users, problem, complete outcome, form factor, and the few structural facts that frame the rest. -->

## In scope

<!-- List product capabilities and behaviors, not tasks. Every item maps to final acceptance. Include the full active horizon being specified, not merely the first implementation increment. -->

## Out of scope

<!-- Name plausible adjacent capabilities that are deliberately deferred or forbidden, with the reason or gate where useful. -->

## User directives and non-negotiables

<!-- Number the few durable invariants consistently with AGENTS.md. For each: rule, reason, observable failure mode, and verification path or human-review method. -->

## Architecture boundaries and contracts

<!-- State canonical sources of truth, ownership, layer and IO boundaries, external contracts, extension seams, and authority rules. Link detailed architecture/data/API docs. Avoid framework-conventional directory maps. -->

## Research, decisions, and open gates

<!-- Summarize decision-shaping findings with compact provenance. Clearly label adopted decisions, inferences, assumptions, rejected alternatives, and unresolved gates. Link research.md when needed. Do not include a search diary. -->

## Risks and failure modes

<!-- List material risks only. Give each a mitigation, detection/evidence path, fallback, or explicit accepted-risk owner. Link risks.md when needed. -->

## Known dependencies

<!-- Record genuine causal constraints and explain why they exist. Do not turn them into execution-sized steps. -->

## Suggested implementation approach

_This is strategic guidance, not a required sequence. The implementation agent should evaluate it against the live repository and may reorder it when code, tests, or unforeseen constraints support a better plan._

<!-- For nontrivial scope, give a short ordered list of broad capability areas or decision gates and explain the risk/dependency rationale. Do not define slices, tasks, issues, branches, PRs, or per-step acceptance. Delete this section only when the work is genuinely trivial. -->

## Definition of done

<!-- State the complete observable outcome, exact verification commands or linked source of truth, and that every item in acceptance.md passes. Do not define “done” as completing a task list. -->
