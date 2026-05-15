# Prüfungsstrategie

Die WCA-101 prüft nicht nur, ob du Wireshark schon einmal geöffnet hast.

Die Prüfung zielt auf praktische Analysefähigkeit:

- wichtige Wireshark-Funktionen nutzen
- Captures sinnvoll erstellen und auswerten
- Filter korrekt anwenden
- Protokolle und Headerfelder erkennen
- TCP-Verhalten verstehen
- typische Netzwerk- und Anwendungsprobleme eingrenzen

## Vor der Prüfung offizielle Informationen prüfen

Prüfungsdetails können sich ändern.

Prüfe vor der Anmeldung immer die offiziellen Informationen:

- offizielle WCA-Seite
- offizielles WCA-101 Exam Objectives PDF
- Preis
- Zeit
- Anzahl und Typen der Fragen
- technische Anforderungen für Online-Proctoring
- Regeln zu Wiederholungsversuchen

Dieser Kurs kann darauf vorbereiten, ersetzt aber nicht den Blick in die offiziellen Prüfungsinformationen.

## Grundprinzip

> Trainiere nicht Fragen. Trainiere Fähigkeiten.

Die WCA ist besonders dann gut vorbereitet, wenn du mit unbekannten Captures arbeiten kannst.

Du solltest nicht nur wissen:

```text
tcp.flags.syn == 1
```

Sondern auch:

```text
Was bedeutet dieses SYN im Ablauf?
Was müsste danach kommen?
Was bedeutet es, wenn nichts kommt?
Welche alternativen Ursachen gibt es?
Wo wurde mitgeschnitten?
```

## Lernphasen

### Phase 1: Fundament

Ziel:

- Kurs lesen
- Begriffe verstehen
- Oberfläche bedienen
- Filter ausprobieren
- erste Captures öffnen

Kapitel:

- Lernumgebung
- Linux-Grundlagen
- Wireshark erster Kontakt
- Basis-Kurs

### Phase 2: Analysefähigkeit

Ziel:

- Streams isolieren
- Zeitverhalten lesen
- TCP-Hinweise bewerten
- DNS/HTTP/TLS sauber trennen
- Analyseberichte schreiben

Kapitel:

- TCP Deep Dive
- Performanceanalyse
- HTTP und TLS
- Fehleranalyse-Methodik
- Security-Basics

### Phase 3: Prüfungsnahe Wiederholung

Ziel:

- Lernzielmatrix prüfen
- Lücken schließen
- Labs bearbeiten
- Quizfragen wiederholen
- PCAP-Challenges lösen
- Probeprüfung unter Zeitdruck durchführen

## Was du sicher können solltest

### Wireshark-Funktionen

Du solltest sicher umgehen können mit:

- Datei öffnen und speichern
- pcap und pcapng grob unterscheiden
- Packet List, Packet Details und Packet Bytes
- Profile
- Spalten
- Zeitdarstellung
- Name Resolution
- Conversations
- Endpoints
- Protocol Hierarchy
- I/O Graphs
- Follow TCP/UDP Stream
- Expert Information
- Find Packet
- Capture File Properties

### Filter

Du solltest sicher sein bei:

- Protokollfiltern
- IP-Filtern
- Port-Filtern
- MAC-Filtern
- logischen Operatoren
- Negation
- Klammern
- Display Filter vs. Capture Filter
- Filter aus Paketdetails erzeugen
- Filtern aus Conversations/Endpoints
- generierten Feldern

### TCP

TCP ist besonders wichtig.

Du solltest sicher sein bei:

- 3-Way Handshake
- FIN und RST
- Sequence Number
- ACK Number
- Window Size
- Window Scaling
- MSS
- SACK
- Duplicate ACK
- Retransmission
- Fast Retransmit
- Zero Window
- Stream Graphs
- iRTT / RTT-Grundverständnis

## Prüfungsnahe Denkweise

Viele Fragen werden wahrscheinlich nicht nur Definitionen abfragen, sondern Zusammenhänge.

Beispielhafte Denkmuster:

```text
Ich sehe SYN, aber kein SYN/ACK.
Welche Aussagen sind belegbar?
```

```text
Ich sehe HTTP 500.
Ist das ein Netzwerkproblem?
```

```text
Ich sehe DNS NXDOMAIN.
Was bedeutet das wirklich?
```

```text
Ich sehe Previous Segment Not Captured.
Ist damit Paketverlust bewiesen?
```

## Gute Antwortstrategie

Bei Szenarien:

1. Was wird gefragt?
2. Welche Schicht ist betroffen?
3. Welche Beobachtung ist gegeben?
4. Welche Aussage ist dadurch wirklich belegbar?
5. Welche Antwort geht zu weit?
6. Welche Antwort verwechselt Symptom und Ursache?
7. Welche Antwort ignoriert den Capture-Punkt?

AHA:

> In Analysefragen ist oft die vorsichtigere, besser belegbare Antwort die richtige.

## Typische Prüfungsfallen

| Falle | Bessere Haltung |
|---|---|
| rote Wireshark-Zeile automatisch als Fehler werten | Kontext prüfen |
| Ping als vollständigen Netzwerktest sehen | nur ICMP wurde geprüft |
| HTTP 500 als Netzwerkfehler sehen | Anwendung hat geantwortet |
| No DNS Traffic als kein DNS interpretieren | Cache, DoH, DoT, Capture-Punkt prüfen |
| Retransmission als eindeutigen Netzwerkverlust sehen | Capture-Qualität und ACKs prüfen |
| VLAN-Tags erwarten, obwohl Access-Port genutzt wird | Capture-Punkt beachten |
| RST immer als Fehler sehen | aktiver Abbruch, Kontext prüfen |

## Empfohlener Trainingsplan

### Woche 1: Foundation

- Lernumgebung prüfen
- erster Capture
- Oberfläche
- Profile
- TShark
- OSI-Referenz

### Woche 2: Basis-Protokolle

- Ethernet, ARP, VLAN
- IPv4, IPv6, ICMP
- UDP, DNS, DHCP
- Display Filter üben

### Woche 3: TCP

- TCP-Grundlagen
- TCP Deep Dive
- TCP Streams
- Sequence und ACK
- Retransmissions
- Window-Themen

### Woche 4: Analyse und Prüfung

- Performanceanalyse
- HTTP/TLS
- Fehleranalyse-Methodik
- Security-Basics
- WCA-Matrix prüfen
- Probeprüfung

## Mindest-Reife vor der Prüfung

Du solltest dich erst anmelden, wenn du:

- unbekannte PCAPs strukturiert öffnen kannst
- Conversations und Endpoints nutzen kannst
- TCP Streams sicher isolierst
- DNS Query/Response sicher interpretierst
- TCP Handshake, RST und FIN sicher erkennst
- TCP Retransmissions und Duplicate ACKs einordnen kannst
- I/O Graphs und Zeitdarstellung einsetzen kannst
- TShark für einfache Auswertungen nutzt
- Analyseberichte mit Frame-Nummern schreiben kannst
- die Lernzielmatrix größtenteils auf „Trainiert“ oder „Prüfungsnah“ hast

## Merksatz

> Die beste WCA-Vorbereitung ist nicht, Wireshark auswendig zu lernen.  
> Die beste Vorbereitung ist, unbekannte Captures methodisch zu untersuchen.
