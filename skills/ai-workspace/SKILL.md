---
name: ai-workspace
description: "Give prompts, context, generated artifacts, history, and memory clear roles and user control."
---


# Make AI work visible and recoverable

Based on Kole Jain’s UX/UI tutorials. These are unofficial, AI-assisted study notes and adapted skills; they were not written, approved or endorsed by Kole Jain. Permission has not been obtained from him.

[Source credit and reuse limits](../../SOURCE-MATERIAL.md)

## Mental model

An AI interface is a workspace around uncertain work. Prompt context, retrievable history, editable output, visible memory, and honest feedback help people understand what the tool is using and what it has produced.

## When this skill applies

Use when designing a prompt composer, generation flow, research assistant, or AI editing surface.

## Reasoning

Keep the input’s attachments and context visible before submission. Preserve the draft while work is pending. Model partial output, cancellation, refusal, and retry explicitly; streaming text alone does not prove that the operation succeeded.

Make outputs retrievable and editable without regenerating everything. If memory exists, show what is stored and provide real controls. Surface actual source evidence and operation status; avoid invented progress steps or unsupported numeric confidence.

## Worked example — original implementation adaptation

A document research assistant

Before: a blank input sends a request, then shows a simulated “researching” animation and an arbitrary 97% confidence label.

After: the selected document is visible in the composer. Confirmed retrieval results link to their sources; generated output is labeled and retained in searchable history. Cancellation preserves the prompt, and unsupported claims are identified without fabricated probabilities.

## Failure modes

- A decorative research trail presented as actual work.

- A confidence percentage with no calibrated meaning.

- Memory that cannot be inspected, edited or removed by its owner.

## Evidence that would support the decision

Test attachments, pending work, partial output, cancellation, search, edits, and any memory controls. Confirm evidence links actually support the output.

## Verification references

- [Follow the primary task to its result](../../checks/task-completion.md)

- [Check semantics, then inspect meaning](../../checks/semantic-accessibility.md)

- [Exercise the component’s complete state model](../../checks/state-matrix.md)

## Source moments

- [The 7 UI Components to Design Like Unicorn AI Startups](https://www.youtube.com/watch?v=If7iCPDy2vk&t=111s): Related source discussion; the skill’s examples and reasoning are our adaptation.

## Related skills

- [hidden-ui](../hidden-ui/SKILL.md)

- [progressive-disclosure](../progressive-disclosure/SKILL.md)

Source moments and labeled source-frame comparisons are attributed teaching. Implementation examples, reasoning, and verification are our original agent-oriented adaptations. Read the source ledger for review limits.
