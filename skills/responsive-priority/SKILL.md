---
name: responsive-priority
description: "Make narrow layouts preserve the reading order and the most useful action."
---


# Adapt priority before shrinking pixels

Based on Kole Jain’s UX/UI tutorials. These are unofficial, AI-assisted study notes and adapted skills; they were not written, approved or endorsed by Kole Jain. Permission has not been obtained from him.

[Source credit and reuse limits](../../SOURCE-MATERIAL.md)

## Mental model

Available space changes what can be shown together. A responsive layout should preserve the intended task and order while changing grouping, density, and surface placement.

## When this skill applies

Use when a desktop design becomes crowded on mobile or relies on fixed, ideal content.

## Reasoning

Identify what must stay visible together to make a decision. Decide which relationships can stack and which require intentional scrolling. Use flexible tracks and content-driven constraints rather than many arbitrary breakpoints.

Test the difficult content first: long names, large values, missing images, empty lists, and translated labels. Make truncation a considered information choice with a recovery path. Keep essential controls in a predictable place.

## Worked example — original implementation adaptation

A results table on a narrow screen

Before: all six columns compress until labels overlap and actions move outside the viewport.

After: the key identity and status remain legible, secondary fields move into an accessible detail view, and any necessary table scrolling is clearly bounded. The main action stays reachable.

## Failure modes

- A global overflow-hidden rule that conceals broken content.

- Changing visual order while leaving keyboard order confusing.

- Assuming a few screenshots cover text resizing and real-device behavior.

## Evidence that would support the decision

Use real and adversarial content at narrow, medium and wide widths. Complete the same task and inspect reflow, focus and any intentional scroll region.

## Verification references

- [Stress the layout with real content](../../checks/responsive-content.md)

- [Make focus follow the interaction](../../checks/keyboard-focus.md)

## Source moments

- [Website Layouts To Make A Professional Website Design in 2024](https://www.youtube.com/watch?v=P2ksReDwWkE&t=17s): Cards on a contrast surface rely on consistent, precise gaps.

- [Awful To AMAZING Web Designs Easily](https://www.youtube.com/watch?v=ulSOdTgoGeY&t=26s): Wireframe first; repeated left-image/right-copy rows can make a full page feel monotonous.

## Related skills

- [typographic-roles](../typographic-roles/SKILL.md)

- [dashboard-orchestration](../dashboard-orchestration/SKILL.md)

Source moments and labeled source-frame comparisons are attributed teaching. Implementation examples, reasoning, and verification are our original agent-oriented adaptations. Read the source ledger for review limits.
