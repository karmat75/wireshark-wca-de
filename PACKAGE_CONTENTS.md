# Paket 30: Advanced Lab – HTTP und TLS

Dieses Paket ergänzt den Lab-Bereich um ein Advanced-Lab zu HTTP und TLS.

## Enthaltene Dateien

```text
mkdocs.yml
docs/40-labs-und-uebungen/index.md
docs/40-labs-und-uebungen/advanced-http-tls.md
docker/compose/lab-advanced-http-tls/README.md
docker/compose/lab-advanced-http-tls/compose.yml
docker/compose/lab-advanced-http-tls/web-tls/Dockerfile
docker/compose/lab-advanced-http-tls/web-tls/entrypoint.sh
docker/compose/lab-advanced-http-tls/web-tls/nginx.conf
docker/compose/lab-advanced-http-tls/web-tls/index.html
labs/advanced/lab-advanced-020-http-tls/README.md
labs/advanced/lab-advanced-020-http-tls/scenario.md
labs/advanced/lab-advanced-020-http-tls/tasks.md
labs/advanced/lab-advanced-020-http-tls/hints.md
labs/advanced/lab-advanced-020-http-tls/solution.md
labs/advanced/lab-advanced-020-http-tls/metadata.yml
labs/advanced/lab-advanced-020-http-tls/check_tshark.sh
```

## Ziel

Dieses Lab trainiert HTTP- und TLS-Analyse praktisch:

- HTTP im Klartext erkennen
- HTTPS/TLS-Verkehr erkennen
- verstehen, was bei TLS noch sichtbar ist
- SNI im TLS Client Hello finden
- ALPN-Felder suchen
- TLS Alert durch Zertifikatsfehler provozieren
- HTTP Request/Response von TLS Application Data unterscheiden
- TShark-Auswertung für HTTP und TLS verwenden
- sichere und vorsichtige Analyseformulierungen üben

Das Lab erzeugt ein eigenes Docker-Netz `172.28.70.0/24`.
