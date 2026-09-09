# PR Review

Two companion skills for the pull-request lifecycle, plus the sub-agents they
delegate to. Both skills live here because they share the same severity
vocabulary (`[Blocking]`/`[Issue]`/`[Suggestion]`/`[Nit]`) and one reads the
other's output.

## Skills

- `pr-review` — run a complete, verified code review of a PR and post it as ONE
  GitHub review with inline line-level comments and suggested changes.
  Instructions: `skills/pr-review/SKILL.md`.
- `address-pr-review` — address unresolved review comments from any reviewer,
  validating each finding before fixing or pushing back.
  Instructions: `skills/address-pr-review/SKILL.md`.

## Agents

- `agents/pr-reviewer.md` — forked into by `pr-review`.
- `agents/pr-review-responder.md` — spawned by `address-pr-review` after the
  target PR is resolved in the main context; has the skill preloaded.

## Usage

```text
/pr-review 123
/address-pr-review https://github.com/org/repo/pull/123
```

For `address-pr-review`, pass the PR URL (preferred), `org/repo#123`, or a bare
number. With no argument it targets the last PR this session opened or pushed
to; if there is none it lists your open PRs across all working directories and
asks. It never infers the PR from the current directory's branch, because the
shell cwd resets between commands and can point at the wrong repo.

## Development

Run the marketplace validator from the repository root after changes:

```bash
uv run --locked scripts/validate.py
```
