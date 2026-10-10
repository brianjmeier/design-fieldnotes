---
name: gesture-intent
description: "A swipe should express a coherent spatial action and preserve a visible alternative."
---


# Make gestures legible and reversible

## Mental model

Gestures can reveal an action, move between contexts, or manipulate an object. Their motion and release behavior should communicate the intended operation instead of relying on memorized hidden shortcuts.

## When this skill applies

Use for swipe actions, carousels, draggable surfaces, and touch navigation.

## Reasoning

Define the object, direction, and consequence before designing the movement. Distinguish horizontal intent from ordinary vertical scrolling. Show enough feedback for someone to predict what release will do.

Provide a visible control for the same operation and a recovery path for accidental actions. Keep cancellation possible before committing. Test slow movement, partial release, reversal, and repeated input rather than only a perfect swipe.

## Worked example — original implementation adaptation

Archiving a message

Before: any left movement immediately removes the row with no explanation.

After: movement reveals a labeled archive action; incomplete intent returns the row. A menu also exposes Archive, and completion offers Undo with the same underlying result.

## Failure modes

- A swipe threshold chosen without testing scroll conflict.

- Gesture-only access to an important operation.

- A playful spring that obscures whether the action committed.

## Evidence that would support the decision

Observe real touch gestures and their ordinary-control equivalent. Verify release, cancellation, reversal, and recovery produce coherent outcomes.

## Verification references

- [Verify motion and its quiet equivalent](../../checks/motion-states.md)

- [Give gestures a discoverable alternative](../../checks/gesture-alternative.md)

## Source moments

- [Master the 3 Types of CRAZY Mobile UI Swipe Interactions](https://www.youtube.com/watch?v=14h1VnkQvIc&t=108s): Provide a visible button alternative to a swipe action so users can discover and perform it.

- [I spent a week gamifying apps. This is what I built](https://www.youtube.com/watch?v=jSxxAFxjxbU&t=29s): Connect points, streaks, milestones and social comparison to a meaningful real-world goal.

## Related skills

- [mobile-navigation](../mobile-navigation/SKILL.md)

- [motion-causality](../motion-causality/SKILL.md)

Source moments and labeled source-frame comparisons are attributed teaching. Implementation examples, reasoning, and verification are our original agent-oriented adaptations. Read the source ledger for review limits.
