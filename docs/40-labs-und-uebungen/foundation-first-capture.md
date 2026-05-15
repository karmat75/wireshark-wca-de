# Foundation Lab 001: First Capture

Dieses Lab ist der erste praktische Schritt.

Du erzeugst einen kleinen eigenen Capture, öffnest ihn in Wireshark und prüfst ihn mit TShark.

## Lab-Pfad

```text
labs/foundation/lab-foundation-001-first-capture/
```

## Ziel

Du übst:

- Wireshark oder TShark für einen einfachen Mitschnitt zu verwenden
- gezielt Test-Traffic zu erzeugen
- eine Capture-Datei zu speichern
- die Datei wieder zu öffnen
- einfache Display Filter anzuwenden
- erste Beobachtungen zu dokumentieren

## Voraussetzungen

Du brauchst:

- Wireshark
- TShark
- `curl`
- `dig`
- `ping`
- funktionierende Netzwerkverbindung

Falls `dig` fehlt:

```bash
sudo apt install -y dnsutils
```

## Kurzablauf

1. Capture starten
2. DNS-, ICMP- und HTTPS-Traffic erzeugen
3. Capture stoppen
4. Datei speichern
5. in Wireshark öffnen
6. mit Display Filtern prüfen
7. mit TShark gegenprüfen
8. Beobachtungen notieren

## Verweis auf Lab-Dateien

Die vollständigen Lab-Dateien liegen unter:

```text
labs/foundation/lab-foundation-001-first-capture/
```

Dort findest du:

- Szenario
- Aufgaben
- Hinweise
- Musterlösung
- Metadaten

## Erwartetes Ergebnis

Am Ende solltest du eine lokale Datei haben:

```text
pcaps/generated/lab-foundation-001-first-capture.pcapng
```

Diese Datei ist lokal erzeugt und sollte normalerweise nicht committed werden.

## WCA-Bezug

Dieses Lab trainiert grundlegende WCA-nahe Fähigkeiten:

- Capture-Datei erstellen
- Capture-Datei öffnen
- einfache Display Filter verwenden
- Paketliste, Paketdetails und Zeitbezug nutzen
- TShark für reproduzierbare Prüfung verwenden
