from html.parser import HTMLParser
from pathlib import Path, PurePosixPath
from urllib.parse import urlsplit
import json
import sys
import yaml


CONFIGS = {
    "public": "mkdocs.public.yml",
    "techdocs": "mkdocs.techdocs.yml",
    "api": "mkdocs.api.yml",
}


def refs(node):
    if isinstance(node, str):
        return [node] if node.endswith(".md") else []
    if isinstance(node, list):
        return sum((refs(item) for item in node), [])
    if isinstance(node, dict):
        return sum((refs(value) for value in node.values()), [])
    return []


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            href = dict(attrs).get("href")
            if href:
                self.links.append(href)


def output_for(source):
    path = PurePosixPath(source)
    if path.name == "index.md":
        return (path.parent / "index.html").as_posix()
    return (path.parent / path.stem / "index.html").as_posix()


def url_for(source):
    path = PurePosixPath(source)
    if source == "index.md":
        return ""
    if path.name == "index.md":
        return path.parent.as_posix().rstrip("/") + "/"
    return (path.parent / path.stem).as_posix().rstrip("/") + "/"


def local_target(page_output, href):
    if "{{" in href or "}}" in href:
        return None
    parsed = urlsplit(href)
    if parsed.scheme or parsed.netloc or href.startswith(("mailto:", "tel:", "#")):
        return None
    path = parsed.path
    if not path:
        return None
    if path.startswith("/"):
        target = PurePosixPath(path.lstrip("/"))
    else:
        target = PurePosixPath(page_output).parent / path
    parts = []
    for part in target.parts:
        if part == "..":
            if parts:
                parts.pop()
        elif part not in (".", ""):
            parts.append(part)
    target = PurePosixPath(*parts)
    if path.endswith("/"):
        target /= "index.html"
    elif target.suffix == "":
        target /= "index.html"
    return target.as_posix()


def main():
    if len(sys.argv) != 3 or sys.argv[1] not in CONFIGS:
        raise SystemExit("Usage: verify_role_build.py <public|techdocs|api> <site-dir>")
    role, site_name = sys.argv[1:]
    site = Path(site_name)
    config = yaml.unsafe_load(Path(CONFIGS[role]).read_text(encoding="utf-8"))
    nav = refs(config["nav"])
    source = {p.relative_to("docs").as_posix() for p in Path("docs").rglob("*.md")}
    errors = []
    if len(source) != 234:
        errors.append(f"Expected 234 Markdown sources, found {len(source)}")
    if len(nav) != len(set(nav)):
        errors.append("Duplicate navigation target")
    missing_sources = sorted(set(nav) - source)
    if missing_sources:
        errors.append(f"Missing navigation sources: {missing_sources}")
    expected = {output_for(p) for p in nav}
    actual = {p.relative_to(site).as_posix() for p in site.rglob("index.html")}
    unexpected = sorted(actual - expected)
    missing_html = sorted(expected - actual)
    if unexpected:
        errors.append(f"Unexpected role pages: {unexpected}")
    if missing_html:
        errors.append(f"Missing role pages: {missing_html}")

    index = json.loads((site / "search" / "search_index.json").read_text(encoding="utf-8"))
    locations = [item.get("location", "").split("#", 1)[0] for item in index.get("docs", [])]
    allowed_urls = {url_for(p) for p in nav}
    leaked = sorted({x for x in locations if x and x not in allowed_urls})
    if leaked:
        errors.append(f"Search index leakage: {leaked}")

    broken = []
    for html in site.rglob("*.html"):
        parser = LinkParser()
        parser.feed(html.read_text(encoding="utf-8"))
        page_output = html.relative_to(site).as_posix()
        for href in parser.links:
            target = local_target(page_output, href)
            if target and not (site / target).exists():
                broken.append((page_output, href))
    if broken:
        errors.append(f"Broken local links: {broken[:20]}")

    role_forbidden = {
        "public": ("api/", "support/", "web-portal/admin-support/"),
        "techdocs": ("api/",),
        "api": ("support/", "web-portal/", "tresomat/"),
    }[role]
    forbidden = sorted(p for p in actual if p.startswith(role_forbidden))
    if forbidden:
        errors.append(f"Forbidden role content: {forbidden}")

    if errors:
        raise SystemExit("\n".join(errors))
    print(f"{role}: {len(nav)} pages, isolated search index, no broken/cross-role links, 234 sources preserved")


if __name__ == "__main__":
    main()
