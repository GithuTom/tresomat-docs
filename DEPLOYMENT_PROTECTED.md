# Deployment Protected

```bash
mkdocs build --strict -f mkdocs.protected.yml
```

Die Ausgabe `site-protected/` wird in CI validiert und als internes Artefakt gespeichert, aber nicht öffentlich veröffentlicht. Für `https://techdocs.tresomat.ch` ist ein vorgeschalteter Access Gateway vorgesehen, beispielsweise Cloudflare Access mit Gruppen für Support, Techniker, Integrationspartner und Entwickler.

MkDocs selbst implementiert keine Anmeldung und speichert keine Benutzer oder Secrets.
