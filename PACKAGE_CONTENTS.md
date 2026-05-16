# Paket 26: Basic Lab – TCP Handshake und Reset

Dieses Paket ergänzt den Lab-Bereich um ein weiteres praktisches TCP-Lab.

## Enthaltene Dateien

```text
mkdocs.yml
docs/40-labs-und-uebungen/index.md
docs/40-labs-und-uebungen/basic-tcp-handshake-reset.md
labs/basic/lab-basic-030-tcp-handshake-reset/README.md
labs/basic/lab-basic-030-tcp-handshake-reset/scenario.md
labs/basic/lab-basic-030-tcp-handshake-reset/tasks.md
labs/basic/lab-basic-030-tcp-handshake-reset/hints.md
labs/basic/lab-basic-030-tcp-handshake-reset/solution.md
labs/basic/lab-basic-030-tcp-handshake-reset/metadata.yml
labs/basic/lab-basic-030-tcp-handshake-reset/check_tshark.sh
```

## Ziel

Dieses Lab trainiert TCP-Grundlagen praktisch:

- erfolgreichen TCP 3-Way Handshake erkennen
- TCP Stream isolieren
- HTTP über TCP Port 80 einordnen
- geschlossenen TCP-Port erkennen
- RST/RST-ACK bewerten
- Unterschied zwischen Beobachtung und Ursache formulieren
- TShark-Auswertung mit Frame-Nummern verwenden

Das Lab verwendet das bereits vorhandene Docker-Lab `lab-basic-dns-http`.
