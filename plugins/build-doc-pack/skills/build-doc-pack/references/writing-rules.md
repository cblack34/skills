# Writing Rules

Write every pack for a capable agent with no shared conversation history. Lean, precise, human-owned constraints improve agent outcomes; padding broadens exploration and increases cost.

## 1. Strategic, not pre-decomposed

- Specify the complete intended outcome, scope boundary, non-negotiables, architecture contracts, decision-shaping evidence, risks, causal dependencies, and final acceptance.
- For nontrivial work, include a short suggested order of broad capability areas or decision gates. Explain the rationale and label it non-binding; the implementation agent may revise it after inspecting live code or encountering unforeseen issues.
- Do not default to milestones, execution-sized slices, stories, tasks, branch plans, PR plans, issue backlogs, or sub-agent assignments.
- Distinguish three things: a hard causal constraint, a broad advisory order, and a tactical plan. “Evaluate standard X before adopting the canonical schema because interoperability depends on it” may be hard; “then establish domain contracts before output adapters to reduce rework” may be suggested; execution-sized steps are tactical.
- When tactical planning is explicitly requested, put it in a separate, revisable addendum. Strategic specs and final acceptance remain authoritative.
- Preserve the authority ladder: strategic lead sets outcomes and guardrails; implementation lead owns rolling one-slice planning, issues, sequencing, integration, and delegation; execution agents own bounded assigned code work; only the human physically merges to `main`.
- Separate governance from decomposition. Mandatory CI/review rules and merge authority may govern every future PR without the strategic pack deciding how many PRs exist or which scope each contains.

## 2. Non-obvious only

- Include what the agent cannot cheaply discover or infer: decisions, invariants, constraints, research conclusions, risks, and gotchas.
- Prefer enforcement in tooling. Name the exact command instead of repeating prose a linter or test already enforces.
- Include directory structure only when ownership or layering would surprise someone familiar with the stack.
- Link instead of restating. Delete borderline text by default.

## 3. Exact and self-verifiable

- Give exact commands with flags, never descriptions such as “run the linter.”
- Define final done as commands plus observable product or feature behavior.
- Number priority rules when constraints can conflict.
- Keep final acceptance at the product or feature level. Optional per-slice checks may derive from it but may not replace it.

## 4. Evidence and uncertainty

- Prefer current official documentation, primary sources, standards bodies, and license texts for decision-shaping research.
- Record the conclusion, why it matters, and compact provenance. Do not include a search diary.
- Label inference as inference. Separate adopted decisions, assumptions, rejected alternatives, and unresolved research or user gates.
- Do not lock a schema, provider, dependency, or irreversible architecture decision while its stated research gate remains open.

## 5. Prohibitions need alternatives

Pair every “do not” with the approved behavior or decision path. A bare wall of prohibitions makes an implementation agent cautious without making it effective.

## 6. Examples are few, short, and illustrative

- Use a handful of short examples only when they disambiguate intent.
- Label code, types, schemas, commands, and file layouts in strategic specs as **illustrative guidance, not mandated implementation**.
- Treat described behavior, contracts, and acceptance as authoritative; require the implementation agent to verify APIs against current official docs.

## 7. Explain why, briefly

Give a one-line reason for architecture rules and causal dependencies so later agents can generalize. Avoid design-philosophy essays and history lessons.

## 8. Place non-negotiables deliberately

Summarize the few project invariants in `AGENTS.md`, explain them in the brief or design, and connect them to acceptance where verifiable. This bounded repetition is intentional; all other duplication should be removed.

## 9. Cold-read discipline

- Refer only to this project and supplied or cited evidence.
- Do not claim a procedure worked elsewhere. Mark anything unverified in this repository.
- Make agent-specific tools optional and provide an inline fallback.
- Resolve placeholders or surface them explicitly in delivery.
- Include personal or account identifiers only when they are facts required for this project.

## 10. Formatting

- Use no numeric filename prefixes; state reading order once.
- Use relative links within the pack and verify every link.
- Use tables for genuine comparisons or contract mappings, prose for rules, and checkboxes for final acceptance.
- Use task checkboxes only in an explicitly requested tactical addendum.
- Keep root agent instructions well under 150 lines and every document only as long as its non-obvious content requires.
