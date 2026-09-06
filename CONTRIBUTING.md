# Contributing

Thanks for helping keep this list accurate. Corrections matter as much as additions.

## What gets listed

A skill pack qualifies if all three are true:

1. **It contains at least one real `SKILL.md`.** Not a plan, not a blog post, not a prompt collection in a README.
2. **It is public and installable.** Someone can clone it or add it as a plugin today.
3. **It does SEO work.** Technical audits, keyword research, content briefs, schema, internal linking, indexing, GEO and AEO, reporting.

## What does not get listed

- MCP servers. Those go in [awesome-seo-mcp](https://github.com/RankSpotAI/awesome-seo-mcp).
- Prompt libraries with no `SKILL.md`.
- Paid packs with no public repo to inspect. People need to read a skill before running it.
- Dead repos. If a listed pack is archived or deleted, open an issue and we will move or remove it.

## Adding an entry

Open a PR that adds one row to the right section, in descending star order.

```
| [owner/repo](https://github.com/owner/repo) | What it covers, and how many skills if the author says | Claude Code | MIT | 0 | 2026-09-06 |
```

Fill the columns like this:

- **What it covers**: plain language, no marketing. Say what SEO ground it covers. If the author states a skill count, include it.
- **Works with**: only agents the README actually claims. Do not guess, even though most skills are portable.
- **Licence**: the SPDX id, or `none` if the repo ships no licence file. This one matters, people are copying your files.
- **Stars** and **Updated**: put anything in, a workflow refreshes both weekly.

## Self-submissions

Submitting your own pack is fine and encouraged. Say so in the PR description, describe it factually, and put it in star order like everything else. Entries that read like ad copy get edited down, not rejected.

## Corrections

Open an issue or a PR for anything wrong: a dead link, a rename, a wrong licence, a pack that moved, an agent we listed that the README does not actually support. This list only earns its keep by being right.
