---
name: promotion-gate
description: Review evidence for an explicit idea lifecycle transition, explain blocks, record actual observations and human decisions, and enforce active/building limits without starting implementation.
---

# Gate commitment

Read [the shared contract](../../docs/CONTRACT.md), [lifecycle](../../README.md), and [record format](../../docs/RECORDS.md). Trigger when asked to check promotion, change a lifecycle state, or record real validation results.

## Inputs and ownership

Require CONTEXT.md; read STATE.md or use legacy SEED, all available analysis and evidence, and portfolio commitments. Own only the selected idea's GATE.md, EVIDENCE.md and STATE.md. Append actual observations or human decisions to EVIDENCE.md; never synthesize missing evidence. Append assessments to GATE.md, preserving human annotations and earlier failures. STATE.md is written only through the helper after review and actual human intent. No missing optional file is a reason to fabricate a prerequisite.

## Substantive review

State the requested transition and check [the lifecycle requirements](../../README.md#lifecycle), not merely file existence:
- RESEARCHED: usable primary market evidence with bounded conclusions. Partial coverage can support a narrow finding; inaccessible snippet leads cannot.
- VALIDATING: at least one load-bearing, falsifiable assumption and an executable cheap experiment with predeclared outcomes. Unknown customer access should be tested, not assumed.
- PROMOTED: real external evidence from the relevant users addresses an important assumption and meets a defensible predeclared criterion. Examine contradictions, selection bias, retractions and alternative explanations. A paid commitment or costly real behavior is stronger than compliments; a waitlist alone cannot support a willingness-to-pay claim. Technical fascination and LLM output are not customer evidence.
- BUILDING: prior PROMOTED state and explicit human intent to start implementation of this particular idea, with bounded scope and a stop condition. A request to check readiness, create NEXT.md or “explore” is not build intent.
- SHIPPED: externally usable release/access evidence, actual release scope, known limits. A local prototype or architecture document is insufficient.
- PARKED/REJECTED/MERGED: actual human disposition and reason. A merge links a distinct nonterminal destination and preserves both folders. Terminal states cannot skip back into the pipeline; PARKED returns only to SEED.

Inspect all other canonical states before consuming capacity. ACTIVE is VALIDATING/PROMOTED/BUILDING, max 3; BUILDING max 1. Record what loses attention on every new active entry, even with spare slots. If full, identify the specific required exit; do not silently park another idea. Resolve manual commitment/state conflicts before admitting new work.

GATE.md must say ALLOWED IN PRINCIPLE or BLOCKED, which requirements are met, specific evidence IDs/artifact references, counterevidence, missing facts, capacity/opportunity cost, and the smallest action that could unblock it. No missing threshold is retroactively invented to fit observed results. If an experiment was unplanned, disclose exploratory status and require a credible confirmatory step where needed.

## Apply only a real decision

A readiness check is read-only with respect to state. If the user already authorized this exact transition in the visible conversation, record that real decision; no extra confirmation is needed. Otherwise leave the gate assessment for the human to decide. Never invent an authorization or use a broad system-development request as approval to build an idea.

Record reviewed sources as typed EVIDENCE.md entries. Use a new ID for corrections and explicitly retract invalid evidence. The source of a human-decision record must identify the actual instruction, not the assistant's recommendation.

Run the helper from the repository root, first without --apply:
`python3 scripts/portfolio.py transition <slug> <STATE> --reason <reason> --evidence <ID>`
Omit --evidence for transitions not requiring it. On actual authorization, repeat with `--apply --decision <human-decision-ID>`. New active entries also need `--tradeoff <specific foregone work>`; merges need `--merge-target <slug>`. The helper enforces structural requirements and serializes cooperating writers. It cannot authenticate claims or replace your semantic review. Fail closed on errors; do not bypass it with direct writes.

After applying, report the state and capacity change with links. Suggest a retrospective after parking, rejection, merge or shipment, or execution-bridge after promotion, but do not invoke either automatically.

## Non-goals

No autonomous promotion, implementation, external actions, cascading transitions or manufactured evidence. Even BUILDING records a human commitment only; this skill executes no build.
