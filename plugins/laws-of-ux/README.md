# Laws of UX

Design and review user interfaces against the Laws of UX and Nielsen's 10 usability heuristics. Design mode applies them while building or changing a screen, form, flow, or component; review mode hands the UI to a fresh reviewer that reports ranked, evidence-backed findings with fixes. Use whenever building or changing UI, even if UX is not mentioned, and when asked for a UX review, UI review, usability audit, or heuristic evaluation, or when Fitts's Law, Hick's Law, or another Law of UX comes up. Not for visual branding or aesthetics, or a WCAG conformance audit.

The shared skill instructions are in `skills/laws-of-ux/SKILL.md`.

The check table, severity scale, and report format are adapted from the `ux-review` skill in [rolemodel/rolemodel-skills](https://github.com/rolemodel/rolemodel-skills), Copyright (c) 2026 Rolemodel Software, used under the MIT License; see `LICENSE-rolemodel`.

## Development

Run the marketplace validator from the repository root after changes:

```bash
uv run --locked scripts/validate.py
```
