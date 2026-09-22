# Deployment Public

```bash
mkdocs build --strict -f mkdocs.public.yml
python scripts/verify_role_build.py public site-public
```

`site-public/` wird vom GitHub-Actions-Workflow auf GitHub Pages veröffentlicht. Vorgesehene Domain: `docs.tresomat.ch`. DNS und Custom-Domain-Zuordnung erfolgen getrennt; keine Zugangsdaten werden im Repository gespeichert.
