# How Design Fieldnotes was created

## Catalog and review

On October 4, 2026, the public channel’s Videos tab was scrolled to exhaustion. The 52 distinct watch-page IDs matched the visible count. Titles, published dates and durations were checked against the watch pages. No separate Shorts or Live tab was visible in that snapshot. Private, unlisted, deleted, member-only and later uploads are outside that inventory.

Three `gpt-6-luna` agents reviewed separate batches of full timestamped caption exports. Some tracks were English; others were auto-dubbed Spanish. Extraction was retried when preroll playback prevented access. Caption cues and video durations were used to check timestamp anchors. This is **full-caption review**, not a claim of continuous full-length visual or audio watching.

Each of the 52 video records has a sampled-frame note, including the requested time, observed player time and what the frame supports. A still frame does not establish animation quality or the completeness of a demonstrated flow. The ledger preserves those limits.

## From lessons to skills

The source discussions were grouped into mechanisms: information hierarchy, useful state transitions, contextual disclosure, typography, spatial relationships, motion, responsive priority and other design decisions. The resulting 29 concept skills are original agent-oriented synthesis. Worked examples and verification snippets are adaptations, not copied tutorial implementations or transcripts.

Each skill explains a mental model, when it helps, how to reason, a concrete before/after example, common failure modes and evidence that could support or falsify the choice. Verification guides are separate: a checklist or passing test is not itself a design concept. Sponsor recommendations and dated tool preferences do not become mandatory dependencies.

Accessibility thresholds reference primary W3C material separately from video teaching. Automated scans and screenshots do not establish full accessibility conformance.

## Curated visual comparisons

On October 9, 2026, three demonstrated problem/revision pairs were inspected in the official YouTube player. A local capture page used the documented IFrame API to seek, play and pause; the observed paused time was recorded separately from the requested time. Browser screenshots preserve the full 960 × 540 player image, with player controls hidden. There was no video download, image retouching or fabricated source frame.

Candidate frames showing transition slides, another product, player chrome or incomplete changes were rejected. The pairs were compared for the same task/content, with additional changes and camera-scale differences documented. An Astra reviewer inspected the six accepted images and reviewed the distinction between observed facts and interpreted mechanisms.

“Problem shown” and “Change shown” describe the source teaching, not a universal quality score. No conversion, task-speed or accessibility outcome is inferred from the stills. Contrast badges embedded in a source frame are the creator’s annotations, not independently verified scores. Each record retains transfer conditions and counterexamples so a model can generalize the mechanism without blindly copying the appearance.

The initial corpus covers three videos, not every catalogued upload. Source frames have separate [rights and attribution](SOURCE-MATERIAL.md). Public image URLs and offline-pack paths make visual input explicit; models must actually load both images through a vision-capable tool.

## Clean and inspectable data

The repository separates editable source records from generated exports. Validation checks unique IDs, relationships, dates, timestamp bounds, required content, generated-link integrity and export consistency. Every catalogued video is cited by at least one concept; multiple concepts may share a video. The build uses deterministic ZIP entries and contains no raw captions or complete video files. It includes six labeled source-frame excerpts.

See [DATA.md](DATA.md) for the file map, [videos.json](videos.json) for individual evidence, and [provenance.json](provenance.json) for the structured creation record. Updating the catalog requires new source evidence and a revised snapshot date; regeneration alone does not review new uploads.

## Publication review

For the public edition, the site was checked using its own intent-and-flow,
relative-emphasis, typographic-roles, responsive-priority, component-states and
evidence-story concepts. An Astra reviewer independently inspected the actual
desktop/mobile screens and interaction evidence, and selected the visual
direction from two supplied references. The review found no blocking UI issue
in the checked discovery, reading and reuse flows.

[PUBLICATION.md](PUBLICATION.md) records exact checked behavior and limitations;
[DESIGN.md](DESIGN.md) explains the visual direction. A passing bounded review
is not a claim of complete accessibility conformance or physical-device coverage.

## Limits

Auto-generated and auto-dubbed captions can mistranscribe names, technical terms and quantities. Demonstrations not described in captions may be missed. Exact code and current tool capabilities require their current primary documentation. This edition preserves the dated research snapshot and does not promise complete coverage of the channel today.
