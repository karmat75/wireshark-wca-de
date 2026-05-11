# Lern- und Übungsumgebung

In diesem Abschnitt richtest du die Umgebung ein, mit der du den Kurs bearbeiten kannst.

Die Referenzplattform ist ein Ubuntu-basiertes Desktop-System.

Empfohlen:

- Ubuntu Desktop LTS
- Pop!_OS als kompatible Ubuntu-basierte Variante

## Ziel dieses Abschnitts

Nach Abschluss dieses Abschnitts soll deine Umgebung Folgendes können:

- VSCode öffnen und das Repository bearbeiten
- Docker-Container starten
- Wireshark lokal ausführen
- Paketmitschnitte ohne Root-Rechte erstellen
- TShark im Terminal nutzen
- tcpdump im Terminal nutzen
- MkDocs lokal bauen und starten
- erste Labs vorbereiten

## Geplante Werkzeuge

Die Lernumgebung nutzt bewusst Werkzeuge, die auch im Alltag von Admins und Operations-Teams nützlich sind.

| Werkzeug | Zweck im Kurs |
|---|---|
| Ubuntu oder Pop!_OS | Lernsystem |
| VSCode | Editor und Arbeitsoberfläche |
| Git | Versionsverwaltung |
| Docker | reproduzierbare Lab-Umgebungen |
| Wireshark | grafische Paket- und Protokollanalyse |
| TShark | automatisierte Analyse im Terminal |
| tcpdump | Paketmitschnitt im Terminal |
| Python | Prüfskripte und Hilfswerkzeuge |
| MkDocs | Kursdokumentation lokal anzeigen |

## Warum Linux als Basis?

Linux ist für diesen Kurs besonders gut geeignet, weil viele Netzwerk- und Analysewerkzeuge direkt verfügbar sind.

Vorteile:

- gute Paketverfügbarkeit
- native Nutzung von tcpdump, TShark und Docker
- einfache Automatisierung mit Bash und Python
- gute Unterstützung in VSCode
- gute Eignung für reproduzierbare Labs

## Reihenfolge der Einrichtung

Die Einrichtung soll später Schritt für Schritt dokumentiert werden.

Geplante Reihenfolge:

1. Betriebssystem installieren
2. System aktualisieren
3. Basispakete installieren
4. Git einrichten
5. VSCode installieren
6. Docker installieren
7. Wireshark installieren
8. Benutzerrechte für Captures konfigurieren
9. TShark und tcpdump testen
10. Repository klonen
11. Python-Umgebung für MkDocs einrichten
12. Kurs lokal bauen
13. erstes Demo-Lab starten

## Aktueller Minimaltest

Für den aktuellen Projektstand reicht dieser Test:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
mkdocs build
mkdocs serve
```

Danach sollte die Kursseite lokal erreichbar sein:

```text
http://127.0.0.1:8000
```

## Pop!_OS-Hinweis

Pop!_OS basiert auf Ubuntu und eignet sich grundsätzlich gut für den Kurs.

Je nach Version können einzelne Paketnamen, Desktop-Funktionen oder Installationswege leicht abweichen. Solche Unterschiede werden später in eigenen Hinweisen dokumentiert.

## Nächste Seiten in diesem Abschnitt

Geplant sind unter anderem:

- Ubuntu installieren
- Pop!_OS Hinweise
- benötigte Pakete installieren
- VSCode einrichten
- Docker installieren
- Wireshark installieren
- Umgebung prüfen

Diese Seiten werden im weiteren Projektverlauf ergänzt.
