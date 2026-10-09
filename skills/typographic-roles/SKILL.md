---
name: typographic-roles
description: "Choose type roles, measure, and rhythm around what someone needs to read and compare."
---


# Make typography express the information

## Mental model

A type system creates repeatable levels of information. Size, weight, line height, line length, and spacing work together; a mathematical scale gives a starting point that still needs real-content judgment.

## When this skill applies

Use when headings compete, body text feels tiring, or a layout breaks when copy changes.

## Reasoning

Define a small set of roles such as display, section title, body, label, and metadata. Start from readable body copy, then create enough separation for the needed hierarchy. Fit the scale to product density.

Test a paragraph and a wrapped heading before applying the type system widely. Adjust measure and line height together. Use tabular figures where people compare numbers; preserve actual text instead of baking essential copy into images.

## Worked example — original implementation adaptation

A financial summary

Before: amounts, labels, headings and notes all use unrelated sizes chosen per card.

After: amounts share one numeric role; labels and metadata have consistent weights. The longest account name wraps naturally, and the explanatory paragraph has a bounded measure.

```css
.body-copy { max-width: 65ch; font-size: 1rem; line-height: 1.65; }
.section-title { font-size: clamp(1.5rem, 2vw + 1rem, 2.25rem); line-height: 1.2; }
/* These values are a worked starting point; evaluate the actual font and content. */
```

## Failure modes

- Treating a scale ratio as proof that text is readable.

- Letting display type rules shrink body text on mobile.

- Measuring only the text box while ignoring actual glyph and baseline relationships.

## Evidence that would support the decision

Capture long and short copy at narrow widths and larger text settings. Read body paragraphs, inspect label hierarchy, and compare numerical columns.

## Verification references

- [Stress the layout with real content](../../checks/responsive-content.md)

- [Measure color in its actual role](../../checks/color-contrast.md)

## Source moments

- [Mathematically Perfect Typography for Web Design](https://www.youtube.com/watch?v=7sUUzOCv47U&t=568s): Related source discussion; the skill’s examples and reasoning are our adaptation.

- [The stupid simple way to learn UI/UX design in exactly 10 minutes](https://www.youtube.com/watch?v=9WVt1CelBfg&t=242s): Choose a layout around what the content needs to communicate.

## Related skills

- [alignment-structure](../alignment-structure/SKILL.md)

- [responsive-priority](../responsive-priority/SKILL.md)

Source moments are attributed teaching. Examples, reasoning, and verification are our original agent-oriented adaptations. Read the source ledger for review limits.
