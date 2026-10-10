#!/usr/bin/env python3
"""Build static HTML, Markdown and portable exports from the canonical data."""
import json
import pathlib
import zipfile
from validate import validate_source
DIST = pathlib.Path(__file__).resolve().parent.parent
DATA = DIST / 'data'
RESEARCH = json.loads((DATA / 'research.json').read_text(encoding='utf-8'))
SITE = json.loads((DATA / 'site.json').read_text(encoding='utf-8'))
CHECKS = json.loads((DATA / 'checks.json').read_text(encoding='utf-8'))

ATTRIBUTION = json.loads((DATA / 'attribution.json').read_text(encoding='utf-8'))

EXAMPLES = json.loads((DATA / 'examples.json').read_text(encoding='utf-8'))

def write_examples():
    folder = DIST / 'examples'
    folder.mkdir(exist_ok=True)
    exported = []
    for original in EXAMPLES:
        example = json.loads(json.dumps(original))
        pieces = [f"# {example['title']}", ATTRIBUTION['notice'], ATTRIBUTION['sourceRights'], 'Source-video comparison, not a controlled usability experiment.',
                  f"[Kole Jain — {example['source']['title']}]({example['source']['url']})"]
        for frame in example['frames']:
            frame['imageUrl'] = SITE['siteUrl'].rstrip('/') + '/' + frame['imagePath']
            label = 'Problem shown' if frame['role'] == 'problem' else 'Change shown'
            time = frame['observedSeconds']
            pieces += [f"## {label} · {int(time // 60)}:{int(time % 60):02d}",
                       f"![{frame['altText']}](../{frame['imagePath']})", frame['visibleFacts'],
                       f"[Open public image]({frame['imageUrl']}) · [Watch this moment in Kole Jain’s original video]({example['source']['url']}&t={int(time)}s)"]
        for key, label in [('problem', 'Problem'), ('observedChanges', 'Observed change'), ('mechanism', 'Interpreted mechanism'), ('transferWhen', 'Transfer when'), ('doNotGeneralize', 'Limits and counterexamples'), ('unverifiedOutcomes', 'Unverified outcomes')]:
            pieces += ['## ' + label, example['comparison'][key]]
        pieces += ['## Provenance', example['provenance']['captureMethod'],
                   'Captured ' + example['provenance']['captureDate'] + '. No image edits. Source annotations and any subtitles remain part of the excerpt.',
                   '[Source-material rights](../SOURCE-MATERIAL.md)',
                   'Use a vision-capable image tool to load both local images or public image URLs. Text links and alt text alone do not provide the visual evidence.']
        (folder / (example['id'] + '.md')).write_text('\n\n'.join(pieces) + '\n', encoding='utf-8')
        exported.append(example)
    manifest = {'schemaVersion': 1, 'attribution': ATTRIBUTION, 'examples': exported, 'coverage': {'pairs': len(exported), 'sourceVideos': len({x['source']['videoId'] for x in exported}), 'limit': 'Selected verified comparisons only; the 52-video catalog does not yet have a visual pair for every lesson.'}}
    (DIST / 'examples.json').write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    return manifest

def write_library(skills, videos, coverage):
    examples = write_examples()
    library = {'title': 'Design Fieldnotes', 'schemaVersion': 2, 'date': RESEARCH['sourceSnapshot'], 'channel': 'https://www.youtube.com/@KoleJain', 'skills': skills, 'videos': videos, 'checks': CHECKS, 'examples': examples['examples'], 'exampleCoverage': examples['coverage'], 'coverage': coverage, 'site': SITE, 'attribution': ATTRIBUTION}
    DIST.mkdir(parents=True, exist_ok=True)
    (DIST / 'attribution.json').write_text(json.dumps(ATTRIBUTION, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    (DIST / 'videos.json').write_text(json.dumps(videos, indent=2, ensure_ascii=False), encoding='utf-8')
    for s in skills:
        folder = DIST / 'skills' / s['id']
        folder.mkdir(parents=True, exist_ok=True)
        description=json.dumps(s['summary'],ensure_ascii=False)
        pieces = [f"---\nname: {s['id']}\ndescription: {description}\n---\n", f"# {s['title']}", ATTRIBUTION['notice'], '[Source credit and reuse limits](../../SOURCE-MATERIAL.md)', '## Mental model', *s['model'], '## When this skill applies', s['when'], '## Reasoning', *s['reasoning']]
        relevant = [e for e in library['examples'] if s['id'] in e['conceptIds']]
        if relevant:
            pieces += ['## Source-video visual comparison', *[f"- [{e['title']}](../../examples/{e['id']}.md): load both images before drawing visual conclusions." for e in relevant]]
        pieces += ['## Worked example — original implementation adaptation', s['example']['title'], s['example']['before'], s['example']['after']]
        if s['example'].get('code'):
            pieces.append('```css\n' + s['example']['code'] + '\n```')
        pieces += ['## Failure modes', *['- ' + x for x in s['gotchas']], '## Evidence that would support the decision', s['evidence'], '## Verification references', *[f"- [{c['title']}](../../checks/{c['id']}.md)" for c in CHECKS if c['id'] in s['checks']], '## Source moments']
        for src in s['sources']:
            v = next(v for v in videos if v['id'] == src['id'])
            pieces.append(f"- [{v['title']}](https://www.youtube.com/watch?v={v['id']}&t={int(src['seconds'])}s): {src['lesson']}")
        pieces += ['## Related skills', *[f'- [{id}](../{id}/SKILL.md)' for id in s['related']], 'Source moments and labeled source-frame comparisons are attributed teaching. Implementation examples, reasoning, and verification are our original agent-oriented adaptations. Read the source ledger for review limits.']
        s['markdown'] = '\n\n'.join(pieces) + '\n'
        (folder / 'SKILL.md').write_text(s['markdown'], encoding='utf-8')
    index = DIST / 'skills/index'
    index.mkdir(parents=True, exist_ok=True)
    indextext = """---
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

"""
    indextext += '\n'.join(f"- [{s['title']}](../{s['id']}/SKILL.md): {s['when']}" for s in skills)
    indextext += '\n\n## Visual comparisons\n\n[Image manifest](../../examples.json) includes selected problem/change pairs, source times, visible facts, interpreted mechanisms and transfer limits. Load both local images with a vision-capable tool; a text link is not visual input. Public image URLs are also provided. The full pack includes the images for offline use. Source frames are excluded from MIT; see [source-material rights](../../SOURCE-MATERIAL.md). These are teaching demonstrations, not measured usability results.\n'
    indextext += '\n\n## Evidence\n\n' + coverage['long'] + '\n\n' + coverage['method'] + '\n\n' + coverage['limits'] + '\n\n[How this library was created](../../METHODOLOGY.md) · [Structured library](../../library.json) · [Source ledger](../../videos.json)\n'
    (index / 'SKILL.md').write_text(indextext, encoding='utf-8')
    checksdir = DIST / 'checks'
    checksdir.mkdir(exist_ok=True)
    for c in CHECKS:
        (checksdir / (c['id'] + '.md')).write_text((f"# {c['title']}\n\n{c['purpose']}\n\nExpected evidence: {c['expected']}\n\n```\n{c['code']}\n```\n\n{c['limit']}\n\n" + '\n'.join(f"[{l['title']}]({l['url']})" for l in c['links']) + '\n').rstrip() + '\n', encoding='utf-8')
    (DIST / 'llms.txt').write_text('# Design Fieldnotes\n\n' + ATTRIBUTION['notice'] + '\n\n' + ATTRIBUTION['sourceRights'] + '\n\n' + coverage['short'] + '\n\n## Entry points\n\n- [Start-here skill](skills/index/SKILL.md)\n- [Structured complete library](library.json)\n- [Per-video evidence ledger](videos.json)\n- [Visual comparison manifest](examples.json)\n\n## Concept skills\n\n' + '\n'.join(f"- [{s['title']}](skills/{s['id']}/SKILL.md): {s['summary']}" for s in skills) + '\n', encoding='utf-8')
    (DIST / 'AGENTS.md').write_text(indextext.replace('../../', '').replace('../', 'skills/'), encoding='utf-8')
    library['entryMarkdown'] = indextext.replace('../../', '').replace('../', 'skills/')
    (DIST / 'library.json').write_text(json.dumps(library, indent=2, ensure_ascii=False), encoding='utf-8')
    (DIST / 'library.js').write_text('window.FIELDNOTES = ' + json.dumps(library, ensure_ascii=False).replace('</', '<\\/') + ';\n', encoding='utf-8')
    (DIST / 'SKILL.md').write_text(indextext.replace('../../', '').replace('../', 'skills/'), encoding='utf-8')
    with zipfile.ZipFile(DIST / 'skills.zip', 'w', zipfile.ZIP_DEFLATED) as archive:
        paths = sorted(DIST.glob('skills/**/*.md')) + sorted(checksdir.glob('*.md'))
        paths += [DIST / name for name in ['SKILL.md', 'AGENTS.md', 'llms.txt', 'videos.json', 'library.json', 'provenance.json', 'README.md', 'METHODOLOGY.md', 'DATA.md', 'CONTRIBUTING.md', 'DESIGN.md', 'PUBLICATION.md', 'LICENSE', 'SOURCE-MATERIAL.md', 'examples.json', 'attribution.json']]
        paths += sorted(DIST.glob('examples/*.md')) + sorted(DIST.glob('assets/examples/*.jpg'))
        for path in paths:
            info = zipfile.ZipInfo('design-fieldnotes/' + path.relative_to(DIST).as_posix(), (2026, 10, 4, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes())
    return library


if __name__ == '__main__':
    validate_source(DIST)
    skills = json.loads((DATA / 'skills.json').read_text(encoding='utf-8'))
    videos = json.loads((DATA / 'videos.json').read_text(encoding='utf-8'))
    (DIST/'provenance.json').write_text(json.dumps({**RESEARCH, 'counts': {'videos': len(videos), 'conceptSkills': len(skills), 'verificationRecipes': len(CHECKS), 'visualComparisonPairs': len(EXAMPLES), 'fullCaptionsReviewed': sum(v['transcriptFull'] for v in videos), 'sampledVideos': sum(bool(v.get('visualSample', {}).get('observation')) for v in videos)}}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    result = write_library(skills, videos, RESEARCH['coverage'])
    template = (DIST / 'templates/index.html').read_text(encoding='utf-8')
    template = template.replace('@@REPOSITORY_URL@@', SITE['repositoryUrl'])
    html = template.replace('<link rel="stylesheet" href="styles.css">', '<style>\n' + (DIST/'styles.css').read_text(encoding='utf-8') + '\n</style>')
    html = html.replace('<script defer src="library.js"></script>', '').replace('<script defer src="app.js"></script>', '')
    scripts = '<script>\n' + (DIST/'library.js').read_text(encoding='utf-8') + '\n</script>\n<script>\n' + (DIST/'app.js').read_text(encoding='utf-8') + '\n</script>\n'
    rendered = html.replace('</body>', scripts + '</body>')
    (DIST/'index.html').write_text('\n'.join(line.rstrip() for line in rendered.splitlines()) + '\n', encoding='utf-8')
    print(json.dumps({'skills': len(skills), 'videos': len(videos), 'checks': len(CHECKS), 'visualPairs': len(EXAMPLES)}))
