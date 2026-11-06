---
name: tech-writing
description: "Write and rewrite technical documentation that is typed, clear, and concise. Classifies each doc as a Diátaxis tutorial, how-to guide, reference, or explanation, drafts from a short recipe for that type with Google developer style and STE-inspired sentence limits, then runs a ranked review that cuts AI filler, hedging, padding, and stock phrases. Use whenever writing or rewriting a README, guide, tutorial, runbook, API or CLI reference, design doc, ADR, or any other technical doc, even if style is not mentioned. For existing docs, flags what does not conform but rewrites only when asked. Not for marketing copy, fiction, or code comments."
compatibility: Works offline. Web access is optional and only used to read the linked source pages for extra depth.
---

# Tech Writing

You already know Diátaxis, the Google developer documentation style guide, and plain-language writing. This skill decides which doc type you are writing, how long it may be, and what to cut before you hand it over.

The usual failure is not bad grammar. It is a doc that tries to teach, explain, list every option, and summarize itself all at once. Fix that by choosing one job for the doc and dropping everything that does not serve it.

## When this applies

- **Writing a new doc, or the user asked for a rewrite:** run the full workflow below.
- **Adding to or editing part of an existing doc:** write your new text to these rules. Keep the doc's local conventions (heading case, terms, voice) where they differ, so the doc stays consistent. Do not rewrite text you were not asked to touch.
- **Reading or using an existing doc without a rewrite request:** do not rewrite it. If it breaks these rules badly enough to mislead or slow a reader, add at most three one-line notes to your reply (see the format in [references/review.md](references/review.md#notes-on-existing-docs)) and offer a rewrite.

## Workflow

### 1. Classify

Pick one type per doc or page. Ask two questions: does the reader need to *do* something or *understand* something? Are they *learning* or *working*?

| | Learning | Working |
| --- | --- | --- |
| **Doing** | Tutorial: a lesson with one guided path | How-to guide: steps toward a goal the reader already has |
| **Understanding** | Explanation: why it is this way, context, trade-offs | Reference: facts to look up (options, fields, errors, limits) |

Common docs map like this:

- Runbook, playbook, setup guide, troubleshooting entry: how-to.
- API, CLI, config, schema, changelog, error catalog: reference.
- Design doc, ADR, architecture overview, "why we chose X": explanation.
- Getting-started lesson for newcomers: tutorial.
- README: a landing page, not a fifth type. Write one or two sentences on what the project is and who it is for. Then give the shortest working quickstart (a how-to), and link to the rest. Put no history, roadmap, or feature tour in it.

If a request mixes types, split them into separate docs or clearly separated sections and link between them. Do not blend a tutorial with its reference tables, or a how-to with design rationale.

Then read the one recipe that matches: [tutorial](references/tutorial.md), [how-to](references/how-to.md), [reference](references/reference.md), or [explanation](references/explanation.md).

### 2. Draft

Before writing, name the reader and the one thing they must be able to do or know when they finish. Every section must move them toward it. If a section answers a question this reader would not ask, leave it out.

Follow the recipe and [references/style.md](references/style.md). The rules you will need most often:

- Put the answer, command, or result first. No opener that says what the doc will cover, and no closer that repeats it.
- Keep instructions to 20 words or fewer and descriptions to 25 or fewer. Code, commands, paths, and URLs do not count. Write one instruction per sentence and keep one topic per paragraph.
- Write to "you" in the present tense and active voice. Put the condition before the instruction: "To enable caching, set `cache: true`."
- Use one term for each concept, and the same term every time.
- State what is true. Give the number, name, command, or error text instead of a general claim. Do not invent facts, versions, or citations; check the code or ask.
- Stop when the reader can act. Link to depth; do not inline it.

### 3. Review

Run [references/review.md](references/review.md) on the draft and fix what it finds. It is a ranked list of the tells that survive drafting, with the fix for each.

For a new doc longer than about one screen, test it on a fresh reader if your harness can start a sub-agent. Give the sub-agent only the doc and the reader's goal, not your reasoning. Ask it to list what it could not do or understand, and what it skipped as unneeded. Fix the gaps and cut what it skipped. If you cannot start a sub-agent, reread the doc as the named reader and do the same.

If the project already lints prose with [Vale](https://vale.sh/) (a `.vale.ini` at the repo root), run `vale <file>` and fix the findings. Do not add Vale to a project that does not use it.

## Output

Hand over the doc itself. In your reply, give the doc type you chose in one line and anything you could not verify. Keep those caveats out of the doc unless the reader needs them to act safely. Do not explain the style rules you applied.

## Sources

Read these only when a rule's edge is unclear. Everything needed to write correctly is in this skill.

- Diátaxis: [compass](https://diataxis.fr/compass/), [tutorials vs how-to guides](https://diataxis.fr/tutorials-how-to/), [reference vs explanation](https://diataxis.fr/reference-explanation/). The type guidance here is paraphrased from Diátaxis by Daniele Procida.
- [Google developer documentation style guide](https://developers.google.com/style), with its [highlights](https://developers.google.com/style/highlights) and [word list](https://developers.google.com/style/word-list). Google, CC BY 4.0.
- [The Elements of Agent Style](https://github.com/yzhao062/agent-style) by Yue Zhao, CC BY 4.0. Several review checks are adapted from its rules.
- Sentence limits are inspired by [ASD-STE100 Simplified Technical English](https://www.asd-ste100.org/). ASD-STE100 is a trademark of ASD; this skill does not apply the STE dictionary and makes no compliance claim.
