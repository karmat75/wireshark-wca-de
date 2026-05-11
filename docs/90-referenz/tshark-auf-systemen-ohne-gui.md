# TShark auf Systemen ohne GUI

TShark ist die Terminal-Variante von Wireshark.

Das ist nicht nur ein nettes Zusatzwerkzeug. Für echte Netzwerkanalyse ist TShark besonders wichtig, wenn du auf Systemen arbeitest, auf denen keine grafische Oberfläche vorhanden ist.

Typische Beispiele:

- Ubuntu Server
- virtuelle Maschinen ohne Desktop
- Container-Hosts
- Appliances
- Jump Hosts
- Testsysteme im Rechenzentrum
- Server, auf denen du nur per SSH arbeitest

!!! important "AHA!"
    Wireshark ist die grafische Oberfläche.  
    TShark ist die gleiche Analysewelt im Terminal.  
    Wer TShark installieren und bedienen kann, ist nicht auf einen Desktop angewiesen.

## Warum das prüfungs- und praxisrelevant ist

In der Praxis bekommst du nicht immer ein System mit Desktop, Maus und Wireshark-GUI.

Oft sieht die Realität so aus:

```text
ssh admin@server
```

Dann musst du trotzdem in der Lage sein:

- TShark zu installieren
- eine vorhandene Capture-Datei zu lesen
- Live-Traffic mitzuschneiden
- relevante Pakete zu filtern
- einzelne Felder auszugeben
- Ergebnisse reproduzierbar zu dokumentieren

Für die WCA-Vorbereitung ist das wichtig, weil die Prüfung nicht nur grafische Bedienung abfragt. Sie prüft auch Verständnis für Capture-Methoden, Kommandozeilenwerkzeuge, Filter, Capture-Dateien und Analyseabläufe.

## TShark installieren: Desktop-System

Auf einem Ubuntu- oder Pop!_OS-Desktop ist häufig Wireshark bereits das Hauptpaket, das du installierst.

```bash
sudo apt update
sudo apt install -y wireshark tshark
```

Prüfen:

```bash
wireshark --version
tshark --version
```

Wenn du die GUI nicht brauchst, reicht TShark allein.

## TShark installieren: System ohne GUI

Auf einem Server ohne grafische Oberfläche installierst du nicht die Wireshark-GUI, sondern nur TShark.

```bash
sudo apt update
sudo apt install -y tshark
```

Prüfen:

```bash
tshark --version
```

Interfaces anzeigen:

```bash
tshark -D
```

Eine vorhandene Capture-Datei lesen:

```bash
tshark -r capture.pcapng
```

!!! note "Analyse vorhandener PCAPs braucht keine Capture-Rechte"
    Um eine vorhandene Capture-Datei mit `tshark -r` zu lesen, brauchst du normalerweise keine besonderen Netzwerkrechte.  
    Live-Capturing ist etwas anderes. Dafür werden zusätzliche Rechte benötigt.

## Installation ohne empfohlene Zusatzpakete

Auf sehr kleinen Systemen möchtest du manchmal möglichst wenig zusätzliche Pakete installieren.

Dann kannst du versuchen:

```bash
sudo apt install -y --no-install-recommends tshark
```

Danach unbedingt prüfen:

```bash
tshark --version
tshark -D
```

Wenn Funktionen fehlen, installiere ohne `--no-install-recommends` erneut.

Für Lernsysteme ist die normale Installation meistens besser.

## Neuere Version über Wireshark-PPA

Die Ubuntu-Paketquellen enthalten nicht immer die neueste stabile Wireshark-Version.

Wenn du bewusst eine aktuellere stabile Version verwenden möchtest, kannst du das Wireshark Stable PPA verwenden.

```bash
sudo apt update
sudo apt install -y software-properties-common
sudo add-apt-repository ppa:wireshark-dev/stable
sudo apt update
sudo apt install -y tshark
```

Version prüfen:

```bash
tshark --version
apt policy tshark
```

!!! warning "PPA bewusst einsetzen"
    Ein PPA ist eine zusätzliche Paketquelle. Das kann sinnvoll sein, wenn du eine neuere Version brauchst.  
    Auf produktiven Systemen sollte das aber bewusst entschieden und dokumentiert werden.

## Live-Capture-Rechte verstehen

TShark kann zwei unterschiedliche Dinge tun:

| Aktion | Beispiel | Besondere Rechte nötig? |
|---|---|---|
| vorhandene Datei lesen | `tshark -r capture.pcapng` | normalerweise nein |
| live mitschneiden | `tshark -i eth0` | ja |

Live-Capturing greift auf Netzwerkinterfaces zu.

Dafür sind erhöhte Rechte nötig.

Wir starten TShark aber nicht dauerhaft als `root`. Besser ist eine saubere Rechtevergabe über die Wireshark-Konfiguration und die Gruppe `wireshark`.

## Capture-Rechte auf Debian/Ubuntu-Systemen setzen

Bei der Installation kann eine Frage erscheinen, ob normale Benutzer Pakete mitschneiden dürfen.

Wenn du das nachträglich ändern möchtest:

```bash
sudo dpkg-reconfigure wireshark-common
```

Wähle aus, dass Nicht-Root-Benutzer Pakete erfassen dürfen.

Danach den Benutzer zur Gruppe `wireshark` hinzufügen:

```bash
sudo usermod -aG wireshark "$USER"
```

Danach einmal abmelden und wieder anmelden.

Prüfen:

```bash
groups
```

Die Gruppe `wireshark` sollte sichtbar sein.

## Soforttest nach neuer Gruppenmitgliedschaft

Nach einer neuen Gruppenmitgliedschaft reicht ein neues Terminal oft nicht aus.

Am zuverlässigsten ist:

1. abmelden
2. anmelden
3. Terminal öffnen
4. prüfen

```bash
groups
tshark -D
```

Wenn du nicht abmelden möchtest, kann für Tests manchmal helfen:

```bash
newgrp wireshark
```

Für den Kurs ist Ab- und Anmelden aber verständlicher.

## Live-Capture testen

Interfaces anzeigen:

```bash
tshark -D
```

Kurzen Mitschnitt erzeugen:

```bash
tshark -i any -c 10
```

Bedeutung:

| Option | Bedeutung |
|---|---|
| `-i any` | auf allen Interfaces mitschneiden |
| `-c 10` | nach 10 Paketen stoppen |

Auf einem System mit wenig Traffic kannst du parallel Traffic erzeugen:

```bash
ping -c 4 example.org
```

## In Datei schreiben

```bash
mkdir -p pcaps/generated
tshark -i any -c 50 -w pcaps/generated/server-test.pcapng
```

Danach lesen:

```bash
tshark -r pcaps/generated/server-test.pcapng
```

Oder auf ein anderes System kopieren und dort mit Wireshark öffnen.

## Typische Fehlerbilder

### `tshark: There are no interfaces on which a capture can be done`

Mögliche Ursachen:

- fehlende Berechtigungen
- Benutzer ist nicht in der Gruppe `wireshark`
- neue Gruppenmitgliedschaft ist noch nicht aktiv
- System läuft in einem Container oder einer Umgebung ohne passende Capabilities

Prüfen:

```bash
groups
tshark -D
dumpcap -D
```

### `Permission denied`

Nicht sofort `sudo` davor schreiben.

Erst prüfen:

```bash
groups
getcap "$(command -v dumpcap)"
```

Wenn die Wireshark-Konfiguration nicht passt:

```bash
sudo dpkg-reconfigure wireshark-common
sudo usermod -aG wireshark "$USER"
```

Dann abmelden und wieder anmelden.

### `tshark: command not found`

TShark ist nicht installiert oder nicht im Pfad.

Prüfen:

```bash
command -v tshark
```

Installieren:

```bash
sudo apt update
sudo apt install -y tshark
```

## Nicht jedes Problem mit `sudo` lösen

Dieser Befehl funktioniert oft:

```bash
sudo tshark -i any
```

Aber er ist nicht unser Standardweg.

Warum?

- TShark läuft dann mit vollen Root-Rechten.
- Fehler können mehr Schaden anrichten.
- Es widerspricht dem Kursprinzip: normale Arbeit mit normalen Rechten, erhöhte Rechte nur gezielt.
- Es verdeckt das eigentliche Rechteproblem.

Besser:

```bash
sudo dpkg-reconfigure wireshark-common
sudo usermod -aG wireshark "$USER"
```

Dann abmelden, anmelden und ohne `sudo` testen:

```bash
tshark -D
tshark -i any -c 10
```

## Air-Gap und Systeme ohne direkten Internetzugang

In manchen Umgebungen hat der Zielserver keinen direkten Zugriff auf Paketquellen.

Dann gibt es mehrere Wege:

- interne Paketmirror
- Repository-Proxy
- vorbereitete `.deb`-Pakete für genau diese Ubuntu-Version
- Installationsmedium mit passenden Paketen
- separater Staging-Host mit gleicher Ubuntu-Version

Wichtig:

> `.deb`-Pakete müssen zur Distribution und Version passen. Ein Paket von einem anderen Ubuntu-Release kann funktionieren, muss aber nicht.

Für den Kurs ist der bevorzugte Weg:

1. normales apt-Repository oder interner Mirror
2. bei Bedarf Wireshark Stable PPA auf Lernsystemen
3. manuelle Offline-Pakete nur als fortgeschrittener Sonderfall

## Merksatz

> Wenn du TShark auf einem Headless-System installieren, Captures lesen und kurze Live-Mitschnitte erzeugen kannst, bist du nicht mehr von der Wireshark-GUI abhängig.

## Offizielle Referenzen

- [TShark Manual Page](https://www.wireshark.org/docs/man-pages/tshark.html)
- [Wireshark User's Guide: Installing from debs under Debian, Ubuntu and other Debian derivatives](https://www.wireshark.org/docs/wsug_html/#ChBuildInstallUnixInstallBins)
- [Wireshark Download Page](https://www.wireshark.org/download.html)
- [Wireshark Manual Pages](https://www.wireshark.org/docs/man-pages/)
