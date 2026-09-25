"""Rewrite the two generated README blocks from live GitHub data.

OSS block: the curated contributions in oss.json, with state (open / merged / fixed) and the repository's star count
written as TEXT, so search and sourcing crawlers read the same thing people see. A live badge sits beside each.
RECENT block: my newest issues and pull requests in other people's public repositories with 1,000+ stars
(open source only: own repositories, closed-unmerged PRs, not-planned issues and web-upload PRs are left out).

Fails closed: if an API call fails, the old block stays. Runs in Actions with GITHUB_TOKEN; locally with `gh auth token`.
usage: GITHUB_TOKEN=... OWNER=Kushal9889 python3 .github/scripts/refresh.py
"""
import json
import os
import re
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OWNER = os.environ.get("OWNER", "Kushal9889")
MIN_STARS = 1000


def api(path):
    req = urllib.request.Request(f"https://api.github.com/{path}", headers={
        "Accept": "application/vnd.github+json", "User-Agent": "profile-refresh",
        **({"Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}"} if os.environ.get("GITHUB_TOKEN") else {})})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.load(r)


_stars = {}


def stars(repo):
    if repo not in _stars:
        _stars[repo] = api(f"repos/{repo}")["stargazers_count"]
    return _stars[repo]


def clean(t):
    """No em or en dashes on the page (design rule); GitHub titles are rewritten, never truncated."""
    return t.replace("\u2014", ",").replace("\u2013", "-").replace(" ,", ",")


def k(n):
    return f"{n / 1000:.1f}k" if n >= 1000 else str(n)


def state(repo, number):
    it = api(f"repos/{repo}/issues/{number}")
    if "pull_request" in it:
        pr = api(f"repos/{repo}/pulls/{number}")
        return "PR", "merged" if pr.get("merged_at") else ("under review" if pr["state"] == "open" else "closed")
    return "issue", "open" if it["state"] == "open" else ("fixed" if it.get("state_reason") == "completed" else "closed")


def oss_block():
    rows = ["| Project | Contribution | Status | Stars |", "|---|---|---|---|"]
    for c in json.loads((ROOT / "oss.json").read_text()):
        repo, n = c["repo"], c["number"]
        kind, st = state(repo, n)
        path = "pull" if kind == "PR" else "issues"
        extra = (f", from my report [#{c['report']}](https://github.com/{repo}/issues/{c['report']})" if c.get("report") else "") + \
                (f"; maintainer fix [#{c['fix']}](https://github.com/{repo}/pull/{c['fix']}) credits my report" if c.get("fix") else "")
        badge = ('<img alt="merged" src="https://img.shields.io/badge/merged-d9480f?style=flat-square">' if st == "merged" else
                 f'<img alt="live status" src="https://img.shields.io/github/{"pulls" if kind == "PR" else "issues"}'
                 f'/detail/state/{repo}/{n}?style=flat-square&label=live">')  # a merge stays in the signal colour
        rows.append(f"| [{c['name']}](https://github.com/{repo}) | {kind} [#{n}](https://github.com/{repo}/{path}/{n}): {c['what']}{extra} "
                    f"| **{kind}, {st}** {badge} | **{k(stars(repo))}** ★ |")
    return "\n".join(rows)


def recent_block(limit=6):
    q = f"author:{OWNER}+is:public+-user:{OWNER}&sort=created&order=desc&per_page=40"
    lines = []
    for it in api(f"search/issues?q={q}")["items"]:
        repo = it["repository_url"].split("/repos/", 1)[1]
        pr = it.get("pull_request")
        if pr and it["state"] != "open" and not pr.get("merged_at"):
            continue  # closed without merge
        if it.get("state_reason") == "not_planned" or re.match(r"^(Add|Create|Update|Delete) files? via", it["title"]):
            continue
        if stars(repo) < MIN_STARS:
            continue  # open source only: popular public projects
        kind = "PR" if pr else "issue"
        st = ("merged" if pr.get("merged_at") else "under review") if pr else ("open" if it["state"] == "open" else "fixed")
        lines.append(f"- [{repo}#{it['number']}]({it['html_url']}) · {k(stars(repo))} stars, {kind}, {st}: {clean(it['title'])}")
        if len(lines) == limit:
            break
    return "\n".join(lines)


def splice(text, tag, block):
    return re.sub(rf"<!--START_{tag}-->.*?<!--END_{tag}-->", f"<!--START_{tag}-->\n{block}\n<!--END_{tag}-->", text, flags=re.S)


def main():
    readme = ROOT / "README.md"
    text = readme.read_text()
    new = text
    for tag, fn in (("OSS", oss_block), ("ACTIVITY", recent_block)):
        try:
            block = fn()
            if block.strip():
                new = splice(new, tag, block)
        except Exception as e:  # fail closed: keep the previous block
            print(f"{tag}: kept previous block ({e})")
    if new != text:
        readme.write_text(new)
        print("README updated")
    else:
        print("no change")


if __name__ == "__main__":
    assert k(92673) == "92.7k" and k(999) == "999" and clean("a \u2014 b") == "a, b"
    main()
