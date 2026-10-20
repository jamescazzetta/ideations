---
name: triage-ideas
description: Compare ideas and recommend which to pursue, test, park, merge or stop, with explicit attention tradeoffs.
---

# Choose what deserves attention

Rank the portfolio against current commitments and the option of starting nothing.

Follow the [shared rules](../../docs/CONTRACT.md) and [lifecycle](../../docs/lifecycle.md). Use `python3 scripts/portfolio.py status`, then read the ideas' context, states, available assessments and evidence. Read PORTFOLIO.md and its human annotations, plus FOUNDER.md when present.

## Compare the ideas

1. Judge pain strength, founder fit, credible differentiation, access to buyers and cheap testability. Mark unknowns. Consider personal interest, time to an external signal, available resources and operating dependencies where they change the ranking.
2. Include acquisition, onboarding, delivery and support effort. Ongoing work for shipped customers consumes attention. Compare a building idea with finishing its current scope.
3. Give each idea one recommendation:

   | Recommendation | Meaning |
   |---|---|
   | PROMOTE | External evidence appears sufficient for gate review. |
   | VALIDATE | One cheap test could change the decision. |
   | PARK | Lower priority or useful as a reference; name a revisit trigger. |
   | MERGE | Same underlying job/mechanism; name the destination and what to retain. |
   | KILL | Strong negative evidence or an unacceptable dependency; explain what failed. |

4. Name what loses attention for each proposed entrant, even with spare capacity. When full, identify which idea would need to leave first. Respect the lifecycle limits; a recommendation never frees a slot.

## Save the ranking

Append to workspace **PORTFOLIO.md** using `append-report triage-ideas` without `--idea`. Each ranked row gives the recommendation, comparative rationale, evidence confidence and what would change it. Use qualitative judgments rather than numerical scores.

Terminal ideas have “no active candidacy”: retain MERGE for MERGED, KILL for REJECTED, and PARK for SHIPPED as a recommendation of no new work, not a state change. For BUILDING, explain when VALIDATE means its next test or PROMOTE means continuing a justified commitment; neither resets state.

An empty portfolio gets an empty assessment; one idea is compared with existing commitments and doing nothing. Missing evidence lowers confidence. Malformed state or a human commitment that conflicts with recorded state blocks recommendations to increase commitment until resolved.

Finish with the capacity summary and attention tradeoff. An all-PARK/KILL result is valid. Gate reviews and tests remain suggested follow-ups.
