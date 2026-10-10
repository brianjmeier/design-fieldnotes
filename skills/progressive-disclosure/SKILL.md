---
name: progressive-disclosure
description: "Keep the main task explicit while revealing secondary choices in context."
---


# Reveal complexity at the right moment

## Mental model

Progressive disclosure manages when information appears. Frequency, importance, and the person’s current intent determine how explicit an action should be. A popover or drawer can preserve context while keeping the default view focused.

## When this skill applies

Use when a screen is overloaded with secondary actions, advanced controls, or onboarding explanations.

## Reasoning

Place frequent and consequential actions where people can discover them. Give occasional actions a clear contextual entry point. Keep related secondary work near its subject when navigation to a whole page would interrupt the task.

Design entry, dismissal, focus, and return as one interaction. Hover may offer a shortcut, but keyboard and touch need a reachable equivalent. Onboarding should follow useful actions and permit skipping.

## Source-video visual comparison

- [Separate the core form from optional controls](../../examples/focused-link-creation.md): load both images before drawing visual conclusions.

## Worked example — original implementation adaptation

Sharing a project

Before: a permanently expanded permission form occupies the side of every project table.

After: a labeled “Share” action opens a contextual panel with search first, current collaborators next, and advanced permissions beneath a clear disclosure. Closing returns to the original row.

## Failure modes

- Moving essential actions into an unexplained overflow menu.

- Hover-only controls with no touch or keyboard path.

- A long first-run modal whose instructions disappear before they are useful.

## Evidence that would support the decision

Find the action from its default state without prompting. Test opening, completing, dismissing, and returning using keyboard and touch alternatives.

## Verification references

- [Make focus follow the interaction](../../checks/keyboard-focus.md)

- [Give gestures a discoverable alternative](../../checks/gesture-alternative.md)

## Source moments

- [The 3 dashboard UI flaws that give away you've NEVER built one](https://www.youtube.com/watch?v=Ksx9C2-3yMo&t=145s): Related source discussion; the skill’s examples and reasoning are our adaptation.

- [Everything you need to know about Mobile App UI’s in 8 minutes (beginner friendly)](https://www.youtube.com/watch?v=Gfsd8NNuD9g&t=313s): Teach gestures and retain visible alternatives for the same actions.

## Related skills

- [intent-and-flow](../intent-and-flow/SKILL.md)

- [hidden-ui](../hidden-ui/SKILL.md)

Source moments and labeled source-frame comparisons are attributed teaching. Implementation examples, reasoning, and verification are our original agent-oriented adaptations. Read the source ledger for review limits.
