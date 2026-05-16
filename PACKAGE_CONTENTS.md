# Paket 34: PCAP-Challenge – TCP Retransmission Triage

Dieses Paket ergänzt den Bereich `60-pcap-challenges` um eine dritte prüfungsnahe Challenge.

## Enthaltene Dateien

```text
mkdocs.yml
docs/60-pcap-challenges/index.md
docs/60-pcap-challenges/challenge-003-tcp-retransmission-triage.md
challenges/challenge-003-tcp-retransmission-triage/README.md
challenges/challenge-003-tcp-retransmission-triage/scenario.md
challenges/challenge-003-tcp-retransmission-triage/tasks.md
challenges/challenge-003-tcp-retransmission-triage/hints.md
challenges/challenge-003-tcp-retransmission-triage/solution.md
challenges/challenge-003-tcp-retransmission-triage/metadata.yml
challenges/challenge-003-tcp-retransmission-triage/check_tshark.sh
```

## Ziel

Diese Challenge prüft Advanced-TCP-Analyse prüfungsnah:

- TCP Stream finden
- Download-Verbindung identifizieren
- Retransmissions erkennen
- Duplicate ACKs einordnen
- Fast Retransmit erkennen
- Wireshark-Analysefelder vorsichtig bewerten
- Capture-Punkt und Belegbarkeit berücksichtigen
- kurze Triage mit Frame-Nummern schreiben

Die Challenge nutzt das vorhandene Docker-Lab `lab-advanced-tcp-loss`.
