# PCAP-Challenge-Struktur

Alle PCAP-Challenges sollen einheitlich aufgebaut sein.

## Standardstruktur

```text
challenges/challenge-001-dns-http-triage/
├── README.md
├── scenario.md
├── tasks.md
├── hints.md
├── solution.md
├── metadata.yml
└── check_tshark.sh
```

Optional später:

```text
files/
└── challenge.pcapng
```

oder:

```text
pcaps/challenge/challenge-001-dns-http-triage.pcapng
```

## Dateien

| Datei | Zweck |
|---|---|
| `README.md` | Einstieg und Ablauf |
| `scenario.md` | prüfungsnahe Ausgangslage |
| `tasks.md` | Analysefragen |
| `hints.md` | gestufte Hinweise |
| `solution.md` | Musterlösung |
| `metadata.yml` | maschinenlesbare Informationen |
| `check_tshark.sh` | einfacher TShark-Check |

## Challenge-ID

Format:

```text
challenge-<nummer>-<kurzer-name>
```

Beispiele:

```text
challenge-001-dns-http-triage
challenge-002-tcp-handshake-reset
challenge-003-slow-http-response
challenge-004-tls-alert
challenge-005-dhcp-no-offer
```

## Metadaten

Beispiel:

```yaml
id: challenge-001-dns-http-triage
title: "DNS/HTTP Triage"
level: basic
estimated_time: 45m
pcap:
  mode: generated
  path: pcaps/generated/challenge-001-dns-http-triage.pcapng
wca_objectives:
  - dns
  - display-filters
  - http
  - tshark
```

## Bewertung

Eine Challenge sollte nicht nur prüfen, ob eine Antwort stimmt.

Bewertet werden:

- passende Filter
- relevante Frames
- richtige Beobachtungen
- vorsichtige Bewertung
- genannte Einschränkungen
- keine überzogenen Aussagen

## Gestufte Hinweise

Hinweise sollen helfen, ohne direkt die Lösung zu verraten.

Beispiel:

```text
Hinweis 1:
Beginne mit DNS.

Hinweis 2:
Prüfe DNS Response Codes.

Hinweis 3:
NXDOMAIN ist ein wichtiger Hinweis.
```

## TShark-Check

Ein TShark-Check soll nicht die komplette Analyse ersetzen.

Er prüft nur, ob bestimmte erwartete Muster im Capture vorhanden sind.

Beispiele:

- DNS Query vorhanden
- NXDOMAIN vorhanden
- HTTP Response vorhanden
- bestimmter Hostname sichtbar
- erwartete Ziel-IP sichtbar

Ein TShark-Check ist also ein technischer Plausibilitätscheck, keine vollständige Bewertung.
