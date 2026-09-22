# Deployment API Login-Gateway

1. mkdocs build --strict -f mkdocs.api.yml ausführen.
2. Im Hostpoint Control Panel bisherigen Basic-Auth-Schutz für api.tresomat.ch deaktivieren.
3. Eigene config/users.php mit PASSWORD_DEFAULT-Hashes erstellen. Nicht mit der anderen Site teilen.
4. Inhalt von TRESOMAT_API_GATEWAY in den separaten Webroot von api.tresomat.ch hochladen.
5. DNS auf Hostpoint ausrichten und HTTPS aktivieren.
6. Login, direkte URL, Search Index, Download, Logout, Timeout und Session-Trennung testen.

Keine echten Zugangsdaten eintragen.
