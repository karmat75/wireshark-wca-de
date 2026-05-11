# TShark erster Kontakt

TShark ist die Kommandozeilenvariante von Wireshark.

Es nutzt dieselbe grundlegende Analysebasis wie Wireshark, arbeitet aber im Terminal. Damit eignet es sich besonders gut für wiederholbare Prüfungen, Skripte, automatisierte Lab-Checks und schnelle Auswertungen.

!!! important "TShark ist kein optionales Extra"
    In diesem Kurs behandeln wir TShark als festen Bestandteil der Wireshark-Arbeitsweise.  
    Wer Wireshark ernsthaft für Analyse und Troubleshooting nutzt, sollte nicht nur die grafische Oberfläche kennen, sondern auch TShark im Terminal bedienen können.

!!! tip "AHA-Referenz"
    TShark ist besonders wichtig auf Systemen ohne grafische Oberfläche.  
    Lies dazu auch die Referenz: [TShark auf Systemen ohne GUI](../90-referenz/tshark-auf-systemen-ohne-gui.md).

## Warum TShark für die WCA-Vorbereitung wichtig ist

Die WCA-101-Ziele verlangen nicht nur, dass du Pakete in der grafischen Oberfläche untersuchen kannst.

Zu den Zielen gehört auch, verschiedene Methoden zur Paketerfassung zu verstehen und Traffic mit Kommandozeilenwerkzeugen erfassen zu können.

TShark ist dafür das wichtigste Werkzeug aus der Wireshark-Welt.

Im Kurs verwenden wir TShark deshalb für mehrere Dinge:

- Capture-Dateien schnell prüfen
- Display Filter außerhalb der GUI testen
- bestimmte Felder gezielt ausgeben
- DNS-, TCP- oder HTTP-Pakete zählen
- Aufgaben automatisiert kontrollieren
- reproduzierbare Analysebefehle dokumentieren
- spätere Quiz- und Lab-Checks ermöglichen

Das Ziel ist nicht, Wireshark durch TShark zu ersetzen.

Das Ziel ist:

> Du sollst dieselbe Analysefrage sowohl grafisch in Wireshark als auch reproduzierbar im Terminal bearbeiten können.

## Wireshark und TShark im Zusammenspiel

| Aufgabe | Wireshark | TShark |
|---|---|---|
| ersten Überblick gewinnen | sehr gut | gut |
| einzelne Pakete visuell untersuchen | sehr gut | eingeschränkt |
| Protokollfelder aufklappen | sehr gut | möglich, aber weniger komfortabel |
| wiederholbare Prüfung bauen | eingeschränkt | sehr gut |
| viele Dateien automatisch prüfen | eingeschränkt | sehr gut |
| Ergebnisse in Skripten verwenden | eingeschränkt | sehr gut |
| Lern- und Lab-Checks automatisieren | eingeschränkt | sehr gut |

In der Praxis ist die Kombination stark:

1. Problem in Wireshark visuell verstehen
2. passende Filter finden
3. relevante Felder identifizieren
4. TShark-Befehl daraus ableiten
5. Ergebnis reproduzierbar dokumentieren

## Version prüfen

```bash
tshark --version
```

Wenn der Befehl fehlt:

```bash
sudo apt update
sudo apt install -y tshark
```

Je nach Installation ist TShark bereits mit Wireshark installiert.

## Interfaces anzeigen

```bash
tshark -D
```

Beispiel:

```text
1. enp0s3
2. any
3. lo
4. docker0
```

Die Nummern und Namen können bei dir anders sein.

## Capture-Datei lesen

Wenn du im vorherigen Abschnitt eine Datei gespeichert hast:

```bash
tshark -r pcaps/generated/first-contact.pcapng
```

Das zeigt eine kurze Paketübersicht im Terminal.

## Nur bestimmte Pakete anzeigen

TShark kann Display Filter verwenden.

DNS-Pakete:

```bash
tshark -r pcaps/generated/first-contact.pcapng -Y "dns"
```

ICMP-Pakete:

```bash
tshark -r pcaps/generated/first-contact.pcapng -Y "icmp"
```

TCP-Pakete:

```bash
tshark -r pcaps/generated/first-contact.pcapng -Y "tcp"
```

## Bestimmte Felder ausgeben

TShark kann gezielt Felder ausgeben.

DNS-Abfragen:

```bash
tshark -r pcaps/generated/first-contact.pcapng \
  -Y "dns.flags.response == 0" \
  -T fields \
  -e frame.number \
  -e ip.src \
  -e dns.qry.name
```

Das bedeutet:

| Option | Bedeutung |
|---|---|
| `-r` | Capture-Datei lesen |
| `-Y` | Display Filter anwenden |
| `-T fields` | nur bestimmte Felder ausgeben |
| `-e` | ein Feld auswählen |

## Pakete zählen

Eine einfache, aber sehr nützliche Technik ist das Zählen gefilterter Pakete.

Dafür verwenden wir häufig eine Pipe und `wc -l`.

`wc` steht historisch für `word count`. Mit der Option `-l` zählt es aber nicht Wörter, sondern Zeilen.

DNS-Pakete zählen:

```bash
tshark -r pcaps/generated/first-contact.pcapng -Y "dns" | wc -l
```

TCP-Pakete zählen:

```bash
tshark -r pcaps/generated/first-contact.pcapng -Y "tcp" | wc -l
```

ICMP-Pakete zählen:

```bash
tshark -r pcaps/generated/first-contact.pcapng -Y "icmp" | wc -l
```

Das funktioniert hier, weil TShark in dieser Ausgabe pro gefundenem Paket eine Zeile ausgibt.

!!! note "`wc -l` zählt Zeilen"
    `wc -l` weiß nichts über Pakete. Es zählt nur Ausgabezeilen.  
    In diesem Fall ist das genau das, was wir wollen, weil TShark pro Paket eine Zeile ausgibt.

Das ist später hilfreich, wenn Lab-Checks prüfen sollen, ob bestimmte Pakete vorhanden sind.

## Ausgabe reproduzierbar machen

Für Analyseberichte ist es gut, konkrete Befehle anzugeben.

Beispiel:

```bash
tshark -r pcaps/generated/first-contact.pcapng \
  -Y "dns.flags.response == 0" \
  -T fields \
  -e frame.number \
  -e frame.time_relative \
  -e ip.src \
  -e dns.qry.name
```

Damit dokumentierst du nicht nur deine Beobachtung, sondern auch, wie du sie ermittelt hast.

Das ist ein wichtiger Unterschied:

```text
"Ich habe DNS gesehen."
```

ist schwächer als:

```text
"Mit folgendem Filter wurden DNS-Anfragen gefunden: dns.flags.response == 0"
```

## TShark ist kein Ersatz für Wireshark

Für die erste Analyse ist Wireshark oft angenehmer.

Für Wiederholung, Prüfung und Automatisierung ist TShark sehr stark.

Im Kurs verwenden wir beides:

| Werkzeug | Stärken |
|---|---|
| Wireshark | visuelle Analyse, Drilldown, Streams, Statistiken |
| TShark | Automatisierung, Tests, wiederholbare Checks |

## WCA-Bezug

Dieser Abschnitt berührt besonders diese WCA-nahe Kompetenzbereiche:

- Pakete mit verschiedenen Methoden erfassen
- Kommandozeilenwerkzeuge für Capture und Analyse verwenden
- Display Filter sicher anwenden
- relevante Pakete aus einem Mitschnitt isolieren
- wichtige Informationen aus einer Capture-Datei ableiten
- Analyseergebnisse reproduzierbar dokumentieren

Im weiteren Kurs wird TShark deshalb regelmäßig wieder auftauchen.

Du musst am Ende nicht jeden TShark-Parameter auswendig kennen.

Du solltest aber verstehen:

- wie eine Capture-Datei gelesen wird
- wie ein Display Filter angewendet wird
- wie bestimmte Felder ausgegeben werden
- wie Ergebnisse gezählt oder verglichen werden
- wie ein TShark-Befehl eine Analyse nachvollziehbar macht

## Mini-Aufgabe

Prüfe deine erste Capture-Datei mit TShark:

```bash
tshark -r pcaps/generated/first-contact.pcapng
```

Zähle DNS-Pakete:

```bash
tshark -r pcaps/generated/first-contact.pcapng -Y "dns" | wc -l
```

Gib DNS-Namen aus:

```bash
tshark -r pcaps/generated/first-contact.pcapng \
  -Y "dns.flags.response == 0" \
  -T fields \
  -e dns.qry.name
```

Gib DNS-Namen mit Paketnummern aus:

```bash
tshark -r pcaps/generated/first-contact.pcapng \
  -Y "dns.flags.response == 0" \
  -T fields \
  -e frame.number \
  -e dns.qry.name
```

Wenn du hier mehrere Zeilen siehst, ist das für den Anfang völlig ausreichend.

## Merksatz

> Wireshark hilft dir, Pakete visuell zu verstehen. TShark hilft dir, dieselbe Analyse reproduzierbar zu machen.
