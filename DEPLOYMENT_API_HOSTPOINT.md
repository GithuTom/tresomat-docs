# Deployment API-Dokumentation auf Hostpoint

```bash
mkdocs build --strict -f mkdocs.api.yml
python scripts/verify_role_build.py api site-api
```

Den **Inhalt** von `site-api/` in den eigenen Webroot von `api.tresomat.ch` hochladen (der konkrete Zielordner wird im Hostpoint Control Panel der Subdomain zugeordnet).

Im Hostpoint Control Panel für diesen Webroot einen eigenen Passwortschutz aktivieren und separate Benutzer ausschließlich für Integratoren und berechtigte Kunden anlegen. Keine Passwörter mit Techdocs teilen und keine echten Zugangsdaten dokumentieren. Den DNS-Eintrag der Subdomain auf das Hostpoint-Webhosting ausrichten.
