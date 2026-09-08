#!/usr/bin/env python3
"""Render the directory from the reviewed, checked-in snapshot. No network calls."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def cell(value):
    return value.replace('|', '\\|').replace('\n', ' ')


def render(data):
    projects = data['projects']
    labels = data['category_labels']
    slugs = [p['slug'] for p in projects]
    if len(slugs) != len(set(slugs)):
        raise ValueError('Duplicate entity slugs')
    groups = {}
    for project in projects:
        if project['hoodl2_url'] != 'https://hoodl2.com/entity/' + project['slug']:
            raise ValueError('Profile URL does not match slug: ' + project['slug'])
        groups.setdefault(project['category'], []).append(project)
    lines = [
        '# Robinhood Chain directory by HoodL2.com', '',
        '[HoodL2.com](https://hoodl2.com) · [Curated list](../README.md) · [JSON snapshot](../data/projects.json)', '',
        f"**{len(projects)} public records · Snapshot: {data['snapshot_date']}**", '',
        'Browse the [current HoodL2 directory](https://hoodl2.com/ecosystem) for subsequent updates. '
        'This snapshot preserves the source categories and recorded websites. It includes community projects, '
        'adjacent infrastructure and records with source gaps. Inclusion does not verify a deployment, '
        'current availability, official affiliation or contract safety. Source profile URLs remain in the JSON for provenance.', '',
        'Use your browser’s Find command to search project names. Names link to a recorded website, documentation, repository, app or X profile, in that order. Missing destinations remain unlinked. '
        'The JSON also contains other public links recorded by HoodL2, including documentation and X profiles where present.', '',
        '## Categories', '',
    ]
    for key, label in labels.items():
        if key in groups:
            lines.append(f'- [{label}](#{key}): {len(groups[key])}')
    for key, label in labels.items():
        if key not in groups:
            continue
        lines += ['', f'<a id="{key}"></a>', '', f'## {label}', '',
                  '| Project | Destination |', '| --- | --- |']
        for project in sorted(groups[key], key=lambda p: p['name'].casefold()):
            links = project['recorded_links']
            options = [('website', 'Website'), ('docs', 'Docs'), ('github', 'GitHub'), ('app', 'App'), ('twitter', 'X profile')]
            chosen = next(((links[key], label) for key, label in options if links.get(key)), None)
            name = cell(project['name'])
            if chosen:
                url, label = chosen
                lines.append(f"| [{name}]({url}) | {label} |")
            else:
                lines.append(f"| {name} | Not recorded |")
    if set(groups) - set(labels):
        raise ValueError('Missing category labels')
    lines += ['', '---', '', 'Maintained by **[HoodL2.com](https://hoodl2.com)**, an Autonomous Finance property. '
              'See [sources and review notes](../SOURCES.md).', '']
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Fail if the generated directory differs')
    args = parser.parse_args()
    data = json.loads((ROOT / 'data/projects.json').read_text())
    output = render(data)
    destination = ROOT / 'directory/README.md'
    if args.check:
        if not destination.exists() or destination.read_text() != output:
            raise SystemExit('Directory is out of date; run python3 scripts/render_directory.py')
        print(f"Directory matches {len(data['projects'])} source records")
    else:
        destination.write_text(output)
        print(f"Rendered {len(data['projects'])} source records")


if __name__ == '__main__':
    main()
