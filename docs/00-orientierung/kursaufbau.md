# Kursaufbau

Der Kurs ist in mehrere Lernbereiche aufgeteilt. Jeder Bereich baut auf dem vorherigen auf.

## Lernpfade

Der Kurs besteht aus vier großen Lernpfaden.

### 1. Lern- und Übungsumgebung

In diesem Abschnitt richtest du deine Arbeitsumgebung ein.

Geplante Inhalte:

- Ubuntu oder Pop!_OS installieren
- System aktualisieren
- benötigte Pakete installieren
- VSCode einrichten
- Docker installieren
- Wireshark installieren
- TShark und tcpdump testen
- erstes Demo-Lab ausführen

### 2. Basis-Kurs

Der Basis-Kurs vermittelt die Grundlagen der Netzwerkanalyse mit Wireshark.

Geplante Inhalte:

- Wireshark-Oberfläche
- Capture-Dateien
- Capture Filter
- Anzeige-Filter (Display Filter)
- Ethernet
- ARP
- VLAN-Grundlagen
- IPv4
- IPv6
- ICMP
- UDP
- DNS
- DHCP
- TCP-Grundlagen

### 3. Erweiterter Kurs

Der erweiterte Kurs behandelt komplexere Analyse- und Troubleshooting-Situationen.

Geplante Inhalte:

- TCP Deep Dive
- Retransmissions
- Duplicate ACKs
- SACK
- Window Size
- Window Scaling
- Zero Window
- Resets
- Round Trip Time
- Paketverlust
- Latenz
- HTTP
- TLS
- Performanceanalyse
- Fehleranalyse-Methodik

### 4. WCA-Vorbereitung

Dieser Abschnitt dient der strukturierten Wiederholung und Prüfungsvorbereitung.

Geplante Inhalte:

- Lernzielmatrix
- Wiederholungsfragen
- Zwischenprüfungen
- PCAP-Challenges
- Probeprüfungen
- Prüfungsstrategie
- typische Denkfehler

## Aufbau einer Lektion

Eine typische Lektion soll möglichst gleich aufgebaut sein:

1. **Ziel**  
   Was soll nach der Lektion verstanden oder beherrscht werden?

2. **Einordnung**  
   Warum ist das Thema in der Netzwerkanalyse relevant?

3. **Grundlagen**  
   Die wichtigsten Konzepte werden erklärt.

4. **Beispiel**  
   Das Thema wird an einem kleinen Beispiel gezeigt.

5. **Übung oder Lab**  
   Lernende wenden das Thema selbst an.

6. **WCA-Bezug**  
   Die Lektion wird grob den passenden WCA-Lernzielen zugeordnet.

7. **Weiterführende Ressourcen**  
   Offizielle Dokumentation, Artikel oder Videos werden verlinkt.

## Aufbau eines Labs

Ein Lab soll eine konkrete Analyseaufgabe beschreiben.

Geplante Struktur:

```text
labs/basic/lab-basic-030-dns-nxdomain/
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

Jedes Lab soll enthalten:

- Ziel
- Voraussetzungen
- Szenario
- Aufgaben
- Hinweise
- Musterlösung
- WCA-Bezug
- weiterführende Ressourcen
- optional automatisierte Prüfung

## Lernprinzip

Der Kurs folgt einem einfachen Prinzip:

```text
Erklären → Zeigen → Selbst analysieren → Begründen → Prüfen
```

Wireshark wird dabei nicht als Selbstzweck behandelt. Jede Funktion soll mit einer praktischen Analysefrage verbunden werden.

Beispiel:

Nicht nur:

> Nutze `Statistics > Conversations`.

Sondern:

> Nutze `Statistics > Conversations`, um herauszufinden, welche Verbindung im Capture den größten Datenanteil verursacht.

## Basis-Kurs und erweiterter Kurs

Der Basis-Kurs soll solide Grundlagen vermitteln. Der erweiterte Kurs soll echte Analysefähigkeit aufbauen.

Der Übergang ist bewusst sichtbar getrennt:

- **Basis-Kurs:** verstehen, erkennen, einfache Fehlerbilder
- **Erweiterter Kurs:** bewerten, vergleichen, begründen, Troubleshooting

Dadurch können Lernende den Kurs abschnittsweise nutzen.

## Empfohlene Lerngeschwindigkeit

Für den späteren vollständigen Kurs ist grob geplant:

- Foundation und Setup: 3 bis 5 Stunden
- Basis-Kurs: 15 bis 25 Stunden
- Erweiterter Kurs: 25 bis 40 Stunden
- WCA-Vorbereitung: 10 bis 20 Stunden

Diese Angaben sind nur Orientierung. Praktische Analyse braucht Zeit und Wiederholung.
