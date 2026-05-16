# Paket 37: PCAP-Challenge – Performance Triage

Dieses Paket ergänzt den Bereich `60-pcap-challenges` um eine sechste prüfungsnahe Challenge.

## Enthaltene Dateien

```text
mkdocs.yml
docs/60-pcap-challenges/index.md
docs/60-pcap-challenges/challenge-006-performance-triage.md
challenges/challenge-006-performance-triage/README.md
challenges/challenge-006-performance-triage/scenario.md
challenges/challenge-006-performance-triage/tasks.md
challenges/challenge-006-performance-triage/hints.md
challenges/challenge-006-performance-triage/solution.md
challenges/challenge-006-performance-triage/metadata.yml
challenges/challenge-006-performance-triage/check_tshark.sh
```

## Ziel

Diese Challenge prüft Performanceanalyse prüfungsnah:

- schnellen und langsamen Webserver vergleichen
- DNS-Zeit, TCP-Zeit und HTTP Request/Response-Zeit trennen
- Conversations und Protocol Hierarchy nutzen
- Time Display und Frame-Zeitpunkte auswerten
- Wartezeit sauber lokalisieren
- nicht vorschnell „Netzwerk langsam“ behaupten
- Triage mit Frame-Nummern schreiben

Die Challenge nutzt das vorhandene Docker-Lab `lab-basic-dns-http`.
