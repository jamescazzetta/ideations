---
name: portfolio-review
description: Review attention allocation across all ideas, flag stalls and shiny-object risk, and check active/building limits using current evidence and meaningful progress.
---

# Review the portfolio

Read [the shared contract](../../docs/CONTRACT.md) and [lifecycle](../../README.md). Trigger on a requested periodic or ad hoc portfolio review; there is no scheduler.

## Inputs and ownership

Read PORTFOLIO.md, all immediate workspace ideas' canonical states, CONTEXT.md, latest available assessments, external observations, validation outcomes, NEXT.md and retrospective history. Use `python3 scripts/portfolio.py audit` for capacity. Own only workspace REVIEWS.md; append a dated review with an as-of inventory, never rewrite PORTFOLIO or state. Missing optional artifacts mean unknown evidence; an empty repository is a valid review. Corrupt state blocks claims that capacity is available.

## Review

Answer “Given what we know, what deserves attention now?” Compare current commitments with alternatives and finishing existing work. State whether max 3 ACTIVE and max 1 BUILDING are respected. For an entrant identify the exact work/idea displaced. If limits are already violated, name the corrective decisions needed without silently making them.

For each relevant idea flag **Shiny-object risk: LOW / MEDIUM / HIGH** using: “Is this attractive because its technical/intellectual problem is interesting while customer evidence remains weak?” Cite the specific imbalance; unknown evidence can warrant MEDIUM with low confidence, not a personality judgment.

Identify last meaningful progress from dated external observations or completed validation, not file modification times or word count. If unknown, say unknown. Flag evidenced stalls due to endless research, architecture, branding/design, scope expansion, failure to contact users or repeated validation avoidance. Distinguish deliberate parking from a stalled active commitment.

Review commercial work as well as engineering: attempted/reached customers, discovery findings, paid commitments, onboarding delays, accepted delivery, repeat use/purchases, and support burden. Distinguish observed measurements from estimates and proposed work. Count time owed to shipped customers in allocation decisions without reopening terminal states or silently expanding scope. A release alone proves neither profit nor retention.

For a continuing acquisition or delivery experiment, compare actual inputs and outcomes with its predeclared review window. Recommend a sustainable cadence and a continue/change/stop decision; persistence does not excuse missed thresholds or reset a failed experiment. A future review date is a suggestion, never a scheduled action.

End with a short attention recommendation: what to finish/test now, what to stop researching, and what to park/merge/reject for human decision. Include revisit triggers or review dates. Do not generate new projects or recommend a larger active set. Mention calibration lessons only when supported by actual histories.

## Non-goals and handoff

No research refresh, state changes, implementation, scheduled monitoring, recursion or automatic triage/retrospective invocation. Review recommendations do not change commitments.
