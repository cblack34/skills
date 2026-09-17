# Build Pack Workflow

Create or transition a strategic documentation package, lead its implementation through approved rolling slices, and turn each passing draft into a maintainable handoff.

Three skills that build on each other, with explicitly separated responsibilities:

- `skills/create-build-pack/SKILL.md` authors or audits the durable strategic contract, including the cold-read transition from a delivered pack to new feature work.
- `skills/implement-build-pack/SKILL.md` proposes and executes one approved slice at a time, using durable slice plans, GitHub issues, and right-sized execution agents.
- `skills/refactor-before-handoff/SKILL.md` takes a behaviorally passing diff through a design pass, justified refactors, a fresh-context read-only design review, re-verification, and a receipt. `implement-build-pack` runs it before PR preparation; it also works on any diff without a build pack.

The implementation skill is manual-only. It prepares reviewed, green PRs, but only the human may physically merge to `main`.

## Agents

- `agents/design-reviewer.md` — read-only, fresh-context design reviewer spawned by `refactor-before-handoff`. Returns a receipt to the implementation lead; never edits or posts to GitHub. Generated packs document a fallback (fresh read-only sub-agent or human review) for harnesses without plugin agents.

## Development

Run the marketplace validator from the repository root after changes:

```bash
uv run --locked scripts/validate.py
```
