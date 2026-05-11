# Pop!_OS Hinweise

Pop!_OS ist eine Ubuntu-basierte Distribution und eignet sich gut als Lernsystem für diesen Kurs.

Die meisten Befehle aus dem Kurs funktionieren unter Pop!_OS genauso wie unter Ubuntu. Trotzdem gibt es ein paar Besonderheiten, die Lernende kennen sollten.

## Pop!_OS als unterstützte Variante

Der Kurs verwendet Ubuntu Desktop LTS als Referenzplattform. Pop!_OS wird als kompatible Variante betrachtet.

Das bedeutet:

- Paketverwaltung erfolgt ebenfalls über `apt`
- viele Ubuntu-Anleitungen funktionieren direkt
- Docker, Wireshark, Git, Python und VSCode lassen sich ähnlich installieren
- einzelne Desktop-Funktionen oder Menüs können anders aussehen

## Version prüfen

Zur Prüfung der Version:

```bash
cat /etc/os-release
```

Für Docker ist besonders interessant, ob ein Ubuntu-Codename vorhanden ist:

```bash
grep -E 'VERSION_CODENAME|UBUNTU_CODENAME' /etc/os-release
```

Bei Pop!_OS ist häufig `UBUNTU_CODENAME` relevant, weil Docker seine Paketquellen nach Ubuntu-Codenamen strukturiert.

## Terminal öffnen

Unter Pop!_OS kann das Terminal je nach Desktop-Version unterschiedlich heißen, zum Beispiel:

- Terminal
- Ptyxis
- GNOME Terminal
- COSMIC Terminal

In der Regel funktioniert:

```text
Strg + Alt + T
```

## App-Installation

Pop!_OS bietet zusätzlich zum Terminal einen grafischen App Store. Für den Kurs bevorzugen wir trotzdem die Installation über Terminalbefehle, weil sie reproduzierbarer ist.

## Wayland, X11 und Wireshark

Wireshark selbst funktioniert unabhängig davon, ob die Desktop-Sitzung Wayland oder X11 nutzt.

Für den Kurs ist nur wichtig:

- Wireshark soll lokal als GUI-Anwendung starten
- TShark und tcpdump sollen im Terminal funktionieren
- Docker-Container sollen nicht selbst die Wireshark-GUI starten müssen

Wir betreiben Wireshark also bewusst auf dem Host-System und nutzen Docker nur für reproduzierbare Lab-Dienste und Traffic-Erzeugung.

## Typische Unterschiede zu Ubuntu

Mögliche Unterschiede:

- andere Standardprogramme
- andere Systemeinstellungen-App
- anderer grafischer App Store
- andere Desktop-Tastenkombinationen
- andere vorinstallierte Pakete

Für die Kursarbeit sind diese Unterschiede normalerweise nicht kritisch.

## Zielzustand

Pop!_OS ist für den Kurs geeignet, wenn folgende Befehle erfolgreich laufen:

```bash
sudo apt update
git --version
python3 --version
```

Danach können die normalen Installationsschritte für Pakete, VSCode, Docker und Wireshark durchgeführt werden.
