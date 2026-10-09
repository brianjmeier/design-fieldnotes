---
name: hidden-ui
description: "Menus, tooltips, errors, announcements, and transient states make the visible screen function."
---


# Design the UI between screenshots

## Mental model

A product includes interactions that are absent from its resting screenshot. Contextual controls, explanations, state changes, and recoveries need the same design attention as the default view.

## When this skill applies

Use when a generated or portfolio interface has an attractive shell but incomplete behavior.

## Reasoning

Follow every visible affordance through its result. Inspect the lifecycle of menus and overlays: what invokes them, where they appear, how they leave, and where focus goes. Name ambiguous actions with useful labels.

Include useful feedback when work starts, completes, or fails. Reserve tooltips for supporting explanation rather than the only source of essential content. Keep persistent errors near the thing that needs correction.

## Worked example — original implementation adaptation

Copying a table identifier

Before: an unlabeled icon copies silently, leaving the user uncertain whether anything happened.

After: the control has a clear accessible name; activating it announces “Identifier copied.” If the clipboard fails, a recoverable alternative appears beside the value.

## Failure modes

- A click handler that only changes the button’s appearance.

- Success messages before the underlying operation has succeeded.

- Tooltips containing essential content unavailable to touch users.

## Evidence that would support the decision

Inspect the interface in active states as well as at rest. Verify names, focus order, dismissal, pending work, success, and failure behavior.

## Verification references

- [Check semantics, then inspect meaning](../../checks/semantic-accessibility.md)

- [Exercise the component’s complete state model](../../checks/state-matrix.md)

## Source moments

- [The 3 dashboard UI flaws that give away you've NEVER built one](https://www.youtube.com/watch?v=Ksx9C2-3yMo&t=300s): Related source discussion; the skill’s examples and reasoning are our adaptation.

- [Upgrading 9 CRUCIAL UI Elements (free figma file included)](https://www.youtube.com/watch?v=gKM6b2EnW1k&t=130s): Give charts readable scales and time context so their visual treatment supports interpretation.

## Related skills

- [component-states](../component-states/SKILL.md)

- [progressive-disclosure](../progressive-disclosure/SKILL.md)

Source moments are attributed teaching. Examples, reasoning, and verification are our original agent-oriented adaptations. Read the source ledger for review limits.
