#!/usr/bin/env python3
"""Check source identity, teaching references and consistency of portable exports."""
import datetime
import hashlib
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
    examples = read(root, 'examples')
    unique(examples, 'visual example')
    assets = set()
    for example in examples:
        assert re.fullmatch(r'[a-z][a-z0-9-]+', example['id'])
        text(example['title'], 'example title')
        assert example['conceptIds'] and set(example['conceptIds']) <= skill_ids
        source = example['source']
        assert source['videoId'] in video_ids
        video = by_video[source['videoId']]
        assert source['url'] == video['url'] and source['title'] == video['title']
        assert [frame['role'] for frame in example['frames']] == ['problem', 'revision']
        for frame in example['frames']:
            for key in ('requestedSeconds', 'observedSeconds'):
                assert 0 <= frame[key] <= video['durationSeconds']
            for key in ('altText', 'visibleFacts', 'timestampConfidence'):
                text(frame[key], key)
            path = frame['imagePath']
            assert re.fullmatch(r'assets/examples/[a-z0-9-]+\.jpg', path)
            assert path not in assets, 'Each source frame must have one owner'
            assets.add(path)
            data = (root / path).read_bytes()
            assert hashlib.sha256(data).hexdigest() == frame['sha256'], 'Source image changed without provenance update'
            assert jpeg_size(data) == (frame['width'], frame['height'])
        for key in ('problem', 'observedChanges', 'mechanism', 'transferWhen', 'doNotGeneralize', 'unverifiedOutcomes'):
            text(example['comparison'][key], key)
        provenance = example['provenance']
        datetime.date.fromisoformat(provenance['captureDate'])
        assert provenance['assetKind'] == 'source-frame' and provenance['edits'] == []
        text(provenance['captureMethod'], 'capture method')
        text(provenance['sourceRightsNotice'], 'source rights')
    assert assets == {p.relative_to(root).as_posix() for p in root.glob('assets/examples/*.jpg')}, 'Uncatalogued source image'
    return {'skills': len(skills), 'videos': len(videos), 'checks': len(checks), 'visualPairs': len(examples), 'sourceReferences': sum(len(s['sources']) for s in skills), 'snapshot': research['sourceSnapshot']}


def jpeg_size(data):
    """Read image dimensions without importing or altering pixel data."""
    assert data[:2] == b'\xff\xd8', 'Expected JPEG'
    offset = 2
    while offset < len(data):
        assert data[offset] == 255
        while data[offset] == 255:
            offset += 1
        marker = data[offset]
        offset += 1
        if marker in (0xD8, 0xD9):
            continue
        length = int.from_bytes(data[offset:offset + 2], 'big')
        if marker in (0xC0, 0xC1, 0xC2):
            return (int.from_bytes(data[offset + 5:offset + 7], 'big'), int.from_bytes(data[offset + 3:offset + 5], 'big'))
        offset += length
    raise AssertionError('JPEG has no size marker')


def validate_exports(root):
    result = validate_source(root)
    library = json.loads((root / 'library.json').read_text(encoding='utf-8'))
    assert library['date'] == result['snapshot']
    assert json.loads((root / 'videos.json').read_text(encoding='utf-8')) == read(root, 'videos')
    assert library['videos'] == read(root, 'videos') and library['checks'] == read(root, 'checks')
    manifest = json.loads((root / 'examples.json').read_text(encoding='utf-8'))
    assert library['examples'] == manifest['examples'] and library['exampleCoverage'] == manifest['coverage']
    for original, example in zip(read(root, 'examples'), manifest['examples']):
        assert {k: v for k, v in example.items() if k != 'frames'} == {k: v for k, v in original.items() if k != 'frames'}
        for source, frame in zip(original['frames'], example['frames']):
            assert {k: v for k, v in frame.items() if k != 'imageUrl'} == source
            assert frame['imageUrl'] == library['site']['siteUrl'].rstrip('/') + '/' + frame['imagePath']
    originals = {skill['id']: skill for skill in read(root, 'skills')}
    for skill in library['skills']:
        assert {k: v for k, v in skill.items() if k != 'markdown'} == originals[skill['id']]
        assert (root / 'skills' / skill['id'] / 'SKILL.md').read_text(encoding='utf-8') == skill['markdown']
    assert (root / 'SKILL.md').read_text(encoding='utf-8') == library['entryMarkdown']
    assert (root / 'AGENTS.md').read_text(encoding='utf-8') == library['entryMarkdown']
    links = 0
    for path in list(root.rglob('*.md')) + [root / 'llms.txt']:
        for target in re.findall(r'\[[^\]\n]+\]\(([^)\n]+)\)', path.read_text(encoding='utf-8')):
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
                for target in re.findall(r'\[[^\]\n]+\]\(([^)\n]+)\)', archive.read(name).decode('utf-8')):
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
