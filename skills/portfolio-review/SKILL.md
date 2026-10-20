---
name: portfolio-review
description: Review current commitments, stalled ideas and customer obligations to recommend where attention should go next.
---

# Review where time is going

Ask: given what we know, what deserves attention now?

Follow the [shared rules](../../docs/CONTRACT.md) and [lifecycle](../../docs/lifecycle.md). Read PORTFOLIO.md, recorded states, context, latest assessments, evidence, NEXT notes and retrospectives. Include FOUNDER.md when present. Run `python3 scripts/portfolio.py audit` for capacity.

## Review the commitments

1. Compare current work with alternatives and finishing what is already underway. If limits are exceeded, name the decisions needed to correct them. A new commitment must identify the work it displaces.
2. Find the last meaningful progress from dated external observations or completed validation. File modification times and document length do not establish progress. Say when progress is unknown.
3. Look for stalls: repeated research, architecture, branding, scope expansion, or avoidance of customer contact and tests. Distinguish deliberate parking from stalled active work.
4. For each relevant idea, report **Shiny-object risk: LOW / MEDIUM / HIGH**. Ask whether technical interest is outrunning customer evidence; cite the imbalance without making a personality judgment. Unknown evidence can justify MEDIUM with low confidence.
5. Review acquisition, buying discussions, paid commitments, onboarding delays, accepted delivery, repeat use/purchases and support burden. Separate observed results from plans and estimates. Shipped customer obligations still consume time.
6. Compare continuing experiments with their declared review window and thresholds. Recommend a sustainable cadence and a continue/change/stop decision; persistence does not redefine a failed test.

## Save the review

Append to workspace **REVIEWS.md** using `append-report portfolio-review` without `--idea`. Include the dated inventory, capacity, evidence of progress or stalls, and a short attention recommendation: what to finish/test, stop researching, or consider parking, merging or rejecting. Give revisit triggers or review dates.

Corrupt state blocks claims of available capacity. Empty portfolios are valid; calibration lessons need actual histories. A review changes neither PORTFOLIO.md nor state, and a suggested review date does not create a schedule.
