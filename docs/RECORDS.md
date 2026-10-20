# Minimal records inside Markdown

Ordinary assessments use prose. Only evidence used at a gate and canonical state events need fenced JSON records. This gives mechanical guards a few inspectable fields without a second source of truth. Files may contain human notes anywhere outside records; append operations preserve them. IDs are unique within one idea's EVIDENCE.md. Examples below are **fictional format examples**, never evidence for existing ideas.

## Evidence and human decisions

promotion-gate may append records to EVIDENCE.md when actual source material is supplied or already exists. The human can also add observations. Required common fields: `id`, `kind`, ISO `date`, `summary`, `source`, `limitations`. Source is a URL, an idea-relative text artifact reference (optional `#anchor`), or `conversation:<date and identifying excerpt/context>`. Local files must exist inside the idea folder. The helper checks file existence, not fragment resolution or truth. Do not copy credentials or unnecessary personal data into records.

Kinds used by gates:

- `market`: observed current product evidence, `result: supports`. Needs MARKET.md and an accessible source URL or saved source notes. Conversation assertions alone do not qualify.
- `external`: actual observed target-user behavior, commitment, payment, interview evidence or test outcome. Include `result: supports | contradicts | inconclusive`, `assumption` and `experiment` as local artifact references, and `threshold_result` stating observed quantities/behavior against the predeclared criterion. Only supporting results can mechanically advance; the skill must judge relevance and credibility. Interview compliments, unqualified waitlists and market competitors alone do not prove demand.
- `release`: `result: supports`, plus `access` identifying how an external user can use the release. A local build is not an external release.
- `human-decision`: actual user's decision, with `from`, `to`, and `intent: change-state`; BUILDING specifically needs `intent: start-building`. Include the user's exact intent and source in summary/source, with authorized scope and stop condition in the accompanying prose. A model's recommendation is never a human decision.

```ideations-evidence
{
  "id": "E1",
  "kind": "external",
  "date": "2026-09-09",
  "summary": "FICTIONAL EXAMPLE: three target users completed the manual trial and two requested a paid continuation.",
  "source": "OBSERVATIONS.md#trial-1",
  "limitations": "Small convenience sample; actual retention unknown.",
  "result": "supports",
  "assumption": "ASSUMPTIONS.md#a1",
  "experiment": "VALIDATION.md#v1",
  "threshold_result": "FICTIONAL: the predeclared two paid-continuation requests threshold was met."
}
```

A human-decision example uses the same common fields plus `"from": "PROMOTED", "to": "BUILDING", "intent": "start-building"`. Its summary must quote real authorization; do not copy an invented example to approve an idea. Reuse previous authorization only when it actually covers this transition and scope. Record contradictory outcomes too; do not cherry-pick a supporting record while ignoring later retractions or failures.

## State history

Only `portfolio.py transition ... --apply` appends a `ideations-state` fenced record to STATE.md. Each event includes `from`, `to`, `at`, `reason`, `decision`, `evidence`, `opportunity_cost`, and `merge_target`. The last event determines state after the chain is validated from implicit SEED. No mutable “current state” field exists elsewhere. Existing empty/malformed state files fail closed instead of reverting to SEED.

The helper does not apply recommendations or authenticate user messages. Skills must substantively review the records before using `--apply`. It cannot establish that someone actually paid, a release is usable, or a user authorized a change just by parsing JSON. GATE.md records that review and its limitations. If manual damage makes history invalid, stop and request a targeted repair preserving the original; do not silently reset history.
