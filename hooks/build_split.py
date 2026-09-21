from mkdocs.structure.files import Files


PUBLIC_HOME = r"""
<section class="tresomat-hero tresomat-hero--compact">
  <div class="hero-inner">
    <picture class="hero-logo">
      <source srcset="assets/branding/tresomat-logo-dark.svg" media="(prefers-color-scheme: dark)">
      <img src="assets/branding/tresomat-logo.svg" alt="TRESOMAT">
    </picture>
    <h1>Dokumentation</h1>
    <button class="md-button md-button--primary" type="button" data-docs-search>Dokumentation durchsuchen</button>
  </div>
</section>

## Bereiche

<div class="grid cards" markdown>

-   :material-cash-register:{ .lg .middle }

    **TRESOMAT**

    Frontend, Backend sowie Installation und Betrieb.

    ---

    [Bereich öffnen :material-arrow-right:{ .link-icon }](tresomat/index.md)

-   :material-monitor-dashboard:{ .lg .middle }

    **Web-Portal**

    Kundenbereich und Werkzeuge für Administration und Support.

    ---

    [Bereich öffnen :material-arrow-right:{ .link-icon }](web-portal/index.md)

-   :material-download:{ .lg .middle }

    **Downloads**

    Handbücher, Anleitungen und freigegebene PDF-Dokumente.

    ---

    [Bereich öffnen :material-arrow-right:{ .link-icon }](downloads/index.md)

-   :material-history:{ .lg .middle }

    **Release Notes**

    Versionshinweise für die TRESOMAT-Produktfamilie.

    ---

    [Bereich öffnen :material-arrow-right:{ .link-icon }](release-notes/index.md)

</div>
"""

PROTECTED_HOME = r"""
<section class="tresomat-hero tresomat-hero--compact tresomat-hero--protected">
  <div class="hero-inner">
    <h1>TRESOMAT<br>Technik-Dokumentation</h1>
    <button class="md-button md-button--primary" type="button" data-docs-search>Technik-Dokumentation durchsuchen</button>
  </div>
</section>

## Geschützte Bereiche

<div class="grid cards" markdown>

-   :material-api:{ .lg .middle }

    **Integration API**

    Authentifizierung, Endpunkte, Werkzeuge und Codebeispiele.

    ---

    [Bereich öffnen](api/index.md)

-   :material-lifebuoy:{ .lg .middle }

    **Support**

    Diagnose, Vorgangssuche, Logs und technische Checklisten.

    ---

    [Bereich öffnen](support/index.md)

-   :material-cog-outline:{ .lg .middle }

    **TRESOMAT Technik**

    Installation, Betrieb, Hardware und technische Diagnose.

    ---

    [Bereich öffnen](tresomat/index.md)

-   :material-shield-account-outline:{ .lg .middle }

    **Web-Portal Technik**

    Admin, Security, Cloud Sync und Health Center.

    ---

    [Bereich öffnen](web-portal/index.md)

</div>
"""


def on_files(files, config):
    if config.get("extra", {}).get("docs_variant") != "public":
        return files
    protected_prefixes = ("api/", "support/")
    return Files([f for f in files if not f.src_uri.startswith(protected_prefixes)])


def on_page_markdown(markdown, page, config, files):
    if page.file.src_uri != "index.md":
        return markdown
    variant = config.get("extra", {}).get("docs_variant")
    if variant == "public":
        return PUBLIC_HOME
    if variant == "protected":
        return PROTECTED_HOME
    return markdown
