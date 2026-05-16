# Paket 36: PCAP-Challenge – Security Basics Triage

Dieses Paket ergänzt den Bereich `60-pcap-challenges` um eine fünfte prüfungsnahe Challenge.

## Enthaltene Dateien

```text
mkdocs.yml
docs/60-pcap-challenges/index.md
docs/60-pcap-challenges/challenge-005-security-basics-triage.md
challenges/challenge-005-security-basics-triage/README.md
challenges/challenge-005-security-basics-triage/scenario.md
challenges/challenge-005-security-basics-triage/tasks.md
challenges/challenge-005-security-basics-triage/hints.md
challenges/challenge-005-security-basics-triage/solution.md
challenges/challenge-005-security-basics-triage/metadata.yml
challenges/challenge-005-security-basics-triage/check_tshark.sh
```

## Ziel

Diese Challenge prüft defensive Security-Triage mit Wireshark:

- HTTP-Klartext erkennen
- Basic Auth Header finden
- Formularwerte und synthetische Tokens im HTTP Body erkennen
- Beacon-ähnliche Requests einordnen
- User-Agent und URI auswerten
- Follow TCP Stream bewusst einsetzen
- Schutzbedarf echter Captures benennen
- nicht vorschnell Malware behaupten
- Triage mit Frame-Nummern schreiben

Die Challenge nutzt das vorhandene Docker-Lab `lab-advanced-security-basics`.

Alle Werte sind synthetische Lab-Werte.
