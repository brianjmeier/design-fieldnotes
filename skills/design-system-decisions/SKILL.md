---
name: design-system-decisions
description: "Use roles, tokens, and shared behavior to make new screens familiar and coherent."
---


# Turn repeated decisions into a system

Based on Kole Jain’s UX/UI tutorials. These are unofficial, AI-assisted study notes and adapted skills; they were not written, approved or endorsed by Kole Jain. Permission has not been obtained from him.

[Source credit and reuse limits](../../SOURCE-MATERIAL.md)

## Mental model

A design system preserves decisions across contexts. Repeatable type, spacing, colors, controls, and states make the interface learnable; a large component collection without consistent roles does not.

## When this skill applies

Use when UI drift appears, or an agent is adding screens to an established product.

## Reasoning

Inspect the existing system before inventing a new one. Find which roles already express the needed behavior. Separate semantic decisions from raw values so theme and density changes have explicit owners.

Extract repetition after understanding the variation. Share a component when its behavior is genuinely the same, and expose meaningful variants. Keep the implementation small enough that a contributor can understand and change it.

## Worked example — original implementation adaptation

Several creation dialogs

Before: every dialog has a different padding, label style, action order and pending treatment.

After: the dialogs share a field rhythm and action area with consistent primary, secondary, error, and pending states. Content remains local to each task.

```css
:root { --space-field: 12px; --space-section: 24px; --radius-control: 5px; }
.form-field + .form-field { margin-block-start: var(--space-field); }
.form-actions { margin-block-start: var(--space-section); }
```

## Failure modes

- New one-off values that ignore existing tokens.

- A huge generic component with flags for unrelated workflows.

- Consistent visuals paired with inconsistent keyboard or state behavior.

## Evidence that would support the decision

Compare the same control in several contexts and themes. Exercise its active states; verify that familiar appearance predicts familiar behavior.

## Verification references

- [Make focus follow the interaction](../../checks/keyboard-focus.md)

- [Exercise the component’s complete state model](../../checks/state-matrix.md)

## Source moments

- [Stop Making Pretty UIs. Think Like a Product Designer](https://www.youtube.com/watch?v=ADaQuZS04Rc&t=207s): Related source discussion; the skill’s examples and reasoning are our adaptation.

- [Figma Update: Everything In Under 2 Minutes](https://www.youtube.com/watch?v=fL1X2Mw6s3w&t=6s): Multi-edit applies a change across corresponding elements as if editing them separately.

## Related skills

- [semantic-color](../semantic-color/SKILL.md)

- [component-states](../component-states/SKILL.md)

Source moments and labeled source-frame comparisons are attributed teaching. Implementation examples, reasoning, and verification are our original agent-oriented adaptations. Read the source ledger for review limits.
