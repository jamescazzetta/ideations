---
name: capture-ideas
description: Preserve promising ideas from ongoing conversation as individual CONTEXT.md notes for later ideation. Use when a discussion surfaces a potentially novel mechanism, reusable pattern, useful connection, or thought worth revisiting, or when the user asks to capture an idea.
---

# Capture ideas

Read [the shared contract](../../docs/CONTRACT.md). Inputs are the conversation context available to this invocation and existing idea notes; own only the selected idea's CONTEXT.md and, for a genuinely new idea, its folder. No chat monitoring, status changes, implementation, or analysis cascade belongs to capture.

Resolve the private workspace using the shared contract and `python3 scripts/portfolio.py settings`. Capture one descriptive lowercase hyphenated folder per distinct idea there, containing `CONTEXT.md`. Never store portfolio data in the core checkout.

## When to capture

Notice ideas during ordinary conversation as well as explicit brainstorming. Capture when you can explain both the idea and why revisiting it could be valuable: an interesting mechanism, transferable pattern, unexpected connection, testable hypothesis, or useful unresolved question. An incomplete thought can qualify if its core insight is recoverable.

Use judgment; do not turn every explanation, routine task, or familiar example into an idea. Potential novelty relative to this discussion is enough; do not claim global originality or require a research search before saving. An explicit request to save an idea is sufficient regardless of novelty. Respect requests to skip capture.

## Write the note

- Capture during the current turn once enough context is available, without asking for confirmation or interrupting the main task for a brainstorming session.
- Use the helper inventory and a targeted search of existing workspace `CONTEXT.md` notes to find related ideas. Read likely matches. Extend the existing note when the mechanism is the same; create a new folder for a distinct idea and link related notes where useful. Avoid overwriting unrelated notes or the user's edits.
- Search only immediate workspace idea folders (CONTEXT.md present, SKILL.md absent), excluding fixtures and skill outputs. Match by mechanism and user problem, not title alone. Include parked and terminal ideas in duplicate checks; a repeated rejected idea is a dated addition, not an automatic restart. Preserve all original text and append dated developments. Optionally use `python3 scripts/portfolio.py capture <slug> --content <draft-file> --existing <matched-slug>` for an append to an existing idea; omit --existing only after checking for duplicates. The helper rejects a colliding new slug and never runs research.
- Write enough context for a future conversation to resume without the original chat. Prefer a few focused paragraphs and useful questions over a transcript or an elaborate proposal.
- Include a title, capture date, and a short source description based on the visible conversation. Add a conversation link only if one is available; never invent one.
- Explain the core idea, how the proposed mechanism works, the discussion that prompted it, and why it is worth exploring. Include a concrete example when it helps.
- Distinguish what the user proposed, what the assistant suggested, and any new extrapolation. Mark assumptions, uncertainty, and untested claims explicitly. Preserve disagreements and constraints that affect the idea.
- Include open questions and a small next exploration or experiment. These are suggestions for later, not authorization to begin implementation or research.
- On subsequent material developments, preserve the original capture date and add an updated date plus the new insight. Do not rewrite notes merely because the same idea was mentioned again.
- Exclude credentials and unnecessary sensitive details; summarize only context needed to understand the idea.
- Read the saved note to verify its fidelity, then briefly tell the user it was captured or updated with a clickable file link. Do not announce captures when no file was written.

## Suggested note shape

Adapt these sections to the idea; omit empty sections:

```markdown
# Descriptive idea title

Captured: YYYY-MM-DD
Source: Brief description of the conversation that prompted this idea.
Status: Seed / untested

## Idea and mechanism

## Context and why it matters

## Assumptions and open questions

## Next exploration
```

This workflow operates on conversation context available to the agent when these instructions are loaded. It does not monitor other chats or run in the background.

The `Status: Seed / untested` in a new context is historical capture metadata. Canonical state comes from STATE.md; absence means SEED. Light extrapolation should stay small and clearly labeled, usually one useful consequence or question, not an architecture or extra product ideas. Cross-pollination candidates, research reports, tests, and work on this system never trigger recursive capture.

## Market-check handoff

After saving a new product or service idea, apply [market-check](../market-check/SKILL.md) to produce a bounded market scan with a cheap delegated model. The user's current preference takes precedence; skip when they ask to capture only. Save the context first so research cannot block capture. Do not scan purely conceptual notes, repeat scans on routine edits, or turn the market report itself into another automatic capture. If research is unavailable, keep the idea saved and disclose that the scan is pending.
