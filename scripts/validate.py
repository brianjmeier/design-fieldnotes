#!/usr/bin/env python3
"""Check source identity, teaching references and consistency of portable exports."""
import datetime
import json
import pathlib
import posixpath
import re
import zipfile


def read(root, name):
    return json.loads((root / 'data' / (name + '.json')).read_text(encoding='utf-8'))


def unique(records, label):
    ids = [item['id'] for item in records]
    assert len(ids) == len(set(ids)), f'Duplicate {label} IDs'
    return set(ids)


def text(value, label):
    assert isinstance(value, str) and value.strip(), f'Missing {label}'


def validate_source(root):
    skills, videos, checks = [read(root, name) for name in ('skills', 'videos', 'checks')]
    research, site = [read(root, name) for name in ('research', 'site')]
    skill_ids, video_ids, check_ids = [unique(records, name) for records, name in ((skills, 'skill'), (videos, 'video'), (checks, 'check'))]
    snapshot = datetime.date.fromisoformat(research['sourceSnapshot'])
    datetime.date.fromisoformat(site['publicationDate'])
    assert all(site[key].startswith('https://') for key in ('repositoryUrl', 'siteUrl'))
    assert all('markdown' not in s for s in skills), 'Edit source fields, not generated Markdown'
    by_video = {item['id']: item for item in videos}
    cited = set()
    for skill in skills:
        assert re.fullmatch(r'[a-z][a-z0-9-]+', skill['id'])
        for key in ('title', 'summary', 'category', 'when', 'evidence'):
            text(skill[key], f"{skill['id']}.{key}")
        for key in ('model', 'reasoning', 'gotchas'):
            assert skill[key], f"Empty {skill['id']}.{key}"
            for value in skill[key]:
                text(value, f"{skill['id']}.{key}")
        for key in ('title', 'before', 'after'):
            text(skill['example'][key], f"{skill['id']}.example.{key}")
        assert set(skill['related']) <= skill_ids and skill['id'] not in skill['related']
        assert len(skill['related']) == len(set(skill['related']))
        assert set(skill['checks']) <= check_ids and skill['sources']
        for reference in skill['sources']:
            assert reference['id'] in video_ids, f"Missing source {reference['id']}"
            assert 0 <= reference['seconds'] <= by_video[reference['id']]['durationSeconds']
            text(reference['lesson'], 'source lesson')
            cited.add(reference['id'])
    assert cited == video_ids, 'Every catalogued source must have an attributed concept'
    assert sorted(v['index'] for v in videos) == list(range(1, len(videos) + 1))
    for video in videos:
        assert re.fullmatch(r'[A-Za-z0-9_-]{11}', video['id'])
        assert video['url'] == 'https://www.youtube.com/watch?v=' + video['id']
        assert datetime.date.fromisoformat(video['published']) <= snapshot
        assert isinstance(video['transcriptFull'], bool)
        assert set(video['skills']) <= skill_ids
        assert isinstance(video['durationSeconds'], (int, float)) and video['durationSeconds'] > 0
        for moment in video['moments']:
            assert 0 <= moment['seconds'] <= video['durationSeconds']
            text(moment['label'], 'moment label')
        sample = video.get('visualSample')
        if sample:
            assert sample['evidence'] == 'sampled-frame-note'
            for key in ('requestedSeconds', 'observedSeconds'):
                assert 0 <= sample[key] <= video['durationSeconds']
            text(sample['observation'], 'sample observation')
            text(sample['limit'], 'sample limit')
    for check in checks:
        assert re.fullmatch(r'[a-z][a-z0-9-]+', check['id'])
        for key in ('title', 'purpose', 'expected', 'code', 'limit'):
            text(check[key], f"{check['id']}.{key}")
    return {'skills': len(skills), 'videos': len(videos), 'checks': len(checks), 'sourceReferences': sum(len(s['sources']) for s in skills), 'snapshot': research['sourceSnapshot']}


def validate_exports(root):
    result = validate_source(root)
    library = json.loads((root / 'library.json').read_text(encoding='utf-8'))
    assert library['date'] == result['snapshot']
    assert json.loads((root / 'videos.json').read_text(encoding='utf-8')) == read(root, 'videos')
    assert library['videos'] == read(root, 'videos') and library['checks'] == read(root, 'checks')
    originals = {skill['id']: skill for skill in read(root, 'skills')}
    for skill in library['skills']:
        assert {k: v for k, v in skill.items() if k != 'markdown'} == originals[skill['id']]
        assert (root / 'skills' / skill['id'] / 'SKILL.md').read_text(encoding='utf-8') == skill['markdown']
    assert (root / 'SKILL.md').read_text(encoding='utf-8') == library['entryMarkdown']
    assert (root / 'AGENTS.md').read_text(encoding='utf-8') == library['entryMarkdown']
    links = 0
    for path in list(root.rglob('*.md')) + [root / 'llms.txt']:
        for target in re.findall(r'(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)', path.read_text(encoding='utf-8')):
            target = target.strip('<>').split('#')[0]
            if not target or re.match(r'^[a-z]+:', target):
                continue
            destination = (path.parent / target).resolve()
            assert destination.is_relative_to(root.resolve()), f'Link escapes library: {path}:{target}'
            assert destination.exists(), f'Broken link: {path}:{target}'
            links += 1
    with zipfile.ZipFile(root / 'skills.zip') as archive:
        names = archive.namelist()
        assert len(names) == len(set(names))
        assert all(name.startswith('design-fieldnotes/') and '..' not in pathlib.PurePosixPath(name).parts for name in names)
        assert archive.read('design-fieldnotes/SKILL.md').decode() == library['entryMarkdown']
        for name in names:
            path = root / pathlib.PurePosixPath(name).relative_to('design-fieldnotes')
            assert archive.read(name) == path.read_bytes(), f'Archive drift: {name}'
            if name.endswith(('.md', '.txt')):
                for target in re.findall(r'(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)', archive.read(name).decode('utf-8')):
                    target = target.strip('<>').split('#')[0]
                    if not target or re.match(r'^[a-z]+:', target):
                        continue
                    destination = posixpath.normpath(posixpath.join(posixpath.dirname(name), target))
                    assert destination in names, f'Broken portable-pack link: {name}:{target}'

    for marker in ('@@REPOSITORY_URL@@', 'src="library.js"', 'src="app.js"'):
        assert marker not in (root / 'index.html').read_text(encoding='utf-8'), 'Incomplete self-contained HTML build'
    result.update(localMarkdownLinks=links, archiveEntries=len(names))
    return result


if __name__ == '__main__':
    print(json.dumps(validate_exports(pathlib.Path(__file__).resolve().parent.parent), indent=2))
