# Interview Guide

Extract strategic decisions that cannot be discovered from code or authoritative research. Do not use the interview to pre-plan implementation.

Batch related questions, usually three to five at a time. Offer options when the choice space is known. Reflect answers back compactly. Skip anything already answered by the user's prompt, supplied artifacts, or current repository. Stop when the strategic contract is complete or the user delegates the remaining decisions.

## Round 1 — Product outcome and scope

- What is the product or feature, for whom, and what outcome should it enable?
- What complete capability is this pack specifying? If it is a release horizon, which horizon?
- Which behaviors and user journeys are in scope?
- Which plausible adjacent capabilities are deliberately deferred or forbidden for now, and why?
- What would make the result strategically wrong even if the software technically ran?

Avoid asking for the smallest slice or first implementation increment. Scope may be bounded without being tactically decomposed.

## Round 2 — Directives and non-negotiables

Ask what a competent agent would still get wrong without being told. Probe for:

- user constraints that may be enriched but never countermanded;
- canonical sources of truth and data ownership;
- boundary and conversion rules;
- compatibility, fidelity, determinism, privacy, licensing, or portability contracts;
- deliberate stubs and extension seams;
- caveats the product must surface;
- prohibited outcomes such as data loss, secret exposure, or irreversible writes.

Capture the reason and observable failure mode for each. Rank the few true non-negotiables; ordinary requirements belong in scope or design.

## Round 3 — Architecture, research, and risk

- Which stack or architecture choices are fixed, preferred, or delegated?
- Which components, boundaries, representations, or external contracts must remain independent?
- Which standards, libraries, licenses, providers, or feasibility questions require research before a design can be adopted?
- Which known dependencies are genuinely causal? What cannot be decided or validated until what other fact is known?
- What risks, tradeoffs, failure modes, or expensive reversals should the pack make visible?
- Which future changes should the current architecture enable without implementing them now?
- Does the user have any strategic sequencing preference the suggested implementation approach should reflect?

Do not ask the user for facts current documentation can establish. Research them and cite the useful conclusion. If research remains inconclusive, preserve a gate rather than inventing certainty.

## Round 4 — Final acceptance and authority

- How will users recognize the complete outcome as successful?
- Which automated commands and observable behaviors constitute final verification?
- Which criteria require human judgment, external hardware, licensed software, or another environment?
- Which decisions may the implementation agent make, and which require user approval?
- Which delivery topology applies: human merge of every PR to `main`, or agent squash-merge of leaf PRs to a feature spine followed by human merge of the spine PR to `main`?
- Is GitHub Copilot review available in this repository, and what exact request method works? Are the `review-pr` and `address-pr-review` fallback skills and sub-agent delegation available?
- What existing CI, merge, branch-protection, or release policies are durable company-wide governance facts?
- Which conditions require implementation to stop and return to the user?

Strategic mode defaults to this handoff: the implementation agent cold-reads the pack and repository, proposes only the single best next slice, and only after human agreement creates that slice's durable high-level plan and GitHub execution issues. It delegates bounded code work using the least expensive capable model and effort, prepares a reviewed green PR, and stops for the human to physically merge it to `main` before proposing another slice. Confirm a different handoff only if the user requests one, except that agent merge authority never extends to `main`.

## Feature-pack variant

Read the repository's active agent instructions, specs, relevant code, manifests, and verification commands first. Then confirm only the feature-specific outcome, scope and deferrals, invariants, architecture boundaries, research gates, risks, causal dependencies, and final acceptance. Follow the repository's spec location and priority rules. Treat archived packs and issue history as evidence, not authority.

## Tactical addendum variant — only after an explicit request

First finish and audit the strategic contract. Then ask about desired planning granularity, delivery constraints, user checkpoints, issue tracker, and delegation model. Make proposed slices and order discussable; do not present them as strategic facts. Do not create external issues, branches, or PRs without authorization.

## Do not ask

Do not spend interview time on discoverable file names, framework-conventional layouts, library API syntax, test minutiae, slice count, execution-task ordering, branch names, issue hierarchy, or sub-agent assignments in strategic mode. The strategic agent may derive a broad suggested order from architecture, research gates, and risks, then label it non-binding.
