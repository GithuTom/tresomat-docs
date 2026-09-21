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
python scripts/verify_public_build.py site-public
mkdocs build --strict -f mkdocs.protected.yml
```

Die öffentliche Ausgabe entsteht in `site-public/`, die geschützte technische Ausgabe in
`site-protected/`. Die zusätzliche Prüfung stellt sicher, dass die öffentliche Ausgabe keine
API- oder Support-Inhalte (einschließlich Suchindex) enthält. Build-Ordner und `.venv/` werden
nicht versioniert.

## Medien und Downloads

- Bilder und animierte GIFs: `docs/assets/images/`
- Videos (MP4/WebM): `docs/assets/videos/`
- PDF-Downloads: `docs/assets/downloads/`

Binärdateien nicht als Base64 in Markdown einbetten.

## Veröffentlichung

Der GitHub-Actions-Workflow unter `.github/workflows/docs.yml` baut beide Varianten. Nur die
öffentliche Ausgabe wird auf GitHub Pages veröffentlicht; die geschützte Ausgabe wird als
Workflow-Artefakt bereitgestellt. Details stehen in `DEPLOYMENT_PUBLIC.md` und
`DEPLOYMENT_PROTECTED.md`.
