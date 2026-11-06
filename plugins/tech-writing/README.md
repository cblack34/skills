# Tech Writing

Write and rewrite technical documentation that is typed, clear, and concise. Classifies each doc as a Diátaxis tutorial, how-to guide, reference, or explanation, drafts from a short recipe for that type with Google developer style and STE-inspired sentence limits, then runs a ranked review that cuts AI filler, hedging, padding, and stock phrases. Use whenever writing or rewriting a README, guide, tutorial, runbook, API or CLI reference, design doc, ADR, or any other technical doc, even if style is not mentioned. For existing docs, flags what does not conform but rewrites only when asked. Not for marketing copy, fiction, or code comments.

The shared skill instructions are in `skills/tech-writing/SKILL.md`.

## Sources

- Doc types are paraphrased from [Diátaxis](https://diataxis.fr/) by Daniele Procida.
- Style rules are a subset of the [Google developer documentation style guide](https://developers.google.com/style), CC BY 4.0.
- Several review checks are adapted from [The Elements of Agent Style](https://github.com/yzhao062/agent-style) by Yue Zhao, CC BY 4.0.
- Sentence limits are inspired by [ASD-STE100 Simplified Technical English](https://www.asd-ste100.org/). ASD-STE100 is a trademark of ASD. This plugin does not use the STE dictionary and makes no compliance claim.

## Development

Run the marketplace validator from the repository root after changes:

```bash
uv run --locked scripts/validate.py
```
