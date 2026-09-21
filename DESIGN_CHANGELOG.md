# TRESOMAT Docs V2 – Design Changelog

## Navigation

- Material-Tabs aktiviert und Integration API als kompakter Tab „API“ beschriftet.
- API-Navigation in Erste Schritte, Authentifizierung, Endpunkte, Werkzeuge, Fehlerbehandlung und Codebeispiele gruppiert.
- Bestehende 234 Dokumentationsseiten und deren Dateipfade beibehalten.
- Sidebar bleibt standardmäßig eingeklappt; `navigation.expand` ist nicht aktiviert.

## Design und Branding

- TRESOMAT-Farbvariablen, Systemfont-Stack und vollständige Light-/Dark-Surfaces ergänzt.
- Moderne Hero-Zone, Karten, dezente Hover-Zustände, aktive Navigation und kompakte Hierarchie umgesetzt.
- Branding-Verzeichnis für Logo, Dark-Logo und Favicon vorbereitet; keine fremden Platzhalterlogos erzeugt.
- Responsive Tabellen, Screenshots (`docs-screenshot`) und Video-Container gestaltet.

## Inhalte und Komponenten

- Startseite sowie TRESOMAT-, Web-Portal-, API- und Support-Landingpages neu gestaltet.
- Frontendvarianten und Scannerreferenz als Karten-Dashboards umgesetzt.
- Download-Karten und modernes Release-Notes-Muster mit Status-Badges ergänzt.
- Material-Admonitions, Code-Copy, verknüpfte Tabs und Syntax-Highlighting aktiviert.
- Professionelle 404-Seite ergänzt.

## Hosting

- Bestehender manueller GitHub-Pages-Workflow unverändert beibehalten.
- Cloudflare-Pages-Kompatibilität bleibt erhalten.

## Qualitätssicherung

- Repräsentative Seiten in 1920 px, 1366 px, Tablet- und Smartphone-Breite gerendert.
- Light und Dark Mode visuell geprüft.
- Keine horizontale Seitenüberbreite in den geprüften Ansichten.
- `mkdocs build --strict` erfolgreich ausgeführt.
