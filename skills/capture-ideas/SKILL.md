---
name: capture-ideas
description: Save a promising idea from the current conversation, or extend an existing note when the same idea develops.
---

# Capture an idea

Preserve enough context for a future conversation to pick up the thought.

Follow the [shared rules](../../docs/CONTRACT.md). Use the current conversation and existing workspace ideas. Save only CONTEXT.md and, for a new idea, its folder.

## Decide whether to capture

Capture a thought when you can explain its mechanism or insight and why revisiting it could be useful. An incomplete thought can qualify. An explicit request to save is sufficient; novelty research is unnecessary. Respect requests to skip capture and leave routine tasks uncaptured.

## Save the thought

1. Use the helper inventory and read likely matches. Match by the underlying mechanism and user problem, not the title. Extend an existing note when it is the same idea; create a folder only for a distinct one. Include parked and terminal ideas in this check. A repeated terminal idea gets a dated addition, not a restart.
2. Write a few focused paragraphs: title, capture date, visible source, idea and mechanism, why it matters, relevant context, and open questions. Use a conversation link only when available. Separate the user's proposal from assistant suggestions and keep any extrapolation small and labeled.
3. Add one possible next exploration. It is a suggestion, not an instruction to build or research. Preserve disagreements, uncertainty, original dates and earlier annotations.
4. Save during this turn, keeping the main task moving. Use a lowercase hyphenated slug. For an existing match, append with:

   ```sh
   python3 scripts/portfolio.py capture <slug> --content <draft-file> --existing <matched-slug>
   ```

   Omit `--existing` only after checking for duplicates. The draft contains the new note or dated addition, not a copy of existing history.
5. Read the saved note to check fidelity. Tell the user what was captured or extended and link it. A routine mention without new substance needs no rewrite.

## Optional market scan

After saving a **new product or service idea**, hand off to [market-check](../market-check/SKILL.md) unless the user asked to skip research. Save first so research cannot block capture.

Conceptual notes, routine edits, and skill outputs need no scan. If research tools are unavailable, keep the note and report the scan as pending once. This is the only default follow-up; no later skills run automatically.
