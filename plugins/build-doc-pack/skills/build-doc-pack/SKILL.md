---
name: build-doc-pack
description: Author or audit a strategic documentation package ("build pack") that lets an AI coding agent cold-read the complete product or feature scope before planning implementation. Capture outcomes, scope, non-negotiables, architecture boundaries, research, risks, known dependencies, and final acceptance in AGENTS.md, briefs, specs, and engineering standards. Use when the user wants to start a project with AI agents, create or revise a build/spec pack, write AGENTS.md, spec a feature for later implementation, or review a documentation package for agent-readiness. Keep execution planning optional and add slices, ordered tasks, PRs, branches, or issues only when the user explicitly requests tactical planning.
---

# Build Doc Pack

Create a strategic package of Markdown documents that an AI coding agent can cold-read before it proposes how to build a project (greenfield) or feature (existing repo). The output follows the AGENTS.md open standard, so the same pack works with Claude Code, Codex, Copilot, Cursor, Gemini CLI, and Grok-based tools.

The build-pack agent is the **strategic lead**—analogous to a VP or director. Capture the complete intended outcome and the durable constraints that implementation must preserve. Offer informed direction without taking over the implementation lead's management decisions.

The implementation agent is the **implementation lead**—analogous to a direct manager. It must cold-read the finished pack and current repository, propose only the single best next slice in discussion with the user, and only after approval create that slice's execution issues and delegate concrete work. It repeats this rolling process after the human merges the completed slice to `main`.

Sub-agents are **execution agents**—analogous to individual contributors. Give them bounded, concrete assignments derived from the approved plan. The implementation lead retains responsibility for sequencing, integration, verification, and escalation.

**The single most important fact, from empirical research on agent context files:** verbose, LLM-padded documentation makes agents worse because agents follow padding faithfully. Lean, human-sourced docs containing genuinely non-obvious information make agents better. Extract decisions only the user can make; research facts that materially affect the design; omit implementation detail a capable agent should decide after inspecting the live code.

## Choose two independent dimensions

### Pack scope

- **Greenfield pack** — a full `docs/` package plus root `AGENTS.md` and `CLAUDE.md` for a new project.
- **Feature pack** — a smaller `docs/features/<feature-name>/` set for a repository that already has constitution docs. Do not regenerate or duplicate existing engineering standards; audit against them instead.

Ask only when the requested scope is genuinely ambiguous.

### Planning depth

- **Strategic (default)** — define the complete scope, product behavior, non-negotiables, architecture boundaries and contracts, research findings and gates, risks, known dependencies, final acceptance, durable delivery governance, and a high-level suggested implementation approach. Keep the suggested order broad, rationale-backed, and explicitly non-binding; it is input to tactical planning, not an execution plan.
- **Tactical addendum (explicit request only)** — after the strategic contract is stable, add the requested slices, implementation order, task breakdown, or delivery artifacts. Keep these separate from the strategic contract and label them as revisable planning. Do not create GitHub issues, branches, or PRs unless the user separately authorizes those external changes.

Do not infer tactical mode from phrases such as “agent-ready,” “build pack,” “ready to implement,” or “end-to-end.” The user must explicitly request decomposition or execution planning.

## Responsibility boundary

The strategic pack owns:

- user and product outcomes;
- in-scope and deliberately deferred behavior;
- user directives and non-negotiable invariants;
- architecture boundaries, contracts, data ownership, and extension seams;
- relevant research, source-backed conclusions, unresolved research gates, and assumptions;
- material risks, failure modes, and known hard dependencies;
- a high-level suggested implementation order for nontrivial work, labeled as guidance the implementation agent may revise;
- company-wide delivery governance such as CI, review, merge authority, and the selected PR topology;
- final project- or feature-level acceptance and verification.

The tactical implementation agent owns:

- slices, milestones, stories, chores, and tasks;
- the actual implementation order after inspecting current code and considering the strategic suggestion;
- issue, branch, and PR structure;
- work allocation and sub-agent delegation;
- per-slice acceptance derived from, but never replacing, final acceptance.

Execution sub-agents own only their assigned concrete work. They surface unexpected constraints to the implementation lead rather than changing strategic scope or independently replanning the broader effort.

## Workflow

### 1. Read the references

Read `references/doc-catalog.md` and `references/writing-rules.md` completely. Read `references/interview-guide.md` before interviewing and `references/audit-checklist.md` before auditing. Use the bundled templates and static assets rather than recreating them.

### 2. Inspect the available evidence

For an existing repository, read its agent instructions, active specifications, relevant code, dependency manifests, and current verification commands before drafting. Treat archived plans and issue history as evidence, not current authority. For greenfield work, inspect every artifact the user supplied.

### 3. Interview for strategic decisions

Follow `references/interview-guide.md`. Never one-shot a pack from a thin prompt. Ask only for facts the user must own: intended outcomes, scope, directives, non-negotiables, architecture constraints, risk tolerance, deliberate deferrals, delivery authority, and how final success is judged. Record delegated decisions as agent authority rather than inventing answers.

Stop when the strategic contract is complete enough for a fresh implementation agent to identify open decisions and propose a plan. Do not interview for slices, task order, branch names, or issue structure in strategic mode.

### 4. Research decision-shaping unknowns

Research standards, libraries, external contracts, licenses, or technical feasibility when they could change architecture or acceptance. Prefer current official and primary sources. Distinguish verified facts, inferences, assumptions, and unresolved gates. Record only conclusions and provenance that future agents cannot cheaply rediscover; do not paste a research diary into the pack.

### 5. Select the document set

Choose documents from `references/doc-catalog.md`. Every pack needs a stable strategic contract and final acceptance. Add conditional documents only when their content earns a separate home. In strategic mode, do not generate `tasks.md`, slice tables, milestone plans, or issue backlogs.

Filenames have no numeric prefixes. State reading order once in the root `AGENTS.md` or the repository's existing navigation document.

### 6. Copy and fill static assets

For a greenfield pack, copy:

- `assets/CLAUDE.md` to the repository root;
- `assets/engineering/code-quality.md` to `docs/engineering/`;
- `assets/engineering/workflow.md` to `docs/engineering/`.

Resolve the marked `<!-- PROJECT-FILL … -->` blocks from user decisions and discovered repository facts, and follow explicit template deletion instructions such as removing the inactive delivery topology. Preserve the remaining static governance text. The workflow asset establishes the strategic-to-tactical handoff and company-wide PR/CI/review rules; it governs how later tactical units ship without predefining those units.

### 7. Draft the strategic documents

Use the templates in `assets/templates/` where available and follow `references/writing-rules.md`. Prioritize:

1. Complete and bounded outcomes over implementation choreography.
2. Non-negotiables, architecture seams, and contracts over discoverable framework detail.
3. Research conclusions, open gates, risks, and causal dependencies over speculative design.
4. A broad suggested implementation approach, with rationale and explicit permission to revise it, over a prescribed sequence.
5. Exact final acceptance and verification over per-task checklists.
6. Illustrative guidance over mandated code shapes; the implementation agent owns the how.

For nontrivial work, recommend a short high-level order of capability areas or decision gates. Explain why the order is likely to reduce risk or rework. Label it **suggested, not required** and instruct the implementation agent to revise it when repository reality, test feedback, or unforeseen issues justify a better plan. State hard ordering only when one decision truly cannot be valid before another, and distinguish that constraint from the advisory sequence. Never expand the suggestion into slices, execution-sized tasks, issues, branches, or PRs.

### 8. Audit the pack

Run `references/audit-checklist.md`: cold-read integrity, reference integrity, cross-document consistency, scope-to-acceptance coverage, research/risk coverage, and the strategic/tactical boundary. Treat a failed item as a pack defect.

If tactical planning was explicitly requested, audit the strategic pack first, then audit the separate execution addendum for traceability. Never let a task plan redefine scope or final acceptance.

### 9. Deliver the handoff

Present the file tree, research performed, inferred assumptions, unresolved gates, and decisions the user should make before implementation. State explicitly that the next implementation lead should cold-read the pack and repository, propose only the single best next slice, and obtain the user's agreement before creating that slice's plan, GitHub issues, branches, or code. The high-level slice plan should remain durable history while GitHub issues own checklists and WIP. The lead should delegate bounded code work using the least expensive capable model and effort while retaining plan, issue, integration, and verification ownership.

## Hard rules

- **Strategic by default.** A high-level suggested implementation order is allowed and expected for nontrivial work, but it must be advisory. Do not emit execution-sized tasks, slices, milestone/story hierarchies, PR plans, branch plans, or GitHub issues unless explicitly requested.
- **Complete does not mean pre-decomposed.** Cover the full intended capability, constraints, research, risks, dependencies, and final acceptance without deciding the tactical work breakdown.
- **Separate constraints from suggestions.** Record hard causal dependencies as facts. Present broader sequencing only as a rationale-backed recommendation the implementation agent may change.
- **Final acceptance stays stable.** Keep project- or feature-level acceptance separate from optional per-slice criteria.
- **Governance is not decomposition.** Preserve mandatory CI, review, human-to-main merge authority, and the selected delivery topology without deciding feature slices or naming future PRs.
- **Review precedence is stable.** Prefer GitHub Copilot review when available, fall back to `review-pr`, then delegate a fresh bounded review sub-agent. Author self-review does not satisfy the independent gate. Retain the clean-HEAD address/reply/resolve loop regardless of reviewer.
- **Rolling implementation handoff.** The implementation lead plans, approves, and executes one slice at a time. It keeps the slice plan stable, tracks work in linked GitHub issues, and selects the least expensive capable model and effort for each bounded execution assignment.
- **Human physically merges to `main`.** Agents may prepare a reviewed green PR but never merge, auto-merge, queue, automate, delegate, or push directly to `main`. Broad instructions to finish or integrate do not transfer this authority.
- **Cold-read ready.** Assume no shared conversation history. Include no references to unrelated projects, people, employers, or repositories.
- **No numeric filename prefixes.** Put reading order in one navigation document.
- **Portable core.** Keep agent-specific helpers optional and provide a self-contained fallback.
- **Never invent facts.** Source repository facts, research claims, tool availability, and constraints; otherwise mark them as an explicit assumption or unresolved user decision.
