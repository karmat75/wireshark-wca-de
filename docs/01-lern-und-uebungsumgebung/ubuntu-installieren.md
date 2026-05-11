# Ubuntu installieren

Diese Seite beschreibt die empfohlene Grundinstallation für Lernende, die mit Ubuntu Desktop arbeiten möchten.

Der Kurs ist nicht als allgemeiner Linux-Kurs gedacht. Trotzdem soll die Installation so dokumentiert sein, dass Lernende eine stabile Arbeitsumgebung erhalten und nicht schon an Betriebssystemdetails scheitern.

## Empfohlene Basis

Empfohlen wird eine aktuelle Ubuntu Desktop LTS-Version.

Für den Kurs ist wichtig:

- grafische Desktop-Umgebung vorhanden
- Terminal verfügbar
- Internetzugang vorhanden
- ausreichend Speicherplatz für Docker-Images und PCAP-Dateien
- Benutzerkonto mit `sudo`-Berechtigung

## Empfohlene Ressourcen

Für eine VM oder ein dediziertes Lernsystem sind sinnvoll:

| Ressource | Empfehlung |
|---|---:|
| CPU | 2 bis 4 Kerne |
| RAM | mindestens 8 GB, besser 16 GB |
| Speicher | mindestens 40 GB, besser 80 GB |
| Netzwerk | NAT oder Bridge, je nach Lab |

Für einfache Labs reichen 8 GB RAM meistens aus. Wenn mehrere Docker-Container, Browser, VSCode und Wireshark parallel laufen, sind 16 GB deutlich angenehmer.

## Installation

Die Ubuntu-Installation selbst folgt dem normalen grafischen Installer.

Empfohlene Entscheidungen:

- Sprache: Deutsch oder Englisch, je nach Vorliebe
- Tastaturlayout: passend zur eigenen Tastatur
- Benutzerkonto: normaler Benutzer mit Administratorrechten
- Updates während der Installation: aktivieren, wenn Internet verfügbar ist
- Drittanbieter-Treiber: aktivieren, wenn das System spezielle WLAN- oder Grafiktreiber benötigt

## Verschlüsselung

Für ein echtes Lernsystem ist Festplattenverschlüsselung sinnvoll, aber nicht zwingend.

Empfehlung:

- Laptop: Verschlüsselung aktivieren
- VM für Lab-Zwecke: Verschlüsselung optional
- Wegwerf-Testsystem: Verschlüsselung optional

## Nach der Installation

Nach dem ersten Login sollte das System aktualisiert werden:

```bash
sudo apt update
sudo apt upgrade -y
```

Danach einmal neu starten:

```bash
sudo reboot
```

## Erster Orientierungstest

Nach dem Neustart Terminal öffnen:

```text
Strg + Alt + T
```

Dann prüfen:

```bash
whoami
hostnamectl
lsb_release -a
```

Wenn `lsb_release` nicht vorhanden ist:

```bash
cat /etc/os-release
```

## Zielzustand

Die Lernumgebung ist für die nächsten Schritte bereit, wenn:

- der Benutzer sich anmelden kann
- `sudo` funktioniert
- Internetzugang vorhanden ist
- `apt update` erfolgreich läuft
- ein Terminal geöffnet werden kann
