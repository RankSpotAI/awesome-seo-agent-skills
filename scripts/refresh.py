#!/usr/bin/env python3
"""Refresh star counts and last-updated dates for every GitHub-linked server in README.md.

Also reports servers that have been archived or have gone quiet for over a year,
so the list does not rot the way most awesome lists do.

Usage: GITHUB_TOKEN=... python3 scripts/refresh.py [--check]
  --check  report what would change and exit non-zero, do not write
"""

import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone

README = os.path.join(os.path.dirname(__file__), "..", "README.md")
API = "https://api.github.com/repos/"

# A table row we own looks like:
# | [label](https://github.com/owner/repo) | what | Type | Auth | 123 | 2026-01-01 |
ROW = re.compile(
    r"^\|\s*\[[^\]]+\]\(https://github\.com/(?P<owner>[^/)\s]+)/(?P<repo>[^/)\s#]+)\)\s*\|"
    r"(?P<middle>[^|]*\|[^|]*\|[^|]*\|)"
    r"\s*(?P<stars>[^|]*?)\s*\|\s*(?P<updated>[^|]*?)\s*\|\s*$"
)

STALE_AFTER = timedelta(days=365)


def fetch(slug):
    req = urllib.request.Request(API + slug, headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": "awesome-seo-agent-skills-refresh",
    })
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", "Bearer " + token)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.load(resp)
    except urllib.error.HTTPError as err:
        if err.code == 404:
            return None
        if err.code == 403:
            sys.exit(
                "GitHub rate limit hit. Set GITHUB_TOKEN to a token with public repo "
                "read access and run again."
            )
        raise


def main():
    check_only = "--check" in sys.argv
    with open(README, encoding="utf-8") as handle:
        lines = handle.read().split("\n")

    now = datetime.now(timezone.utc)
    changed, archived, stale, missing = 0, [], [], []

    for index, line in enumerate(lines):
        match = ROW.match(line)
        if not match:
            continue
        slug = "{}/{}".format(match["owner"], match["repo"])
        data = fetch(slug)
        if data is None:
            missing.append(slug)
            continue

        full = data["full_name"]
        if full.lower() != slug.lower():
            print("renamed: {} is now {}".format(slug, full))

        stars = str(data["stargazers_count"])
        updated = data["pushed_at"][:10]
        pushed = datetime.strptime(data["pushed_at"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)

        if data.get("archived"):
            archived.append(full)
        elif now - pushed > STALE_AFTER:
            stale.append("{} (last push {})".format(full, updated))

        if match["stars"] != stars or match["updated"] != updated:
            changed += 1
            head = line[: match.start("middle")]
            lines[index] = "{}{} {} | {} |".format(head, match["middle"], stars, updated)

    if missing:
        print("\ncould not resolve, check for a rename or deletion:")
        for slug in missing:
            print("  " + slug)
    if archived:
        print("\narchived, move to the superseded table:")
        for slug in archived:
            print("  " + slug)
    if stale:
        print("\nno push in over a year, worth testing:")
        for slug in stale:
            print("  " + slug)

    print("\n{} row(s) need updating".format(changed))

    if check_only:
        sys.exit(1 if (changed or missing or archived) else 0)

    if changed:
        with open(README, "w", encoding="utf-8") as handle:
            handle.write("\n".join(lines))
        print("README.md updated")


if __name__ == "__main__":
    main()
