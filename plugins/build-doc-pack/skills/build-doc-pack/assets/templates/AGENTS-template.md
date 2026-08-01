<!-- TEMPLATE: root AGENTS.md. Resolve and delete every template comment. Target well under 150 lines. Include only instructions a capable agent cannot infer from the repository. -->

# AGENTS.md — {{PROJECT_NAME}}

Instructions for the AI agent that plans and builds this project. This file is the source of truth for **how** to work; the active strategic pack listed below defines **what** must be true.

**Code, types, schemas, commands, and file layouts in strategic docs are illustrative guidance, not mandates.** Described behavior, architecture contracts, non-negotiables, and final acceptance are authoritative. Verify implementation details against current official documentation and the live repository.

## What this is

<!-- State the product, users, form factor, stack or delegated stack authority, and authoritative lockfiles in 2–4 lines. Do not tie setup to a preplanned story or slice. -->

## Prime directive

**Cold-read the active pack and current repository, then propose only the single best next implementation slice before coding.** Preserve the complete strategic outcome and stop when final acceptance passes.

The pack's high-level suggested implementation approach is informed but non-binding. Keep hard causal dependencies, but revise advisory order when current code, tests, or unforeseen constraints justify a better plan. Discuss material replanning with the user.

<!-- Add the user's autonomy boundary: who approves the plan, external issue/PR actions, merges, releases, and scope changes. -->

## Definition of done

Run these exact commands before every PR is integration-ready and before declaring the project complete:

```bash
# PROJECT-FILL: Exact verification commands, one per line. Include a smoke/run check for a runnable product. Keep commands character-identical everywhere.
```

Every item in the final acceptance document must also pass. Slice-level checks show progress but never replace final acceptance.

## Non-negotiables

<!-- Summarize the 1–4 project invariants a capable agent could not infer. Number them consistently with the brief and acceptance, and include a short reason. -->

## Strategic-to-tactical handoff

- The strategic lead and pack own scope, directives, architecture boundaries, research gates, risks, known dependencies, suggested high-level order, and final acceptance.
- The implementation lead understands the full strategy but proposes, plans, and executes only one slice at a time. It retains issue, sequencing, integration, and verification responsibility.
- Create the slice plan, GitHub issues, branches, PRs, or sub-agent assignments only after that slice is agreed and the relevant action is authorized.
- Keep the durable slice plan focused on high-level what and why. Use linked GitHub issues for task checklists, WIP, blockers, assignments, and evidence.
- Give execution sub-agents bounded code and test assignments. Select the least expensive capable model and reasoning effort for each task rather than inheriting the primary agent's configuration. They surface surprises to the implementation lead rather than changing scope or replanning the broader effort.
- When evidence invalidates the plan, explain the impact and propose a revision; do not treat the strategic suggestion as a hard sequence.

## Delivery governance

- A human is the only authority that physically merges to `main` in GitHub. Agents never merge, auto-merge, queue, automate, delegate, or push directly to `main`.
- **Active topology:** <!-- direct PRs to main OR feature spine with leaf PRs. State one and remove this comment. -->
- For direct PRs, the agent stops after review and green CI for human merge.
- For spine-and-leaf delivery, the implementation lead may squash-merge clean leaf PRs to the spine; the final spine PR to `main` requires human merge.
- Request GitHub Copilot review first when available; use `review-pr` when it is unavailable; otherwise delegate inline adversarial review to a fresh review sub-agent. The author's own self-review never satisfies the independent gate. Follow the full CI, HEAD-matched review, reply/resolve, re-request-until-clean, and stop loop in [`docs/engineering/workflow.md`](docs/engineering/workflow.md).
- Use a Conventional Commits PR title and the workflow's issue-closing rules; only a PR to `main` may carry `Closes #N`.
<!-- Remove the inactive topology bullet and add repository-specific branch/reviewer facts. -->

## Always / Ask first / Never

- **Always:** follow [`docs/engineering/workflow.md`](docs/engineering/workflow.md); resolve required research gates; verify unfamiliar APIs against current official docs; run required checks; update affected strategic and descriptive docs with behavior changes.
- **Ask first or stop:** changing active scope, public contracts, non-negotiables, final acceptance, or an architecture boundary; adopting a paid service; making an external or destructive change beyond recorded authority; starting a broad refactor.
- **Never:** invent repository facts; commit secrets; bypass red verification; merge, auto-merge, queue, automate, delegate, or push directly to `main`; force current code into an obsolete plan; implement deferred scope or speculative adapters.
<!-- Add project-specific rules, paired with their approved alternative or escalation path. -->

## Dependencies

Prefer existing or standard-library capabilities. Add a dependency when it clearly beats hand-rolling and passes the project's maintenance, license, security, and compatibility policy.

<!-- Add exact project-specific dependency policy or link to tech-stack/research docs. -->

## Code quality

- Follow [`docs/engineering/code-quality.md`](docs/engineering/code-quality.md).
<!-- Add at most 2–4 project-specific deviations that truly belong at root. -->

## Active build pack

<!-- List every active document that exists, in reading order, with a one-line purpose. Start with the strategic brief and end with workflow/code quality as appropriate. Name archived specs separately as historical evidence, never active instructions. -->
