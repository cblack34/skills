#!/usr/bin/env bash
# Create or update ./.gitignore from gitignore.io templates.
# Usage: merge_gitignore.sh [TEMPLATE...]   e.g. merge_gitignore.sh python node
#        merge_gitignore.sh --check         run the offline self-check
# The Windows, macOS, Linux, VS Code, and JetBrains templates are always included.
# Existing lines that are not in the fetched template are kept in place, so one-off
# paths appended by hand survive. Unknown template names make the API return a
# header-only body; that is treated as a failure and the file is left untouched.
set -euo pipefail

DEFAULTS="windows,macos,linux,visualstudiocode,jetbrains+all"
API="https://www.toptal.com/developers/gitignore/api"
FILE=".gitignore"

# stdin: fetched template. $1: existing file, may be absent. stdout: merged content.
merge() {
  { [ -f "$1" ] && cat "$1"; cat; } | awk '
    NR == 1 && $0 == "" { next }
    $0 == ""            { blank = 1; next }
    seen[$0]++          { next }
    blank               { print ""; blank = 0 }
                        { print }'
}

# Fail unless stdin holds at least one line that is neither blank nor a comment.
has_rules() { grep -qvE '^[[:space:]]*(#|$)'; }

self_check() {
  local dir; dir=$(mktemp -d); trap 'rm -rf "$dir"' RETURN
  printf '# mine\nsecrets.env\n\n\n*.pyc\n' > "$dir/.gitignore"
  local template=$'# Created by gitignore.io\n\n### Python ###\n*.pyc\n__pycache__/\n\n\n### Python ###\n'
  local out; out=$(printf '%s' "$template" | merge "$dir/.gitignore")
  [ "$(grep -c '^secrets.env$' <<<"$out")" = 1 ] || { echo "custom rule lost"; return 1; }
  [ "$(grep -c '^\*\.pyc$' <<<"$out")" = 1 ]    || { echo "duplicate not collapsed"; return 1; }
  [ "$(grep -c '^### Python ###$' <<<"$out")" = 1 ] || { echo "duplicate header not collapsed"; return 1; }
  ! grep -qE '^$' <(printf '%s\n' "$out" | awk 'prev=="" && $0=="" {print} {prev=$0}') || { echo "blank run not collapsed"; return 1; }
  [ "$(head -1 <<<"$out")" = "# mine" ] || { echo "order not preserved"; return 1; }
  printf '# Created by gitignore.io\n\n### Nothing ###\n' | has_rules && { echo "header-only template accepted"; return 1; }
  echo "self-check ok"
}

if [ "${1:-}" = "--check" ]; then self_check; exit; fi

TEMPLATES="$DEFAULTS"
for t in "$@"; do TEMPLATES="$TEMPLATES,$t"; done
fetched=$(curl -fsSL "$API/$TEMPLATES")
printf '%s\n' "$fetched" | has_rules || { echo "No rules returned for '$TEMPLATES'; check names at $API/list?format=lines" >&2; exit 1; }
printf '%s\n' "$fetched" | merge "$FILE" > "$FILE.tmp" && mv "$FILE.tmp" "$FILE"
echo "Wrote $FILE with templates: $TEMPLATES"
