# Lab Foundation 001: First Capture

## Ziel

In diesem Lab erzeugst du deinen ersten eigenen Capture für den Kurs.

Du lernst, einen kleinen, kontrollierten Mitschnitt zu erstellen und anschließend mit Wireshark und TShark zu prüfen.

## Voraussetzungen

Du brauchst:

- Ubuntu oder Pop!_OS
- Wireshark
- TShark
- `curl`
- `dig`
- `ping`
- Netzwerkzugriff auf das Internet

Prüfen:

```bash
wireshark --version
tshark --version
curl --version
dig -v
ping -V
```

Falls `dig` fehlt:

```bash
sudo apt update
sudo apt install -y dnsutils
```

## Dateien

```text
README.md
scenario.md
tasks.md
hints.md
solution.md
metadata.yml
```

## Ergebnisdatei

Speichere deinen Capture lokal als:

```text
pcaps/generated/lab-foundation-001-first-capture.pcapng
```

Diese Datei wird lokal erzeugt und soll normalerweise nicht ins Repository committed werden.

## Geschätzte Dauer

```text
30 Minuten
```

## WCA-Bezug

Dieses Lab übt:

- Capture starten und stoppen
- Capture-Datei speichern und öffnen
- einfache Display Filter anwenden
- DNS, ICMP und TCP/TLS grob erkennen
- TShark für einfache Prüfungen verwenden
