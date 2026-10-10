---
name: density-recognition
description: "Group and differentiate meaningful content so people can locate answers without reading everything."
---


# Make density easier to scan

## Mental model

Density becomes difficult when information is undifferentiated. Grouping, recognizable identities, and distinct representations let people scan for a question instead of consuming a wall of similar text.

## When this skill applies

Use when a busy interface gets longer after adding whitespace but still feels difficult to read.

## Reasoning

Ask what someone is scanning for: due date, owner, urgency, or type. Group by the dimension that supports that task. Reserve visual variation for distinctions that carry meaning.

Preserve an explicit label when an icon is ambiguous. Familiarity depends on the audience: an avatar can cue a teammate, while an unfamiliar symbol may add another decoding task. Keep source data available when a summary replaces it.

## Worked example — original implementation adaptation

A release activity feed

Before: every event is a same-weight sentence in one chronological block.

After: events are grouped by release; actor identity is visually consistent, failures include a labeled severity marker, and the time is quiet. Full details remain available from the event.

## Failure modes

- Replacing precise language with unfamiliar icons.

- Grouping by what is convenient in code instead of the user’s query.

- Using color as the only way to recognize categories.

## Evidence that would support the decision

Give a reader a specific question and observe whether they can locate the answer. Compare that result against the ungrouped version using the same content.

## Verification references

- [Follow the primary task to its result](../../checks/task-completion.md)

- [Check semantics, then inspect meaning](../../checks/semantic-accessibility.md)

## Source moments

- [The secret behind weirdly perfect UI designs](https://www.youtube.com/watch?v=neE6wOuBIP8&t=146s): Related source discussion; the skill’s examples and reasoning are our adaptation.

- [The 8 UI/UX Cheat Codes for INSTANTLY Better Designs](https://www.youtube.com/watch?v=c1TvOcKdBVE&t=21s): Refine large type spacing, nested corner radii, and palettes with deliberate relationships.

## Related skills

- [alignment-structure](../alignment-structure/SKILL.md)

- [relative-emphasis](../relative-emphasis/SKILL.md)

Source moments and labeled source-frame comparisons are attributed teaching. Implementation examples, reasoning, and verification are our original agent-oriented adaptations. Read the source ledger for review limits.
