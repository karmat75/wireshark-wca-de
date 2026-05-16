# Aufgaben

## Aufgabe 1: Docker-Lab starten

Aus dem Repository-Root:

```bash
docker compose -f docker/compose/lab-advanced-tcp-loss/compose.yml up -d --build
```

Status prüfen:

```bash
docker compose -f docker/compose/lab-advanced-tcp-loss/compose.yml ps
```

Logs prüfen:

```bash
docker compose -f docker/compose/lab-advanced-tcp-loss/compose.yml logs lab-web-loss
```

Achte darauf, ob `netem` gesetzt wurde.

## Aufgabe 2: Capture starten

Ordner vorbereiten:

```bash
mkdir -p pcaps/generated
```

Capture starten:

```bash
sudo tshark -i any -f "net 172.28.60.0/24" \
  -w pcaps/generated/lab-advanced-010-tcp-retransmission.pcapng
```

Stoppen später mit:

```text
Ctrl + C
```

Alternativ kannst du Wireshark verwenden und als Capture Filter setzen:

```text
net 172.28.60.0/24
```

## Aufgabe 3: Download erzeugen

In einem zweiten Terminal:

```bash
docker compose -f docker/compose/lab-advanced-tcp-loss/compose.yml exec lab-client sh -lc '
rm -f /tmp/bigfile.bin
curl -o /tmp/bigfile.bin http://172.28.60.10/bigfile.bin
ls -lh /tmp/bigfile.bin
'
```

Falls der Download sehr schnell war und keine Retransmissions sichtbar werden, wiederhole den Download ein- bis zweimal während der Capture läuft.

## Aufgabe 4: Capture stoppen

Stoppe den Capture mit:

```text
Ctrl + C
```

Öffne die Datei:

```bash
wireshark pcaps/generated/lab-advanced-010-tcp-retransmission.pcapng
```

## Aufgabe 5: grobe Orientierung

Prüfe:

```text
Statistics > Protocol Hierarchy
```

```text
Statistics > Conversations
```

Beantworte:

- Welche IPs sind beteiligt?
- Welche TCP-Verbindung hat die meisten Bytes?
- Welcher Port wird verwendet?
- Welcher TCP Stream gehört zum Download?

## Aufgabe 6: TCP Stream isolieren

Suche ein Paket der Verbindung und ermittle den Stream Index.

Filtere:

```text
tcp.stream == <nummer>
```

Beantworte:

- Ist der TCP Handshake sichtbar?
- Welche Richtung sendet den größeren Datenanteil?
- Gibt es Verbindungsabschluss per FIN oder RST?
- Gibt es Analysehinweise im Stream?

## Aufgabe 7: TCP Analysehinweise anzeigen

Teste:

```text
tcp.analysis.flags
```

Dann gezielter:

```text
tcp.analysis.retransmission
```

```text
tcp.analysis.fast_retransmission
```

```text
tcp.analysis.duplicate_ack
```

```text
tcp.analysis.lost_segment
```

Beantworte:

- Welche Analysehinweise sind sichtbar?
- Welche Frame-Nummern sind relevant?
- Sind Retransmissions sichtbar?
- Sind Duplicate ACKs sichtbar?
- Gibt es Fast Retransmissions?

## Aufgabe 8: Sequenz und ACK betrachten

Wähle eine Retransmission oder Fast Retransmission.

Prüfe im Paketdetailbereich:

```text
Transmission Control Protocol
```

Notiere:

- Sequence Number
- ACK Number
- TCP Flags
- Stream Index
- Wireshark Analysehinweis
- vorherige und folgende Frames

Beantworte:

- Warum interpretiert Wireshark dieses Paket als Retransmission?
- Welche Pakete davor sind relevant?
- Ist die Ursache allein durch dieses Paket bewiesen?

## Aufgabe 9: I/O Graph optional prüfen

Öffne:

```text
Statistics > I/O Graphs
```

Filtere auf den TCP Stream oder den Webserver:

```text
ip.addr == 172.28.60.10
```

Optional:

```text
tcp.analysis.retransmission
```

Beantworte:

- Gibt es unregelmäßige Übertragungsmuster?
- Sind Retransmissions im Zeitverlauf sichtbar?
- Was kann ein Graph zeigen und was nicht?

## Aufgabe 10: TShark-Auswertung

Setze:

```bash
PCAP="pcaps/generated/lab-advanced-010-tcp-retransmission.pcapng"
```

TCP Analysehinweise:

```bash
tshark -r "$PCAP" \
  -Y "tcp.analysis.flags" \
  -T fields \
  -e frame.number \
  -e frame.time_relative \
  -e tcp.stream \
  -e ip.src \
  -e tcp.srcport \
  -e ip.dst \
  -e tcp.dstport \
  -e _ws.col.Info
```

Retransmissions:

```bash
tshark -r "$PCAP" \
  -Y "tcp.analysis.retransmission or tcp.analysis.fast_retransmission" \
  -T fields \
  -e frame.number \
  -e frame.time_relative \
  -e tcp.stream \
  -e ip.src \
  -e ip.dst \
  -e _ws.col.Info
```

Duplicate ACKs:

```bash
tshark -r "$PCAP" \
  -Y "tcp.analysis.duplicate_ack" \
  -T fields \
  -e frame.number \
  -e frame.time_relative \
  -e tcp.stream \
  -e ip.src \
  -e ip.dst \
  -e _ws.col.Info
```

## Aufgabe 11: Check-Skript ausführen

```bash
bash labs/advanced/lab-advanced-010-tcp-retransmission/check_tshark.sh "$PCAP"
```

## Aufgabe 12: Kurzbericht schreiben

Schreibe einen Bericht:

```text
Capture-Punkt:
<wo wurde mitgeschnitten?>

TCP Stream:
<stream nummer>

Beobachtungen:
- Frame <n>: <Beobachtung>
- Frame <n>: <Beobachtung>
- Frame <n>: <Beobachtung>

Verwendete Filter:
<filter>

Bewertung:
<fachliche Einordnung>

Einschränkungen:
<was ist nicht bewiesen?>

Nächster Schritt:
<was wäre in einem echten Fall sinnvoll?>
```

## Aufgabe 13: Lab stoppen

```bash
docker compose -f docker/compose/lab-advanced-tcp-loss/compose.yml down
```
