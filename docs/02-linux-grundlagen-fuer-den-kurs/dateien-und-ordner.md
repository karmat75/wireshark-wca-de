# Dateien und Ordner

Viele Übungen im Kurs verweisen auf Dateien im Repository.

Deshalb solltest du wissen, wie du dich im Dateisystem bewegst und Inhalte prüfst.

## In einen Ordner wechseln

```bash
cd /home/mkargel/DailyWorkspace/source/repos/wireshark-wca-de
```

In einen Unterordner wechseln:

```bash
cd docs
```

Eine Ebene zurück:

```bash
cd ..
```

Zurück ins Home-Verzeichnis:

```bash
cd
```

oder:

```bash
cd ~
```

## Ordnerinhalt anzeigen

```bash
ls
```

Ausführlicher:

```bash
ls -la
```

Typische Ausgabe:

```text
drwxr-xr-x  5 user user 4096 May 10 10:00 .
drwxr-xr-x 10 user user 4096 May 10 09:50 ..
-rw-r--r--  1 user user 1234 May 10 10:00 README.md
```

## Projektstruktur anzeigen

Das Werkzeug `tree` zeigt Ordner übersichtlich an:

```bash
tree -L 2
```

Beispiel:

```text
.
├── docs
│   ├── index.md
│   └── 02-linux-grundlagen-fuer-den-kurs
├── mkdocs.yml
└── README.md
```

Falls `tree` fehlt:

```bash
sudo apt install -y tree
```

## Datei anzeigen

Kurze Dateien:

```bash
cat README.md
```

Längere Dateien:

```bash
less README.md
```

Die ersten Zeilen:

```bash
head README.md
```

Die letzten Zeilen:

```bash
tail README.md
```

## Datei bearbeiten

Im Kurs verwenden wir hauptsächlich VSCode.

Repository im aktuellen Ordner öffnen:

```bash
code .
```

Eine einzelne Datei öffnen:

```bash
code README.md
```

## Datei suchen

Nach Dateinamen suchen:

```bash
find . -name "mkdocs.yml"
```

Nach Markdown-Dateien suchen:

```bash
find docs -name "*.md"
```

## Text in Dateien suchen

```bash
grep -R "Wireshark" docs
```

Mit Zeilennummern:

```bash
grep -R -n "Wireshark" docs
```

## Vorsicht bei Löschbefehlen

Datei löschen:

```bash
rm datei.txt
```

Ordner rekursiv löschen:

```bash
rm -rf ordnername
```

!!! warning "Vorsicht"
    `rm -rf` löscht ohne Papierkorb. Verwende diesen Befehl nur, wenn du sicher bist, dass der Pfad stimmt.

## Praktische Kursregel

Wenn eine Übung sagt:

```text
Führe den Befehl im Repository-Root aus.
```

Dann sollte `pwd` ungefähr so aussehen:

```text
/home/<benutzer>/.../wireshark-wca-de
```

Und `ls` sollte unter anderem zeigen:

```text
README.md
mkdocs.yml
docs
labs
pcaps
```
