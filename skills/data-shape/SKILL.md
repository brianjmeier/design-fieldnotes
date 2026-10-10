---
name: data-shape
description: "Use comparison, chronology, identity, and magnitude to choose representations."
---


# Let the data choose its form

## Mental model

Different data asks for different reading behavior. Tables support comparison, timelines express sequence, chips mark bounded categories, and charts summarize relationships. The format should make the intended question easier to answer.

## When this skill applies

Use for dashboards or dense lists that look plausible but are awkward to use.

## Reasoning

Name the question before selecting the component. Use a table when readers compare the same fields across entities, and a timeline when order and intervals are the point. Avoid charts added merely to fill a card.

Format units and precision consistently. Preserve full values when truncation would hide identity. Treat sorting, filtering, grouping and details as part of the data experience, including clear empty results.

## Worked example — original implementation adaptation

An operations dashboard

Before: deployment steps are a table of timestamp strings, and costs are left-aligned numbers without units.

After: the steps form a chronological sequence with labeled outcomes. Comparable costs stay in a table with right-aligned amounts, explicit currency, and consistent precision.

## Failure modes

- Summaries that conceal the underlying values needed for a decision.

- Truncation without any way to recover the full identifier.

- Charts with missing units, misleading axes, or no useful question.

## Evidence that would support the decision

Try comparison, finding an exception, and reconstructing a sequence with realistic data. Observe whether the representation supports each intended task.

## Verification references

- [Follow the primary task to its result](../../checks/task-completion.md)

- [Stress the layout with real content](../../checks/responsive-content.md)

## Source moments

- [The 3 dashboard UI flaws that give away you've NEVER built one](https://www.youtube.com/watch?v=Ksx9C2-3yMo&t=22s): Related source discussion; the skill’s examples and reasoning are our adaptation.

- [Redesigning a Finance Dashboard UI from SCRATCH (ft. Dribbble)](https://www.youtube.com/watch?v=Yr2uIcFZDDQ&t=40s): Rank dashboard modules by task importance and make important work visible without an extra click.

## Related skills

- [density-recognition](../density-recognition/SKILL.md)

- [dashboard-orchestration](../dashboard-orchestration/SKILL.md)

Source moments and labeled source-frame comparisons are attributed teaching. Implementation examples, reasoning, and verification are our original agent-oriented adaptations. Read the source ledger for review limits.
