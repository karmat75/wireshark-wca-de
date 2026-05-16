# Advanced-Quiz

Das Advanced-Quiz wiederholt die Inhalte aus dem erweiterten Kurs.

## Datei

```text
quizzes/questions/advanced.yml
```

## Aktueller Umfang

```text
20 Fragen
```

## Themen

- TCP Deep Dive
- Retransmissions
- Duplicate ACKs
- Previous Segment Not Captured
- SACK
- Zero Window
- Performanceanalyse
- DNS-, TCP-, TLS- und Anwendungszeit
- HTTP und TLS
- SNI, ALPN und TLS Alerts
- Fehleranalyse-Methodik
- Security-Basics

## Nutzung

```bash
python3 tools/wwca/wwca.py quiz run advanced
```

Mit zufälliger Reihenfolge:

```bash
python3 tools/wwca/wwca.py quiz run advanced --shuffle
```

Nur zehn Fragen:

```bash
python3 tools/wwca/wwca.py quiz run advanced --limit 10 --shuffle
```

## Ziel

Das Advanced-Quiz prüft weniger reine Begriffe und stärker die Einordnung:

- Was ist wirklich im Capture belegbar?
- Welche Beobachtung ist nur ein Hinweis?
- Wo entstehen typische Fehlinterpretationen?
- Welche Zusatzinformation wäre nötig?
