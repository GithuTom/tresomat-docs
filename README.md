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

```bash
mkdocs build --strict
```

Das Ergebnis wird im Ordner `site/` erzeugt. `site/` und `.venv/` werden nicht versioniert.

## Medien und Downloads

- Bilder und animierte GIFs: `docs/assets/images/`
- Videos (MP4/WebM): `docs/assets/videos/`
- PDF-Downloads: `docs/assets/downloads/`

Binärdateien nicht als Base64 in Markdown einbetten.

## Veröffentlichung

Ein manueller GitHub-Pages-Workflow liegt unter `.github/workflows/docs.yml`. Er wird nur über
„Run workflow“ gestartet. Für Cloudflare Pages kann `mkdocs build --strict` als Build-Befehl und
`site` als Ausgabeverzeichnis verwendet werden. DNS-Konfiguration ist nicht Bestandteil dieses Projekts.
