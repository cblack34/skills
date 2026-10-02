#!/usr/bin/env python3
"""Bump every plugin changed between two commits; CI runs this after a merge to main."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path
from typing import Sequence

sys.path.insert(0, str(Path(__file__).resolve().parent))
from bump_plugin_version import PLUGINS_ROOT, update_plugin_version  # noqa: E402

CONVENTIONAL_RE = re.compile(r"^(?P<type>[a-z]+)(?:\([^)]*\))?(?P<bang>!)?:")
MANIFESTS = {".claude-plugin/plugin.json", ".codex-plugin/plugin.json"}


def git(*args: str) -> str:
    return subprocess.run(["git", *args], check=True, capture_output=True, text=True).stdout


def bump_level(message: str) -> str:
    subject, _, body = message.partition("\n")
    match = CONVENTIONAL_RE.match(subject)
    if (match and match.group("bang")) or "BREAKING CHANGE" in body:
        return "major"
    if match and match.group("type") == "feat":
        return "minor"
    return "patch"


def changed_plugins(before: str, after: str) -> list[str]:
    base = f"{after}~1" if set(before) <= {"0"} else before
    changed: dict[str, set[str]] = {}
    for line in git("diff", "--name-only", base, after).splitlines():
        parts = Path(line).parts
        if len(parts) >= 3 and parts[0] == "plugins" and (PLUGINS_ROOT / parts[1]).is_dir():
            changed.setdefault(parts[1], set()).add("/".join(parts[2:]))
    # ponytail: a push touching only manifests is a bump itself; skip it so CI never re-bumps its own commit
    return sorted(p for p, files in changed.items() if not files <= MANIFESTS)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("before", help="Commit before the push (all zeros for a new branch)")
    parser.add_argument("after", help="Head commit of the push")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)

    level = bump_level(git("log", "-1", "--format=%s%n%b", args.after))
    try:
        for plugin in changed_plugins(args.before, args.after):
            current, target, _ = update_plugin_version(PLUGINS_ROOT, plugin, level, dry_run=args.dry_run)
            print(f"{plugin}: {current} -> {target} ({level})")
    except (OSError, ValueError, subprocess.CalledProcessError) as error:
        print(f"Version bump failed: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
