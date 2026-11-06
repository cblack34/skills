# Review

Run this after drafting. Read the whole draft once per section below, in order. The sections are ranked: structure problems cost the reader the most, so fix them first.

Fix each problem at its cause. Do not swap a flagged word for a synonym. Find the specific fact the vague phrase stood in for, and write that instead. If there is no fact behind it, delete the phrase.

When rewriting someone else's doc, keep every fact, command, and warning it had unless it is wrong or out of scope. Do not add facts you have not verified.

## 1. Structure and type

Fix each of these on a single sighting.

- **Mixed types.** The doc teaches *and* explains *and* lists options. Find sections that belong to another type (a "How it works" section in a how-to, a "Why" section in a reference, internals in a README) and move them out or link to them.
- **Sections the reader did not need.** Delete any section that does not serve the named reader's goal, such as a feature tour, history, roadmap, a "Benefits" list, or troubleshooting for failures nobody hits.
- **Announcing openers.** "This guide covers…", "In this document, we will…", "Overview" sections that restate the title. Start with the content.
- **Closing summaries.** "In summary", "Conclusion", "Key takeaways", or a last paragraph that restates the doc. Delete it. If the point survives without it, it stays deleted.
- **Prose chopped into bullets.** Bullets that are really reasoning ("because", "so", "which means") belong in a paragraph. Keep lists for steps and parallel items.
- **Bold-label bullets.** `- **Conflicts.** Two PRs…`. Unless the list is a glossary, write the label into the sentence or turn the list into prose or a table.
- **Heading inflation.** Headings over one or two sentences. Merge them into the parent section.

## 2. Claims

Fix each of these on a single sighting.

- **Invented specifics.** Versions, flags, numbers, file paths, or citations you did not read in the code, docs, or output. Verify them or remove them.
- **Inflated significance.** "Plays a crucial role", "is a key part of", "a powerful way to", "ensures seamless". State what it does.
- **Hedging stacks.** "May potentially", "could possibly", "it might be worth considering", "generally tends to". Say it, or say exactly when it is not true.
- **Throat-clearing.** "It is important to note that", "It's worth mentioning", "Keep in mind that". Delete the frame and keep the fact.
- **Vague attribution.** "Experts recommend", "It is widely considered", "best practice is". Name the source or drop the claim.

## 3. Sentences

These are weaker signs. Fix them when there are several in one section or the same one recurs.

- Sentences over the 20-word or 25-word limit in [style.md](style.md#sentences).
- Passive voice that hides who acts.
- Forms of "will" for normal behavior.
- Sentences that announce the next sentence ("Here's how it works:" before a list is fine; "Let's take a look at" is not).
- Three consecutive sentences that open the same way.
- Transition chains: "Additionally", "Furthermore", "Moreover", "Notably". Usually delete them; the order already shows the link.
- "Not X, but Y" and "It's not just X, it's Y" contrasts set up to sound insightful. State Y.
- Lists of exactly three adjectives or clauses for rhythm ("fast, reliable, and scalable"). Keep only the ones you can back with a fact.
- Em dashes used as general punctuation. Use a period, comma, colon, or parentheses. A dash in a range or a code literal is fine.
- Stock metaphors: "dive into", "deep dive", "unlock", "under the hood", "the heart of", "game changer", "paves the way", "in today's world".
- Words from the [style word list](style.md#words): "simply", "just", "easy", "leverage", "utilize", "robust", "seamless".

## 4. Format

- Headings in sentence case, with no emoji and no ending punctuation.
- Code, paths, and commands in code font. Every command in a copyable block.
- Link text that names the destination.
- No bold for emphasis.

## 5. Final scan

Scan the whole doc once more for the three tells most likely to survive a rewrite: a closing summary, bold-label bullets, and a section from another doc type. Then check that the doc is no longer than its reader needs. If you can delete a sentence without the reader losing anything, delete it.

## Notes on existing docs

When you read an existing doc without a rewrite request, do not rewrite it. If it has problems from sections 1 or 2 that would mislead or slow a reader, add at most three notes to your reply, then offer a rewrite:

```markdown
Doc notes for `docs/deploy.md` (not changed):
- Mixes how-to and explanation: "How the pipeline works" (line 40) belongs on its own page.
- Step 4 names flag `--force-sync`, which `deploy --help` does not list.
Want me to rewrite it?
```

Skip sections 3 and 4 in notes. They are not worth interrupting the user for.

Adapted in part from the rules in [The Elements of Agent Style](https://github.com/yzhao062/agent-style) by Yue Zhao (CC BY 4.0). For more tells and their background, see Wikipedia's [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing).
