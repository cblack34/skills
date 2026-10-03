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
# Order matters in .gitignore because the last matching rule wins, so a repeated rule is
# dropped only when no negation has appeared since its previous occurrence (and a repeated
# negation only when no plain rule has). Comments always dedupe.
merge() {
  { [ -f "$1" ] && cat "$1" && echo; cat; } | awk '
    NR == 1 && $0 == "" { next }
    $0 == ""            { blank = 1; next }
    /^#/                { if (seen[$0]++) next }
    /^!/                { if (($0 in nl) && nl[$0] == pos) next; nl[$0] = pos; neg++ }
    !/^[#!]/            { if (($0 in pl) && pl[$0] == neg) next; pl[$0] = neg; pos++ }
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
  local ordered; ordered=$(printf '*.log\n!important.log\n*.log\n' | merge /dev/null)
  [ "$(grep -c '^\*\.log$' <<<"$ordered")" = 2 ] || { echo "rule repeated across a negation was dropped"; return 1; }
  local plain; plain=$(printf '*.log\n*.tmp\n*.log\n' | merge /dev/null)
  [ "$(grep -c '^\*\.log$' <<<"$plain")" = 1 ] || { echo "plain duplicate not collapsed"; return 1; }
  printf 'secrets.env' > "$dir/no-newline"
  local joined; joined=$(printf '# Created by gitignore.io\n*.pyc\n' | merge "$dir/no-newline")
  [ "$(grep -c '^secrets.env$' <<<"$joined")" = 1 ] || { echo "last line without newline was glued to the template"; return 1; }
  printf '# Created by gitignore.io\n\n### Nothing ###\n' | has_rules && { echo "header-only template accepted"; return 1; }
  echo "self-check ok"
}

if [ "${1:-}" = "--check" ]; then self_check; exit; fi

TEMPLATES="$DEFAULTS"
for t in "$@"; do TEMPLATES="$TEMPLATES,$t"; done
fetched=$(curl -fsSL "$API/$TEMPLATES")
printf '%s\n' "$fetched" | has_rules || { echo "No rules returned for '$TEMPLATES'; check names at $API/list?format=lines" >&2; exit 1; }
tmp=$(mktemp "$FILE.XXXXXX"); trap 'rm -f "$tmp"' EXIT
printf '%s\n' "$fetched" | merge "$FILE" > "$tmp" && mv "$tmp" "$FILE"
echo "Wrote $FILE with templates: $TEMPLATES"
