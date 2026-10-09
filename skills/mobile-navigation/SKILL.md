---
name: mobile-navigation
description: "Organize navigation, contextual surfaces, and controls around a small touch viewport."
---


# Fit the interaction to the phone

## Mental model

Mobile interfaces use constrained space and touch interaction to shape their structure. Stable destinations, contextual sheets, and reachable controls need deliberate organization rather than a shrunk desktop layout.

## When this skill applies

Use when moving a workflow to mobile or designing a small-screen application.

## Reasoning

Separate persistent destinations from actions on the current object. Give navigation an understandable hierarchy. Decide whether secondary work belongs in a sheet, a new screen, or an inline disclosure based on context and complexity.

Keep keyboard appearance, safe areas, and long content in view. Touch has no hover state. Give crowded icons actual hit areas and preserve labels where the action is unfamiliar. Use real-device testing for platform behavior.

## Worked example — original implementation adaptation

Editing a task on a phone

Before: a desktop side panel becomes a narrow overlay with its save action behind the on-screen keyboard.

After: the editor uses a scrollable contextual surface, clear dismissal, and reachable save action. Invalid fields are named and brought into view without losing the draft.

## Failure modes

- Assuming a narrow browser viewport proves touch behavior.

- Bottom navigation overloaded with rarely used destinations.

- Fixed controls that cover content when the keyboard opens.

## Evidence that would support the decision

Complete the flow on a real phone with the keyboard visible, one long field, and a recoverable error. Check orientation and scrolling as relevant.

## Verification references

- [Stress the layout with real content](../../checks/responsive-content.md)

- [Give gestures a discoverable alternative](../../checks/gesture-alternative.md)

## Source moments

- [Everything you need to know about Mobile App UI’s in 8 minutes (beginner friendly)](https://www.youtube.com/watch?v=Gfsd8NNuD9g&t=23s): Reserve bottom navigation for a few key destinations.

- [TikTok’s UX is so GOOD it should be ILLEGAL (seriously)](https://www.youtube.com/watch?v=ixUq4HM4FNg&t=71s): The video connects TikTok's ease of use to preference learning, a dominant swipe action, large targets and fast feedback.

## Related skills

- [gesture-intent](../gesture-intent/SKILL.md)

- [platform-grammar](../platform-grammar/SKILL.md)

Source moments are attributed teaching. Examples, reasoning, and verification are our original agent-oriented adaptations. Read the source ledger for review limits.
