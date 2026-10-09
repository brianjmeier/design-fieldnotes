---
name: alignment-structure
description: "Shared edges organize compact content before borders, cards, or additional whitespace."
---


# Use edges to create structure

## Mental model

Alignment gives the eye stable paths across related information. Consistent text starts, numerical ends, and internal baselines can create structure without enclosing every item in another box.

## When this skill applies

Use for lists, cards, sidebars, forms, and interfaces that feel subtly unsettled.

## Reasoning

Identify the edges a person compares: names, values, labels, and actions. Choose a few shared anchors. A number column should support magnitude comparison; an action column should remain predictable as names wrap.

Use content-driven grid tracks and consistent internal gaps. Inspect optical alignment after mathematical alignment: an icon’s visible shape can sit off-center inside its asset box. Add a border only if it clarifies a real boundary.

## Worked example — original implementation adaptation

A task row with changing content

Before: the checkbox, name, owner and menu are independently positioned. Long task titles push the menu out of alignment.

After: the row shares three tracks; the title wraps in the flexible middle, while the checkbox and menu keep stable edges. Related rows align without nested cards.

```css
.task-row { display: grid; grid-template-columns: 24px minmax(0, 1fr) max-content; gap: 12px; align-items: start; }
.amount { text-align: right; font-variant-numeric: tabular-nums; }
```

## Failure modes

- Centering long labels makes scanning inconsistent.

- Hiding useful actions solely to make the composition tidy.

- Adding many independent offsets instead of fixing the shared structure.

## Evidence that would support the decision

Compare the row with short and three-line titles, missing owners, and large values. Inspect both the alignment and whether the action remains reachable.

## Verification references

- [Stress the layout with real content](../../checks/responsive-content.md)

## Source moments

- [The secret behind weirdly perfect UI designs](https://www.youtube.com/watch?v=neE6wOuBIP8&t=26s): Related source discussion; the skill’s examples and reasoning are our adaptation.

- [8 Web Design Hacks To ACTUALLY Make Your Designs Better](https://www.youtube.com/watch?v=Lp6ey4AyDzA&t=81s): Related source discussion; the skill’s examples and reasoning are our adaptation.

## Related skills

- [density-recognition](../density-recognition/SKILL.md)

- [data-shape](../data-shape/SKILL.md)

Source moments are attributed teaching. Examples, reasoning, and verification are our original agent-oriented adaptations. Read the source ledger for review limits.
