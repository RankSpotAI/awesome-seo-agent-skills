# Awesome SEO Agent Skills [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Agent Skills that teach Claude Code, Codex, Cursor, OpenClaw and other agents how to do SEO work. Technical audits, keyword research, content briefs, schema, GEO and AI visibility.

A skill is a folder with a `SKILL.md` file that an agent loads on demand. Anthropic published the format in October 2025 and released it as an open standard in December 2025, and it now works across Claude Code, Claude.ai, the Claude API, OpenAI Codex, Cursor, Gemini CLI, Antigravity, OpenClaw and Windsurf. SEO turned out to be one of the first places the format caught on, and there are now packs with tens of thousands of stars.

Every entry below was checked by hand in September 2026. We record what each pack covers, which agents it targets, its licence, and when it was last touched, because a skill you clone into your agent runs with your permissions and you should know if it has been abandoned.

---

**Maintained by [RankSpot](https://www.rankspot.ai/)**, an AI search visibility platform that tracks brand mentions in ChatGPT, Claude, Gemini, and Google AI Overviews. We do not publish a competing skill pack, so this list has no house favourite. Spot a mistake in any entry? [Open a PR](CONTRIBUTING.md) and we will merge it.

---

## Contents

- [How to read this list](#how-to-read-this-list)
- [Official vendor skills](#official-vendor-skills)
- [Large multi-skill packs](#large-multi-skill-packs)
- [Technical SEO and auditing](#technical-seo-and-auditing)
- [GEO, AEO and AI visibility](#geo-aeo-and-ai-visibility)
- [Content, keywords and publishing](#content-keywords-and-publishing)
- [Framework and language specific](#framework-and-language-specific)
- [Smaller and newer packs](#smaller-and-newer-packs)
- [Installing a skill](#installing-a-skill)
- [Data sources these skills plug into](#data-sources-these-skills-plug-into)
- [Before you install anything](#before-you-install-anything)
- [Skill directories](#skill-directories)
- [Gaps worth filling](#gaps-worth-filling)
- [Related lists](#related-lists)
- [Contributing](#contributing)

## How to read this list

| Column | Meaning |
| --- | --- |
| **What it covers** | The SEO ground the pack covers, and how many skills it ships where the author states a number. |
| **Works with** | Agents the author explicitly supports. Most skills are portable in practice, since `SKILL.md` is an open standard, but this is what the README claims. |
| **Licence** | Matters more than usual here. You are copying files into your own agent, so check you can. `none` means the repo ships no licence file, which means default copyright applies. |
| **Stars** and **Updated** | Refreshed weekly by a workflow in this repo. Anything older than a year is worth reading before you run it. |

## Official vendor skills

Built by the company whose data the skills use.

| Repo | What it covers | Works with | Licence | Stars | Updated |
| --- | --- | --- | --- | --- | --- |
| [seranking/seo-skills](https://github.com/seranking/seo-skills) | Content briefs, AI search share of voice, audits, backlink gaps, keyword clusters, schema, sitemaps, GEO. Built for the SE Ranking MCP server, but every API call is documented so it can be adapted | Claude Code | MIT | 136 | 2026-06-25 |

## Large multi-skill packs

Broad marketing or SEO suites. These are where most people start, and the star counts show it.

| Repo | What it covers | Works with | Licence | Stars | Updated |
| --- | --- | --- | --- | --- | --- |
| [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | Marketing skills across CRO, copywriting, SEO, analytics and growth engineering. The largest pack in the ecosystem by a wide margin | Claude Code, AI agents | MIT | 47267 | 2026-09-05 |
| [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | 25 sub-skills and 18 sub-agents: technical SEO, E-E-A-T, schema, GEO and AEO, backlinks, local SEO, semantic clustering, e-commerce, international SEO, reporting | Claude Code | MIT | 16424 | 2026-08-26 |
| [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | GEO-first SEO for any site, built around citability in AI answers rather than rankings | Claude Code | MIT | 10310 | 2026-09-06 |
| [TheCraigHewitt/seomachine](https://github.com/TheCraigHewitt/seomachine) | A full Claude Code workspace for producing long-form SEO content, 26 commands | Claude Code | MIT | 7401 | 2026-08-05 |
| [aaron-he-zhu/aaron-marketing-skills](https://github.com/aaron-he-zhu/aaron-marketing-skills) | 120 marketing skills including 16 SEO and GEO skills, usable as a plugin or an eight-bot team | Claude Code, Codex, Cursor | Apache-2.0 | 2734 | 2026-09-06 |
| [kostja94/marketing-skills](https://github.com/kostja94/marketing-skills) | 160+ skills spanning SEO, social, influencer and content marketing | Claude Code | MIT | 954 | 2026-06-09 |
| [OpenClaudia/openclaudia-skills](https://github.com/OpenClaudia/openclaudia-skills) | 34 open-source marketing skills covering SEO, content, email, ads, analytics and growth | Claude Code | MIT | 680 | 2026-08-25 |
| [nicepkg/ai-workflow](https://github.com/nicepkg/ai-workflow) | 170+ prebuilt skills across 14+ AI tools, with a content creator workflow | Claude Code, Cursor, Codex | MIT | 282 | 2026-01-20 |

## Technical SEO and auditing

| Repo | What it covers | Works with | Licence | Stars | Updated |
| --- | --- | --- | --- | --- | --- |
| [Bhanunamikaze/Agentic-SEO-Skill](https://github.com/Bhanunamikaze/Agentic-SEO-Skill) | LLM-first SEO analysis, 16 sub-skills and 10 specialised agents | Claude Code, Codex, Antigravity | MIT | 889 | 2026-07-23 |
| [JeffLi1993/seo-audit-skill](https://github.com/JeffLi1993/seo-audit-skill) | Beginner audits through to advanced technical analysis | Claude Code, OpenClaw, AI agents | MIT | 752 | 2026-06-17 |
| [Suganthan-Mohanadasan/tech-seo-audit-skill](https://github.com/Suganthan-Mohanadasan/tech-seo-audit-skill) | Technical audits across 10 categories | Claude Code | MIT | 62 | 2026-04-11 |
| [norahe0304-art/30x-seo](https://github.com/norahe0304-art/30x-seo) | 23 production skills across technical SEO, content optimisation and keyword research | Claude Code | MIT | 50 | 2026-03-14 |
| [mangollc/claude-seo-skill](https://github.com/mangollc/claude-seo-skill) | Agency-oriented pack: keyword research, technical audits, content, brand SERP monitoring | Claude Code | none | 37 | 2026-02-19 |
| [agharsallah/seo-engine-skills](https://github.com/agharsallah/seo-engine-skills) | Issue identification with actionable recommendations | Any agent | none | 3 | 2026-03-08 |

## GEO, AEO and AI visibility

The fastest moving category. Almost everything here was published in 2026.

| Repo | What it covers | Works with | Licence | Stars | Updated |
| --- | --- | --- | --- | --- | --- |
| [yaojingang/GEOHub](https://github.com/yaojingang/GEOHub) | Evidence-bounded GEO and SEO skills for AI search, with research-grounded defaults | Any agent | AGPL-3.0 | 152 | 2026-08-31 |
| [199-biotechnologies/claude-skill-seo-geo-optimizer](https://github.com/199-biotechnologies/claude-skill-seo-geo-optimizer) | Analyses content for both traditional search and AI citation, multi-format reporting | Claude Code | MIT | 44 | 2026-05-24 |
| [jrr996shujin-png/openclaw-seo-aeo-skills](https://github.com/jrr996shujin-png/openclaw-seo-aeo-skills) | Site health diagnosis plus long-tail question mining from Reddit and Quora | OpenClaw | MIT | 11 | 2026-02-26 |
| [factive1/claude-code-seo-skill](https://github.com/factive1/claude-code-seo-skill) | SEO and GEO content strategy for ranking and getting cited by AI | Claude Code | none | 10 | 2026-01-22 |
| [cartoonitunes/inlay-skills](https://github.com/cartoonitunes/inlay-skills) | Website AI readiness: audit, llms.txt, MCP server setup | Any agent | MIT | 1 | 2026-05-07 |
| [hmzainjamil/geo-seo-claude](https://github.com/hmzainjamil/geo-seo-claude) | GEO plus technical SEO audit suite | Claude Code | MIT | 0 | 2026-05-26 |

## Content, keywords and publishing

| Repo | What it covers | Works with | Licence | Stars | Updated |
| --- | --- | --- | --- | --- | --- |
| [ashleytheash/seo-agent-skill](https://github.com/ashleytheash/seo-agent-skill) | Diagnosis, competitive analysis, blog production and indexing automation | Any agent | none | 3 | 2026-05-31 |
| [sherotree/seo-agent-skills](https://github.com/sherotree/seo-agent-skills) | Ranked keywords, competitor backlink gaps, keyword-driven landing page copy | Any agent | MIT | 2 | 2026-08-18 |
| [boshify/ai-seo-agent-skills](https://github.com/boshify/ai-seo-agent-skills) | Self-contained AI SEO instruction sets any agent can fetch | Any agent | MIT | 2 | 2026-06-16 |
| [Wotaso/seodrafts-agent-skills](https://github.com/Wotaso/seodrafts-agent-skills) | Draft production and publishing setup, official to the SEODrafts project | Any agent | none | 0 | 2026-08-04 |

## Framework and language specific

Worth knowing about if they match your stack or your market, easy to miss otherwise.

| Repo | What it covers | Works with | Licence | Stars | Updated |
| --- | --- | --- | --- | --- | --- |
| [imgompanda/fireauto](https://github.com/imgompanda/fireauto) | Korean language automation plugin covering SEO, security, PRDs and Reddit research | Claude Code | MIT | 140 | 2026-04-09 |
| [huifer/claude-code-seo](https://github.com/huifer/claude-code-seo) | Next.js specific audits with 100-point scoring | Claude Code | MIT | 110 | 2026-01-04 |
| [Horosheff/google-yandex-seo-skill](https://github.com/Horosheff/google-yandex-seo-skill) | Dual-engine audits for Google and Yandex, self-contained | Cursor, OpenClaw | MIT | 36 | 2026-03-11 |
| [MYehia565/google-seo-agent-skills](https://github.com/MYehia565/google-seo-agent-skills) | Skills grounded in Google Search Central documentation. Not affiliated with Google | Any agent | NOASSERTION | 0 | 2026-08-22 |

## Smaller and newer packs

Fewer stars, but several are recent and specific. Read the `SKILL.md` before you rely on one.

| Repo | What it covers | Works with | Licence | Stars | Updated |
| --- | --- | --- | --- | --- | --- |
| [aaron-he-zhu/seo-geo-claude-skills](https://github.com/aaron-he-zhu/seo-geo-claude-skills) | Signpost repo. The 16 SEO and GEO skills moved to `aaron-marketing-skills`, the standalone 20-skill set stays here | Claude Code | Apache-2.0 | 193 | 2026-09-04 |
| [ccforseo/seo-claude-code-skills](https://github.com/ccforseo/seo-claude-code-skills) | Technical audits, keyword clustering, content optimisation, AI visibility | Claude Code | none | 2 | 2026-03-06 |
| [gaguero/seo-agent-skills](https://github.com/gaguero/seo-agent-skills) | Technical audit and content pack written against the Agent Skills open standard | Any agent | MIT | 0 | 2026-05-29 |
| [anandan-digital-marketer/seo-agent-skills](https://github.com/anandan-digital-marketer/seo-agent-skills) | 29 skills covering technical auditing, LLM visibility, GEO and content | Claude Code | none | 0 | 2026-06-04 |

## Installing a skill

Skills are plain folders, so installing one is mostly copying files into the right directory.

**Claude Code**, project scoped or user scoped:

```bash
# available in one project
git clone https://github.com/seranking/seo-skills .claude/skills/seo-skills

# available everywhere
git clone https://github.com/seranking/seo-skills ~/.claude/skills/seo-skills
```

**Packs that ship as a plugin** usually tell you to add a marketplace instead, which keeps them updatable:

```bash
/plugin marketplace add owner/repo
/plugin install pack-name
```

**Codex, Cursor, Gemini CLI, OpenClaw and Windsurf** each read skills from their own directory. Check the pack's README, since the same `SKILL.md` files usually work in all of them and only the destination path changes.

After installing, restart the agent or start a new session so it picks up the new skill. Most agents load a skill only when the task matches its description, so if nothing happens, read the `description` line in the `SKILL.md` and phrase your request closer to it.

## Data sources these skills plug into

Most SEO skills are instructions, not data. They get their numbers from an MCP server or an API you connect separately, so a skill pack is usually only half the setup.

Common pairings:

- **Search Console data**, via one of the community GSC servers
- **Keyword, backlink and SERP data**, via DataForSEO, SE Ranking, Ahrefs, Semrush or SerpApi
- **Crawling and scraping**, via Firecrawl or Screaming Frog
- **AI search visibility**, via [RankSpot](https://www.rankspot.ai/), Peec or Local Falcon

We keep the full list of those in [awesome-seo-mcp](https://github.com/RankSpotAI/awesome-seo-mcp), including remote endpoints and auth requirements.

## Before you install anything

A skill is instructions your agent will follow with your permissions and your API keys. That is worth thirty seconds of care.

- **Read the `SKILL.md`.** It is markdown, it is short, and it tells you exactly what the agent is being told to do.
- **Check for scripts.** Many packs ship helper scripts the skill will run. Read those too.
- **Check the licence.** A repo with no licence file is not actually free to copy, whatever the README says.
- **Check the last commit date.** SEO advice ages badly, and a skill written against 2025 guidance will confidently tell your agent things that are no longer true.
- **Be careful with skills that publish.** Anything that writes to your CMS, submits to indexing APIs, or posts externally should be run with review turned on the first few times.

## Skill directories

Places to search when this list does not have what you need. None are SEO specific.

- [skills.sh](https://skills.sh), open marketplace with an npm-style installer
- [SkillsMP](https://skillsmp.com), the largest catalogue by index size
- [SkillHub](https://agentskillshub.dev), smaller and curated, skills scored on several dimensions
- [Official Claude skills documentation](https://code.claude.com/docs/en/skills), the format itself

## Gaps worth filling

Nobody has built these well yet. Build one and we will list it.

- **Log file analysis.** No skill reads server logs to show which bots crawled what.
- **Internal linking at scale.** Plenty of skills mention it, none actually map a link graph.
- **Hreflang and international SEO.** Barely covered outside the big suites.
- **Migration and redirect mapping.** A genuinely painful job that suits an agent well.
- **Schema validation.** Many skills generate JSON-LD, none validate it against Google's rich result requirements.
- **Skills tied to a specific CMS.** Webflow, Ghost, Shopify and Framer are almost unserved.

## Related lists

- [awesome-seo-mcp](https://github.com/RankSpotAI/awesome-seo-mcp), the MCP servers these skills get their data from. Also maintained by us.
- [awesome-geo-tools](https://github.com/RankSpotAI/awesome-geo-tools), GEO and AI visibility platforms compared on engines tracked, refresh rate, price and data access. Also maintained by us.
- [sharozdawa/awesome-seo-mcp-servers](https://github.com/sharozdawa/awesome-seo-mcp-servers), a broader list mixing MCP servers, skills and standalone tools. Useful prior art, and a source we cross-checked against.
- [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills), 1000+ skills across every category, not SEO specific.
- [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills), general Claude Skills list.

## Contributing

Additions and corrections are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

The short version: the pack has to contain at least one real `SKILL.md`, it has to be public, and the description has to say what it does rather than sell it.

## License

[CC0](LICENSE). No rights reserved, copy it freely.

---

Maintained by [RankSpot](https://www.rankspot.ai/). If you want to know whether ChatGPT, Claude and Gemini recommend your brand, that is the problem we work on.
