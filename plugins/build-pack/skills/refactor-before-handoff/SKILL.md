---
name: refactor-before-handoff
description: Turn a behaviorally passing implementation into a maintainable handoff before a PR is declared ready. Reads every changed production file in full plus its owning abstractions, checks cohesion, responsibilities, dependency direction, IO boundaries, duplication, package structure, and testability, applies justified behavior-preserving refactors, runs a fresh-context read-only design review, re-verifies, and emits a receipt. Invoke it yourself, without being asked, whenever you have changed production code and its tests pass and you are about to open a PR, mark a PR ready, or report the work as done; passing tests mean the draft works, not that it is ready. Also use when the user says "refactor before handoff", "is this ready to hand off", "clean this up before the PR", "design pass", or "tests pass, now make it maintainable". Works on any diff, with or without a build pack. Not a correctness or security review (that is pr-review) and not for code you did not change.
---

# Refactor before handoff

A bounded implementation that passes its focused behavioral checks is a **working draft**. Passing tests prove the draft works; they do not prove it is ready for handoff. Run this once per delivery unit (each PR) after behavior passes and before PR preparation. Execution-agent receipts, issue closure, and green CI do not satisfy it.

Implementation may begin rough and become clearer as behavior is discovered. The defect this skill prevents is returning the rough draft because its tests pass. The gate is mandatory; the exact refactors remain implementation decisions.

## Inputs

Establish before starting:

- **Changed surface:** a base ref (`git diff --name-only <base>...HEAD`) or an explicit changed-file list. Never infer it from memory. The diff only selects the files; it is not what gets reviewed.
- **Rules:** the applicable `AGENTS.md` family and the repository's code-quality document. If the repository has a workflow document with its own refactor-before-handoff section, it is stricter or equal; follow it.
- **Verification:** the repository's exact definition-of-done commands and the cheapest focused check for the touched area.
- **Record target:** where the receipt goes. A GitHub issue when one tracks this work, otherwise the PR body, otherwise the reply to the user.
- **Edit authority:** whether to apply refactors directly or route them as bounded assignments (an orchestrating skill such as `implement-build-pack` says which). Direct invocation by the user means apply them directly.

## 1. Review the changed surface

Read every changed production file **in full**, not just its diff hunks, plus the owning abstractions and callers needed to judge whether responsibilities still fit. An addition that looks local in the diff can be the change that tips a module into two responsibilities; only the whole file shows that. Do not filter by file size or line count.

Evaluate against the repository's code-quality rules:

- cohesion and reasons to change for each function, class, and module;
- dependency direction and boundary placement, including IO at the edges;
- creation versus use;
- duplication and scattered knowledge;
- avoidable complexity and speculative abstractions;
- whether a package or subpackage boundary would create clearer ownership, or whether existing fragmentation is ceremonial;
- whether tests are hard to write because the coupling is wrong;
- when modules or subpackages were added or moved: manifests, package discovery, built-artifact contents, and a clean-install import where the stack produces distributable artifacts.

## 2. Apply justified refactors

Preserve behavior. Apply the refactors the evaluation justifies and nothing more: no file splitting by size, no one-class modules, no abstraction for its own sake. Stay inside the delivery unit's changed surface. A refactor that needs to reach beyond that surface is a stop condition: report it, do not perform it.

After every structural edit, run the cheapest focused executable check first (the affected tests, an import, or a build of the touched package) before continuing.

## 3. Fresh-context design review

Obtain a read-only design review of the complete changed surface from a context that did not author it. This review is separate from author self-review and from the later PR review: it judges maintainability and ownership, while the PR review remains the correctness, security, and test gate.

Reviewer precedence:

1. This plugin's `design-reviewer` agent (`build-pack:design-reviewer` in Claude Code) when the harness exposes plugin agents.
2. Otherwise a fresh read-only subagent whose instructions are the body of `agents/design-reviewer.md` at the plugin root.
3. Otherwise stop and ask the human for an explicit design review.

Give the reviewer the repository path, the base ref and changed-file list, the applicable `AGENTS.md` family and code-quality rules, any plan or issue that frames the work, and the refactors already made. Require explicit changed-file coverage. A review that skips a changed production file without a stated reason is incomplete; re-request it.

## 4. Validate findings before acting

Verify every finding against the code before changing anything. Apply correct findings as in step 2. Reject weak findings with evidence in the record. Do not accept a finding because the reviewer stated it, and do not dismiss one because tests pass.

## 5. Verify before handoff

After the last structural edit, run the complete repository verification from `AGENTS.md` on the final head. If a package or subpackage was added or moved, also confirm manifests, built-artifact contents, and a clean-install import.

## 6. Record the receipt

Write the receipt to the record target and include it in the PR body or handoff message.

```markdown
## Refactor and handoff receipt
- Changed production files reviewed:
- Owning abstractions/callers reviewed:
- Cohesion/SRP findings:
- Structural changes made:
- Findings rejected and evidence:
- Package/artifact verification:
- Post-refactor focused checks:
- Complete repository checks:
- Fresh-context design review:
- Remaining risks or justified debt:
```

`Structural changes made: none` is valid only when the receipt identifies the reviewed surface and explains why current responsibilities remain cohesive. `Fresh-context design review` names the reviewer used (agent, fallback subagent, or human) and its coverage.

## Hard rules

- Behavior is preserved; this skill never changes scope, public contracts, or deferred work.
- It does not create branches, open or merge PRs, or run the PR review loop. It ends at the receipt.
- Line count is never the sole argument for a finding or a split.
- Author self-review never substitutes for the fresh-context review.
- Never claim a check, review, or coverage that was not run.
