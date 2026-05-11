# Terminal und Shell

Das Terminal ist die Arbeitsfläche für viele Übungen im Kurs.

Über das Terminal startest du Programme, prüfst Dateien, führst Tests aus und arbeitest mit Docker, TShark oder Git.

## Terminal öffnen

Unter Ubuntu und Pop!_OS funktioniert meistens:

```bash
Ctrl + Alt + T
```

Alternativ kannst du im Anwendungsmenü nach `Terminal` suchen.

In VSCode kannst du ein integriertes Terminal öffnen:

```text
Terminal > New Terminal
```

oder mit:

```text
Ctrl + Shift + `
```

## Shell erkennen

Die Standard-Shell ist auf Ubuntu-basierten Systemen meist Bash.

Prüfen kannst du das mit:

```bash
echo "$SHELL"
```

Typische Ausgabe:

```text
/bin/bash
```

## Aktuellen Ordner anzeigen

```bash
pwd
```

Beispiel:

```text
/home/mkargel/DailyWorkspace/source/repos/wireshark-wca-de
```

`pwd` bedeutet `print working directory`.

## Befehle abbrechen

Wenn ein Befehl hängt oder du ihn abbrechen möchtest:

```text
Ctrl + C
```

Das ist besonders nützlich bei Befehlen wie `ping`, `tcpdump`, `mkdocs serve` oder laufenden Docker-Logs.

## Ausgabe seitenweise lesen

Lange Ausgaben kannst du mit `less` lesbar machen:

```bash
ip addr | less
```

Navigation in `less`:

```text
Pfeil hoch/runter  zeilenweise bewegen
Leertaste          eine Seite weiter
q                  beenden
```

## Befehlshistorie

Mit den Pfeiltasten kannst du alte Befehle erneut aufrufen:

```text
Pfeil hoch   vorheriger Befehl
Pfeil runter nächster Befehl
```

Mit `history` siehst du die letzten Befehle:

```bash
history
```

## Tab-Vervollständigung

Die Tab-Taste vervollständigt Datei- und Ordnernamen.

Beispiel:

```bash
cd Doc
```

Dann `Tab` drücken.

Wenn es eindeutig ist, wird daraus zum Beispiel:

```bash
cd Documents/
```

## Wichtige Grundregel

Führe Befehle nicht blind aus.

Lies zuerst:

- in welchem Ordner du bist
- ob `sudo` verwendet wird
- ob Dateien gelöscht oder überschrieben werden
- ob der Befehl aus dem Repository-Root ausgeführt werden soll

Im Kurs wird der erwartete Arbeitsordner möglichst immer angegeben.
