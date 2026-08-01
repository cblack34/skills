# Build Pack Workflow

Create a strategic documentation package, then lead its implementation through approved, rolling slices.

This closely related plugin contains two explicitly separated responsibilities:

- `skills/build-doc-pack/SKILL.md` authors or audits the durable strategic contract.
- `skills/implement-build-pack/SKILL.md` proposes and executes one approved slice at a time, using durable slice plans, GitHub issues, and right-sized execution agents.

The implementation skill is manual-only. It prepares reviewed, green PRs, but only the human may physically merge to `main`.

## Development

Run the marketplace validator from the repository root after changes:

```bash
uv run --locked scripts/validate.py
```
