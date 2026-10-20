---
name: promotion-gate
description: Record real results, review readiness, or apply a user-authorized lifecycle decision when its evidence and capacity requirements are met.
---

# Review a commitment

Decide whether the evidence supports the requested state change, then apply it only when the user has authorized that decision.

Follow the [shared rules](../../docs/CONTRACT.md). Read the [lifecycle requirements](../../docs/lifecycle.md) and [record format](../../docs/RECORDS.md). Read the idea's CONTEXT.md, state history, available assessments/evidence and portfolio commitments.

## Review the evidence

1. Identify the requested transition, or whether the user only wants to record observations or check readiness.
2. Compare the actual evidence with the lifecycle requirement. Inspect contradictions, retractions, selection bias and alternative explanations. Record observations against the experiment's original thresholds. For an unplanned test, disclose exploratory status and require confirmation where needed.
3. Check all recorded states before increasing commitment. Name the work displaced, even with spare capacity. If full, identify the exit needed first. Resolve conflicts between human commitments and recorded states before treating capacity as available.
4. Append real supplied observations or decisions to **EVIDENCE.md**. Cite their actual source; correct errors with new IDs and explicit retractions. Never manufacture missing data or authorization.
5. Append the assessment to **GATE.md** using `append-report promotion-gate`: **ALLOWED IN PRINCIPLE** or **BLOCKED**, requirements met, evidence IDs, counterevidence, missing facts, capacity/tradeoff, and the smallest action that could unblock it.

## Apply an authorized decision

A readiness check leaves state unchanged. When the user has already authorized this exact transition, record that decision without asking again. A general request to explore, plan, or improve Ideations is not permission to build an idea.

First check the transition without applying it:

```sh
python3 scripts/portfolio.py transition <slug> <STATE> --reason <reason> --evidence <ID>
```

Omit `--evidence` when the transition does not require it. Include `--tradeoff` when entering the active set and `--merge-target` when merging. Once the evidence review, structural check and real decision support the change, repeat with `--apply --decision <human-decision-ID>`.

Only this helper writes **STATE.md**. Stop on errors; its checks do not authenticate evidence or replace your review. Even BUILDING records a commitment without executing code.

Finish by reporting the applied state/capacity change, or the reason it remains blocked, with file links. Suggest a retrospective or next-action review when useful; leave that follow-up to the user's request.
