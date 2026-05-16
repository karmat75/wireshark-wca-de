# Labs und Übungen

Dieser Bereich verbindet die Kursinhalte mit praktischer Arbeit.

Bis hierhin erklärt der Kurs viele Grundlagen. Die Labs sorgen dafür, dass daraus echte Analysefähigkeit wird.

## Ziel

Die Labs sollen helfen, dass du nicht nur weißt, was ein Filter bedeutet, sondern ihn in einem echten Capture sinnvoll einsetzen kannst.

Du sollst üben:

- Captures zu erzeugen
- Capture-Dateien zu öffnen
- relevante Pakete zu finden
- Display Filter einzusetzen
- TShark-Ausgaben zu verwenden
- Beobachtungen mit Frame-Nummern zu belegen
- Analyseergebnisse sauber zu formulieren

## Lab-Tracks

Die Labs sind in Tracks gegliedert.

| Track | Zweck |
|---|---|
| Foundation | Bedienung, Umgebung, erste Captures |
| Basic | Protokollgrundlagen und einfache Analysen |
| Advanced | TCP, Performance, HTTP/TLS, Methodik |
| WCA Practice | gemischte prüfungsnahe Aufgaben |

## Aktuelle Labs

| Lab | Track | Thema | Status |
|---|---|---|---|
| [Foundation Lab 001](foundation-first-capture.md) | Foundation | erster eigener Capture | verfügbar |
| [Basic Lab 020](basic-dns-http-docker.md) | Basic | Docker-Lab mit DNS, NXDOMAIN, HTTP und Wartezeit | verfügbar |
| [Basic Lab 030](basic-tcp-handshake-reset.md) | Basic | TCP Handshake, Stream, geschlossener Port und Reset | verfügbar |

## Arbeitsweise

Jedes Lab ist gleich aufgebaut:

1. Szenario lesen
2. Aufgaben bearbeiten
3. nur bei Bedarf Hinweise ansehen
4. eigene Beobachtungen notieren
5. Musterlösung prüfen
6. verwendete Filter dokumentieren

!!! tip "Nicht zu schnell in die Lösung schauen"
    Die Musterlösung ist nicht zum Abschreiben gedacht.  
    Erst selbst beobachten, dann vergleichen.

## Speicherorte

Lab-Beschreibungen liegen im Repository unter:

```text
labs/
```

Docker-Labs liegen unter:

```text
docker/compose/
```

Von MkDocs aus werden wichtige Labs zusätzlich unter `docs/40-labs-und-uebungen/` verlinkt.

Lokal erzeugte Captures sollen unterhalb von `pcaps/generated/` gespeichert werden.

```text
pcaps/generated/
```

Diese Dateien werden nicht ins Repository committed, weil sie lokal erzeugt sind und je nach Umgebung abweichen können.

## Warum Labs so wichtig sind

Für die WCA-Vorbereitung reicht Lesen allein nicht.

Du musst lernen, unbekannte Captures zu untersuchen.

Deshalb werden die Labs im weiteren Projektverlauf immer wichtiger als zusätzliche Theorie.
