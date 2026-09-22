# Deployment Techdocs auf Hostpoint

```bash
mkdocs build --strict -f mkdocs.techdocs.yml
python scripts/verify_role_build.py techdocs site-techdocs
```

Den **Inhalt** von `site-techdocs/` in den eigenen Webroot von `techdocs.tresomat.ch` hochladen (der konkrete Zielordner wird im Hostpoint Control Panel der Subdomain zugeordnet).

Im Hostpoint Control Panel für diesen Webroot einen eigenen Passwortschutz aktivieren und separate Benutzer ausschließlich für Techniker und Service anlegen. Keine Passwörter mit der API-Site teilen und keine echten Zugangsdaten dokumentieren. Den DNS-Eintrag der Subdomain auf das Hostpoint-Webhosting ausrichten.
