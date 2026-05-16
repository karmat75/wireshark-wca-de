# Aufgaben

## Aufgabe 1: PCAP auswählen

Wähle eine vorhandene lokale PCAP-Datei.

Empfohlen:

```text
pcaps/generated/lab-basic-020-dns-http-docker.pcapng
```

oder:

```text
pcaps/generated/lab-basic-030-tcp-handshake-reset.pcapng
```

Prüfen:

```bash
ls -lh pcaps/generated/*.pcapng
```

Öffnen:

```bash
wireshark pcaps/generated/lab-basic-020-dns-http-docker.pcapng
```

## Aufgabe 2: Capture File Properties prüfen

Öffne:

```text
Statistics > Capture File Properties
```

Notiere:

- Dateiname
- Dateiformat
- Anzahl Pakete
- Capture-Dauer
- erstes Paket
- letztes Paket
- Paketgrößen- oder Datenratenhinweise, falls sichtbar
- Kommentare, falls vorhanden

## Aufgabe 3: Protocol Hierarchy prüfen

Öffne:

```text
Statistics > Protocol Hierarchy
```

Notiere:

- welche Protokolle sichtbar sind
- ob DNS sichtbar ist
- ob TCP sichtbar ist
- ob HTTP sichtbar ist
- ob TLS sichtbar ist

## Aufgabe 4: Find Packet verwenden

Nutze:

```text
Edit > Find Packet
```

Suche nach einem sinnvollen Begriff.

Beispiele:

```text
web-ok.lab.local
web-slow.lab.local
does-not-exist.lab.local
```

oder bei TCP-Lab:

```text
HTTP
RST
```

Notiere:

- Suchbegriff
- Suchmodus
- gefundene Frame-Nummer
- was dort sichtbar ist

## Aufgabe 5: wichtige Pakete markieren

Markiere mindestens drei relevante Pakete.

Beispiele:

- DNS Query
- DNS NXDOMAIN Response
- HTTP Request
- HTTP Response
- TCP SYN
- TCP SYN/ACK
- TCP RST

In Wireshark:

```text
Right Click > Mark/Unmark Packet
```

oder Menü:

```text
Edit > Mark/Unmark Packet
```

Notiere die Frame-Nummern.

## Aufgabe 6: Packet Comments setzen

Setze bei mindestens zwei Paketen Packet Comments.

Beispiele:

```text
DNS Query für web-ok.lab.local
```

```text
NXDOMAIN für does-not-exist.lab.local
```

```text
RST/ACK auf Verbindungsversuch zu Port 81
```

In Wireshark:

```text
Right Click > Packet Comment
```

oder Paket markieren und Kommentar-Funktion verwenden.

## Aufgabe 7: File Comment setzen

Setze einen File Comment.

Beispiel:

```text
Wireshark WCA DE Lab Foundation 002.
Analyse von DNS/HTTP oder TCP Handshake/Reset.
Wichtige Frames wurden markiert und kommentiert.
```

Hinweis:

Die genaue Position der Funktion kann je nach Wireshark-Version leicht abweichen. Suche im Bereich Capture File Properties oder Datei-/Kommentar-Funktionen.

## Aufgabe 8: Time Reference setzen

Wähle ein sinnvolles Startpaket, zum Beispiel:

- erste DNS Query
- erstes SYN einer Verbindung
- erster HTTP Request

Setze eine Time Reference:

```text
Edit > Time Reference > Set Time Reference
```

oder per Kontextmenü, je nach Version.

Prüfe, wie sich die Zeitdarstellung ändert.

Notiere:

- Frame-Nummer der Time Reference
- warum dieses Paket sinnvoll ist
- welche Zeitabstände danach leichter lesbar sind

## Aufgabe 9: relevante Pakete exportieren

Exportiere nur relevante Pakete in eine neue Datei.

Beispiele:

- alle markierten Pakete
- alle angezeigten Pakete nach einem Filter
- ein Paketbereich

Menü:

```text
File > Export Specified Packets
```

Speichere als:

```text
pcaps/generated/lab-foundation-002-selected-packets.pcapng
```

Prüfe anschließend:

```bash
capinfos pcaps/generated/lab-foundation-002-selected-packets.pcapng
```

oder:

```bash
tshark -r pcaps/generated/lab-foundation-002-selected-packets.pcapng | head
```

## Aufgabe 10: Ignore Packets ausprobieren

Wähle ein nicht wichtiges Paket und setze es testweise auf Ignore.

Menü oder Kontextmenü:

```text
Ignore/Unignore Packet
```

Prüfe:

- wie Wireshark es darstellt
- ob es bei Analysen anders behandelt wird
- warum man diese Funktion vorsichtig verwenden sollte

Danach wieder aufheben.

## Aufgabe 11: Decode As vorsichtig einordnen

Öffne:

```text
Analyze > Decode As
```

Prüfe, wie Wireshark Protokolle bestimmten Ports zuordnen kann.

Wichtig:

> In diesem Lab sollst du normalerweise nichts dauerhaft ändern.  
> Es geht darum, die Funktion zu kennen und zu verstehen, wann sie nützlich sein kann.

Notiere:

- welches Protokoll/Port-Konzept sichtbar ist
- wann Decode As helfen könnte
- warum falsches Decode As zu Fehlinterpretationen führen kann

## Aufgabe 12: Arbeitsbericht schreiben

Schreibe einen kurzen Bericht:

```text
PCAP:
<datei>

Capture File Properties:
<Pakete, Dauer, Start/Ende>

Wichtige Frames:
- Frame <n>: <Beobachtung>
- Frame <n>: <Beobachtung>
- Frame <n>: <Beobachtung>

Verwendete Funktionen:
- Capture File Properties
- Find Packet
- Packet Comments
- File Comment
- Time Reference
- Export Specified Packets
- Mark Packets
- Ignore Packets
- Decode As angesehen

Exportdatei:
pcaps/generated/lab-foundation-002-selected-packets.pcapng

Bewertung:
<kurze Einordnung>
```
