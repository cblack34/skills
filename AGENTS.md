# Marketplace maintenance

These instructions apply to the entire repository.

## Source of truth

- Keep reusable instructions in `plugins/<plugin>/skills/<skill>/SKILL.md`.
- Keep shared workflow instructions in `SKILL.md`. Keep plugin-level harness metadata in `.claude-plugin/` and `.codex-plugin/`; use skill-local `agents/openai.yaml` only for Codex UI or invocation policy that has no portable equivalent.
- Group only closely related skills in the same plugin. Use separate plugins when skills should be installed or versioned independently.
- Keep every runtime dependency inside its plugin directory. Installed plugins cannot safely reference sibling directories.

## Adding a skill

- Run `uv run --locked scripts/new_skill.py <name> --description <description>` from the repository root.
- Use lowercase kebab-case names no longer than 64 characters.
- Before creating a skill inside an existing plugin, confirm that placement with the user.
- Keep the plugin folder name and both plugin manifest names identical. Keep each skill folder name identical to its `SKILL.md` frontmatter name.
- Do not hand-edit only one marketplace catalog. The Claude and Codex catalogs must contain the same plugin names in the same order.
- Do not leave placeholder instructions in a published skill.

## Changing a skill

- Preserve cross-harness behavior in the shared `SKILL.md`; isolate unavoidable harness differences in clearly labeled sections.
- Bump the version in both plugin manifests when publishing changes to an existing plugin.
- Do not add secrets, credentials, machine-specific absolute paths, or private source material.
- Prefer deterministic helper scripts for mechanical work and keep them inside the owning skill.

## Verification

- Manage Python and Python dependencies with `uv`; do not introduce `pip`, Poetry, or ad hoc virtual-environment instructions.
- Run `uv lock --check` and `uv run --locked scripts/validate.py` after every marketplace or plugin change.
- If Claude Code is installed, also run `claude plugin validate .`.
- If Grok is installed, run `grok plugin validate plugins/<plugin>` for each changed plugin.
- Review `git diff --check` before committing.
