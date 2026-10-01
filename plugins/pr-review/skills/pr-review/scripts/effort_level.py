#!/usr/bin/env python3
"""Pick a pr-review effort level from the PR's changed-file list.

Usage:
    gh api repos/O/R/pulls/N/files --paginate | python3 effort_level.py
    python3 effort_level.py --self-test

Input is the REST "list pull request files" payload: file objects with
`filename`, `additions` and `deletions`. `--paginate` prints one JSON array per
page; any number of concatenated arrays is accepted, so PRs past 100 files are
fully seen (`gh pr view --json files` caps at 100).

Prints two lines: the level and the reason. Sensitive paths win, then
trivial-only PRs, then size. Stdlib only; deterministic.
"""

from __future__ import annotations

import json
import re
import sys

# Matched against whole path tokens (split on anything non-alphanumeric), not
# substrings, so `docs/authoring.md` or `author.md` is not "auth".
SENSITIVE_TOKENS = frozenset(
    "auth authn authz oauth oauth2 authentication authorization authorize "
    "login session sessions token tokens secret secrets crypto encryption "
    "password passwords payment payments billing migration migrations migrate "
    "terraform infra infrastructure deploy deployment helm k8s dockerfile".split()
)
# ponytail: extension list, not a generated-file detector; extend when a real PR misclassifies
TRIVIAL = re.compile(
    r"(\.(md|mdx|txt|rst|lock|snap|svg|png|jpg|gif|ico|csv)$|"
    r"(^|/)(package-lock\.json|yarn\.lock|pnpm-lock\.yaml|uv\.lock|poetry\.lock|Cargo\.lock|go\.sum)$)",
    re.IGNORECASE,
)
TERRAFORM_SUFFIXES = (".tf", ".tfvars", ".tf.json", ".tfvars.json", ".hcl")
LOW_MAX_LINES = 50
HIGH_MIN_LINES = 800


def _sensitive(path: str) -> bool:
    lower = path.lower()
    if lower.endswith(TERRAFORM_SUFFIXES) or ".github/workflows/" in lower:
        return True
    return any(t in SENSITIVE_TOKENS for t in re.split(r"[^a-z0-9]+", lower))


def _load(text: str) -> list[dict]:
    """Flatten one or more concatenated JSON arrays (gh api --paginate)."""
    dec, i, out = json.JSONDecoder(), 0, []
    while i < len(text):
        if text[i].isspace():
            i += 1
            continue
        val, i = dec.raw_decode(text, i)
        out.extend(val if isinstance(val, list) else [val])
    return out


def pick(files: list[dict]) -> tuple[str, str]:
    paths = [f["filename"] for f in files]
    # A rename carries the old path in `previous_filename`; scan both.
    scanned = paths + [f["previous_filename"] for f in files if f.get("previous_filename")]
    lines = sum(int(f.get("additions", 0)) + int(f.get("deletions", 0)) for f in files)
    hot = sorted({p for p in scanned if _sensitive(p)})
    if hot:
        return "high", f"sensitive paths: {', '.join(hot[:3])}{'…' if len(hot) > 3 else ''}"
    if paths and all(TRIVIAL.search(p) for p in paths):
        return "low", f"{len(paths)} docs/lock/asset files only"
    if lines > HIGH_MIN_LINES:
        return "high", f"{lines} changed lines"
    if lines <= LOW_MAX_LINES:
        return "low", f"{lines} changed lines, no sensitive paths"
    return "medium", f"{lines} changed lines, no sensitive paths"


def _self_test() -> None:
    def f(*specs: tuple[str, int]) -> list[dict]:
        return [{"filename": n, "additions": a, "deletions": 0} for n, a in specs]

    assert pick(f(("src/auth/login.py", 10)))[0] == "high"
    assert pick(f(("src/oauth/callback.py", 5)))[0] == "high"
    assert pick(f(("infra/main.tf", 5)))[0] == "high"
    for tf in ("prod.tfvars", "main.tf.json", "prod.tfvars.json", "root.hcl"):
        assert pick(f((tf, 5)))[0] == "high", tf
    # a rename out of a sensitive path is still sensitive
    renamed = [{"filename": "src/login.py", "previous_filename": "auth/login.py",
                "status": "renamed", "additions": 1, "deletions": 1}]
    assert pick(renamed)[0] == "high"
    assert pick(f(("src/a.py", 900)))[0] == "high"
    assert pick(f(("README.md", 200), ("uv.lock", 200)))[0] == "low"
    assert pick(f(("src/a.py", 40)))[0] == "low"
    assert pick(f(("src/a.py", 100), ("tests/test_a.py", 112)))[0] == "medium"
    assert pick([])[0] == "low"
    # negative: auth as a substring of an ordinary word is not sensitive
    assert pick(f(("docs/authoring.md", 10)))[0] == "low"
    assert pick(f(("docs/author.md", 10), ("src/authority.py", 10)))[0] == "low"
    # sensitive file past the first page (100+ files) is still seen
    many = f(*[(f"docs/{i}.md", 1) for i in range(150)], ("deploy/run.sh", 1))
    assert pick(many)[0] == "high"
    # concatenated pages, as printed by `gh api --paginate`
    pages = json.dumps(f(("a.md", 1))) + json.dumps(f(("src/session.py", 1)))
    assert pick(_load(pages))[0] == "high"
    # blank or non-JSON stdin is a fetch failure, not a zero-file PR
    import io
    for bad in ("", "  \n", "not json"):
        sys.stdin = io.StringIO(bad)
        assert main([]) != 0, repr(bad)
    sys.stdin = io.StringIO("[]")
    assert main([]) == 0
    print("ok")


def main(argv: list[str]) -> int:
    if "--self-test" in argv:
        _self_test()
        return 0
    text = sys.stdin.read()
    if not text.strip():
        print("effort_level: empty input; the file-list fetch likely failed", file=sys.stderr)
        return 2
    try:
        level, reason = pick(_load(text))
    except (ValueError, KeyError, TypeError) as e:
        print(f"effort_level: invalid file-list input: {e}", file=sys.stderr)
        return 2
    print(level)
    print(reason)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
