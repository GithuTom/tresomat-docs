# Rollentrennung V2.3

Alle 234 Markdown-Quelldateien bleiben im Repository. Die Build-Allowlist entscheidet ausschließlich über Navigation, HTML-Ausgabe und Suchindex.

| Bereich | Public | Techdocs | API |
|---|:---:|:---:|:---:|
| Startseite | JA | JA | JA |
| TRESOMAT Frontend – Bedienung | JA | NEIN | NEIN |
| TRESOMAT Frontend – Scanner-/Zahlungsdiagnose | NEIN | JA | NEIN |
| TRESOMAT Backend – Stammdaten/Verkauf | JA | JA | NEIN |
| TRESOMAT Backend – Datenbanken/Messenger/Hardware | NEIN | JA | NEIN |
| Installation – Voraussetzungen/Installation/Update | JA | JA | NEIN |
| Installation – Konfiguration/Wartung/Fehlerbehebung | NEIN | JA | NEIN |
| Web-Portal Kundenbereich | JA | NEIN | NEIN |
| Web-Portal Admin/Support | NEIN | JA | NEIN |
| Integration API | NEIN | NEIN | JA |
| Support (ohne API-Supportseite) | NEIN | JA | NEIN |
| Öffentliche Handbücher | JA | JA | NEIN |
| Integration API Manual | NEIN | NEIN | JA |
| TRESOMAT-/Web-Portal-Release-Notes | JA | JA | NEIN |
| Integration-API-Release-Notes | NEIN | NEIN | JA |

Die beiden fachlich leeren, rollenübergreifenden Platzhalter `support/integration-api.md` und
`tresomat/installation-und-betrieb/integration-api-konfigurieren.md` bleiben als Quellen erhalten,
werden aber in keinen rollenfremden Build aufgenommen.
