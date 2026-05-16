# Paket 32: Advanced Lab – Security Basics

Dieses Paket ergänzt den Lab-Bereich um ein defensives Security-Basics-Lab.

## Enthaltene Dateien

```text
mkdocs.yml
docs/40-labs-und-uebungen/index.md
docs/40-labs-und-uebungen/advanced-security-basics.md
docker/compose/lab-advanced-security-basics/README.md
docker/compose/lab-advanced-security-basics/compose.yml
docker/compose/lab-advanced-security-basics/web-security/Dockerfile
docker/compose/lab-advanced-security-basics/web-security/app.py
labs/advanced/lab-advanced-040-security-basics/README.md
labs/advanced/lab-advanced-040-security-basics/scenario.md
labs/advanced/lab-advanced-040-security-basics/tasks.md
labs/advanced/lab-advanced-040-security-basics/hints.md
labs/advanced/lab-advanced-040-security-basics/solution.md
labs/advanced/lab-advanced-040-security-basics/metadata.yml
labs/advanced/lab-advanced-040-security-basics/check_tshark.sh
```

## Ziel

Dieses Lab trainiert defensive Security-Analyse mit Wireshark:

- HTTP Basic Auth im Klartext erkennen
- Formularwerte im HTTP-Body erkennen
- regelmäßige Beacon-ähnliche Requests einordnen
- Host-Header, User-Agent und URIs auswerten
- zwischen Beobachtung und Bewertung unterscheiden
- keine produktiven oder echten Zugangsdaten verwenden
- TShark-Felder für HTTP-Security-Triage nutzen

Das Lab erzeugt ein eigenes Docker-Netz `172.28.80.0/24`.

Alle Zugangsdaten und Tokens sind bewusst synthetische Lab-Werte.
