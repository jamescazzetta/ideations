# Lifecycle and commitment

Read this when checking a state change, recommending portfolio commitments, or choosing an action that depends on an idea's state.

`SEED -> RESEARCHED -> VALIDATING -> PROMOTED -> BUILDING -> SHIPPED`

| Transition | Required evidence and decision |
|---|---|
| SEED -> RESEARCHED | Usable sourced market evidence; snippets alone are insufficient. A partial scan can qualify for a narrowly stated conclusion. |
| RESEARCHED -> VALIDATING | At least one important falsifiable assumption and one cheap validation plan with thresholds; an explicit opportunity-cost choice. |
| VALIDATING -> PROMOTED | Observed external evidence addressing an important assumption against the predeclared threshold. No simulated interviews, LLM confidence, or documentation volume. |
| PROMOTED -> BUILDING | Explicit human intent to start building this idea, with scope and stop condition; capacity available. No code runs as part of the gate. |
| BUILDING -> SHIPPED | Something externally usable/released, access evidence and release scope; architecture completion does not qualify. |
| Any nonterminal state -> PARKED / REJECTED / MERGED | Explicit decision and reason. MERGED needs a different, nonterminal destination. Preserve both folders; no destructive merge. |
| PARKED -> SEED | Explicit reactivation reason; redo forward gates using relevant evidence. It consumes no active slot until VALIDATING. |

SHIPPED, REJECTED, and MERGED are terminal. Reconsidering a rejected thesis requires an explicit human decision to capture a materially changed thesis with a backlink, not an automatic resurrection. A duplicate of a terminal idea remains a dated note in that folder until the human makes that choice. SHIPPED leaves the active set; if ongoing maintenance consumes time, account for it as opportunity cost in triage/review. An abandoned BUILDING idea becomes PARKED or REJECTED with a retrospective suggested.

**ACTIVE = VALIDATING + PROMOTED + BUILDING. Maximum 3 combined; maximum 1 BUILDING.** All applied transitions require a recorded real human decision, including parking and merging. Recommendations never mutate lifecycle state. If full, explicitly move an idea out first; naming a displacement alone does not free capacity. “PROMOTE” in triage is a recommendation to evaluate the gate, not approval to code.

## Check and record a decision

`STATE.md` is the canonical append-only state history. Missing STATE means SEED; existing MARKET or long documentation never upgrades it. Moving a workspace never upgrades an idea; existing notes and state history are preserved. [promotion-gate](../skills/promotion-gate/SKILL.md) defines substantive evidence review; the [record format](RECORDS.md) defines the few machine-readable Markdown records.

Run checks from the repository root:

```sh
python3 scripts/portfolio.py status
python3 scripts/portfolio.py audit
python3 scripts/portfolio.py transition my-idea RESEARCHED --reason "Review the sourced market finding" --evidence M1
```

The transition command defaults to **read-only checks**. Applying requires `--apply --decision D1` and the gate's actual evidence review. All mutations use a cooperating-writer directory lock on macOS/Linux. The helper checks graph, artifacts, typed evidence, human-decision records, and capacity; it never runs research or implementation. It does not authenticate who wrote a human-decision record, prove that a cited observation is true, or enforce behavior against someone manually editing the files. Those are explicit human/agent responsibilities. Never manufacture records to satisfy a check. Direct edits to canonical history bypass safeguards; use the helper.

## Judge the evidence

A gate reviews substance as well as record structure. Use primary market evidence; check whether observed behavior addresses the selected assumption and meets the criterion set before the experiment. Inspect contradictions, retractions, selection bias and alternative explanations. Unqualified waitlists, simulated interviews, technical demonstrations and model confidence do not establish willingness to pay.

Record an unplanned experiment as exploratory. Never invent an earlier threshold to fit its results; require a credible confirmatory test where needed. Missing or unusable required evidence blocks the transition. A request for readiness, a plan, or work on Ideations itself is not intent to build a captured idea.

A release review records access, scope and known limits. SHIPPED means externally usable, not demonstrated profitability or retention. Existing customer commitments continue to consume attention.

## Repair and correction

An absent STATE.md means SEED. An existing empty, malformed or invalid history blocks state-dependent decisions. Stop and request a targeted repair that preserves the original; never reset history to create capacity. Correct evidence with a new ID explicitly retracting the old claim, and exclude the invalid record from future gates.
