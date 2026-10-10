---
name: design-fieldnotes
description: Choose a relevant UX/UI concept skill when building or changing an interface, using product intent, evidence, and contextual judgment.
---

# Design Fieldnotes — agent entry point

Based on [Kole Jain’s UX/UI tutorials](https://www.youtube.com/@KoleJain). This is an unofficial, AI-assisted study-note library. These skills were not written, approved or endorsed by Kole Jain. Permission has not been obtained from him. His videos and source-frame excerpts retain their respective owners’ rights and are not covered by this project’s MIT license. Read [source credit and reuse limits](../../SOURCE-MATERIAL.md).
Understand the user outcome before choosing a skill. The concept teaches a mechanism;
the linked verification method helps determine whether your implementation expresses it.
Read the smallest relevant skill in full rather than applying every rule to every screen.

Bring the primary user task, real content, current code and platform constraints.
Explain the mechanism you intend to change. Offer a concrete before/after example and
identify evidence that would falsify your design decision. Implement in the existing
system, observe the result, and report material limitations. Aesthetic suggestions are
contextual; accessibility standards are attributed separately. Do not treat sponsor
recommendations, tools in old tutorials, or trend observations as mandatory choices.

## Route by the problem

- [Design the job, then the screen](../intent-and-flow/SKILL.md): Use when a new screen has no obvious purpose, or an attractive flow leaves users stranded.
- [Use edges to create structure](../alignment-structure/SKILL.md): Use for lists, cards, sidebars, forms, and interfaces that feel subtly unsettled.
- [Make density easier to scan](../density-recognition/SKILL.md): Use when a busy interface gets longer after adding whitespace but still feels difficult to read.
- [Treat emphasis as a relationship](../relative-emphasis/SKILL.md): Use when everything looks important, or repeated decoration hides the next useful action.
- [Make typography express the information](../typographic-roles/SKILL.md): Use when headings compete, body text feels tiring, or a layout breaks when copy changes.
- [Give color a job](../semantic-color/SKILL.md): Use for dashboards, themes, status systems, or designs where colors are scattered decoratively.
- [Let the data choose its form](../data-shape/SKILL.md): Use for dashboards or dense lists that look plausible but are awkward to use.
- [Reveal complexity at the right moment](../progressive-disclosure/SKILL.md): Use when a screen is overloaded with secondary actions, advanced controls, or onboarding explanations.
- [Design the UI between screenshots](../hidden-ui/SKILL.md): Use when a generated or portfolio interface has an attractive shell but incomplete behavior.
- [Compose a dashboard around decisions](../dashboard-orchestration/SKILL.md): Use when building a dashboard from scratch or reorganizing an existing one.
- [Fit the interaction to the phone](../mobile-navigation/SKILL.md): Use when moving a workflow to mobile or designing a small-screen application.
- [Make gestures legible and reversible](../gesture-intent/SKILL.md): Use for swipe actions, carousels, draggable surfaces, and touch navigation.
- [Use the platform’s familiar grammar](../platform-grammar/SKILL.md): Use when designing a native-like desktop application or translating a web workflow to a platform.
- [Build a landing page as an argument](../landing-narrative/SKILL.md): Use for product pages, marketing sites, and redesigns where the offer is difficult to understand.
- [Make the brand belong to its audience](../audience-identity/SKILL.md): Use when a site looks competent but interchangeable, or its visuals contradict the audience named in its copy.
- [Compose one idea per section](../section-composition/SKILL.md): Use when a feature section feels generic, crowded, or disconnected from the claim it is supposed to support.
- [Transfer the mechanism from a reference](../reference-transfer/SKILL.md): Use when starting a layout, exploring alternatives, or specifying work for a coding agent.
- [Turn repeated decisions into a system](../design-system-decisions/SKILL.md): Use when UI drift appears, or an agent is adding screens to an established product.
- [Use motion to explain change](../motion-causality/SKILL.md): Use for microinteractions, navigation transitions, selection, and state feedback.
- [Choreograph a sequence as a dependency](../motion-choreography/SKILL.md): Use for page entrances, transitions between sections, and multi-element interactive prototypes.
- [Adapt priority before shrinking pixels](../responsive-priority/SKILL.md): Use when a desktop design becomes crowded on mobile or relies on fixed, ideal content.
- [Model the component beyond its default](../component-states/SKILL.md): Use for generated UIs, forms, integration actions, and asynchronous data surfaces.
- [Support motivation without stealing agency](../motivation-agency/SKILL.md): Use when adding streaks, rewards, achievements, infinite content, or recurring prompts.
- [Bound the visual experiment](../visual-experiment/SKILL.md): Use for a distinctive marketing direction or a proposed effect whose cost and purpose are unclear.
- [Translate the prototype’s intent](../prototype-production/SKILL.md): Use when implementing Figma interactions or turning an animated concept into a working page.
- [Present decisions through evidence](../evidence-story/SKILL.md): Use for design reviews, case studies, agent handoffs, and portfolio explanations.
- [Choose scope and tools by the outcome](../scope-tool-fit/SKILL.md): Use when briefing design work, choosing a tool, or estimating an agent’s implementation scope.
- [Learn by reconstructing and explaining](../learning-reconstruction/SKILL.md): Use for improving design judgment, building a truthful portfolio exercise, or training an agent on a new interface pattern.
- [Make AI work visible and recoverable](../ai-workspace/SKILL.md): Use when designing a prompt composer, generation flow, research assistant, or AI editing surface.

## Visual comparisons

[Image manifest](../../examples.json) includes selected problem/change pairs, source times, visible facts, interpreted mechanisms and transfer limits. Load both local images with a vision-capable tool; a text link is not visual input. Public image URLs are also provided. The full pack includes the images for offline use. Source frames are excluded from MIT; see [source-material rights](../../SOURCE-MATERIAL.md). These are teaching demonstrations, not measured usability results.


## Evidence

52 unique public uploads were found by scrolling the live channel’s Videos tab to exhaustion, matching its visible 52-video count. All titles, published dates and durations were checked on the watch pages. 52 full caption transcripts were reviewed. No separate Shorts or Live tabs were visible. This snapshot is dated 2026-10-04.

Three gpt-6-luna reviewers analyzed separate video batches using full timestamped YouTube caption exports, with retries after preroll playback. Some caption tracks were English and some were auto-dubbed Spanish. Timestamp anchors were checked against cue passages and video durations. 52 videos have explicit visual sample notes in the ledger. This is transcript-led research with sampled video frames, not a claim of continuous full-length visual or audio viewing.

Auto-generated and auto-dubbed captions can mistranscribe technical terms, names, or numerical details. A static frame does not establish motion quality. Visual demonstrations not described in captions may be missed. Exact prototype code and dated tool capabilities should be checked in their current official sources. Private, deleted, unlisted, and future uploads cannot be counted from the public catalog.

[How this library was created](../../METHODOLOGY.md) · [Structured library](../../library.json) · [Source ledger](../../videos.json)
