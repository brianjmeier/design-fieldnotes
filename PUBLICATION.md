# Public-edition verification — October 9, 2026

Astra selected and independently reviewed the UI direction. Verdict: **ready to share for the verified discovery, reading and reuse flows; no blocking UI finding**. [Design rationale](DESIGN.md) explains the reference transfer.

## Verified before publication

| Behavior | Observed evidence |
| --- | --- |
| Skills search and no-match recovery | Reset restores 29 concepts and focus to the search field; Product filter returns eight matching concepts |
| Source search and recovery | Reset restores 52 videos and focus to source search |
| Skill, entry and brief copying | Actual browser clipboard text matches generated Markdown or visible brief exactly |
| Verification-code copying | Actual clipboard matches the canonical color-contrast recipe |
| File reuse | Actual Markdown download matched its generated version; the latest complete ZIP download matched every byte of the generated pack |
| Section navigation | Requested skill heading and verification article receive focus, retain the correct route and remain visible below the header |
| Reader return context | Keyboard entry to a lower concept, then Back, restores the same focused concept and exact scroll position |
| Invalid link recovery | A malformed encoded skill link shows a useful not-found state and returns to the collection |
| Responsive reading | Browser views at 1280×720, 390×844 and 320×800 keep navigation and primary controls usable; no document-level horizontal overflow in checked views |
| Runtime signals | No browser console errors or warnings observed in checked interactions |
| Source and exports | 29 concepts, 52 dated video records, 65 teaching references and eight verification guides; IDs, relationships and timestamp bounds validate |
| Portable package | Generated data and Markdown agree; relative Markdown links resolve in both repository and extracted package; rebuilding produces identical artifacts |

Astra’s screenshots cover collection, reading, setup, sources and verification.
[Collection desktop](https://brianjmeier.github.io/design-fieldnotes/docs/screenshots/library-desktop.jpg),
[collection mobile](https://brianjmeier.github.io/design-fieldnotes/docs/screenshots/library-mobile.jpg),
[skill reading](https://brianjmeier.github.io/design-fieldnotes/docs/screenshots/skill-desktop.jpg).

## Data cleanup

Three batch-specific visual-evidence formats were normalized without conflating requested and observed timestamps. Thirty-seven teaching notes that ended mid-thought were completed from existing reviewed summaries/concepts; IDs and timestamps did not change. Moment labels remain bounded jump-link snippets. Application examples are generic and the project has no product-specific dependency or private workspace references.

## Limits

Browser viewport checks are not physical-device verification. No full screen-reader, text-zoom or accessibility-conformance audit was performed. Clipboard success was exercised; a forced permission-refusal case was inspected in source rather than induced in the browser. Caption and sampled-frame research retains the limitations in [METHODOLOGY.md](METHODOLOGY.md). Publication smoke checks are separate from this prepublication UI review.

## Visual-comparison addition — October 9, 2026

Three curated source pairs were added for alignment, semantic color and progressive disclosure. Six complete 960 × 540 source-frame images retain exact observed timestamps and hashes. The UI presents equal desktop panels and ordered stacked mobile figures, source/time links, full-frame links, factual captions, contextual reasoning and explicit limits. The relevant concept skills link to their comparison documents; the complete pack includes the actual images and image manifest.

Astra independently reviewed the six source frames, canonical records and rendered desktop/mobile screens. Its three small clarity fixes were applied: copy label specifies image links, displayed timestamp and source URL use the same floor convention, and the source eyebrow retains a quieter text role. No required UI or editorial finding remained in this bounded review.

Verified behavior:

- Desktop 1280 × 720 and mobile 390 × 844 / 320 × 800 reflow without horizontal overflow. Mobile figures preserve problem → change order.
- All six source images load with their expected dimensions. Hash routes focus the selected comparison or concept section.
- Searching for “lavender” finds the relevant semantic-color concept via its visual example.
- “Copy image links + context” was tested by a native paste into a temporary local field; the pasted JSON matched the generated manifest record exactly.
- An actual browser download contains 62 archive entries, including all six source JPEGs and three comparison documents. The downloaded image bytes match the canonical files.
- Source-data/export validation passes, including image hashes/dimensions, links inside the ZIP, source identity and bounded timestamps. No new runtime dependency was added.

These are source teaching comparisons, not controlled usability studies. Camera scale and other simultaneous edits are documented. The video’s contrast badges are not our measurements; screenshots do not establish accessibility conformance. The source excerpts are excluded from MIT under [SOURCE-MATERIAL.md](SOURCE-MATERIAL.md). Verification did not include physical phones, a screen reader, or the source interfaces’ actual interactions.

## Creator credit and permission disclosure — October 10, 2026

Kole Jain is credited before the page content, in each skill’s header and exported Markdown, alongside each source-image comparison, and in the README, methodology, rights document and machine-readable exports. The notice says this is an unofficial, AI-assisted adaptation and that no permission has been obtained from him. Source authorship and adaptation authorship are distinguished; MIT grants no rights to the source videos or frames.

The disclosure was inspected at desktop 1280 × 720 and mobile 390 × 844, with no horizontal overflow. Export validation confirms the same attribution record in the library, image manifest and standalone attribution file, and verifies its presence in all 29 concept-skill Markdown files. The pack has 63 entries after adding the attribution record. These checks establish consistent disclosure, not legal clearance. The six existing frames remain pending the publisher’s separate decision about replacing them with source links.
