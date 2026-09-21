# Public-/Protected-Struktur

## Public

`mkdocs.public.yml` erzeugt `site-public/` mit Start, TRESOMAT, Web-Portal, Downloads und Release Notes. Der Build-Hook entfernt alle Dateien unter `docs/api/` und `docs/support/` vor Verarbeitung, sodass sie weder HTML noch Suchindex erreichen.

## Protected

`mkdocs.protected.yml` erzeugt `site-protected/` mit TRESOMAT Technik, Web-Portal Technik, Integration API, Support und technischen Downloads. Quellinhalte bleiben im gemeinsamen `docs/`-Baum.

## Sicherheit

Navigation oder CSS sind kein Zugriffsschutz. `techdocs.tresomat.ch` muss vor der statischen Site durch einen Access Gateway wie Cloudflare Access geschützt werden. Keine Benutzer, Passwörter, Tokens oder sonstigen Secrets im Repository speichern.
