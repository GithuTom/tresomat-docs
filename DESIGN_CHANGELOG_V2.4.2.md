# TRESOMAT Docs V2.4.2 – Protected UI Cleanup

## Änderungen

- Primäre Navigation der geschützten Techdocs- und API-Seiten kompakter gesetzt, ohne die globale Schriftgröße zu reduzieren.
- Gruppenabstände und Abstände der Unterpunkte reduziert; Einzüge, aktive Markierung und einklappbare Gruppen bleiben erhalten.
- Scanning-Landingpage auf eine dezente Eyebrow „SCANNING“ bereinigt; H1 und Beschreibung bleiben unverändert.
- Alle von der Scanning-Landingpage verlinkten Barcode-Referenzen in den Techdocs-Build aufgenommen.
- Karten-CTAs verwenden ausschließlich relative, vom Gateway auflösbare Ziele.

## QA

- Strict-Build und Rollenprüfung für Techdocs und API erfolgreich.
- 15 Techdocs- und 4 API-Karten-CTAs automatisiert auf gültige Ziele geprüft.
- Keine `docs-content/`-Links und keine `href="#"`-Platzhalter in Karten-CTAs.
- Direkte geschützte URLs liefern angemeldet HTTP 200 und leiten unangemeldet zum Login weiter.
- Desktop, Tablet und Mobile in Light und Dark ohne horizontalen Überlauf geprüft.
- Authentifizierung, Sessions, Rollen, Passwortlogik und Public Docs nicht geändert.
