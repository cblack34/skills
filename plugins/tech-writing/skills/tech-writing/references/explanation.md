# Explanation

Explanation answers "why". The reader steps back from the work to understand the design, its context, and its trade-offs. This is the one doc type where opinion and history belong.

## Shape

```markdown
# <About X | Why X | How X works>

<Two or three sentences: the question this answers and the short answer.>

## <Aspect: the problem, the constraint, or the mechanism>
<Prose. Each paragraph makes one point and supports it.>

## Alternatives considered
<Only for design docs and ADRs: each option and why it lost, one paragraph each.>

## Consequences
<What this choice makes easy, what it makes hard, and when to revisit it.>
```

## Rules

- Bound it with one question. If a section does not help answer it, cut it or give it its own page.
- Give the short answer first, then the reasoning. A reader who stops after the first paragraph should still have the answer.
- Support claims with the specific cause: the constraint, number, incident, or requirement. "It was slow" becomes "p99 latency reached 4 s at 2,000 requests per second".
- Write in prose. Use a list only for parallel items such as options or consequences.
- Name trade-offs honestly, including what the chosen design costs.
- Link to the reference for exact values and to the how-to guide for steps.

## Leave out

Step-by-step instructions, full option tables, and a summary that repeats the opening.

Depth: [diataxis.fr/explanation](https://diataxis.fr/explanation/)
