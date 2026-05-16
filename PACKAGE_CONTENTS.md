# Paket 35: PCAP-Challenge – HTTP/TLS Triage

Dieses Paket ergänzt den Bereich `60-pcap-challenges` um eine vierte prüfungsnahe Challenge.

## Enthaltene Dateien

```text
mkdocs.yml
docs/60-pcap-challenges/index.md
docs/60-pcap-challenges/challenge-004-http-tls-triage.md
challenges/challenge-004-http-tls-triage/README.md
challenges/challenge-004-http-tls-triage/scenario.md
challenges/challenge-004-http-tls-triage/tasks.md
challenges/challenge-004-http-tls-triage/hints.md
challenges/challenge-004-http-tls-triage/solution.md
challenges/challenge-004-http-tls-triage/metadata.yml
challenges/challenge-004-http-tls-triage/check_tshark.sh
```

## Ziel

Diese Challenge prüft HTTP-/TLS-Analyse prüfungsnah:

- HTTP im Klartext erkennen
- HTTPS/TLS von HTTP unterscheiden
- TLS Client Hello finden
- SNI auswerten
- ALPN prüfen
- TLS Alerts einordnen
- TLS Application Data erkennen
- sauber formulieren, was sichtbar ist und was nicht
- Triage mit Frame-Nummern schreiben

Die Challenge nutzt das vorhandene Docker-Lab `lab-advanced-http-tls`.
