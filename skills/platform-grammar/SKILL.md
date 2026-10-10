---
name: platform-grammar
description: "Make layout, controls, menus, and navigation feel coherent with the product’s native platform."
---


# Use the platform’s familiar grammar

Based on Kole Jain’s UX/UI tutorials. These are unofficial, AI-assisted study notes and adapted skills; they were not written, approved or endorsed by Kole Jain. Permission has not been obtained from him.

[Source credit and reuse limits](../../SOURCE-MATERIAL.md)

## Mental model

Platform conventions reduce the amount people need to learn. Familiar control roles, grouping, and navigation can make a new application predictable, while isolated visual imitation may preserve none of the behavior.

## When this skill applies

Use when designing a native-like desktop application or translating a web workflow to a platform.

## Reasoning

Identify which conventions users already know: titlebar responsibilities, sidebar grouping, toolbar actions, menus, shortcuts, and selection. Reuse their roles deliberately; do not assume a screenshot communicates their entire behavior.

Translate a visual convention only when your implementation supports its meaning. A web control styled like a native menu still needs keyboard navigation and dismissal. Check current platform documentation when implementing exact native details.

## Worked example — original implementation adaptation

A desktop document app

Before: a marketing-style header consumes the top of the workspace, while actions float across unrelated cards.

After: stable navigation occupies the sidebar, actions for the current document share a toolbar, and menus preserve the user’s selection and return focus to their trigger.

## Failure modes

- Copying native chrome that has no working counterpart.

- Hardcoding dimensions from a dated screenshot.

- Replacing established platform shortcuts with arbitrary ones.

## Evidence that would support the decision

Perform navigation, selection, menus, and the main task using keyboard and pointer. Confirm that the actual platform behavior matches the convention being presented.

## Verification references

- [Follow the primary task to its result](../../checks/task-completion.md)

- [Make focus follow the interaction](../../checks/keyboard-focus.md)

## Source moments

- [Everything you need to Design macOS Apps EXACTLY like Apple (beginner friendly)](https://www.youtube.com/watch?v=Vy0KKvZJRH8&t=129s): Arrange top-level actions, sidebar navigation and user content into a predictable desktop shell.

- [7 Modern UI Layouts from 50 Top Software Companies (+ Free Figma File)](https://www.youtube.com/watch?v=VPeTgU7la34&t=38s): The walkthrough compares common SaaS layouts; their popularity is inspiration rather than proof of product fit.

## Related skills

- [design-system-decisions](../design-system-decisions/SKILL.md)

- [dashboard-orchestration](../dashboard-orchestration/SKILL.md)

Source moments and labeled source-frame comparisons are attributed teaching. Implementation examples, reasoning, and verification are our original agent-oriented adaptations. Read the source ledger for review limits.
