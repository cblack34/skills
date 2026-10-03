---
name: gitignore
description: "Create or update a repository .gitignore from gitignore.io templates: always the Windows, macOS, Linux, VS Code, and JetBrains defaults plus the stack templates you name, merged without losing existing custom rules. Use when asked to add or refresh a .gitignore for a language, framework, OS, or editor. Not for ignoring a single path; append that line directly."
---

# Gitignore

Templates are named categories such as `python`, `node`, `terraform`, or `macos` that expand into many rules. This skill is for templates. A single path or pattern the user already knows is not a template: append it to `.gitignore` as a plain line and stop. The merge below keeps such lines in place, so they survive later runs.

## Workflow

1. Identify the stack's template names from the repository (lockfiles, manifests, build files). Check an unfamiliar name against `https://www.toptal.com/developers/gitignore/api/list?format=lines`.
2. From the target repository's root, run the bundled script with those names. It lives in this skill's base directory, not in the target repository. The OS and editor defaults are always included, so pass only the stack:

   ```bash
   bash "<skill base dir>/scripts/merge_gitignore.sh" python node
   ```

   The script fetches the templates, merges them with any existing `.gitignore` while keeping every existing line that is not in the template, removes duplicates, collapses blank runs, and writes atomically. If the API returns a header-only body, which is what an unknown template name produces, the script exits non-zero and leaves the file untouched.
3. Report the templates applied. If a name was rejected, say which and offer the closest names from the list endpoint.

Run `bash "<skill base dir>/scripts/merge_gitignore.sh" --check` to exercise the merge logic offline.
