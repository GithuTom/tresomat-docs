from pathlib import PurePosixPath
import re

from mkdocs.structure.files import Files


PUBLIC_HOME = """
<section class="tresomat-hero tresomat-hero--compact"><div class="hero-inner">
<picture class="hero-logo"><source srcset="assets/branding/tresomat-logo-dark.svg" media="(prefers-color-scheme: dark)"><img src="assets/branding/tresomat-logo.svg" alt="TRESOMAT"></picture>
<h1>Dokumentation</h1><button class="md-button md-button--primary" type="button" data-docs-search>Dokumentation durchsuchen</button>
</div></section>

## Bereiche

<div class="grid cards" markdown>

-   :material-cash-register:{ .lg .middle }\n\n    **TRESOMAT**\n\n    Frontend und freigegebene Bedienungsbereiche.\n\n    ---\n\n    [Bereich öffnen :material-arrow-right:{ .link-icon }](tresomat/index.md)\n
-   :material-monitor-dashboard:{ .lg .middle }\n\n    **Web-Portal**\n\n    Öffentlicher Kundenbereich.\n\n    ---\n\n    [Bereich öffnen :material-arrow-right:{ .link-icon }](web-portal/index.md)\n
-   :material-download:{ .lg .middle }\n\n    **Downloads**\n\n    Öffentliche Handbücher und Release Notes.\n\n    ---\n\n    [Bereich öffnen :material-arrow-right:{ .link-icon }](downloads/index.md)\n
-   :material-history:{ .lg .middle }\n\n    **Release Notes**\n\n    Versionshinweise für TRESOMAT und Web-Portal.\n\n    ---\n\n    [Bereich öffnen :material-arrow-right:{ .link-icon }](release-notes/index.md)

</div>
"""

TECHDOCS_HOME = """
<section class="tresomat-hero tresomat-hero--compact tresomat-hero--protected"><div class="hero-inner">
<h1>TRESOMAT<br>Technik-Dokumentation</h1><button class="md-button md-button--primary" type="button" data-docs-search>Technik-Dokumentation durchsuchen</button>
</div></section>

## Geschützte Bereiche

<div class="grid cards" markdown>

-   :material-cog-outline:{ .lg .middle }\n\n    **TRESOMAT Technik**\n\n    Installation, Betrieb, Hardware und technische Diagnose.\n\n    ---\n\n    [Bereich öffnen :material-arrow-right:{ .link-icon }](tresomat/index.md)\n
-   :material-shield-account-outline:{ .lg .middle }\n\n    **Web-Portal Technik**\n\n    Admin, Security, Cloud Sync und Health Center.\n\n    ---\n\n    [Bereich öffnen :material-arrow-right:{ .link-icon }](web-portal/index.md)\n
-   :material-lifebuoy:{ .lg .middle }\n\n    **Support**\n\n    Diagnose, Vorgangssuche, Logs und technische Checklisten.\n\n    ---\n\n    [Bereich öffnen :material-arrow-right:{ .link-icon }](support/index.md)\n
-   :material-download:{ .lg .middle }\n\n    **Downloads**\n\n    Technische Handbücher und Betriebsunterlagen.\n\n    ---\n\n    [Bereich öffnen :material-arrow-right:{ .link-icon }](downloads/index.md)

</div>
"""

API_HOME = """
<section class="tresomat-hero tresomat-hero--compact tresomat-hero--protected"><div class="hero-inner">
<h1>TRESOMAT<br>Integration API</h1><button class="md-button md-button--primary" type="button" data-docs-search>API-Dokumentation durchsuchen</button>
</div></section>

## Bereiche

<div class="grid cards" markdown>

-   :material-rocket-launch-outline:{ .lg .middle }\n\n    **Erste Schritte**\n\n    Inbetriebnahme und Konfiguration der Integration.\n\n    ---\n\n    [Bereich öffnen :material-arrow-right:{ .link-icon }](api/erste-inbetriebnahme.md)\n
-   :material-key-outline:{ .lg .middle }\n\n    **Authentifizierung**\n\n    Login, Bearer Token, Refresh Token und Scopes.\n\n    ---\n\n    [Bereich öffnen :material-arrow-right:{ .link-icon }](api/authentifizierung/index.md)\n
-   :material-api:{ .lg .middle }\n\n    **Endpoints**\n\n    Catalog, Sales, Transactions, Payments und System.\n\n    ---\n\n    [Bereich öffnen :material-arrow-right:{ .link-icon }](api/catalog/index.md)\n
-   :material-tools:{ .lg .middle }\n\n    **Tools & Downloads**\n\n    Swagger, Postman, Testclient, Beispiele und API Manual.\n\n    ---\n\n    [Bereich öffnen :material-arrow-right:{ .link-icon }](downloads/index.md)

</div>
"""

DOWNLOADS = {
    "public": """# Downloads\n\n- [TRESOMAT Handbuch](tresomat-handbuch-pdf.md)\n- [Web-Portal Handbuch](web-portal-handbuch-pdf.md)\n- [Release Notes](release-notes-pdf.md)\n""",
    "techdocs": """# Downloads Technik\n\n- [TRESOMAT Handbuch](tresomat-handbuch-pdf.md)\n- [Web-Portal Handbuch](web-portal-handbuch-pdf.md)\n- [Release Notes](release-notes-pdf.md)\n""",
    "api": """# Downloads Integration API\n\n- [Integration API Manual](integration-api-manual-pdf.md)\n- [Swagger / OpenAPI](../api/swagger.md)\n- [Postman](../api/postman.md)\n- [Testclient](../api/testclient.md)\n- [Codebeispiele](../api/codebeispiele/index.md)\n\nWeitere Downloadpakete werden hier ergänzt, sofern sie im Repository vorhanden sind. Es werden keine Secrets eingebettet.\n""",
}

RELEASE_NOTES = {
    "public": """# Release Notes\n\n- [TRESOMAT](tresomat.md)\n- [Web-Portal](web-portal.md)\n""",
    "techdocs": """# Technische Release Notes\n\n- [TRESOMAT](tresomat.md)\n- [Web-Portal](web-portal.md)\n""",
    "api": """# Integration API Release Notes\n\n- [Integration API](integration-api.md)\n""",
}

ALLOWED = {}
MD_LINK = re.compile(r"(?<!!)\[([^]]+)\]\(([^)]+)\)(\{[^}]*\})?")
HTML_LINK = re.compile(r'<a\s+([^>]*?)href=["\']([^"\']+)["\']([^>]*)>(.*?)</a>', re.I | re.S)


def _refs(node):
    if isinstance(node, str):
        return {node} if node.endswith(".md") else set()
    if isinstance(node, list):
        return set().union(*(_refs(item) for item in node), set())
    if isinstance(node, dict):
        return set().union(*(_refs(value) for value in node.values()), set())
    return set()


def _target_source(page_source, target):
    clean = target.split("#", 1)[0].split("?", 1)[0]
    if not clean or clean.startswith(("http://", "https://", "mailto:", "tel:", "#")):
        return None
    path = PurePosixPath(clean.lstrip("/")) if clean.startswith("/") else PurePosixPath(page_source).parent / clean
    parts = []
    for part in path.parts:
        if part == "..":
            if parts:
                parts.pop()
        elif part not in (".", ""):
            parts.append(part)
    path = PurePosixPath(*parts)
    if clean.endswith("/"):
        path /= "index.md"
    elif path.suffix == "":
        path = path.with_suffix(".md")
    return path.as_posix() if path.suffix == ".md" else None


def _neutralize_cross_links(markdown, page_source, allowed):
    def md_replace(match):
        target = _target_source(page_source, match.group(2))
        return match.group(1) if target and target not in allowed else match.group(0)

    def html_replace(match):
        target = _target_source(page_source, match.group(2))
        return match.group(4) if target and target not in allowed else match.group(0)

    return HTML_LINK.sub(html_replace, MD_LINK.sub(md_replace, markdown))


def on_files(files, config):
    variant = config.get("extra", {}).get("docs_variant")
    if variant not in ("public", "techdocs", "api"):
        return files
    allowed = _refs(config.get("nav", []))
    ALLOWED[variant] = allowed
    return Files([f for f in files if not f.src_uri.endswith(".md") or f.src_uri in allowed])


def on_page_markdown(markdown, page, config, files):
    variant = config.get("extra", {}).get("docs_variant")
    if variant not in ("public", "techdocs", "api"):
        return markdown
    source = page.file.src_uri
    if source == "index.md":
        markdown = {"public": PUBLIC_HOME, "techdocs": TECHDOCS_HOME, "api": API_HOME}[variant]
    elif source == "downloads/index.md":
        markdown = DOWNLOADS[variant]
    elif source == "release-notes/index.md":
        markdown = RELEASE_NOTES[variant]
    return _neutralize_cross_links(markdown, source, ALLOWED.get(variant, set()))
