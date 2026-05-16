# Musterlösung

Die genaue Lösung hängt von deiner PCAP-Datei ab.

Dieses Lab bewertet nicht einen bestimmten Protokollfehler, sondern die saubere Nutzung von Wireshark-Funktionen.

## Erwartete Ergebnisse

Am Ende solltest du dokumentiert haben:

- Capture File Properties
- Protocol Hierarchy
- mindestens einen erfolgreichen Find-Packet-Treffer
- mindestens drei markierte Pakete
- mindestens zwei Packet Comments
- einen File Comment
- eine Time Reference
- eine exportierte Teildatei
- eine kurze Decode-As-Einordnung
- einen kurzen Arbeitsbericht

## Beispiel: Capture File Properties

Beispielhafte Notiz:

```text
Datei:
pcaps/generated/lab-basic-020-dns-http-docker.pcapng

Format:
pcapng

Pakete:
<anzahl>

Dauer:
<dauer>

Start:
<zeitpunkt>

Ende:
<zeitpunkt>
```

Wichtig:

> Capture File Properties beschreiben die Datei und helfen, die Analyse einzuordnen.

## Beispiel: Find Packet

Suchbegriff:

```text
does-not-exist.lab.local
```

Mögliche Beobachtung:

```text
Find Packet springt zu einer DNS Query oder DNS Response für does-not-exist.lab.local.
```

Bewertung:

```text
Find Packet ist hilfreich, wenn man bekannte Strings, Namen oder Werte im Capture sucht.
```

## Beispiel: markierte Pakete

Mögliche Frames:

```text
Frame <n>: DNS Query für web-ok.lab.local
Frame <n>: DNS NXDOMAIN Response für does-not-exist.lab.local
Frame <n>: HTTP Response 200 OK
```

Oder beim TCP-Lab:

```text
Frame <n>: TCP SYN zu Port 80
Frame <n>: TCP SYN/ACK von Port 80
Frame <n>: TCP RST/ACK für Port 81
```

## Beispiel: Packet Comments

Gute Kommentare sind kurz und fachlich.

Beispiele:

```text
DNS Query für web-ok.lab.local
```

```text
NXDOMAIN für does-not-exist.lab.local
```

```text
RST/ACK auf Verbindungsversuch zu TCP Port 81
```

Schlecht:

```text
hier irgendwas
```

oder:

```text
alles kaputt
```

## Beispiel: File Comment

Guter File Comment:

```text
Wireshark WCA DE Lab Foundation 002.
Analyse einer lokal erzeugten Lab-PCAP.
Wichtige Frames wurden markiert und kommentiert.
```

## Beispiel: Time Reference

Sinnvoller Startpunkt:

```text
erste DNS Query
```

oder:

```text
erster TCP SYN
```

Bewertung:

```text
Die Time Reference macht Zeitabstände ab einem fachlich sinnvollen Startpunkt leichter lesbar.
```

## Beispiel: Export Specified Packets

Erwartete Exportdatei:

```text
pcaps/generated/lab-foundation-002-selected-packets.pcapng
```

Prüfung:

```bash
tshark -r pcaps/generated/lab-foundation-002-selected-packets.pcapng | head
```

Bewertung:

```text
Export Specified Packets ist nützlich, um aus einem größeren Capture nur relevante Pakete weiterzugeben. Vor Weitergabe müssen Datenschutz und Sensibilität geprüft werden.
```

## Beispiel: Ignore Packets

Bewertung:

```text
Ignore Packets kann helfen, Pakete bei bestimmten Analysen auszublenden oder anders behandeln zu lassen. Die Funktion sollte vorsichtig verwendet werden, damit die Analyse nicht unbeabsichtigt verfälscht wird.
```

## Beispiel: Decode As

Bewertung:

```text
Decode As kann helfen, wenn ein Protokoll auf einem ungewöhnlichen Port läuft und Wireshark es nicht automatisch erkennt. Falsch gesetztes Decode As kann aber zu irreführender Interpretation führen.
```

## Beispiel-Arbeitsbericht

```text
PCAP:
pcaps/generated/lab-basic-020-dns-http-docker.pcapng

Capture File Properties:
Die Datei wurde als pcapng geöffnet. Anzahl Pakete, Startzeit, Endzeit und Dauer wurden in Capture File Properties geprüft.

Protocol Hierarchy:
DNS, TCP und HTTP sind sichtbar.

Find Packet:
Mit dem Suchbegriff does-not-exist.lab.local wurde eine DNS-Anfrage bzw. DNS-Antwort gefunden.

Wichtige Frames:
- Frame <n>: DNS Query für does-not-exist.lab.local
- Frame <n>: DNS Response NXDOMAIN
- Frame <n>: HTTP Response 200 OK

Kommentare:
Zwei Pakete wurden mit Packet Comments versehen.
Ein File Comment wurde gesetzt.

Time Reference:
Frame <n> wurde als Time Reference gesetzt.

Export:
Relevante Pakete wurden nach pcaps/generated/lab-foundation-002-selected-packets.pcapng exportiert.

Bewertung:
Die Datei wurde als Analyseobjekt vorbereitet. Relevante Pakete sind markiert, kommentiert und als kleinerer Ausschnitt exportiert.
```

## Wichtiger Merksatz

> Gute Wireshark-Arbeit besteht nicht nur aus Filtern.  
> Gute Wireshark-Arbeit macht eine Analyse für andere nachvollziehbar.
