# Ideations

Turn ideas emerging from work and conversation into a small, evidence-informed portfolio. **Ideations should generate fewer projects than the conversations that feed it.** This is a decision and calibration system, not an autonomous startup factory.

## Doctrine

- Capture freely, promote reluctantly.
- Research informs; it does not authorize building.
- External evidence beats internal enthusiasm.
- A clever mechanism is not evidence of customer demand.
- New active ideas must displace existing active ideas when full; even with room, name the work you will forgo.
- Prefer cheap falsification over expensive confirmation.
- Architecture is not progress unless architecture is the thing being validated.
- One BUILDING idea maximum. At most three ACTIVE ideas, including validation work.

## Start here

Requires Python 3.10+ on macOS or Linux and a conversational agent that can read local files. Research additionally needs browsing and an inexpensive worker. The helper uses only Python's standard library.

```sh
mkdir -p ../ideations-workspace
cp ideations.example.json ideations.local.json
python3 scripts/portfolio.py settings
python3 scripts/portfolio.py status
```

Edit the ignored local configuration if your workspace is elsewhere. Follow the [quickstart](docs/quickstart.md), then ask your agent to read this repository's AGENTS.md. A fresh clone does not contain your ideas or credentials.

## Structure and use

The reusable core contains `skills/<skill-name>/SKILL.md`, `scripts/`, `docs/`, `templates/`, `examples/` and `tests/`. Your separate workspace contains immediate `<idea-slug>/CONTEXT.md` folders and portfolio reports. [AGENTS.md](AGENTS.md) routes requests; the [shared contract](docs/CONTRACT.md) defines ownership and workspace resolution. The helper rejects a workspace inside the core, including examples and fixtures.

No chat ingestion service exists: the host supplies context. Skills can be invoked by asking the agent to read their SKILL.md; no global installation or service is required. Procedures recommend or record decisions; they do not run a business for you.

The default is still **capture first, then one optional cheap market scan for new product ideas**. Conceptual notes need no market scan. Research failure never prevents saving. Market research retains its six-query/eight-page worker budget. Its inexpensive worker model and reasoning effort are configurable; unavailable research stays pending. No automatic work follows market-check.

Ask, for example:

- “Challenge my idea, then map its assumptions.”
- “Design one no-code test for its most important uncertainty.”
- “Triage all ideas and show what deserves attention instead of more research.”
- “Record these interview results and check whether promotion is justified.”
- “Review the portfolio for validation avoidance.”

Explicitly requested finite sequences are supported. Each skill writes only its owned output, and never launches the entire pipeline. Market evidence -> challenge -> assumptions -> validation -> external observations is a supported path, not an automatic queue.

## From idea to customer outcome

For commercial ideas, [offer-design](skills/offer-design/SKILL.md) creates a bounded offer hypothesis in OFFER.md: buyer, measurable outcome, scope, price, proof, onboarding and support. It supports services, productized services and software. Conceptual notes need no commercial offer.

Marketing → sales → onboarding → delivery → retention provides a way to locate the next uncertainty. Sales discovery can precede building; customer learning continues after release. [Commercial practice](docs/commercial-practice.md) explains how to use these ideas without treating promotional claims as evidence.

Validation plans include a reachable channel, denominators, a review window and stop rules. Execution-bridge can propose one small action in VALIDATING, PROMOTED, BUILDING or SHIPPED, within that state's boundaries. SHIPPED means externally usable; it does not prove revenue, profit or retention. Ongoing acquisition, delivery and support consume attention even after shipment.

## Lifecycle

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

## Mechanical checks and evidence review

`STATE.md` is the canonical append-only state history. Missing STATE means SEED; existing MARKET or long documentation never upgrades it. Moving a workspace never upgrades an idea; existing notes and state history are preserved. [promotion-gate/SKILL.md](skills/promotion-gate/SKILL.md) defines substantive evidence review; [docs/RECORDS.md](docs/RECORDS.md) defines the few machine-readable Markdown records.

```sh
python3 scripts/portfolio.py status
python3 scripts/portfolio.py audit
python3 scripts/portfolio.py transition my-idea RESEARCHED --reason "Review the sourced market finding" --evidence M1
python3 -m unittest discover -s tests -v
```

The transition command defaults to **read-only checks**. Applying requires `--apply --decision D1` and the gate's actual evidence review. All mutations use a cooperating-writer directory lock on macOS/Linux. The helper checks graph, artifacts, typed evidence, human-decision records, and capacity; it never runs research or implementation. It does not authenticate who wrote a human-decision record, prove that a cited observation is true, or enforce behavior against someone manually editing the files. Those are explicit human/agent responsibilities. Never manufacture records to satisfy a check. Direct edits to canonical history bypass safeguards; use the helper.

## Portfolio and calibration

`PORTFOLIO.md` in your workspace holds ranked recommendations and user annotations. Request triage when choosing what deserves attention. Request portfolio-review periodically (for example weekly while actively validating); it appends REVIEWS.md and flags stale work, resource conflicts and shiny-object risk without silently dropping ideas.

Cross-pollination is opt-in and writes at most three connections to CROSS_POLLINATIONS.md. It cannot invoke capture or create idea folders. Retrospectives append per-idea RETROSPECTIVE.md; cross-idea lessons go to CALIBRATION.md only when histories exist. Record expectations before tests; unknown past expectations stay unknown. Tiny samples yield tentative observations, not statistically significant rules.

## Validation and limits

Tests cover real filesystem behavior and structural gates. [tests/SCENARIOS.md](tests/SCENARIOS.md) adds semantic acceptance cases that code cannot judge, including evidence quality, duplicate mechanism detection and recursion boundaries. No external research, messages, charges, state promotions, or project builds occur in tests. Python's standard library is sufficient; no service, package installation, scheduler, UI, embeddings, or database is needed.

## Contributing and examples

See [CONTRIBUTING.md](CONTRIBUTING.md), the [fictional worked examples](examples/README.md), and [migration guidance](docs/migration.md). The core is MIT licensed; personal workspace contents remain separate.
