# Paket 22: Erste PCAP-Challenge – DNS/HTTP Triage

Dieses Paket ergänzt den Kurs um den Bereich `60-pcap-challenges` und die erste prüfungsnahe PCAP-Challenge.

## Enthaltene Dateien

```text
mkdocs.yml
docs/60-pcap-challenges/index.md
docs/60-pcap-challenges/pcap-challenge-struktur.md
docs/60-pcap-challenges/challenge-001-dns-http-triage.md
pcaps/challenge/README.md
pcaps/challenge/.gitkeep
challenges/README.md
challenges/challenge-001-dns-http-triage/README.md
challenges/challenge-001-dns-http-triage/scenario.md
challenges/challenge-001-dns-http-triage/tasks.md
challenges/challenge-001-dns-http-triage/hints.md
challenges/challenge-001-dns-http-triage/solution.md
challenges/challenge-001-dns-http-triage/metadata.yml
challenges/challenge-001-dns-http-triage/check_tshark.sh
```

## Ziel

Mit diesem Paket bekommt der Kurs die erste Challenge-Struktur:

- klare Trennung zwischen Labs und Challenges
- prüfungsnahes Szenario
- gestufte Hinweise
- Musterlösung mit Frame-/Filter-Bezug
- TShark-Check-Skript
- Vorbereitung für spätere feste Challenge-PCAPs

Die erste Challenge nutzt bewusst das vorhandene Docker-DNS/HTTP-Lab, damit Lernende die PCAP lokal erzeugen können.
