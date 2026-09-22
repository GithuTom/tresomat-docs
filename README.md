# TRESOMAT Dokumentation

Eigenständiges, statisches Dokumentationsprojekt auf Basis von MkDocs Material.

## Lokal starten (Linux/macOS)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

## Lokal starten (Windows PowerShell)

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
mkdocs serve
```

Die Vorschau ist anschließend unter <http://127.0.0.1:8000> erreichbar.

## Prüfen und bauen

```powershell
mkdocs build --strict -f mkdocs.public.yml
python scripts/verify_role_build.py public site-public
mkdocs build --strict -f mkdocs.techdocs.yml
python scripts/verify_role_build.py techdocs site-techdocs
mkdocs build --strict -f mkdocs.api.yml
python scripts/verify_role_build.py api site-api
```

Die drei getrennten Ausgaben entstehen in `site-public/`, `site-techdocs/` und `site-api/`.
Die Prüfungen validieren Navigation, HTML-Ausgabe, Suchindex, lokale Links und Rollentrennung.
Build-Ordner und `.venv/` werden nicht versioniert.

## Medien und Downloads

- Bilder und animierte GIFs: `docs/assets/images/`
- Videos (MP4/WebM): `docs/assets/videos/`
- PDF-Downloads: `docs/assets/downloads/`

Binärdateien nicht als Base64 in Markdown einbetten.

## Veröffentlichung

Der GitHub-Actions-Workflow unter `.github/workflows/docs.yml` baut alle drei Varianten. Nur
Public wird auf GitHub Pages veröffentlicht; Techdocs und API werden als getrennte Artefakte
bereitgestellt. Details stehen in den drei `DEPLOYMENT_*.md`-Dokumenten.
