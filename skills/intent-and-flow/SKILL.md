---
name: intent-and-flow
description: "Start from the person’s intent, the information they need, and the next useful state."
---


# Design the job, then the screen

## Mental model

An interface is one moment in a larger flow. Its quality depends on how someone arrives, what they can decide, and where their action leaves them. A polished screen can still fail when the surrounding sequence is missing.

## When this skill applies

Use when a new screen has no obvious purpose, or an attractive flow leaves users stranded.

## Reasoning

Write the user’s job as an observable outcome. For a release dashboard, “find the release that needs intervention” is more useful than “show analytics.” Identify the minimum evidence needed to make that decision.

Map the entry, action, result, and recovery. Give the result a meaningful destination. Put secondary information where it supports a decision; avoid adding an attractive component without a role in the flow.

## Worked example — original implementation adaptation

Creating a shared project

Before: “Create” closes the form and returns to an unchanged list. The person has to search for what they just made.

After: the project detail opens with the saved name, a completion message, and an optional invitation action. Skipping invitations leaves the project usable.

## Failure modes

- Equating a visible button with a completed task.

- Making onboarding mandatory when the product can already be used.

- Adding an extra screen to compensate for unclear copy.

## Evidence that would support the decision

Observe a person enter the flow, finish the job, and recover from one refusal. Record where they had to guess. A screenshot cannot prove that the result exists.

## Verification references

- [Follow the primary task to its result](../../checks/task-completion.md)

- [Exercise the component’s complete state model](../../checks/state-matrix.md)

## Source moments

- [Stop Making Pretty UIs. Think Like a Product Designer](https://www.youtube.com/watch?v=ADaQuZS04Rc&t=122s): Related source discussion; the skill’s examples and reasoning are our adaptation.

- [How to think like a GENIUS UI/UX designer](https://www.youtube.com/watch?v=HE4rLEQpiXY&t=26s): Start from the user's task and add features only when they serve a real intent.

## Related skills

- [progressive-disclosure](../progressive-disclosure/SKILL.md)

- [component-states](../component-states/SKILL.md)

Source moments and labeled source-frame comparisons are attributed teaching. Implementation examples, reasoning, and verification are our original agent-oriented adaptations. Read the source ledger for review limits.
