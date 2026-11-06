# Style

A subset of the Google developer documentation style guide plus sentence limits inspired by ASD-STE100. Where a project has its own style guide, follow it instead.

## Sentences

- Keep instructions to 20 words or fewer and descriptions to 25 or fewer. Code, commands, paths, and URLs do not count. Split a longer sentence at its "and", "which", or "so that".
- Write one instruction per sentence. "Run `make build`, then deploy." becomes two numbered steps.
- Put the condition or goal before the instruction: "To skip tests, add `--no-test`." "If the build fails, check the log."
- Use active voice with a named actor: "The scheduler retries the job." Use passive voice only when the actor is unknown or does not matter.
- Write in the present tense. Use "will" only for something that happens later in time, not for the system's normal behavior.
- Address the reader as "you". Tutorials may use "we" for steps taken together. Do not use "I", "our team", or "let's".
- Keep articles and verbs. Do not write telegraphically ("Run script, check output").
- Limit noun stacks to three words. "Cluster node pool autoscaler configuration" becomes "the autoscaler configuration for the node pool".
- Contractions are fine.

## Paragraphs

- Write one topic per paragraph, with its point in the first sentence.
- Keep paragraphs to about six sentences. Most should be shorter.

## Words

- Use the plainest word: "use", not "leverage" or "utilize". "Start", not "initiate". "Help", not "facilitate". "Method", not "methodology".
- Use one term per concept. Do not rotate synonyms for variety: if it is a "workspace", it is never also a "project" or "environment".
- Do not tell the reader a step is easy. Drop "simply", "just", "easy", "easily", "quickly", and "obviously". Say "just" only to compare: "just one flag, not a config file".
- Drop "please" from instructions.
- Do not claim "best", "powerful", "seamless", "robust", or "blazing fast". Give the fact that would justify the word, or cut it.
- Define an abbreviation the first time you use it, unless your reader uses it every day (API, URL, CLI).

## Formatting

- Use sentence case for headings: "Configure the proxy", not "Configure The Proxy". Do not end headings with punctuation, and put no emoji in them.
- Use numbered lists for steps in order, bulleted lists for items in no order, and tables for items that share attributes. Write everything else as prose.
- Format code, commands, file names, paths, flags, and literal values as `code`. Bold UI elements the reader clicks. Do not bold for emphasis, and do not start bullets with a bolded label unless the list is a glossary.
- Make link text describe the destination: "see the [proxy settings](...)", not "[click here](...)" or a bare URL.
- Put every command in a code block the reader can copy, with its language tag. Show expected output when it confirms success.
- Use a note or warning only for something that would hurt the reader if missed. Use at most one per section.

## Timeless

Describe the product as it is now. Do not write "new", "currently", "now supports", "as of this release", or "coming soon". Put version history in a changelog.

Depth: [Google style highlights](https://developers.google.com/style/highlights), [word list](https://developers.google.com/style/word-list), [voice](https://developers.google.com/style/voice), [tense](https://developers.google.com/style/tense), [clause order](https://developers.google.com/style/clause-order), [procedures](https://developers.google.com/style/procedures), [lists](https://developers.google.com/style/lists), [link text](https://developers.google.com/style/link-text), [timeless documentation](https://developers.google.com/style/timeless-documentation).
