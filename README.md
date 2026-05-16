# Wireshark WCA DE

Deutschsprachiger Open-Source-Selbstlernkurs für Netzwerkanalyse mit Wireshark, ausgerichtet an den Lernzielen der **Wireshark Certified Analyst (WCA-101)** Zertifizierung.

> Dieses Projekt ist kein offizieller Kurs der Wireshark Foundation und enthält keine Prüfungsfragen, Exam Dumps oder geschützten Zertifizierungsinhalte. Ziel ist der Aufbau echter Analysekompetenz mit Wireshark, TShark und reproduzierbaren Laborübungen.

---

## Ziel des Projekts

Dieses Repository soll einen frei verfügbaren, deutschsprachigen Lernpfad für Netzwerkanalyse mit Wireshark bereitstellen.

Der Kurs richtet sich an Menschen, die bereits erste Kenntnisse im Bereich Netzwerke besitzen, zum Beispiel:

- IP-Adressen und Subnetze
- VLANs
- Verkabelung und Switches
- grundlegende Netzwerkarchitektur
- einfache Fehlersuche im Netzwerkbetrieb

Der Kurs setzt jedoch nicht voraus, dass bereits tiefes Wissen zu Netzwerkprotokollen, Paketaufbau oder TCP/IP-Analyse vorhanden ist.

Ziel ist es, Schritt für Schritt von der Lernumgebung bis zur fortgeschrittenen Paket- und Protokollanalyse zu kommen.

---

## Was dieser Kurs vermitteln soll

Nach Abschluss des Kurses sollen Lernende in der Lage sein:

- Wireshark sicher zu bedienen
- Netzwerkverkehr sinnvoll mitzuschneiden
- Capture- und Display-Filter korrekt einzusetzen
- Ethernet, ARP, IPv4, IPv6, ICMP, UDP, DNS, DHCP, TCP, HTTP und TLS in Captures zu erkennen
- typische Fehlerbilder in Paketmitschnitten zu analysieren
- TCP-Probleme wie Retransmissions, Duplicate ACKs, Window-Probleme und Resets zu bewerten
- zwischen Netzwerk-, Server-, Client- und Applikationsproblemen zu unterscheiden
- Analyseergebnisse nachvollziehbar zu dokumentieren
- sich strukturiert auf die WCA-101-Zertifizierung vorzubereiten

---

## Zielgruppe

Der Kurs ist besonders geeignet für:

- Netzwerkadministratorinnen und Netzwerkadministratoren
- Systemadministratorinnen und Systemadministratoren
- IT-Support und IT-Operations
- Monitoring- und Infrastruktur-Teams
- Auszubildende und Quereinsteiger mit Netzwerkgrundlagen
- Menschen, die sich auf die WCA-101 vorbereiten möchten

Der Kurs ist nicht als offensives Security-Training gedacht. Security-nahe Themen werden ausschließlich aus Sicht der defensiven Analyse und Fehlersuche behandelt.

---

## Referenzplattform

Die primäre Lern- und Übungsumgebung basiert auf Linux.

Geplant und empfohlen:

- Ubuntu Desktop LTS
- Pop!_OS als kompatible Ubuntu-basierte Variante
- VSCode
- Docker
- Wireshark
- TShark
- tcpdump
- Python
- Git

Andere Betriebssysteme können funktionieren, werden aber nicht als primärer Lernpfad dokumentiert.

---

## Geplanter Kursaufbau

Der Kurs ist in mehrere Bereiche unterteilt.

### 1. Lern- und Übungsumgebung

- Ubuntu oder Pop!_OS installieren
- grundlegende Werkzeuge installieren
- VSCode einrichten
- Docker installieren
- Wireshark installieren
- TShark und tcpdump testen
- erstes Lab ausführen
- erste Capture-Datei öffnen

### 2. Basis-Kurs

Der Basis-Kurs vermittelt die Grundlagen der Netzwerkanalyse mit Wireshark.

Themen:

- Wireshark-Oberfläche
- Capture-Dateien
- Capture Filter
- Display Filter
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

Der erweiterte Kurs vertieft die Analyse echter Fehlerbilder.

Themen:

- TCP Deep Dive
- Retransmissions
- Duplicate ACKs
- SACK
- Window Size
- Window Scaling
- Zero Window
- Resets
- Latenz
- Paketverlust
- Performanceanalyse
- HTTP
- TLS
- DNS-Fehleranalyse
- Applikationsprobleme
- Analyseberichte

### 4. WCA-Vorbereitung

Dieser Abschnitt orientiert sich an den Lernzielen der WCA-101-Zertifizierung.

Inhalte:

- Lernzielmatrix
- Wiederholungsfragen
- praktische PCAP-Challenges
- Zwischenprüfungen
- Probeprüfungen
- Prüfungsstrategie
- typische Denkfehler
- Analyse unter Zeitdruck

---

## Repository-Struktur

Die geplante Struktur des Repositories:

```text
.
├── README.md
├── LICENSE
├── AGENTS.md
├── mkdocs.yml
├── docs/
│   ├── index.md
│   ├── 00-orientierung/
│   ├── 01-lern-und-uebungsumgebung/
│   ├── 02-linux-grundlagen-fuer-den-kurs/
│   ├── 03-wireshark-erster-kontakt/
│   ├── 10-basis-kurs/
│   ├── 20-advanced-kurs/
│   ├── 30-wca-vorbereitung/
│   └── 90-referenz/
├── labs/
│   ├── foundation/
│   ├── basic/
│   ├── advanced/
│   └── wca-practice/
├── pcaps/
│   ├── generated/
│   ├── challenge/
│   └── external/
├── docker/
│   ├── compose/
│   ├── images/
│   └── traffic-generators/
├── quizzes/
│   ├── questions/
│   ├── exams/
│   └── objectives/
├── tools/
│   ├── wwca
│   ├── check-lab
│   └── export-progress
├── .devcontainer/
│   └── devcontainer.json
└── .github/
    ├── workflows/
    └── ISSUE_TEMPLATE/
```

---

## Geplante Lab-Struktur

Jede Übung soll möglichst gleich aufgebaut sein.

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

---

## Lokale Fortschrittsspeicherung

Der Kurs soll ohne zentralen Server funktionieren.

Geplant ist eine lokale Fortschrittsspeicherung auf dem System der lernenden Person.

Mögliche Funktionen:

```bash
wwca progress
wwca quiz run basic-030
wwca lab check lab-basic-030-dns-nxdomain
wwca exam start wca-practice-01
wwca progress export ./mein-fortschritt.json
wwca progress import ./mein-fortschritt.json
```

Die Ergebnisse sollen lokal gespeichert und exportierbar sein.

Geplante Speicherorte:

```text
~/.local/share/wireshark-wca-de/progress.json
```

oder später:

```text
~/.local/share/wireshark-wca-de/progress.sqlite
```

---

## Externe Ressourcen

Der Kurs soll auf gute externe Ressourcen verweisen, diese aber nicht ungeprüft kopieren.

Geplante Ressourcentypen:

- offizielle Wireshark-Dokumentation
- Wireshark User Guide
- Wireshark Display Filter Reference
- TShark Manual Page
- SharkFest-Videos
- frei verfügbare Artikel
- öffentlich nutzbare PCAP-Sammlungen
- ergänzende TCP/IP-Lernmaterialien

Jede Lektion soll möglichst passende Querverweise enthalten.

---

## Umgang mit PCAP-Dateien

Paketmitschnitte können sensible Informationen enthalten.

Deshalb gelten für dieses Repository folgende Regeln:

- keine privaten oder produktiven Captures veröffentlichen
- keine echten Zugangsdaten veröffentlichen
- keine Kundendaten veröffentlichen
- keine personenbezogenen Daten veröffentlichen
- bevorzugt selbst erzeugte Captures verwenden
- externe Captures nur bei klarer Lizenzlage aufnehmen
- externe Captures ansonsten nur verlinken

---

## Status

Dieses Projekt befindet sich im Aufbau.

---

## Maintainer-Checkliste (Qualitaet absichern)

Fuer Maintainer und Admins dieses Repositories:

1. CI-Workflow `Quality Checks` ist aktiv und laeuft bei Pull Requests.
2. Unter `Settings -> Branches` ist eine Protection-Regel fuer `main` gesetzt.
3. `Require a pull request before merging` ist aktiv.
4. `Require status checks to pass before merging` ist aktiv.
5. Als Pflichtcheck ist `Quality Checks / quality` gesetzt.
6. (Optional) `Require branches to be up to date before merging` ist aktiv.

Fuer Contributor lokal empfohlen:

```bash
bash tools/quality/install_git_hooks.sh
```

Damit laufen die Repository-Checks automatisch vor jedem Commit.

Details siehe `CONTRIBUTING.md` und `tools/quality/README.md`.

Geplante erste Meilensteine:

### Milestone 0.1: Foundation MVP

- Grundstruktur des Repositories
- README
- AGENTS.md
- Lizenzstruktur
- MkDocs-Grundgerüst
- Setup-Kapitel für Ubuntu/Pop!_OS
- Installation der benötigten Werkzeuge
- erstes Demo-Lab
- erstes Quiz
- lokale Fortschrittsspeicherung als Konzept

### Milestone 0.2: Basis-Kurs

- Wireshark-Grundlagen
- Capture- und Display-Filter
- Ethernet und ARP
- IPv4 und ICMP
- DNS und DHCP
- TCP-Grundlagen
- erste Modulprüfung

### Milestone 0.3: Advanced/WCA

- TCP Deep Dive
- Performanceanalyse
- HTTP und TLS
- Troubleshooting-Szenarien
- WCA-Lernzielmatrix
- Probeprüfung

---

## Schnellstart für Mitwirkende

Repository klonen:

```bash
git clone https://github.com/karmat75/wireshark-wca-de.git
cd wireshark-wca-de
```

Projekt in VSCode öffnen:

```bash
code .
```

Optional mit DevContainer öffnen, sobald die DevContainer-Konfiguration vorhanden ist.

Lokale Dokumentation starten:

```bash
mkdocs serve
```

Build prüfen:

```bash
mkdocs build
```

---

## Mitwirken

Beiträge sind willkommen.

Mögliche Beiträge:

- Korrekturen an Texten
- neue Labs
- neue Quizfragen
- neue PCAPs mit sauberer Lizenz
- Verbesserungen an Docker-Labs
- bessere Erklärungen
- Diagramme
- WCA-Lernzielzuordnung
- technische Prüfskripte
- Übersetzungen und sprachliche Verbesserungen

Bitte beachte:

- keine echten Prüfungsfragen
- keine Exam Dumps
- keine privaten Captures
- keine Zugangsdaten
- keine urheberrechtlich problematischen Inhalte

---

## Schreibstil

Der Kurs soll auf Deutsch geschrieben sein.

Technische Fachbegriffe dürfen zusätzlich mit dem englischen Begriff ergänzt werden.

Beispiele:

- Anzeige-Filter (Display Filter)
- Mitschnitt (Capture)
- Neuübertragung (Retransmission)
- Zeitüberschreitung (Timeout)
- Paketverlust (Packet Loss)
- Rundlaufzeit (Round Trip Time / RTT)

Der Stil soll klar, praktisch und nachvollziehbar sein.

Ziel ist nicht, möglichst akademisch zu klingen, sondern echte Analysefähigkeit aufzubauen.

---

## Lizenz

Dieses Repository verwendet eine gemischte Lizenzierung:

- Inhalte (Dokumentation, Labs, Quiztexte, Aufgaben, Loesungen): **CC BY 4.0**
- Code und Skripte (Python, Bash, Tooling): **MIT**
- Selbst erzeugte PCAPs: **CC BY 4.0**, sofern keine sensiblen Inhalte enthalten sind

Massgeblich ist die Zuordnung in der Datei `LICENSE`.

Wichtige Hinweise:

- Fremdmaterial bleibt unter der jeweiligen Originallizenz.
- Inhalte mit unklarer Lizenz werden nicht uebernommen, sondern nur verlinkt.
- Marken, Produktnamen und Logos (z. B. Wireshark) sind nicht durch diese Lizenz freigegeben.

---

## Haftungsausschluss

Dieses Projekt dient ausschließlich zu Lern- und Ausbildungszwecken.

Die Nutzung von Wireshark und anderen Analysewerkzeugen darf nur in Netzwerken erfolgen, in denen eine entsprechende Berechtigung vorliegt.

Paketmitschnitte können sensible oder personenbezogene Daten enthalten. Lernende und Mitwirkende sind selbst dafür verantwortlich, rechtliche, organisatorische und datenschutzrechtliche Vorgaben einzuhalten.

---

## Kein offizielles Wireshark-Projekt

Dieses Repository ist ein unabhängiges Open-Source-Projekt.

Es ist nicht offiziell mit der Wireshark Foundation verbunden und ersetzt keine offiziellen Schulungs- oder Zertifizierungsunterlagen.

Wireshark ist ein eingetragenes oder verwendetes Markenzeichen der jeweiligen Rechteinhaber.