# Lern- und Übungsumgebung

In diesem Abschnitt richten wir die technische Grundlage für den Kurs ein.

Ziel ist eine Umgebung, in der Lernende zuverlässig mit Wireshark, TShark, Docker, VSCode und den Kursdateien arbeiten können. Die Umgebung soll nachvollziehbar, reproduzierbar und möglichst nah an einer realistischen Arbeitsumgebung sein.

## Warum dieser Abschnitt wichtig ist

Netzwerkanalyse ist praktische Arbeit. Man lernt sie nicht nur durch Lesen, sondern durch Beobachten, Filtern, Vergleichen und Begründen.

Dafür brauchen wir eine Umgebung, in der alle Lernenden ungefähr dieselben Voraussetzungen haben:

- ein Linux-basiertes Desktop-System
- ein Terminal
- VSCode als Arbeitsumgebung
- Git für das Kurs-Repository
- Wireshark für die grafische Analyse
- TShark und tcpdump für die Kommandozeile
- Docker für reproduzierbare Labs
- Python für Prüfskripte und spätere lokale Fortschrittsspeicherung

## Referenzplattform

Die Referenzplattform für diesen Kurs ist:

- Ubuntu Desktop LTS
- Pop!_OS als kompatible Ubuntu-basierte Variante

Andere Systeme können funktionieren, sind aber nicht der primäre Lernpfad.

## Ablauf

1. Ubuntu oder Pop!_OS installieren
2. Betriebssystem aktualisieren
3. benötigte Pakete installieren
4. VSCode einrichten
5. Docker installieren
6. Wireshark installieren
7. Umgebung prüfen
8. erstes Repository lokal öffnen und bauen

## Ergebnis dieses Abschnitts

Am Ende dieses Abschnitts sollte die lernende Person folgende Befehle erfolgreich ausführen können:

```bash
code --version
git --version
docker version
docker compose version
wireshark --version
tshark --version
tcpdump --version
mkdocs build
```

Außerdem sollte die Kursdokumentation lokal mit MkDocs gestartet werden können:

```bash
source .venv/bin/activate
mkdocs serve
```

Danach kann die lokale Kursseite im Browser geöffnet werden:

```text
http://127.0.0.1:8000
```
