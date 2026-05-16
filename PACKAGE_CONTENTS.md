# Paket 33: PCAP-Challenge – TCP Handshake und Reset

Dieses Paket ergänzt den Bereich `60-pcap-challenges` um eine zweite prüfungsnahe Challenge.

## Enthaltene Dateien

```text
mkdocs.yml
docs/60-pcap-challenges/index.md
docs/60-pcap-challenges/challenge-002-tcp-handshake-reset.md
challenges/challenge-002-tcp-handshake-reset/README.md
challenges/challenge-002-tcp-handshake-reset/scenario.md
challenges/challenge-002-tcp-handshake-reset/tasks.md
challenges/challenge-002-tcp-handshake-reset/hints.md
challenges/challenge-002-tcp-handshake-reset/solution.md
challenges/challenge-002-tcp-handshake-reset/metadata.yml
challenges/challenge-002-tcp-handshake-reset/check_tshark.sh
```

## Ziel

Mit dieser Challenge wird aus dem TCP-Handschlag-Lab eine prüfungsnahe Analyseaufgabe:

- erfolgreicher TCP 3-Way Handshake
- HTTP auf Port 80
- geschlossener TCP-Port
- RST/RST-ACK
- TCP Stream Isolation
- saubere Bewertung: erreichbar, abgelehnt, nicht automatisch Firewall
- kurze Triage mit Frame-Nummern

Die Challenge nutzt das vorhandene Docker-Lab `lab-basic-dns-http`.
