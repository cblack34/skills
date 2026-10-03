#!/usr/bin/env bash
# Create or update ./.gitignore from gitignore.io templates.
# Usage: merge_gitignore.sh [TEMPLATE...]   e.g. merge_gitignore.sh python node
#        merge_gitignore.sh --check         run the offline self-check
# The Windows, macOS, Linux, VS Code, and JetBrains templates are always included.
# The fetched templates come first and the existing file's lines follow, so project-specific
# rules and exceptions keep last-match precedence and one-off paths appended by hand survive.
# Every requested template must appear as a "### Name ###" header in the response; otherwise
# the script fails and the file is left untouched.
set -euo pipefail

DEFAULTS="windows,macos,linux,visualstudiocode,jetbrains+all"
API="https://www.toptal.com/developers/gitignore/api"
FILE=".gitignore"

# stdin: fetched template. $1: existing file, may be absent. stdout: template then existing, merged.
# Order matters in .gitignore because the last matching rule wins, so a repeated rule is
# dropped only when no negation has appeared since its previous occurrence (and a repeated
# negation only when no plain rule has). Comments always dedupe.
merge() {
  { cat; if [ -f "$1" ]; then echo; cat "$1" || { echo "Cannot read $1" >&2; exit 1; }; fi; } | awk '
                        { sub(/\r$/, "") }
    NR == 1 && /^[[:space:]]*$/ { next }
    /^[[:space:]]*$/    { blank = 1; next }
    /^#/                { if (seen[$0]++) next }
    /^!/                { if (($0 in nl) && nl[$0] == pos) next; nl[$0] = pos; neg++ }
    !/^[#!]/            { if (($0 in pl) && pl[$0] == neg) next; pl[$0] = neg; pos++ }
    blank               { print ""; blank = 0 }
                        { print }'
}

# Fail unless $1 contains the "### Name ###" header the API emits for template $2 (case-insensitive).
has_template() { grep -qi "^### $2 ###" <<<"$1"; }

# Fail unless $1 holds at least one line that is neither blank nor a comment.
# A here-string, not a pipe: grep -q exits early and would SIGPIPE a large producer under pipefail.
has_rules() { grep -qvE '^[[:space:]]*(#|$)' <<<"$1"; }

self_check() {
  local dir; dir=$(mktemp -d); trap 'rm -rf "$dir"' RETURN
  printf '# mine\nsecrets.env\n\n\n*.pyc\n' > "$dir/.gitignore"
  local template=$'# Created by gitignore.io\n\n### Python ###\n*.pyc\n__pycache__/\n\n\n### Python ###\n'
  local out; out=$(printf '%s' "$template" | merge "$dir/.gitignore")
  [ "$(grep -c '^secrets.env$' <<<"$out")" = 1 ] || { echo "custom rule lost"; return 1; }
  [ "$(grep -c '^\*\.pyc$' <<<"$out")" = 1 ]    || { echo "duplicate not collapsed"; return 1; }
  [ "$(grep -c '^### Python ###$' <<<"$out")" = 1 ] || { echo "duplicate header not collapsed"; return 1; }
  ! grep -qE '^$' <(printf '%s\n' "$out" | awk 'prev=="" && $0=="" {print} {prev=$0}') || { echo "blank run not collapsed"; return 1; }
  [ "$(head -1 <<<"$out")" = "# Created by gitignore.io" ] || { echo "template does not come first"; return 1; }
  [ "$(tail -1 <<<"$out")" = "secrets.env" ] || { echo "existing rules do not come last"; return 1; }
  local prec; prec=$(printf '*.log\n' | merge <(printf '*.log\n!important.log\n'))
  [ "$prec" = $'*.log\n\n!important.log' ] || { echo "existing exception lost last-match precedence: $prec"; return 1; }
  has_template "$(printf '### Python ###\n*.pyc\n')" python || { echo "present template not detected"; return 1; }
  has_template "$(printf '### Python ###\n*.pyc\n')" node && { echo "missing template not detected"; return 1; }
  local ordered; ordered=$(printf '*.log\n!important.log\n*.log\n' | merge /dev/null)
  [ "$(grep -c '^\*\.log$' <<<"$ordered")" = 2 ] || { echo "rule repeated across a negation was dropped"; return 1; }
  local plain; plain=$(printf '*.log\n*.tmp\n*.log\n' | merge /dev/null)
  [ "$(grep -c '^\*\.log$' <<<"$plain")" = 1 ] || { echo "plain duplicate not collapsed"; return 1; }
  printf 'secrets.env' > "$dir/no-newline"
  local joined; joined=$(printf '# Created by gitignore.io\n*.pyc\n' | merge "$dir/no-newline")
  [ "$(grep -c '^secrets.env$' <<<"$joined")" = 1 ] || { echo "last line without newline was glued to the template"; return 1; }
  has_rules $'# Created by gitignore.io\n\n### Nothing ###\n' && { echo "header-only template accepted"; return 1; }
  local crlf; crlf=$(printf 'secrets.env\r\n\r\n   \r\n*.pyc\r\n' | merge /dev/null)
  [ "$crlf" = $'secrets.env\n\n*.pyc' ] || { echo "CRLF or whitespace-only lines not normalized"; return 1; }
  local escaped; escaped=$(printf 'literal\\ \n' | merge /dev/null)
  [ "$escaped" = 'literal\ ' ] || { echo "escaped trailing space was altered"; return 1; }
  if [ "$(id -u)" != 0 ]; then
    printf 'keep\n' > "$dir/unreadable"; chmod 000 "$dir/unreadable"
    if printf '*.pyc\n' | merge "$dir/unreadable" >/dev/null 2>&1; then echo "unreadable file was silently replaced"; return 1; fi
  fi
  local big; big=$(printf '%s\n' "# header" "$(seq -f 'rule-%g' 1 200000)")
  has_rules "$big" || { echo "large template rejected"; return 1; }
  echo "self-check ok"
}

if [ "${1:-}" = "--check" ]; then self_check; exit; fi

[ ! -e "$FILE" ] || [ -r "$FILE" ] || { echo "Cannot read $FILE; refusing to overwrite it" >&2; exit 1; }
TEMPLATES="$DEFAULTS"
for t in "$@"; do TEMPLATES="$TEMPLATES,$t"; done
fetched=$(curl -fsSL "$API/$TEMPLATES")
has_rules "$fetched" || { echo "No rules returned for '$TEMPLATES'; check names at $API/list?format=lines" >&2; exit 1; }
for t in "$@"; do
  has_template "$fetched" "$t" || { echo "Template '$t' not found in the response; check names at $API/list?format=lines" >&2; exit 1; }
done
tmp=$(mktemp "$FILE.XXXXXX"); trap 'rm -f "$tmp"' EXIT
chmod 644 "$tmp"  # mktemp creates 0600; .gitignore is a shared, world-readable file
printf '%s\n' "$fetched" | merge "$FILE" > "$tmp"
mv "$tmp" "$FILE"
echo "Wrote $FILE with templates: $TEMPLATES"
