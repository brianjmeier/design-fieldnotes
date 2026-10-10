# Data and build map

| Editable input | Owns |
| --- | --- |
| `data/skills.json` | Concept IDs, prose, categories, original examples, source moments, related skills and verification references |
| `data/videos.json` | Watch-page metadata, caption-review coverage, concepts, sampled-frame notes and related skills |
| `data/checks.json` | Verification guide text, runnable example snippets and primary-standard links |
| `data/research.json` | Snapshot date, channel, coverage statement, creation method and limitations |
| `data/examples.json` | Selected image-pair IDs, concept references, exact source times, visible facts, interpreted mechanisms, transfer limits and image provenance |
| `assets/examples/*.jpg` | Immutable full source-frame excerpts with separate rights |
| `data/attribution.json` | Creator credit, explicit permission status, adaptation authorship and limited license scope |
| `data/site.json` | Repository/site URLs and publication metadata |
| `templates/index.html`, `app.js`, `styles.css` | Site structure, interactions and presentation |

`python3 scripts/build.py` produces the following exports. Edit their inputs instead of patching them directly:

- `index.html`: HTML with the library and browser code embedded; image excerpts remain relative assets.
- `library.json` / `library.js`: complete derived skills, sources and verification recipes.
- `videos.json`: portable source ledger.
- `attribution.json`: creator credit and unresolved permission status, also embedded in the structured library.
- `examples.json`: visual manifest with local paths and generated public image URLs.
- `examples/<id>.md`: comparison text and images for people and agents.
- `skills/<id>/SKILL.md`: one generated concept per directory; `skills/index/SKILL.md` is the router.
- `SKILL.md` / `AGENTS.md` / `llms.txt`: root agent entry points with correct relative references.
- `checks/<id>.md`: generated verification guides.
- `skills.zip`: a portable `design-fieldnotes/` folder, including relative-link dependencies and attribution.
- `provenance.json`: structured creation record and derived coverage counts.

## Reference meanings

Skill IDs are stable lowercase slugs. A skill’s `sources` point to a video ID and timestamp; `related` points to another concept; `checks` points to a verification guide. Video `skills` are curated related-concept tags, while a skill’s timestamped sources attribute particular teaching. These serve different purposes and need not be identical sets.

Video IDs are the canonical watch-page identity. `durationSeconds` bounds moments and visual samples. `transcriptFull` means the full caption export was reviewed, not that the whole video was visually watched. Sampled-frame evidence remains visibly labeled as sampled.

Use UTF-8 JSON and real numbers/booleans. Preserve dates as ISO calendar dates. The build derives Markdown and coverage counts from the same inputs and validates links after export. Do not add credentials, personal workspace paths, raw captions or complete video files. Source-frame excerpts require explicit provenance, bounded commentary and separate licensing; they are not generic reusable product assets.

## Visual-sample normalization

The original three review batches used different names for the same sample
fields. Public records use `requestedSeconds`, `observedSeconds`, optional
`playerDurationSeconds`, `observation`, `evidence` and `limit`. Requested and
observed times remain distinct; missing optional duration is `null`. Duplicate
video identity/title fields were removed because the enclosing record owns
them. Every sample preserves its original observation and inspection limits.
This normalization creates no new claim of full-length watching.

Teaching-note prose ending mid-sentence was completed editorially from existing
reviewed summaries and concepts. Video IDs and timestamp anchors did not change.
Moment link labels remain bounded review snippets; they are jump labels rather
than complete concept explanations. Full teaching belongs in the skill prose.

## Visual-example schema

Each pair owns a stable slug, `conceptIds`, canonical video identity and two frames in `problem`, `revision` order. Frames include requested/observed seconds, timestamp confidence, local `imagePath`, alt text, visible facts, dimensions and SHA-256. The export derives `imageUrl` from `data/site.json`.

`comparison` separates `problem`, `observedChanges`, interpreted `mechanism`, `transferWhen`, `doNotGeneralize` and `unverifiedOutcomes`. `provenance` identifies `source-frame`, capture date/method, an empty edits array and source-rights notice. Authored reconstructions would require a distinct asset kind and provenance; the current corpus contains none.

`library.json` schema version 2 adds `examples` and `exampleCoverage`; existing skill/video fields retain their meanings. `examples.json` is a standalone manifest at schema version 1. Counts describe this selected corpus, not coverage of all video lessons. The validator checks image identity/dimensions, timestamps, relationships, public-URL derivation, generated text and ZIP-internal links including image links. The skill pack includes all six images and comparison documents for offline reading.
