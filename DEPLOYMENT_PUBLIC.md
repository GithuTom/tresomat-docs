# Deployment Public

```bash
mkdocs build --strict -f mkdocs.public.yml
python scripts/verify_public_build.py site-public
```

Der GitHub-Pages-Workflow veröffentlicht ausschließlich `site-public/`. Das Hosting muss alte Dateien beim Deployment vollständig ersetzen, damit frühere `/api/`- und `/support/`-Routen anschließend 404 liefern.

Später kann dieselbe Ausgabe unter `https://docs.tresomat.ch` bereitgestellt werden.
