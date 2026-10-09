---
name: component-states
description: "Define useful pending, empty, successful, refused, and partial states from the real lifecycle."
---


# Model the component beyond its default

## Mental model

Components represent changing resources and user intent. Their states need clear meaning and useful transitions; designing only the ideal populated state leaves the product incomplete.

## When this skill applies

Use for generated UIs, forms, integration actions, and asynchronous data surfaces.

## Reasoning

Identify the actual operation and the states it can enter. Keep loading distinct from empty, and refusal distinct from success. Define what remains available when only part of the data arrives.

Keep user input through recoverable failures. Match feedback to confirmed outcomes. Prevent duplicate intent while work is pending and rely on the resource owner to handle concurrency, rather than pretending the button can prove idempotency.

## Worked example — original implementation adaptation

Connecting an integration

Before: clicking Connect replaces the button with a success check immediately; a network failure is invisible.

After: the UI announces the pending connection, reports the confirmed result, and explains a refusal with Retry. Existing settings and input remain intact.

## Failure modes

- A loading skeleton displayed when the result is actually empty.

- An optimistic success with no rollback or refusal explanation.

- Removing content during a refresh when it could remain useful.

## Evidence that would support the decision

Force pending, success, failure, empty and partial states through an existing fixture seam. Verify the action’s outcome and recovery, not only its style.

## Verification references

- [Follow the primary task to its result](../../checks/task-completion.md)

- [Exercise the component’s complete state model](../../checks/state-matrix.md)

## Source moments

- [Stop Making Pretty UIs. Think Like a Product Designer](https://www.youtube.com/watch?v=ADaQuZS04Rc&t=61s): Related source discussion; the skill’s examples and reasoning are our adaptation.

- [5 SaaS UI/UX mistakes that SCREAM you Vibe Code](https://www.youtube.com/watch?v=PDcQJOPby1k&t=24s): Review icon coherence, meaningful data and feature completeness in generated SaaS interfaces.

## Related skills

- [hidden-ui](../hidden-ui/SKILL.md)

- [design-system-decisions](../design-system-decisions/SKILL.md)

Source moments are attributed teaching. Examples, reasoning, and verification are our original agent-oriented adaptations. Read the source ledger for review limits.
