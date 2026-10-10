---
name: dashboard-orchestration
description: "Coordinate navigation, summaries, detailed data, and contextual actions into one usable workspace."
---


# Compose a dashboard around decisions

## Mental model

A dashboard is an information and interaction system. Its frame, navigation, content regions, and secondary surfaces need to cooperate. Attractive isolated cards do not automatically produce a usable workspace.

## When this skill applies

Use when building a dashboard from scratch or reorganizing an existing one.

## Reasoning

Identify the recurring decisions and the objects the user acts on. Build the shell around stable navigation and put the most useful evidence near its related action. Choose summaries that lead to meaningful detail.

Coordinate density across regions. A narrow navigation rail and a wide comparison table have different space needs. Keep route, selection, filter, and overlay state coherent so navigating back does not unexpectedly reset the work.

## Worked example — original implementation adaptation

A release workspace

Before: six KPI cards and two charts precede the actual failing release list.

After: releases needing attention lead the view; a selected release opens context beside the list. Summary metrics explain the selected time range and link to the affected records.

## Failure modes

- A collection of unrelated cards with no clear decision path.

- Global filters that do not apply consistently to visible data.

- Creating a dedicated page for every small contextual action.

## Evidence that would support the decision

Track selection, filtering, detail navigation, return, and an empty result. Test whether the user can move from an exception to the relevant action.

## Verification references

- [Follow the primary task to its result](../../checks/task-completion.md)

- [Exercise the component’s complete state model](../../checks/state-matrix.md)

## Source moments

- [EVERYTHING you need to know to build a Dashboard UI in 8 minutes (beginner friendly)](https://www.youtube.com/watch?v=B7k5rOgmOGY&t=91s): Focus the dashboard on the user's most important work, supported by quiet navigation and readable data.

- [Animated Dashboard Sidebar Tutorial in Figma (+ free design files)](https://www.youtube.com/watch?v=NtZeYmTMuo4&t=14s): Build a sidebar from stable navigation, consistent icons, and clearly bounded popovers.

## Related skills

- [data-shape](../data-shape/SKILL.md)

- [responsive-priority](../responsive-priority/SKILL.md)

Source moments and labeled source-frame comparisons are attributed teaching. Implementation examples, reasoning, and verification are our original agent-oriented adaptations. Read the source ledger for review limits.
