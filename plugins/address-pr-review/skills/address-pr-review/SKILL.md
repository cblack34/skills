---
name: address-pr-review
description: Address unresolved review comments on the current branch's PR from any reviewer — GitHub Copilot, other bots, automated review skills, or humans. Validate each finding independently against authoritative sources before acting (reviewers are frequently wrong), apply correct fixes, push back with evidence on wrong ones, reply to every comment, and resolve threads that were fixed. Use when the user says "address review comments", "address copilot review", "handle PR feedback", "respond to the review", or similar.
context: fork
agent: pr-review-responder
---

# Address PR Review Comments

Work through unresolved review comments on the current branch's PR: fix what's
right, push back on what's wrong, reply to everything, resolve only what you
fixed. Handle ALL unresolved threads regardless of author (Copilot, bots,
review automation, humans) unless the user scoped the request to a specific
reviewer.

## Core principle

**Validate every finding before acting.** Treat every comment as a hypothesis,
not a fact. Reviewers — bots especially, but humans too — have been observed to:

- Cite line numbers that have shifted since the review ran
- Flag valid regex as malformed
- Reference APIs/fields that don't exist in the current library/provider version
- Hallucinate file paths
- Claim language-level errors that the project's actual runtime version makes moot
  (e.g. "missing forward reference" on Python >= 3.14 where annotations are lazy)
- Suggest security changes that break the current bootstrap/operational flow
- Contradict their own earlier comments in the same review

Confirm each claim against the actual file, upstream docs, or a real
validate/run — *then* decide whether to apply the fix, modify it, or push back.

## Inputs

- Optional PR number. If omitted, infer from the current branch:
  `gh pr view --json number` (or `gh pr list --head "$(git branch --show-current)"`).
- Get OWNER/REPO from `git remote get-url origin`.

## Workflow

### 1. Pre-flight

- Confirm a git repo + the PR exists.
- Fetch **all unresolved review threads** (REST doesn't expose resolution state;
  GraphQL is required — snippet below). Don't filter by author unless asked.
- Fetch recent review bodies (`gh api repos/{O}/{R}/pulls/{N}/reviews`, sort by
  `submitted_at`). Copilot's review body lists "Comments suppressed due to low
  confidence" — those still represent real issues and must be addressed even
  though they have no inline thread. Human review bodies may also raise
  actionable points with no thread; answer those in a top-level PR comment.

### 2. For each open thread — validate, then fix

Follow this loop for every comment. **Do not skip step (b).**

**(a0) Read the WHOLE thread, not just the first comment.** If the thread has
replies — including a reviewer countering your own earlier pushback — the
latest state of the argument is what you're addressing, not the original
finding. If a reviewer answered your pushback with new evidence, re-evaluate
honestly: concede and fix if they're right; if you still disagree after one
full exchange, say so once more with your strongest evidence, tag the thread
"needs a human decision" in your summary, and stop — no infinite loops.

**(a1) Triage by severity prefix** when the reviewer uses labels like
`[Blocking]`/`[Issue]`/`[Suggestion]`/`[Nit]` (the review-pr skill and
Clayton's own comments do):

- `[Nit]` — low ceremony: apply if trivially correct (often just "Commit
  suggestion"-equivalent), or briefly decline; don't spend validation effort.
- `[Suggestion]` — author's call: apply if it genuinely improves the code,
  otherwise decline with one sentence.
- `[Issue]` / `[Blocking]` — full validation loop below; these deserve the
  most scrutiny in BOTH directions (fixing and pushing back).

**(a) Read the actual code at the cited path/line.** Inspect the file itself,
not just the snippet in the comment — line numbers may have moved since the
review ran.

**(b) Validate the claim against an authoritative source**, chosen by category:

| Category | How to validate |
| --- | --- |
| Library/SDK/provider syntax or behavior | Consult the official docs or registry with available documentation or browsing access, or write a tiny repro and run/validate it |
| Language-level claims (typing, imports, syntax) | Check the project's actual runtime/`requires-python`/tsconfig; verify empirically with a quick import or run |
| Regex / pattern claims | Test the literal string; check it byte-for-byte |
| File-existence / dead-link claims | `ls` / `find` / `grep` the repo |
| "Deprecated" / "removed" claims | Check the currently pinned version's docs, not latest |
| "X contradicts Y" claims | Read **both** locations cited |
| Missing-test-coverage claims | Check whether an equivalent test exists elsewhere (e.g. the async twin of a sync path) |
| Security / best-practice suggestions | Weigh the trade-off in context — technically correct ≠ operationally right |

**(c) Decide one of three outcomes:**

- **Accept** — the reviewer is right; apply the fix (often a paraphrase of
  their suggestion, not their literal text — verify suggested code actually
  parses/validates before using it).
- **Accept with modification** — the concern is real but the suggested fix
  isn't right; fix it properly and say so in the reply.
- **Push back** — the reviewer is wrong, or the suggestion would degrade the
  system for this phase. Cite the source that disproves it. If the same wrong
  flag is likely to recur, document the trade-off in code/README so the next
  review round doesn't re-flag it.

**(d) Apply the change** surgically. Where the same flaw exists elsewhere in
the same file/module, fix it consistently; add a small test pinning the
behavior when cheap.

**(e) Reply to the comment** — the reply is the audit trail; "fixed" alone
isn't enough:

- State what changed (quote the new text where useful) and the commit SHA — or
  that nothing changed and why.
- If pushing back, reference the concrete evidence (version constraints,
  passing checks, doc citations) — never a bare "disagree".
- **Sign every reply** with a trailing line identifying who wrote it, in the
  form `- <agent>-<model>-<effort>` using your actual runtime identity (agent
  name, model, and reasoning effort; omit effort if unknown). Example:

  ```
  Fixed in 605aa95 — workflow IDs are now URL-escaped via _path_part.

  - pr-review-responder-sonnet-5-high
  ```

**(f) Resolve the thread** (GraphQL `resolveReviewThread`, snippet below) only
when the reply substantively addresses the concern. If you pushed back, **leave
it open** — for bots so a human can adjudicate, for human reviewers so they can
respond — and flag it in the final summary.

### 3. Validate after fixes

Run whatever the project's CI runs, before committing:

- Terraform: `terraform validate` (each touched root), `terraform fmt -check -recursive`, `tflint`
- Python: `ruff format --check`, `ruff check`, `mypy`, tests
- JS/TS: `tsc --noEmit`, lint, tests

If a check fails, fix and re-run before proceeding.

### 4. Commit and push (default) — or hand off

Default: commit with a message noting it addresses review feedback, push, and
cite the SHA in replies (replies referencing unpushed code are a broken audit
trail). Exception: if the user said they want to review or commit themselves,
do **not** commit — instead reply/resolve only after they confirm, and hand off
a proposed commit title (sentence case, ~50–72 chars) and body.

### 5. Report

Summarize for the user:

- **Per-comment table**: `author | file:line | claim | verdict | action (commit SHA or push-back rationale)`
- **Diff scope** (`git diff --stat` of what changed)
- **Validation status** (what ran, what passed)
- **Threads left open**, and why

## Anti-patterns to avoid

- Resolving threads without a substantive reply.
- Applying a reviewer's suggested code verbatim without checking it parses/validates.
- Accepting "security" suggestions that would break the current operational
  flow (e.g. disabling public network access on a resource operators still
  need to bootstrap through). Push back with a documented trade-off and a
  future-improvement note.
- Skipping the "low confidence" comments listed only in the review body.
- Rewriting historical decision-log/changelog entries to satisfy a reviewer.
  Prefer `**[Superseded YYYY-MM-DD: ...]**` annotations over rewriting history,
  and remember stale `updated:` frontmatter dates trigger fresh flags next round.

## Useful snippets

### Unresolved threads with IDs for replying and resolving

```bash
gh api graphql --paginate -f query='
query($owner:String!,$repo:String!,$num:Int!,$endCursor:String){
  repository(owner:$owner,name:$repo){
    pullRequest(number:$num){
      reviewThreads(first:100,after:$endCursor){
        nodes{ id isResolved }
        pageInfo{ hasNextPage endCursor }
      }
    }
  }
}' -F owner="$O" -F repo="$R" -F num="$N" \
  --jq '.data.repository.pullRequest.reviewThreads.nodes[] | select(.isResolved == false) | .id' |
while IFS= read -r thread_id; do
  gh api graphql --paginate -f query='
  query($thread:ID!,$endCursor:String){
    node(id:$thread){
      ... on PullRequestReviewThread{
        id isResolved path line
        comments(first:100,after:$endCursor){
          nodes{ databaseId author{login} body }
          pageInfo{ hasNextPage endCursor }
        }
      }
    }
  }' -F thread="$thread_id"
done
```

### Latest review by a given author (for the body / suppressed comments)

```bash
gh api "repos/$O/$R/pulls/$N/reviews" \
  --jq '[.[] | select(.user.login=="copilot-pull-request-reviewer[bot]")] | sort_by(.submitted_at) | last'
```

### Reply to a comment

```bash
gh api "repos/$O/$R/pulls/$N/comments/$CID/replies" -X POST -F body="..."
```

### Resolve a thread

```bash
gh api graphql -f query='
mutation($id:ID!){ resolveReviewThread(input:{threadId:$id}){ thread{isResolved} } }' \
  -F id="$THREAD_ID"
```
