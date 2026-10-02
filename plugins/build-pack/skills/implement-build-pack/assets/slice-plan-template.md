# Slice plan — {{SLICE_NAME}}

<!--
This is a durable high-level charter and historical artifact. Record the slice's what and why. Keep task checklists, assignments, progress, blockers, and detailed verification logs in the linked GitHub issues. Replace every placeholder and delete this comment.
-->

## Strategic source

- **Active build pack:** {{BUILD_PACK_LINKS}}
- **Human approval:** {{APPROVAL_DATE_OR_LINK}}
- **Final acceptance advanced:** {{ACCEPTANCE_REFERENCES}}

## Outcome

{{THE_SINGLE_COHERENT_RESULT_THIS_SLICE_WILL_PRODUCE}}

## Why this slice is next

{{RATIONALE_INCLUDING_HARD_GATES_AND_EVIDENCE_EXPECTED_FROM_THIS_SLICE}}

## Scope

### In scope

- {{APPROVED_BEHAVIOR_OR_CAPABILITY}}

### Out of scope

- {{EXPLICIT_EXCLUSION_OR_DEFERRED_WORK}}

## Strategic traceability

| Strategic requirement or criterion | How this slice advances it |
| --- | --- |
| {{REFERENCE}} | {{CONTRIBUTION}} |

## Gates and dependencies

### Hard gates

- {{CAUSAL_PREREQUISITE_OR_NONE}}

### Sequencing recommendations

- {{PREFERRED_ORDER_THAT_MAY_CHANGE_OR_NONE}}

## Architecture and contracts

- **Affected seams:** {{COMPONENTS_OR_BOUNDARIES}}
- **Public contracts:** {{PRESERVED_OR_INTENTIONALLY_CHANGED_CONTRACTS}}
- **Data and migration considerations:** {{IMPACT_OR_NONE}}

## High-level approach

{{APPROVED_DIRECTION_WITHOUT_EXECUTION_CHECKLISTS_OR_PREMATURE_CODE_SHAPES}}

## Verification

- {{SLICE_LEVEL_BEHAVIOR_OR_EVIDENCE_DERIVED_FROM_FINAL_ACCEPTANCE}}
- Repository definition-of-done commands remain mandatory.

## Risks and stop conditions

- {{MATERIAL_RISK_AND_RESPONSE}}

## Execution issues

GitHub issues are the WIP tracker and source of task-level detail. Every issue for this slice carries the `{{SLICE_LABEL_OR_MILESTONE}}` label or milestone; this plan links the query, not the issues: {{ISSUE_QUERY_URL}}.

## Delivery shape

Keep only the block for the repository's active topology.

- **Topology:** {{DIRECT_PRS_OR_FEATURE_SPINE_OR_PR_STACK}}
- **Human merge gate:** Only the human may physically merge any PR whose base is `main`. Agents must stop when it is ready.

### Direct PRs

- **Branch:** {{NAME}}

### Feature spine

- **Spine:** {{NAME}}
- **Leaf merge authority:** the implementation lead may squash-merge clean leaf PRs to the spine; the spine PR to `main` is human-merged.

### PR stack

- **Merge strategy for `main`:** {{RECORDED_IN_WORKFLOW}}
- **Advancement method:** {{RECORDED_IN_WORKFLOW}}
- **Predecessor merges:** Agents never merge a stacked PR into its predecessor branch; only the bottom PR is ever merged, only by the human, only to `main`. Advancing the stack is sync + verify incremental diff + retarget, never a merge.
- **Layers in dependency order:** {{BRANCH_LIST}}

PR URLs, bases, heads, checks, and review state live in GitHub, not here.

## Amendments

None.

<!--
Append an amendment only after material invalidation and human approval:

### {{DATE}} — {{SHORT_TITLE}}

- Previous assumption or plan statement:
- New evidence:
- Human-approved change:
- Affected issues:
-->

## Delivery record

Complete once when the final PR is ready for human merge. Do not use this section for WIP status.

- **Outcome:** {{DELIVERED_RESULT}}
- **Verification:** {{CONCISE_VERIFICATION_EVIDENCE}}
- **Deviations:** {{APPROVED_DEVIATIONS_OR_NONE}}
- **Unresolved gates or risks:** {{ITEMS_OR_NONE}}
- **Refactor and handoff receipt:** {{ISSUE_COMMENT_OR_PR_LINK}}
- **Final PR:** {{URL_OR_STACK_PR_LIST}}
