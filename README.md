# Clayton's Agent Skills

A personal marketplace for reusable agent skills. Each skill is packaged once and exposed through the native plugin catalogs used by Codex and Claude Code. Grok consumes the Claude-compatible catalog directly.

## Compatibility

| Harness | Catalog | Support |
| --- | --- | --- |
| Codex | `.agents/plugins/marketplace.json` | Native |
| Claude Code and the Code tab in Claude Desktop | `.claude-plugin/marketplace.json` | Native |
| Grok | `.claude-plugin/marketplace.json` | Native Claude-compatibility layer |

The skill instructions themselves live only once, under `plugins/<plugin>/skills/<skill>/SKILL.md`. Harness-specific files contain packaging metadata, not duplicated prompts.

## Add a skill

The repository targets Python 3.14 through `.python-version` and `pyproject.toml`. Install [uv](https://docs.astral.sh/uv/getting-started/installation/) if needed, then create the locked project environment:

```bash
uv sync --locked
```

Create a new plugin with its primary skill from the repository root:

```bash
uv run --locked scripts/new_skill.py my-skill \
  --description "Explain when the agent should use this skill."
```

Then:

1. Replace the generated workflow in `plugins/my-skill/skills/my-skill/SKILL.md` with the real instructions.
2. Add any supporting `scripts/`, `references/`, or `assets/` inside that skill directory.
3. When releasing changes to an existing plugin, update both manifest versions together:

    ```bash
    uv run --locked scripts/bump_plugin_version.py my-skill minor
    ```

Use `major`, `minor`, `patch`, or an explicit semantic version. Add `--dry-run` to preview the change without writing either manifest.

4. Validate the complete marketplace:

```bash
uv run --locked scripts/validate.py
```

The generator creates both plugin manifests and appends matching entries to both catalogs. Separate plugins remain the default when skills should be installed or versioned independently; closely related companion skills may share a plugin after confirming that placement with the user. Add future Python dependencies with `uv add` or development-only dependencies with `uv add --dev` so `pyproject.toml` and `uv.lock` stay synchronized.

## Repository layout

```text
.
├── .agents/plugins/marketplace.json       # Codex catalog
├── .claude-plugin/marketplace.json        # Claude and Grok catalog
├── .python-version                        # uv-managed Python version
├── pyproject.toml                         # Python project and dependencies
├── uv.lock                                # Reproducible uv lockfile
├── plugins/
│   └── <plugin>/
│       ├── .claude-plugin/plugin.json
│       ├── .codex-plugin/plugin.json
│       ├── README.md
│       └── skills/
│           ├── <primary-skill>/SKILL.md
│           └── <related-companion>/          # optional
│               ├── SKILL.md
│               └── agents/openai.yaml        # optional Codex metadata
└── scripts/
    ├── bump_plugin_version.py
    ├── new_skill.py
    └── validate.py
```

Everything needed at runtime must stay inside its plugin directory. Marketplace installers cache plugins independently, so a plugin must not depend on paths such as `../shared`.

## Install the marketplace

Until the repository is pushed, replace `cblack34/skills` with the local checkout path.

### Codex

```bash
codex plugin marketplace add cblack34/skills
codex plugin list
codex plugin add <plugin-name>@cblack34-skills
```

### Claude Code or Claude Desktop

```bash
claude plugin marketplace add cblack34/skills
claude plugin install <plugin-name>@cblack34-skills
```

Configured marketplaces also appear in the plugin browser in the Code tab of Claude Desktop.

### Grok

```bash
grok plugin marketplace add cblack34/skills
```

Open `/marketplace` in Grok and install the plugin from `cblack34-skills`. Grok reads the Claude marketplace, plugin, and skill formats without a separate Grok manifest.

## Local validation

The repository validator checks catalog parity, paths, manifest names and versions, plugin self-containment, and basic `SKILL.md` frontmatter. When the harness CLIs are installed, their native validators are useful additional checks:

```bash
uv lock --check
uv run --locked scripts/validate.py
claude plugin validate .
grok plugin validate plugins/<plugin-name>
```

Codex plugins are validated individually by the Codex app during ingestion.
