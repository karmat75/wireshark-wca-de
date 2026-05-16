# PCAP-Challenges

PCAP-Challenges sind prüfungsnahe Analyseaufgaben.

Im Unterschied zu normalen Labs bekommst du nicht jeden Schritt vorgegeben.

Du bekommst:

- ein Szenario
- eine Capture-Datei oder eine Anleitung zur Capture-Erzeugung
- konkrete Analysefragen
- Hinweise nur bei Bedarf
- eine Musterlösung
- optional einen TShark-Check

## Warum Challenges wichtig sind

Für die WCA-Vorbereitung reicht es nicht, nur Kapitel zu lesen oder einzelne Filter zu kennen.

Du musst unbekannte Captures untersuchen können.

PCAP-Challenges trainieren genau das:

- Orientierung im Capture
- relevante Pakete finden
- Filter auswählen
- Beobachtungen belegen
- Hypothesen prüfen
- Schlussfolgerungen sauber formulieren

## Unterschied zwischen Lab und Challenge

| Lab | Challenge |
|---|---|
| führt Schritt für Schritt | gibt mehr Eigenverantwortung |
| erklärt den Weg | prüft die Anwendung |
| oft stark angeleitet | eher szenariobasiert |
| gut zum Lernen | gut zum Prüfen |
| Lösung direkt nachvollziehbar | Lösung erst nach eigener Analyse prüfen |

## Aktuelle Challenges

| Challenge | Thema | Status |
|---|---|---|
| [Challenge 001: DNS/HTTP Triage](challenge-001-dns-http-triage.md) | DNS, NXDOMAIN, HTTP, Wartezeit | verfügbar |
| [Challenge 002: TCP Handshake/Reset](challenge-002-tcp-handshake-reset.md) | TCP 3-Way Handshake, HTTP, RST/RST-ACK | verfügbar |

## Arbeitsweise

Empfohlener Ablauf:

1. Szenario lesen
2. Capture öffnen oder erzeugen
3. keine Lösung lesen
4. zuerst grob orientieren
5. eigene Filter dokumentieren
6. relevante Frame-Nummern notieren
7. Kurzbericht schreiben
8. TShark-Check ausführen
9. Lösung vergleichen
10. eigene Lücken notieren

!!! tip "Prüfungsnah arbeiten"
    Beantworte nicht nur „was ist richtig?“, sondern auch:  
    „Welche Aussage ist durch den Capture wirklich belegbar?“

## Speicherorte

Challenge-Beschreibungen:

```text
challenges/
```

Challenge-PCAPs, wenn sie später fest eingecheckt werden:

```text
pcaps/challenge/
```

Lokal erzeugte Captures:

```text
pcaps/generated/
```

## Datenschutz

PCAP-Challenges dürfen keine produktiven oder personenbezogenen Daten enthalten.

Für diesen Kurs bevorzugen wir:

- synthetische Captures
- Docker-Lab-Captures
- selbst erzeugte Captures
- öffentliche Captures mit klarer Lizenz
