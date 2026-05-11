# Rechte und Gruppen

Linux verwendet Rechte und Gruppen, um Zugriff auf Dateien, Geräte und Funktionen zu steuern.

Für diesen Kurs ist das besonders bei Wireshark, Docker und Projektdateien relevant.

## Aktuellen Benutzer anzeigen

```bash
whoami
```

## Gruppen anzeigen

```bash
groups
```

Beispiel:

```text
mkargel adm sudo docker wireshark
```

Wichtige Gruppen im Kurs:

| Gruppe | Bedeutung |
|---|---|
| `sudo` | Benutzer darf administrative Befehle mit `sudo` ausführen |
| `docker` | Benutzer darf Docker ohne `sudo` verwenden |
| `wireshark` | Benutzer darf, je nach Systemkonfiguration, Pakete mitschneiden |

## `sudo` verstehen

`sudo` führt einen Befehl mit erhöhten Rechten aus.

Beispiel:

```bash
sudo apt update
```

Verwende `sudo` nur, wenn es nötig ist.

Typische Fälle:

- Pakete installieren
- Systemdienste verwalten
- Dateien unter `/etc` ändern
- Benutzer zu Gruppen hinzufügen

## Warum wir nicht direkt als `root` arbeiten

Unter Linux gibt es den Benutzer `root`. Dieser Benutzer darf grundsätzlich alles.

Das ist für administrative Aufgaben praktisch, aber im Alltag auch gefährlich. Ein falscher Befehl, ein falscher Pfad oder ein unbedacht gestartetes Programm kann als `root` direkt das gesamte System verändern oder beschädigen.

Deshalb arbeiten wir im Kurs nicht dauerhaft als `root`, sondern mit einem normalen Benutzerkonto. Administrative Aktionen werden gezielt mit `sudo` ausgeführt.

Das ist vergleichbar mit Windows:

- Im Alltag arbeitet man nicht mit dem `SYSTEM`-Konto.
- Für administrative Aufgaben verwendet man ein Benutzerkonto mit Admin-Rechten.
- Administrative Aktionen sollen bewusst erfolgen, nicht dauerhaft und automatisch.
- Der klassische lokale `Administrator`-Account ist auf modernen Windows-Systemen eher ein historisches Konto und sollte nach gängigen Sicherheitsrichtlinien möglichst deaktiviert oder zumindest nicht für den Alltag verwendet werden.

Der wichtige Gedanke ist:

> Normale Arbeit erfolgt mit normalen Rechten. Administrative Rechte werden nur für konkrete Aufgaben gezielt aktiviert.

Das reduziert Fehler, macht Befehle bewusster und begrenzt den Schaden, wenn etwas schiefgeht.

Im Kurs bedeutet das:

- Wireshark wird nicht dauerhaft als `root` gestartet.
- Docker wird über die Gruppe `docker` nutzbar gemacht.
- Systemänderungen erfolgen sichtbar mit `sudo`.
- Projektdateien bleiben im Besitz des normalen Benutzers.
- Fehlermeldungen wie `Permission denied` werden zuerst verstanden, bevor Rechte pauschal erweitert werden.

!!! warning "Nicht jeder Fehler ist ein sudo-Problem"
    Wenn ein Befehl mit `Permission denied` fehlschlägt, ist `sudo` nicht automatisch die richtige Lösung. Manchmal fehlt eine Gruppenmitgliedschaft, manchmal ist der Arbeitsordner falsch, manchmal gehören Dateien dem falschen Benutzer.

## Datei- und Ordnerrechte anzeigen

```bash
ls -l
```

Beispiel:

```text
-rw-r--r-- 1 user user 1234 May 10 10:00 README.md
```

Grob gelesen:

```text
rw-   Besitzer darf lesen und schreiben
r--   Gruppe darf lesen
r--   Andere dürfen lesen
```

## Besitz ändern

Im Kurs sollte das selten nötig sein.

Beispiel:

```bash
sudo chown user:user datei.txt
```

!!! warning "Vorsicht"
    Nutze `chown` und `chmod` nicht großflächig auf Systemordnern. Falsche Rechte können Programme oder das System beschädigen.

## Benutzer zu einer Gruppe hinzufügen

Beispiel Docker:

```bash
sudo usermod -aG docker "$USER"
```

Beispiel Wireshark:

```bash
sudo usermod -aG wireshark "$USER"
```

Danach musst du dich meist einmal ab- und wieder anmelden.

Prüfen:

```bash
groups
```

## Warum Ab- und Anmelden nötig ist

Gruppenmitgliedschaften werden beim Login geladen.

Wenn du dich gerade erst zu einer Gruppe hinzugefügt hast, weiß deine aktuelle Sitzung davon oft noch nichts.

Deshalb:

1. Befehl ausführen
2. abmelden
3. anmelden
4. `groups` prüfen

## Wireshark und Capture-Rechte

Wireshark sollte nicht dauerhaft komplett mit Root-Rechten gestartet werden.

Besser ist:

- Wireshark normal als Benutzer starten
- Capture-Rechte sauber über Systemkonfiguration und Gruppe erlauben
- nur die notwendigen Komponenten bekommen erhöhte Rechte

Das reduziert das Risiko, falls ein Capture oder Dissector problematisch ist.

## Docker und Rechte

Wenn dein Benutzer Mitglied der Gruppe `docker` ist, kannst du Docker ohne `sudo` verwenden:

```bash
docker ps
```

!!! warning "Docker-Gruppe"
    Mitgliedschaft in der Docker-Gruppe ist sicherheitlich weitreichend. Auf einem Lernsystem ist das meistens akzeptabel. Auf Produktivsystemen sollte das bewusst entschieden werden.

## Praktische Kursregel

Wenn ein Befehl mit `Permission denied` fehlschlägt:

1. nicht sofort überall `sudo` davor schreiben
2. prüfen, auf welche Datei oder Funktion zugegriffen wird
3. prüfen, ob eine Gruppenmitgliedschaft fehlt
4. prüfen, ob eine neue Anmeldung nötig ist
5. erst dann gezielt mit erhöhten Rechten arbeiten
