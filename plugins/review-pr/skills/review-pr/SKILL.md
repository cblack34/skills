---
name: review-pr
description: Run a complete, verified code review of a pull request and post it as ONE GitHub review with inline line-level comments, severity labels ([Blocking]/[Issue]/[Suggestion]/[Nit]), and one-click suggested changes. Multi-pass finders loop until dry, every finding is adversarially verified before posting, and the review body reports exact coverage — designed to beat Copilot's half-done reviews with one clean cycle. Use when the user says "review this PR", "review the PR", "run the review bot", "code review this pull request", or similar.
context: fork
agent: pr-reviewer
---

# Review PR

Produce ONE complete, verified review of a pull request. The goal is a single
clean cycle — review, fix, merge — not five dirty rounds. Two failure modes to
design against, in priority order:

1. **False positives** — under 10% of posted findings, ideally under 5%. A bot
   that cries wolf gets dismissed and trust never recovers. Every finding is
   verified before posting.
2. **Left-on-the-table findings** — issues that existed in round 1 but only get
   flagged in round 3. Countered by diverse multi-pass finders that loop until
   dry, and explicit coverage accounting (no silent file skipping).

Scope: review where review beats tests and lint — logic/correctness, edge
cases, error handling, validation, concurrency, resource handling, API misuse,
security, test gaps, and design/maintainability. Style and formatting are the
linter's job: never comment on anything a configured linter/formatter would
catch.

## Inputs

- Optional PR number (works in CI where there is no branch context). If
  omitted, infer from the current branch: `gh pr view --json number`.
- OWNER/REPO from `git remote get-url origin`.

## Pipeline

### Phase 0 — Pre-flight

- `gh pr view N --json number,title,body,baseRefName,headRefOid,files`
- `gh api repos/{O}/{R}/pulls/N/files --paginate` — changed files WITH `patch`
  hunks. Record the head SHA you are analyzing; anchor everything to it.
- Fetch ALL existing review threads **including every reply** and resolution
  state (GraphQL snippet below), plus prior review bodies
  (`gh api repos/{O}/{R}/pulls/N/reviews`). You need these for dedup and for
  responding to pushback.
- If >300 changed files or >~4000 changed lines, say so up front, review in
  priority order (source > config > tests > docs), and report what was and
  wasn't covered — never silently truncate.

### Phase 1 — Context build

Read beyond the diff before any finding is generated:

- Full current content of every changed file (not just hunks).
- Callers/callees of changed functions (grep for usages), related tests, and
  sibling implementations (e.g. the sync twin of an async file).
- Repo conventions: CLAUDE.md, lint/type-check configs, pinned dependency
  versions (lockfiles, pyproject/package.json) — findings must be judged
  against the versions actually pinned, not latest.

### Phase 2 — Finder fan-out (parallel subagents)

Spawn parallel finder subagents, one per defect category, each blind to the
others (diversity is the recall advantage — independent bots agree on <10% of
findings, so multiple lenses is where completeness comes from). **Run every
subagent synchronously (`run_in_background: false`) and never end your turn
while finders or verifiers are outstanding** — an early return orphans the
pipeline and a later resume double-posts the review.

1. **Logic/correctness** — wrong behavior, off-by-one, inverted conditions,
   broken invariants
2. **Edge cases & error handling** — unhandled inputs, missing failure paths,
   swallowed errors, omission defects (what SHOULD be here and isn't)
3. **Validation & security** — trust-boundary checks, injection, authz/authn,
   secrets, unsafe defaults
4. **Concurrency & resources** — races, deadlocks, leaks, unclosed handles,
   retry/timeout behavior
5. **API misuse** — wrong endpoint/field/flag per the ACTUAL docs or pinned
   version; hallucination-prone, so cite the source
6. **Test gaps** — new behavior without tests, tests that can't fail, missing
   negative cases
7. **Design & maintainability** — wrong-layer changes, needless complexity,
   inconsistency with the codebase's established patterns

Each finder reviews in chunks of ≤400 changed lines (detection quality falls
off a cliff past that), receives the Phase 1 context, and returns:

- Findings: `path, start_line..line, side, category, severity, claim,
  evidence, suggested_fix (exact replacement text when possible)`
- A coverage report: which files/hunks it actually examined.

### Phase 3 — Loop until dry

Merge findings, then run ANOTHER finder round (vary the file order and prompt
angle). Repeat until **two consecutive rounds surface nothing new**, max 4
rounds. This directly attacks stochastic misses — the root cause of
issues-found-next-cycle.

### Phase 4 — Dedup

Drop candidates that duplicate: (a) other finders' findings (same file,
overlapping lines, same substance), and (b) **any existing thread on the PR,
including resolved ones** — dedup against everything ever posted, not just
open threads, or killed findings resurrect every cycle.

### Phase 5 — Adversarial verification (parallel subagents)

Every surviving candidate gets a skeptic subagent prompted to REFUTE it:

- Read the actual code at the cited lines — full file, not the hunk.
- Verify empirically where possible: run the snippet, write a 5-line repro,
  check the pinned dependency's docs, run the project's own tests. Receipts
  beat reasoning.
- Language-level claims must be checked against the project's actual runtime
  (e.g. annotation semantics differ across Python versions).
- Verdict: CONFIRMED (with the evidence) or KILLED. When uncertain, kill it —
  a missed nit is cheaper than a false alarm. [Blocking] findings require the
  strongest evidence (executed repro or authoritative citation).

Track the kill count for the coverage report.

### Phase 6 — Severity and caps

Label every confirmed finding:

- `[Blocking]` — must fix before merge: correctness, security, data loss
- `[Issue]` — real problem, should fix, wouldn't block alone
- `[Suggestion]` — improvement, author's call
- `[Nit]` — polish; author may ignore freely

Rules: `[Blocking]`/`[Issue]` MUST include a concrete fix — a ```suggestion
block when the fix fits the commented range, otherwise exact described code.
Never post a bare question as a finding. Cap inline nits at **5**; overflow
nits go in a collapsed section of the review body. If total inline comments
would exceed ~25, keep all Blocking/Issue inline and move the rest to the
body (GitHub's spam detection 422s large reviews).

### Phase 7 — Compose and post ONE review

**Validate every anchor first**: each comment's `(path, line, side)` must be a
line present in the diff hunks (parse the `patch` fields from Phase 0). One
bad anchor 422s the entire review. Findings on lines outside any hunk become
file-level comments (`subject_type: "file"`) posted after the review.

Comment format:

```
[Issue] Retries hammer the endpoint with no backoff.

`_send_request` retries immediately on 5xx; three workers failing together
will synchronize their retries. Verified: `RetryPolicy.backoff_seconds`
defaults to 0 in this call path (ran the repro in scratch).

```suggestion
        return retry_with_backoff(self._client.request, method, path)
```

- pr-reviewer-<model>-<effort>
```

Suggestion-block rules (GitHub "suggested changes"):

- The block's content replaces the ENTIRE commented line range
  (`start_line`..`line`) — full final text, correct indentation.
- Only on `side: RIGHT`, only on lines present in the head version, never on
  or spanning deleted lines, one suggestion block per comment.

**Duplicate guard**: immediately before posting, re-fetch the PR's reviews. If
a review signed by this skill already exists for the same head SHA, do NOT
post — another run got there first; reconcile your findings against its
threads instead (reply/resolve only).

Post as ONE atomic call — the comments array cannot be expressed with `-F`
flags; write JSON to a temp file:

```bash
gh api --method POST repos/{O}/{R}/pulls/N/reviews --input review.json
```

with `{"commit_id": "<analyzed head SHA>", "event": "COMMENT", "body": ...,
"comments": [...]}`. Always `COMMENT` — the bot never blocks merge; severity
labels carry the signal. On 422, bisect: post comments individually so one bad
anchor doesn't kill the review, and note any that fail.

**Review body** = the coverage receipt (this is what Copilot never gives you):

```
## Review coverage
- Files reviewed: 12/12 (list skipped files + reason if any)
- Finder rounds: 3 (round 3 found nothing new)
- Candidates: 31 found → 9 duplicates dropped → 14 killed in verification → 8 posted
- Verification: 6/8 verified by execution, 2/8 by doc citation
- Prior threads checked: 4 (2 fixed & resolved, 1 pushback answered, 1 stands)

### Nits not worth inline comments (3)
- path.py:88 — ...

- pr-reviewer-<model>-<effort>
```

### Re-review mode (when this bot has reviewed this PR before)

Always a FULL re-review (delta-only is how issues hide), then reconcile
against every prior thread:

- **Fixed** — the code now addresses it: reply confirming (name the commit),
  resolve the thread.
- **Pushback in replies** — read the author's/responder's argument and
  re-verify with fresh evidence. If they're right: concede in a reply and
  resolve. If they're wrong: counter ONCE with new evidence (not a restatement
  of the original claim). After one counter-exchange, tag it "escalate to a
  human" in the review body and stop arguing — no infinite bot-vs-bot loops.
- **Unaddressed** — do NOT re-post a duplicate comment; list it under "still
  open" in the review body.
- New findings must be genuinely new (not in ANY prior thread, open or
  resolved).

### Sign everything

Every inline comment, reply, and the review body ends with:
`- pr-reviewer-<model>-<effort>` (actual runtime identity; omit effort if
unknown).

## Anti-patterns

- Posting a finding that no verifier confirmed.
- Style/formatting comments (the linter's job), or restating what the diff does.
- Questions as findings — if you can't determine impact, verify harder or drop it.
- Flagging code outside the PR's changes (file an aside in the body if severe).
- Silently skipping files ("evaluated as low risk" with no list = trust killer).
- Re-posting a finding that already has a thread, open or resolved.
- Applying a fix yourself — the reviewer only reviews; fixing is the author's
  (or address-pr-review's) job.

## Snippets

All threads with replies + resolution state:

```bash
gh api graphql --paginate -f query='
query($owner:String!,$repo:String!,$num:Int!,$endCursor:String){
  repository(owner:$owner,name:$repo){
    pullRequest(number:$num){
      reviewThreads(first:100,after:$endCursor){
        nodes{ id }
        pageInfo{ hasNextPage endCursor }
      }
    }
  }
}' -F owner="$O" -F repo="$R" -F num="$N" \
  --jq '.data.repository.pullRequest.reviewThreads.nodes[].id' |
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

File-level comment (finding outside diff hunks):

```bash
gh api --method POST repos/$O/$R/pulls/$N/comments \
  -f body="..." -f path="src/file.py" -f subject_type=file -f commit_id="$SHA"
```

Reply to a thread / resolve a thread: same as the address-pr-review skill —
`POST .../comments/{top_comment_id}/replies` and GraphQL
`resolveReviewThread(input:{threadId:$id})`.
