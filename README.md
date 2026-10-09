# Design Fieldnotes

An independent, agent-first UX/UI concept library synthesized from [Kole Jain’s public videos](https://www.youtube.com/@KoleJain).

[Browse the website](https://brianjmeier.github.io/design-fieldnotes/) · [Download the skill pack](https://brianjmeier.github.io/design-fieldnotes/skills.zip) · [How it was made](METHODOLOGY.md) · [Design & verification](PUBLICATION.md)

29 concept skills connect mental models to concrete examples, failure modes and evidence. Eight verification guides support the concepts. The source ledger records 52 public uploads from the **October 4, 2026 snapshot**. This is transcript-led research with sampled frames; it does not claim uninterrupted viewing of every video.

## Use it with an agent

Download and unpack `skills.zip`. It contains one `design-fieldnotes/` directory with `SKILL.md`, the concept skills, verification guides and source metadata. Give your agent that directory and this prompt:

> Read design-fieldnotes/SKILL.md. My interface’s primary task is [outcome], and the relevant screen/code is [reference]. Choose the smallest useful concept. Explain the mechanism, propose a concrete change, and state what observable evidence would falsify it. Implement within my existing system and verify the outcome.

For a project-local skill folder, copy the **whole extracted directory** to `.agents/skills/design-fieldnotes/`. Other agents can read the same `SKILL.md` by path; automatic discovery depends on the agent. Keeping the full directory preserves the related-skill and verification links. An individual Markdown download is useful to paste into a conversation; its relative links require the full pack.

You can also clone the repository and point an agent at `AGENTS.md`, or consume `library.json` and `llms.txt`. No account, API key, build server or model call is required to read the library.

## Maintain the content

For maintenance, clone the source repository; the download pack is for reading and agent use. Canonical inputs live under `data/`. Generated exports are committed so GitHub Pages can serve the site directly.

```sh
python3 scripts/build.py
python3 scripts/validate.py
python3 -m http.server 8000
```

Open your local server in a browser. Python’s standard library is sufficient; there are no runtime packages to install. See [the data map](DATA.md) and [contribution guide](CONTRIBUTING.md) before editing.

GitHub Pages is configured from `main`, repository root, with `.nojekyll`. Forks can update `data/site.json`, regenerate, and configure their own Pages source. The website uses relative asset/download paths and hash routes, so project subpaths work.

## Attribution and reuse

The implementation, original synthesis and examples are licensed under [MIT](LICENSE). Kole Jain owns the source videos; those videos and caption tracks are not redistributed or relicensed here. Source links and timestamped teaching references remain attached to the relevant concepts. This is an independent project, without affiliation or endorsement.
