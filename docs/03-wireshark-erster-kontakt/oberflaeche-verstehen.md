# Oberfläche verstehen

Wireshark besteht aus mehreren Bereichen, die zusammen eine Paketaufnahme lesbar machen.

Wenn du diese Bereiche kennst, ist die Oberfläche deutlich weniger einschüchternd.

## Startseite

Nach dem Start zeigt Wireshark meistens eine Liste der verfügbaren Netzwerkinterfaces.

Typische Interfaces sind zum Beispiel:

```text
enp0s3
eth0
wlan0
lo
docker0
br-...
```

Die Namen hängen von System, Hardware und Docker-Konfiguration ab.

Wichtig:

- `lo` ist das Loopback-Interface des eigenen Systems.
- `wlan...` oder `wlp...` sind häufig WLAN-Interfaces.
- `en...`, `eth...` oder `eno...` sind häufig kabelgebundene Interfaces.
- `docker0` und `br-...` gehören meistens zu Docker-Netzwerken.

## Paketliste

Die Paketliste ist der obere Hauptbereich.

Hier siehst du eine Zeile pro Paket.

Typische Spalten sind:

| Spalte | Bedeutung |
|---|---|
| No. | laufende Paketnummer im Mitschnitt |
| Time | Zeitpunkt oder Zeitabstand |
| Source | Quelle |
| Destination | Ziel |
| Protocol | erkanntes Protokoll |
| Length | Paketlänge |
| Info | kurze Zusammenfassung |

Die Paketliste beantwortet zuerst die Frage:

> Was ist in welcher Reihenfolge passiert?

## Paketdetails

Der mittlere Bereich zeigt die Details des ausgewählten Pakets.

Hier findest du die einzelnen Protokollschichten.

Beispiel:

```text
Frame
Ethernet II
Internet Protocol Version 4
Transmission Control Protocol
Hypertext Transfer Protocol
```

Dieser Bereich ist fachlich besonders wichtig.

Hier siehst du nicht nur, dass ein Paket TCP ist, sondern auch:

- Ports
- Flags
- Sequenznummern
- ACK-Nummern
- DNS-Felder
- HTTP-Header
- TLS-Handshake-Informationen

## Paketbytes

Der untere Bereich zeigt die Rohdaten des Pakets.

Am Anfang brauchst du diesen Bereich selten.

Später ist er hilfreich, wenn du verstehen möchtest, wie Wireshark einzelne Felder aus den Bytes interpretiert.

## Display Filter

Oben befindet sich die Display-Filter-Leiste.

Display Filter blenden Pakete in einem geöffneten Mitschnitt ein oder aus.

Beispiele:

```text
dns
```

```text
tcp
```

```text
ip.addr == 1.1.1.1
```

Wichtig:

> Display Filter verändern den Mitschnitt nicht. Sie ändern nur, was angezeigt wird.

## Capture Filter

Capture Filter werden vor oder während einer Aufnahme verwendet.

Sie entscheiden, welche Pakete überhaupt mitgeschnitten werden.

Beispiel:

```text
host 1.1.1.1
```

Wichtig:

> Capture Filter reduzieren die aufgenommenen Pakete. Was nicht mitgeschnitten wurde, kann später nicht analysiert werden.

Für den Anfang verwenden wir fast immer Display Filter und nur selten Capture Filter.

## Statusleiste

Unten zeigt Wireshark Informationen zum aktuellen Mitschnitt.

Dort siehst du zum Beispiel:

- wie viele Pakete vorhanden sind
- wie viele Pakete gerade angezeigt werden
- ob ein Filter aktiv ist
- ob Fehler im Filter vorhanden sind

## Farben

Wireshark färbt Pakete ein.

Diese Farben sind Hinweise, aber keine endgültige Bewertung.

Beispiele:

- DNS kann anders eingefärbt sein als TCP
- TCP-Probleme können auffällig markiert werden
- ARP oder ICMP können eigene Farben haben

!!! warning "Farben sind keine Diagnose"
    Eine rote oder dunkle Zeile bedeutet nicht automatisch, dass etwas kaputt ist. Nutze Farben als Hinweis, aber prüfe die Details.

## Nützliche Menüpunkte

Für den Anfang sind besonders diese Bereiche wichtig:

| Menü | Zweck |
|---|---|
| File | Capture-Dateien öffnen, speichern, exportieren |
| Capture | Aufnahme starten, stoppen, Optionen setzen |
| Analyze | Protokollanalyse, Decode As, Expert Information |
| Statistics | Conversations, Endpoints, Protocol Hierarchy, IO Graphs |
| View | Darstellung, Zeitformat, Spalten, Farben |

## Erste Orientierung

Wenn du einen Mitschnitt öffnest, gehe zunächst so vor:

1. Gibt es viele oder wenige Pakete?
2. Welche Protokolle tauchen auf?
3. Welche Geräte sprechen miteinander?
4. Gibt es DNS?
5. Gibt es TCP?
6. Gibt es auffällige Einträge in `Expert Information`?
7. Welche Frage will ich eigentlich beantworten?

Wireshark ist kein Orakel.

Wireshark zeigt Daten. Die Analyse entsteht durch deine Fragen.
