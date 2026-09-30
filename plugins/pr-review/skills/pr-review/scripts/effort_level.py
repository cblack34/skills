#!/usr/bin/env python3
"""Pick a pr-review effort level from `gh pr view --json additions,deletions,files`.

Usage:
    gh pr view N --repo O/R --json additions,deletions,files | python3 effort_level.py
    python3 effort_level.py --self-test

Prints two lines: the level and the reason. Sensitive paths win, then
trivial-only PRs, then size. Stdlib only; deterministic.
"""

from __future__ import annotations

import json
import re
import sys

SENSITIVE = re.compile(
    r"(auth[nz]?|login|session|token|secret|crypt|password|payment|billing|"
    r"migrat|terraform|\.tf$|infra|deploy|\.github/workflows|dockerfile|helm|k8s)",
    re.IGNORECASE,
)
# ponytail: extension list, not a generated-file detector; extend when a real PR misclassifies
TRIVIAL = re.compile(
    r"(\.(md|mdx|txt|rst|lock|snap|svg|png|jpg|gif|ico|csv)$|"
    r"(^|/)(package-lock\.json|yarn\.lock|pnpm-lock\.yaml|uv\.lock|poetry\.lock|Cargo\.lock|go\.sum)$)",
    re.IGNORECASE,
)
LOW_MAX_LINES = 50
HIGH_MIN_LINES = 800


def pick(pr: dict) -> tuple[str, str]:
    paths = [f["path"] for f in pr.get("files", [])]
    lines = int(pr.get("additions", 0)) + int(pr.get("deletions", 0))
    hot = sorted({p for p in paths if SENSITIVE.search(p)})
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
    f = lambda *ps: [{"path": p} for p in ps]  # noqa: E731
    assert pick({"additions": 10, "deletions": 0, "files": f("src/auth/login.py")})[0] == "high"
    assert pick({"additions": 5, "deletions": 5, "files": f("infra/main.tf")})[0] == "high"
    assert pick({"additions": 900, "deletions": 0, "files": f("src/a.py")})[0] == "high"
    assert pick({"additions": 400, "deletions": 0, "files": f("README.md", "uv.lock")})[0] == "low"
    assert pick({"additions": 30, "deletions": 10, "files": f("src/a.py")})[0] == "low"
    assert pick({"additions": 200, "deletions": 12, "files": f("src/a.py", "tests/test_a.py")})[0] == "medium"
    assert pick({"additions": 0, "deletions": 0, "files": []})[0] == "low"
    print("ok")


def main(argv: list[str]) -> int:
    if "--self-test" in argv:
        _self_test()
        return 0
    level, reason = pick(json.load(sys.stdin))
    print(level)
    print(reason)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
