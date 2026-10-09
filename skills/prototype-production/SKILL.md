---
name: prototype-production
description: "Carry the useful behavior from a visual prototype into a resilient implementation."
---


# Translate the prototype’s intent

## Mental model

A prototype demonstrates selected relationships and states. Production code needs layout, semantics, lifecycle behavior, and fallback paths that may not exist in the visual demonstration.

## When this skill applies

Use when implementing Figma interactions or turning an animated concept into a working page.

## Reasoning

Extract the intended states and transition relationships. Determine which properties are visual decoration and which change layout or interaction. Preserve element identity, meaningful markup, and an understandable final state.

Use the existing project’s tools and conventions. Prefer a simple implementation with clear ownership over a literal recreation of every prototype layer. Measure and inspect the resulting behavior in the actual browser.

## Worked example — original implementation adaptation

An animated navigation prototype

Before: implementation copies every absolute coordinate and timeout from the prototype.

After: a semantic navigation region controls its open state; layout adapts to content; motion reinforces that state. Escape, focus return, reduced motion and script-independent content are considered explicitly.

## Failure modes

- A screenshot treated as a complete behavior specification.

- Animation wrappers that change hit areas or semantic order.

- A prototype interaction assumed to be keyboard-accessible automatically.

## Evidence that would support the decision

Compare meaningful start and destination states, then exercise keyboard, resize, failure and motion settings in the actual implementation.

## Verification references

- [Make focus follow the interaction](../../checks/keyboard-focus.md)

- [Verify motion and its quiet equivalent](../../checks/motion-states.md)

## Source moments

- [Developing Premium Load animations (HTML, CSS & JS): Part 2](https://www.youtube.com/watch?v=d4MF6pdAZNw&t=46s): The walkthrough builds a full-screen preloader; loading failure, reduced motion and focus need separate production checks.

- [Animated Dashboard Sidebar Tutorial in Figma (+ free design files)](https://www.youtube.com/watch?v=NtZeYmTMuo4&t=14s): Build a sidebar from stable navigation, consistent icons, and clearly bounded popovers.

## Related skills

- [motion-choreography](../motion-choreography/SKILL.md)

- [design-system-decisions](../design-system-decisions/SKILL.md)

Source moments are attributed teaching. Examples, reasoning, and verification are our original agent-oriented adaptations. Read the source ledger for review limits.
