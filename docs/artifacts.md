# Files and report writing

Read this when saving a report or checking which skill owns a file. All paths below are inside the resolved private workspace. Files are created when needed; the user does not need to scaffold them.

## Save a report

Read the existing file first. Write only the new dated section to a temporary draft, then run the helper from the core:

```sh
python3 scripts/portfolio.py append-report offer-design --idea my-idea --content /path/to/new-section.md
```

Use the owning skill's name. Omit `--idea` for workspace-level reports. `idea-retrospective` uses `--idea` for RETROSPECTIVE.md and omits it for CALIBRATION.md. If the caller selected `--root`, use that same override before every subcommand. The helper restricts the destination to the owner's file and preserves existing bytes; it never creates an idea or launches another skill.

Capture saves CONTEXT.md through its own procedure. Evidence uses the [record format](RECORDS.md). Only promotion-gate changes STATE.md through the helper after the [lifecycle review](lifecycle.md).

## Files and owners

| Artifact | Owner | Meaning |
|---|---|---|
| `CONTEXT.md` | capture-ideas | Original idea plus dated developments |
| `MARKET.md` | market-check | Bounded, cited market assessment |
| `CHALLENGE.md` | red-team-idea | Falsifiable case against building |
| `OFFER.md` | offer-design | Buyer, outcome, bounded scope, pricing and delivery hypotheses |
| `ASSUMPTIONS.md` | assumption-map | 3–5 load-bearing assumptions |
| `VALIDATION.md` | validation-designer | One primary predeclared experiment |
| `EVIDENCE.md` | promotion-gate / explicit human additions | Dated observations and exact human decisions; no invented data |
| `GATE.md` | promotion-gate | Semantic evidence review and allowed/blocked explanation |
| `STATE.md` | promotion-gate via helper | Canonical append-only lifecycle history |
| `NEXT.md` | execution-bridge | At most 1–3 bounded customer-learning or delivery actions |
| `RETROSPECTIVE.md` | idea-retrospective | Predictions versus actual outcomes for an idea |
| `PORTFOLIO.md` | triage-ideas / human annotations | Ranked recommendations, never canonical states |
| `REVIEWS.md` | portfolio-review | Dated allocation review, stalls, shiny-object risks |
| `CROSS_POLLINATIONS.md` | cross-pollinate | Human-reviewable connections; not new ideas |
| `CALIBRATION.md` | idea-retrospective | Cautious cross-idea lessons linked to histories |

All files are human-readable Markdown. The helper reads only fenced records in `STATE.md` and `EVIDENCE.md`; no database or shadow index exists. Legacy `Status:` lines in CONTEXT remain historical, not authoritative.

## History and provenance

Give each assessment a date, inputs, sources, limitations and relevant observation dates. Separate the user's proposal, assistant suggestions, sourced facts, assumptions, speculation, observed results and conclusions.

Append revisions rather than replacing earlier assessments or human annotations. Say which assessment is superseded and why. Retain stable IDs such as A1, V1 and O1; never recycle them. The latest explicitly superseding assessment is current, while failed predictions stay readable. Evidence corrections use a new record with a new ID and an explicit retraction.

Portfolio snapshots need an as-of date and links to state history, or an explicit statement that the idea is SEED because no state history exists. Root reports are recommendations, never an alternative state store.
