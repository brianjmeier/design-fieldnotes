---
name: semantic-color
description: "Separate surfaces, brand accents, semantic states, and data series into distinct roles."
---


# Give color a job

## Mental model

Product color serves several jobs: separate surfaces, express interactive state, communicate meaning, and distinguish data. A fixed area ratio cannot determine all of these decisions.

## When this skill applies

Use for dashboards, themes, status systems, or designs where colors are scattered decoratively.

## Reasoning

Name colors by their role rather than their current pigment. A surface, selected item, failure, and chart series should not silently inherit the same brand token. Consider what each state must communicate without color.

Build theme mappings independently; do not invert a light palette. Evaluate actual foreground/background pairs after opacity and overlays. Choose categorical chart colors that remain distinguishable, with labels or patterns where needed.

## Source-video visual comparison

- [Quiet the repeated card surfaces](../../examples/quiet-card-surfaces.md): load both images before drawing visual conclusions.

## Worked example — original implementation adaptation

A deployment list

Before: brand purple is used for success, failure, selected rows, and every chart series.

After: neutral surfaces carry layout; selection uses the interaction accent; failed builds include an error icon and text; charts have explicit series labels. Each theme maps those roles deliberately.

```css
:root { --surface: #f6f5ef; --text: #22251f; --muted-text: #606558; --selection: #e2e8d6; }
[data-theme="dark"] { --surface: #20241e; --text: #f3f5eb; --muted-text: #b7beac; --selection: #35452e; }
```

## Failure modes

- Making semantic meaning depend on hue alone.

- Applying an arbitrary 60/30/10 ratio to a dense product.

- Assuming perceptually even colors automatically meet contrast requirements.

## Evidence that would support the decision

Measure text and relevant control contrast in each theme. Inspect selected, hover, focus, warning, and error states. Read charts without relying on color alone.

## Verification references

- [Measure color in its actual role](../../checks/color-contrast.md)

- [Exercise the component’s complete state model](../../checks/state-matrix.md)

## Source moments

- [Why the 60-30-10 Rule is RUINING Your UI Designs](https://www.youtube.com/watch?v=66oOi9OLMCw&t=275s): Related source discussion; the skill’s examples and reasoning are our adaptation.

- [The 7 Color Mistakes that RUIN your UI Designs](https://www.youtube.com/watch?v=EOcY3hPMQkk&t=76s): Use neutral surfaces and restrained borders to preserve visual hierarchy.

## Related skills

- [relative-emphasis](../relative-emphasis/SKILL.md)

- [design-system-decisions](../design-system-decisions/SKILL.md)

Source moments and labeled source-frame comparisons are attributed teaching. Implementation examples, reasoning, and verification are our original agent-oriented adaptations. Read the source ledger for review limits.
