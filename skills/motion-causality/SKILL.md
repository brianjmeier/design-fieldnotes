---
name: motion-causality
description: "Animate a meaningful relationship: action, state, location, or continuity."
---


# Use motion to explain change

## Mental model

Motion can connect an input to its result, preserve a sense of location, and make state transitions understandable. Decorative movement adds little when the person cannot explain what changed.

## When this skill applies

Use for microinteractions, navigation transitions, selection, and state feedback.

## Reasoning

Describe the relationship the animation should communicate. A selected item moving into a collection implies continuity; an arbitrary flourish may distract from the actual result. Build the destination state before the transition.

Keep interruption and reversal coherent. Avoid delaying the action for decoration. Provide a reduced-motion version that carries the same status through immediate layout, text, or another quiet cue.

## Worked example — original implementation adaptation

Adding a task to a collection

Before: the whole screen flashes and the item disappears without a clear destination.

After: the collection count updates and the destination is clearly named. A short contextual transition reinforces the move when motion is enabled; the same message remains in reduced motion.

## Failure modes

- Animation used to disguise slow or uncertain work.

- Overlapping transitions after rapid repeated input.

- Essential status conveyed only through movement.

## Evidence that would support the decision

Try normal, reduced, interrupted, and repeated motion. Confirm the destination, state, and focus remain understandable in every version.

## Verification references

- [Verify motion and its quiet equivalent](../../checks/motion-states.md)

- [Exercise the component’s complete state model](../../checks/state-matrix.md)

## Source moments

- [11 Micro Animations That Will Instantly Level Up Your UI (free figma file)](https://www.youtube.com/watch?v=ld1zhQMXxXU&t=14s): Use small transitions to communicate pressed, completed, progressing and expanded states.

- [5 Trendy Animations to Steal for Your Next Web Design](https://www.youtube.com/watch?v=ZsP20PN14O0&t=132s): Hover and click effects are optional treatments that still need input, accessibility and performance checks.

## Related skills

- [gesture-intent](../gesture-intent/SKILL.md)

- [motion-choreography](../motion-choreography/SKILL.md)

Source moments are attributed teaching. Examples, reasoning, and verification are our original agent-oriented adaptations. Read the source ledger for review limits.
