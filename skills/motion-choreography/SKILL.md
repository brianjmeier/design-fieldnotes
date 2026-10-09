---
name: motion-choreography
description: "Design stagger, continuity, and easing around related elements and the reading order."
---


# Choreograph a sequence as a dependency

## Mental model

A motion sequence coordinates elements rather than giving each an unrelated effect. Staging, timing, and easing can reinforce the structure and reading order of a composition.

## When this skill applies

Use for page entrances, transitions between sections, and multi-element interactive prototypes.

## Reasoning

Determine what should become legible first and which elements belong together. Model the sequence as named phases or relationships instead of unexplained timeout values. Preserve stable destinations and consistent element identities.

Translate prototype effects to browser constraints deliberately. Keep the page useful if scripts, media, or motion fail. Do not replay an entrance merely because a rerender occurred; distinguish presentation from actual loading.

## Worked example — original implementation adaptation

A product page entrance

Before: heading, image, navigation and buttons each animate with unrelated delays, leaving the main action unavailable.

After: essential content is available immediately. Optional decoration follows a coherent sequence; reduced motion shows the final composition and repeated navigation does not restart a long intro.

## Failure modes

- A fake loader presented as actual network progress.

- Hardcoded timing that changes meaning with different content.

- Persistent animated transforms that interfere with layout or hit areas.

## Evidence that would support the decision

Inspect first load, revisit, script failure, slow media, and reduced motion. Verify essential content and actions remain available.

## Verification references

- [Stress the layout with real content](../../checks/responsive-content.md)

- [Verify motion and its quiet equivalent](../../checks/motion-states.md)

## Source moments

- [Prototyping Professional Load Animations in Figma: Part 1](https://www.youtube.com/watch?v=nl8OFGdx75w&t=117s): Related source discussion; the skill’s examples and reasoning are our adaptation.

- [Developing Premium Load animations (HTML, CSS & JS): Part 2](https://www.youtube.com/watch?v=d4MF6pdAZNw&t=245s): Related source discussion; the skill’s examples and reasoning are our adaptation.

## Related skills

- [motion-causality](../motion-causality/SKILL.md)

- [prototype-production](../prototype-production/SKILL.md)

Source moments are attributed teaching. Examples, reasoning, and verification are our original agent-oriented adaptations. Read the source ledger for review limits.
