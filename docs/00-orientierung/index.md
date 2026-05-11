# Orientierung

Willkommen im Kurs **Wireshark WCA DE**.

Dieser Kurs ist ein deutschsprachiger Open-Source-Selbstlernkurs für Netzwerkanalyse mit Wireshark. Er richtet sich an Lernende, die bereits grundlegende Netzwerkkenntnisse besitzen, aber Protokolle, Paketaufbau und systematische Trace-Analyse vertiefen möchten.

Der Kurs ist an den Lernzielen der **Wireshark Certified Analyst (WCA-101)** Zertifizierung ausgerichtet, ist aber kein offizieller Kurs der Wireshark Foundation.

!!! warning "Kein offizielles Zertifizierungsmaterial"
    Dieses Projekt enthält keine echten Prüfungsfragen, keine Exam Dumps und keine geschützten Zertifizierungsinhalte. Ziel ist der Aufbau echter Analysekompetenz.

## Was du in diesem Kurs lernst

Du lernst nicht nur, wo sich welche Schaltfläche in Wireshark befindet. Ziel ist, Netzwerkverkehr fachlich zu verstehen und Analyseergebnisse nachvollziehbar zu begründen.

Am Ende sollst du in der Lage sein:

- Paketmitschnitte sinnvoll zu erstellen und zu öffnen
- Wireshark-Profile, Spalten und Ansichten gezielt zu verwenden
- Capture-Filter und Anzeige-Filter (Display Filter) korrekt einzusetzen
- Ethernet, ARP, VLAN, IPv4, IPv6, ICMP, UDP, DNS, DHCP, TCP, HTTP und TLS in Captures zu erkennen
- TCP-Probleme wie Neuübertragungen (Retransmissions), Duplicate ACKs, Resets und Window-Probleme einzuordnen
- zwischen Netzwerkproblem, Clientproblem, Serverproblem und Applikationsproblem zu unterscheiden
- Analyseberichte zu schreiben, die für andere nachvollziehbar sind

## Wie der Kurs gedacht ist

Der Kurs ist als praktischer Lernpfad aufgebaut.

Jedes Thema besteht aus einer Mischung aus:

- Erklärung
- kleinen Beispielen
- praktischen Labs
- PCAP-Analyse
- Wiederholungsfragen
- optionalen Vertiefungsressourcen

Die Grundidee lautet:

> Erst verstehen, dann sehen, dann selbst analysieren.

## Empfohlene Reihenfolge

1. **Lern- und Übungsumgebung einrichten**  
   Ubuntu oder Pop!_OS, VSCode, Docker, Wireshark und TShark vorbereiten.

2. **Wireshark erster Kontakt**  
   Oberfläche, Profile, Spalten, erste Capture-Dateien und TShark kennenlernen.

3. **Basis-Kurs**  
   Protokollgrundlagen und einfache Fehlerbilder analysieren.

4. **Erweiterter Kurs**  
   TCP-Analyse, Performanceprobleme, HTTP/TLS und komplexere Troubleshooting-Fälle bearbeiten.

5. **WCA-Vorbereitung**  
   Lernzielmatrix, Wiederholungsfragen, Probeprüfungen und PCAP-Challenges durcharbeiten.

## Arbeitsweise im Repository

Das Repository enthält verschiedene Bereiche:

```text
README.md      Projektüberblick
docs/          Kursdokumentation
labs/          praktische Übungen
pcaps/         Capture-Dateien
docker/        reproduzierbare Lab-Umgebungen
quizzes/       Fragen und Zwischenprüfungen
tools/         Hilfswerkzeuge und lokale Fortschrittsspeicherung
```

Die Kurswebseite wird mit MkDocs Material gebaut. Lokal kannst du sie später mit folgendem Befehl starten:

```bash
mkdocs serve
```

## Aktueller Status

Der Kurs befindet sich im Aufbau. Inhalte, Labs, Prüfungen und Werkzeuge werden Schritt für Schritt ergänzt.

Wenn du mitarbeitest, beachte bitte:

- keine privaten PCAP-Dateien einchecken
- keine Zugangsdaten einchecken
- keine echten Zertifizierungsfragen verwenden
- externe Inhalte nur verlinken, wenn die Lizenzlage unklar ist
- alle Lerninhalte auf Deutsch schreiben
