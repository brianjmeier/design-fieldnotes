---
name: relative-emphasis
description: "A focal point stands out because its surroundings are quieter and its role is clear."
---


# Treat emphasis as a relationship

Based on Kole Jain’s UX/UI tutorials. These are unofficial, AI-assisted study notes and adapted skills; they were not written, approved or endorsed by Kole Jain. Permission has not been obtained from him.

[Source credit and reuse limits](../../SOURCE-MATERIAL.md)

## Mental model

Visual priority is relational. An accent does little when every neighboring element uses it. Quiet defaults make meaningful selection, urgency, and primary action distinguishable.

## When this skill applies

Use when everything looks important, or repeated decoration hides the next useful action.

## Reasoning

Name the decision that should lead the screen. Give its action or evidence the strongest relevant contrast; make supporting information quieter without making it unreadable.

Change the surroundings before escalating the focal point. Keep semantic urgency separate from ordinary brand emphasis. Several tasks can have local primary actions; the screen still needs a clear overall entry point.

## Worked example — original implementation adaptation

A settings panel

Before: all six default settings are bright accent chips, and “Save changes” is another equally bright element.

After: unchanged values are neutral. The modified setting has an explicit “Changed” label; the save action has a consistent primary treatment. Error color appears only when correction is needed.

## Failure modes

- Dimming secondary text below readable contrast.

- Using selected styling for every default value.

- Treating one primary action per page as an inflexible rule.

## Evidence that would support the decision

Inspect default, selected, changed, and error states side by side. Ask what changed and where the reader would act next without explaining the screen.

## Verification references

- [Measure color in its actual role](../../checks/color-contrast.md)

- [Exercise the component’s complete state model](../../checks/state-matrix.md)

## Source moments

- [The secret behind weirdly perfect UI designs](https://www.youtube.com/watch?v=neE6wOuBIP8&t=382s): Related source discussion; the skill’s examples and reasoning are our adaptation.

- [7 UI/UX mistakes that SCREAM you’re a beginner](https://www.youtube.com/watch?v=AH_ugxmLeUM&t=23s): Map navigation, skip paths, empty states and dynamic feedback before polishing the interface.

## Related skills

- [semantic-color](../semantic-color/SKILL.md)

- [typographic-roles](../typographic-roles/SKILL.md)

Source moments and labeled source-frame comparisons are attributed teaching. Implementation examples, reasoning, and verification are our original agent-oriented adaptations. Read the source ledger for review limits.
