# Slice plan — {{SLICE_NAME}}

<!--
This is a durable high-level charter and historical artifact. Record the slice's what and why. Keep task checklists, assignments, progress, blockers, and detailed verification logs in the linked GitHub issues. Replace every placeholder and delete this comment.
-->

## Strategic source

- **Active build pack:** {{BUILD_PACK_LINKS}}
- **Human approval:** {{APPROVAL_EVIDENCE_OR_DATE}}
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

GitHub issues are the WIP tracker and source of task-level detail.

| Issue | Purpose | Dependencies |
| --- | --- | --- |
| [#{{NUMBER}}]({{URL}}) — {{TITLE}} | {{WHY_THIS_ISSUE_EXISTS}} | {{ISSUE_LINKS_OR_NONE}} |

## Delivery shape

- **Topology:** {{DIRECT_PR_OR_FEATURE_SPINE}}
- **Branch or spine:** {{NAME}}
- **Final PR:** {{URL_WHEN_AVAILABLE}}
- **Human merge gate:** Only the human may physically merge the final PR to `main`. Agents must stop when it is ready.

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
- **Verification:** {{CONCISE_EVIDENCE_AND_ISSUE_LINKS}}
- **Deviations:** {{APPROVED_DEVIATIONS_OR_NONE}}
- **Unresolved gates or risks:** {{ITEMS_OR_NONE}}
- **Final PR:** {{URL}}
- **Merge state:** Ready for the human to merge; agents do not merge to `main`.
