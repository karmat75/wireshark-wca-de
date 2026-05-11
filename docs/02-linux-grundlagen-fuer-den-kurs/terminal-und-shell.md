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

## Befehle verbinden: die Pipe

Mit einer Pipe (`|`) leitest du die Ausgabe eines Befehls an den nächsten Befehl weiter.

Beispiel:

```bash
ip addr | less
```

Das bedeutet:

1. `ip addr` erzeugt eine Ausgabe
2. diese Ausgabe wird nicht direkt vollständig ins Terminal geschrieben
3. `less` bekommt die Ausgabe und zeigt sie seitenweise an

Pipes sind im Kurs wichtig, weil wir damit TShark-Ausgaben filtern, zählen oder weiterverarbeiten können.

## Zeilen, Wörter und Bytes zählen mit `wc`

Der Befehl `wc` steht historisch für `word count`.

Der Name ist etwas zu kurz gegriffen, denn `wc` kann nicht nur Wörter zählen.

Wichtige Optionen:

| Befehl | Bedeutung |
|---|---|
| `wc -l` | Zeilen zählen |
| `wc -w` | Wörter zählen |
| `wc -c` | Bytes zählen |

Beispiel:

```bash
printf "eins\nzwei\ndrei\n" | wc -l
```

Ausgabe:

```text
3
```

Im Kurs verwenden wir `wc -l` häufig, um Zeilen zu zählen.

Das ist besonders praktisch bei TShark, weil viele TShark-Ausgaben pro Paket eine Zeile erzeugen.

Beispiel:

```bash
tshark -r capture.pcapng -Y "dns" | wc -l
```

Das bedeutet sinngemäß:

> Zeige alle DNS-Pakete aus der Capture-Datei und zähle die Ausgabezeilen.

Wenn TShark pro Paket eine Zeile ausgibt, entspricht die Anzahl der Zeilen der Anzahl der gefundenen Pakete.

!!! note "Nicht blind als Wahrheit nehmen"
    `wc -l` zählt Zeilen, nicht direkt Pakete.  
    In vielen TShark-Standardausgaben ist das praktisch identisch, weil ein Paket als eine Zeile ausgegeben wird. Bei anderen Ausgabeformaten muss man prüfen, ob diese Annahme passt.

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
