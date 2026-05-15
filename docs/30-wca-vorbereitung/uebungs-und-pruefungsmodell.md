# Übungs- und Prüfungsmodell

Dieser Kurs soll nicht nur erklären, sondern trainieren.

Dafür brauchen wir ein klares Modell für Übungen, Labs, Quizfragen, Modulprüfungen und PCAP-Challenges.

## Grundidee

Jedes Thema soll idealerweise vier Stufen bekommen:

```text
Erklären -> Üben -> Prüfen -> Anwenden
```

Beispiel TCP:

| Stufe | Inhalt |
|---|---|
| Erklären | TCP Handshake, Flags, Streams |
| Üben | Lab mit einfachem Webaufruf |
| Prüfen | Quizfragen zu SYN, SYN/ACK, ACK |
| Anwenden | PCAP-Challenge mit Verbindungsproblem |

## Übungstypen

### 1. Leseaufgaben

Ziel:

- Begriff verstehen
- Zusammenhang erkennen
- Merksatz aufnehmen

### 2. Bedienaufgaben

Ziel:

- Wireshark-Funktion nutzen
- Oberfläche kennenlernen
- Menüpunkte finden

Beispiel:

```text
Öffne Conversations und identifiziere den TCP Stream mit den meisten Bytes.
```

### 3. Filteraufgaben

Ziel:

- Display Filter anwenden
- passende Pakete isolieren
- Filter dokumentieren

Beispiel:

```text
Finde alle DNS-Antworten mit einem Response Code ungleich 0.
```

### 4. TShark-Aufgaben

Ziel:

- Analyse reproduzierbar machen
- Filter im Terminal anwenden
- Felder gezielt ausgeben

### 5. Analyseberichte

Ziel:

- Beobachtung und Bewertung trennen
- Frame-Nummern nennen
- Einschränkungen benennen
- nächsten Schritt formulieren

### 6. PCAP-Challenges

Ziel:

- unbekannten Capture analysieren
- mehrere Hinweise kombinieren
- Ergebnis sauber begründen

## Lab-Struktur

Jedes Lab soll möglichst gleich aufgebaut sein.

```text
labs/<track>/<lab-id>/
├── README.md
├── scenario.md
├── tasks.md
├── hints.md
├── solution.md
├── metadata.yml
├── check.py
└── files/
    └── capture.pcapng
```

## Lab-Metadaten

Jedes Lab bekommt eine maschinenlesbare `metadata.yml`.

Beispiel:

```yaml
id: lab-basic-030-dns-nxdomain
title: "DNS NXDOMAIN analysieren"
track: basic
level: foundation
estimated_time: 30m
wca_objectives:
  - dns
  - display-filters
  - packet-details
tools:
  - wireshark
  - tshark
  - dig
requires:
  - lab-foundation-001-first-capture
outputs:
  - analysis-report
  - quiz
```

## Quizmodell

Quizfragen sollen in YAML oder JSON abgelegt werden.

Geplante Struktur:

```text
quizzes/
├── questions/
│   ├── foundation.yml
│   ├── basic.yml
│   ├── advanced.yml
│   └── wca-practice.yml
├── exams/
│   ├── module-basic.yml
│   ├── module-advanced.yml
│   └── practice-exam-01.yml
└── objectives/
    └── wca-objectives.yml
```

## Fragetypen

Geplante Fragetypen:

| Typ | Zweck |
|---|---|
| single-choice | eine richtige Antwort |
| multiple-choice | mehrere richtige Antworten |
| true-false | schnelle Begriffsprüfung |
| matching | Begriffe zuordnen |
| ordering | Reihenfolge herstellen |
| filter-task | passenden Filter auswählen |
| pcap-question | Frage zu einem Capture beantworten |
| short-answer | kurze freie Antwort |
| report-task | Analysebericht schreiben |

## Beispiel: Single Choice

```yaml
id: q-basic-tcp-001
type: single-choice
objective: tcp-handshake
question: "Welche Paketfolge beschreibt einen erfolgreichen TCP 3-Way Handshake?"
answers:
  - text: "SYN, SYN/ACK, ACK"
    correct: true
  - text: "SYN, ACK, FIN"
    correct: false
  - text: "RST, SYN, ACK"
    correct: false
  - text: "ACK, SYN, SYN/ACK"
    correct: false
explanation: "Ein TCP-Verbindungsaufbau beginnt mit SYN, SYN/ACK und ACK."
references:
  - docs/10-basis-kurs/06-tcp-grundlagen.md
```

## Zwischenprüfungen

Zwischenprüfungen sollen pro Kursblock entstehen:

| Prüfung | Inhalt |
|---|---|
| Foundation Check | Umgebung, Oberfläche, TShark |
| Basis-Modulprüfung | Ethernet, ARP, IP, ICMP, UDP, DNS, DHCP, TCP-Grundlagen |
| Advanced-Modulprüfung | TCP Deep Dive, Performance, HTTP/TLS, Methodik, Security |
| WCA Practice 01 | gemischte prüfungsnahe Fragen |
| WCA Practice 02 | gemischte Fragen plus PCAP-Szenarien |

## Bewertung

Für Kurszwecke reicht eine einfache Bewertung.

| Ergebnis | Bewertung |
|---:|---|
| 90–100 % | sehr sicher |
| 80–89 % | prüfungsnah gut |
| 70–79 % | solide, Lücken prüfen |
| 60–69 % | Grundlagen wiederholen |
| unter 60 % | Thema erneut durcharbeiten |

Für PCAP-Challenges ist eine reine Prozentzahl oft zu schwach.

Dort sollte bewertet werden:

- richtige Beobachtungen
- passende Filter
- Frame-Nummern genannt
- Bewertung nachvollziehbar
- Einschränkungen benannt
- keine überzogenen Aussagen

## Lokale Fortschrittsspeicherung

Der Kurs soll ohne zentralen Server funktionieren.

Geplante lokale Speicherung:

```text
~/.local/share/wireshark-wca-de/progress.json
```

Spätere Alternative:

```text
~/.local/share/wireshark-wca-de/progress.sqlite
```

Beispielstruktur:

```json
{
  "course_version": "0.1.0",
  "attempts": [
    {
      "id": "module-basic",
      "timestamp": "2026-05-15T10:30:00+02:00",
      "score": 82,
      "passed": true,
      "objectives": ["dns", "tcp", "display-filters"]
    }
  ],
  "completed_labs": [
    "lab-foundation-001-first-capture",
    "lab-basic-030-dns-nxdomain"
  ]
}
```

## Geplantes CLI-Tool

Später kann ein kleines Tool `wwca` entstehen.

Beispielbefehle:

```bash
wwca progress
wwca quiz run basic
wwca lab check lab-basic-030-dns-nxdomain
wwca exam start practice-exam-01
wwca progress export ./mein-fortschritt.json
wwca progress import ./mein-fortschritt.json
```

Wichtig:

> Fortschritt bleibt lokal beim Lernenden. Kein zentraler Server ist nötig.

## Qualität von Quizfragen

Gute Fragen prüfen Verständnis.

Schlecht:

```text
Was ist DNS?
```

Besser:

```text
Ein Client fragt `app.example.local` ab und erhält NXDOMAIN.
Welche Aussage ist durch den Capture belegbar?
```

Gute Fragen sollten:

- realistische Situationen verwenden
- nicht künstlich tricksen
- eine klare Begründung enthalten
- auf Kurskapitel verweisen
- keine echten Prüfungsfragen kopieren
- nicht nur Definitionen abfragen
- WCA-Ziele abdecken

## Nächster praktischer Schritt

Nach diesem Konzept sollten wir als nächstes erstellen:

```text
labs/foundation/lab-foundation-001-first-capture/
labs/basic/lab-basic-010-display-filter/
labs/basic/lab-basic-020-dns-nxdomain/
quizzes/questions/foundation.yml
quizzes/questions/basic.yml
```

Damit beginnt der Kurs, von einer starken Dokumentation zu einem echten Trainingssystem zu werden.
