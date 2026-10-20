# Fictional worked examples

Every customer, observation, price, decision and outcome in these folders is invented teaching data. No outreach, payment, implementation or release occurred. Their records exercise the format and structural gates; they cannot satisfy a real evidence review. In particular, example.invalid is intentionally not a usable release.

## Booking recovery: from an offer to learning after delivery

Read [CONTEXT](booking-recovery/CONTEXT.md), [OFFER](booking-recovery/OFFER.md), [ASSUMPTIONS](booking-recovery/ASSUMPTIONS.md) and [VALIDATION](booking-recovery/VALIDATION.md). The service starts with a scoped manual pilot, a price hypothesis and a predeclared two-payment threshold.

The [invented observations](booking-recovery/OBSERVATIONS.md) include contact denominators, objections, payments, acquisition time and delivery effort. [GATE](booking-recovery/GATE.md), [EVIDENCE](booking-recovery/EVIDENCE.md) and [STATE](booking-recovery/STATE.md) illustrate distinct checks and decisions for promotion, bounded implementation and shipment. The gate never performs the build.

[NEXT](booking-recovery/NEXT.md) proposes a retention/outcome conversation after shipment; it does not reopen the terminal state or execute contact. [RETROSPECTIVE](booking-recovery/RETROSPECTIVE.md) separates revenue, effort and unknown repeat business. A successful pilot does not establish durable demand.

## Invoice reminder: a failed test and deliberate parking

Read [OFFER](invoice-reminder/OFFER.md) and [VALIDATION](invoice-reminder/VALIDATION.md), then [OBSERVATIONS](invoice-reminder/OBSERVATIONS.md). Zero payments meet the declared failure threshold despite positive comments.

[GATE](invoice-reminder/GATE.md) blocks promotion; an explicit fictional decision in [EVIDENCE](invoice-reminder/EVIDENCE.md) precedes PARKED in [STATE](invoice-reminder/STATE.md). [RETROSPECTIVE](invoice-reminder/RETROSPECTIVE.md) preserves the missed prediction. The response is not an automatic new build or an indefinite extension of outreach.

## Inspect in isolation

The helper rejects a workspace inside the core. Copy examples to a temporary directory first:

```sh
demo_workspace=$(mktemp -d)
cp -R examples/booking-recovery examples/invoice-reminder "$demo_workspace/"
python3 scripts/portfolio.py --root "$demo_workspace" status
```

Expected states: booking-recovery SHIPPED and invoice-reminder PARKED, with no active/building slots. The automated suite replays these histories in temporary workspaces, verifies negative evidence blocks promotion and checks that offer/next-action reports never advance state. This is structural validation, not an independent model-behavior evaluation.
