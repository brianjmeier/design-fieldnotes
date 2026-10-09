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

def write_library(skills, videos, coverage):
    library = {'title': 'Design Fieldnotes', 'schemaVersion': 1, 'date': RESEARCH['sourceSnapshot'], 'channel': 'https://www.youtube.com/@KoleJain', 'skills': skills, 'videos': videos, 'checks': CHECKS, 'coverage': coverage, 'site': SITE}
    DIST.mkdir(parents=True, exist_ok=True)
    (DIST / 'videos.json').write_text(json.dumps(videos, indent=2, ensure_ascii=False), encoding='utf-8')
    for s in skills:
        folder = DIST / 'skills' / s['id']
        folder.mkdir(parents=True, exist_ok=True)
        description=json.dumps(s['summary'],ensure_ascii=False)
        pieces = [f"---\nname: {s['id']}\ndescription: {description}\n---\n", f"# {s['title']}", '## Mental model', *s['model'], '## When this skill applies', s['when'], '## Reasoning', *s['reasoning'], '## Worked example — original implementation adaptation', s['example']['title'], s['example']['before'], s['example']['after']]
        if s['example'].get('code'):
            pieces.append('```css\n' + s['example']['code'] + '\n```')
        pieces += ['## Failure modes', *['- ' + x for x in s['gotchas']], '## Evidence that would support the decision', s['evidence'], '## Verification references', *[f"- [{c['title']}](../../checks/{c['id']}.md)" for c in CHECKS if c['id'] in s['checks']], '## Source moments']
        for src in s['sources']:
            v = next(v for v in videos if v['id'] == src['id'])
            pieces.append(f"- [{v['title']}](https://www.youtube.com/watch?v={v['id']}&t={int(src['seconds'])}s): {src['lesson']}")
        pieces += ['## Related skills', *[f'- [{id}](../{id}/SKILL.md)' for id in s['related']], 'Source moments are attributed teaching. Examples, reasoning, and verification are our original agent-oriented adaptations. Read the source ledger for review limits.']
        s['markdown'] = '\n\n'.join(pieces) + '\n'
        (folder / 'SKILL.md').write_text(s['markdown'], encoding='utf-8')
    index = DIST / 'skills/index'
    index.mkdir(parents=True, exist_ok=True)
    indextext = """---
name: design-fieldnotes
description: Choose a relevant UX/UI concept skill when building or changing an interface, using product intent, evidence, and contextual judgment.
---

# Design Fieldnotes — agent entry point

This is a concept library synthesized from Kole Jain's public video catalog.
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
    indextext += '\n\n## Evidence\n\n' + coverage['long'] + '\n\n' + coverage['method'] + '\n\n' + coverage['limits'] + '\n\n[How this library was created](../../METHODOLOGY.md) · [Structured library](../../library.json) · [Source ledger](../../videos.json)\n'
    (index / 'SKILL.md').write_text(indextext, encoding='utf-8')
    checksdir = DIST / 'checks'
    checksdir.mkdir(exist_ok=True)
    for c in CHECKS:
        (checksdir / (c['id'] + '.md')).write_text((f"# {c['title']}\n\n{c['purpose']}\n\nExpected evidence: {c['expected']}\n\n```\n{c['code']}\n```\n\n{c['limit']}\n\n" + '\n'.join(f"[{l['title']}]({l['url']})" for l in c['links']) + '\n').rstrip() + '\n', encoding='utf-8')
    (DIST / 'llms.txt').write_text('# Design Fieldnotes\n\nAgent-first concept skills synthesized from Kole Jain’s public YouTube catalog.\n\n' + coverage['short'] + '\n\n## Entry points\n\n- [Start-here skill](skills/index/SKILL.md)\n- [Structured complete library](library.json)\n- [Per-video evidence ledger](videos.json)\n\n## Concept skills\n\n' + '\n'.join(f"- [{s['title']}](skills/{s['id']}/SKILL.md): {s['summary']}" for s in skills) + '\n', encoding='utf-8')
    (DIST / 'AGENTS.md').write_text(indextext.replace('../../', '').replace('../', 'skills/'), encoding='utf-8')
    library['entryMarkdown'] = indextext.replace('../../', '').replace('../', 'skills/')
    (DIST / 'library.json').write_text(json.dumps(library, indent=2, ensure_ascii=False), encoding='utf-8')
    (DIST / 'library.js').write_text('window.FIELDNOTES = ' + json.dumps(library, ensure_ascii=False).replace('</', '<\\/') + ';\n', encoding='utf-8')
    (DIST / 'SKILL.md').write_text(indextext.replace('../../', '').replace('../', 'skills/'), encoding='utf-8')
    with zipfile.ZipFile(DIST / 'skills.zip', 'w', zipfile.ZIP_DEFLATED) as archive:
        paths = sorted(DIST.glob('skills/**/*.md')) + sorted(checksdir.glob('*.md'))
        paths += [DIST / name for name in ['SKILL.md', 'AGENTS.md', 'llms.txt', 'videos.json', 'library.json', 'provenance.json', 'README.md', 'METHODOLOGY.md', 'DATA.md', 'CONTRIBUTING.md', 'DESIGN.md', 'PUBLICATION.md', 'LICENSE']]
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
    (DIST/'provenance.json').write_text(json.dumps({**RESEARCH, 'counts': {'videos': len(videos), 'conceptSkills': len(skills), 'verificationRecipes': len(CHECKS), 'fullCaptionsReviewed': sum(v['transcriptFull'] for v in videos), 'sampledVideos': sum(bool(v.get('visualSample', {}).get('observation')) for v in videos)}}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    result = write_library(skills, videos, RESEARCH['coverage'])
    template = (DIST / 'templates/index.html').read_text(encoding='utf-8')
    template = template.replace('@@REPOSITORY_URL@@', SITE['repositoryUrl'])
    html = template.replace('<link rel="stylesheet" href="styles.css">', '<style>\n' + (DIST/'styles.css').read_text(encoding='utf-8') + '\n</style>')
    html = html.replace('<script defer src="library.js"></script>', '').replace('<script defer src="app.js"></script>', '')
    scripts = '<script>\n' + (DIST/'library.js').read_text(encoding='utf-8') + '\n</script>\n<script>\n' + (DIST/'app.js').read_text(encoding='utf-8') + '\n</script>\n'
    rendered = html.replace('</body>', scripts + '</body>')
    (DIST/'index.html').write_text('\n'.join(line.rstrip() for line in rendered.splitlines()) + '\n', encoding='utf-8')
    print(json.dumps({'skills': len(skills), 'videos': len(videos), 'checks': len(CHECKS)}))
