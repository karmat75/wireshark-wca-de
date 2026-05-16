# Aufgaben

## Aufgabe 1: Docker-Lab starten

Aus dem Repository-Root:

```bash
docker compose -f docker/compose/lab-basic-dns-http/compose.yml up -d
```

Status prüfen:

```bash
docker compose -f docker/compose/lab-basic-dns-http/compose.yml ps
```

## Aufgabe 2: Capture starten

Ordner vorbereiten:

```bash
mkdir -p pcaps/generated
```

Capture starten:

```bash
sudo tshark -i any -f "net 172.28.50.0/24" \
  -w pcaps/generated/lab-advanced-030-performance-analyse.pcapng
```

Stoppen später mit:

```text
Ctrl + C
```

Alternativ kannst du Wireshark verwenden und als Capture Filter setzen:

```text
net 172.28.50.0/24
```

## Aufgabe 3: Testtraffic erzeugen

In einem zweiten Terminal:

```bash
docker compose -f docker/compose/lab-basic-dns-http/compose.yml exec lab-client sh -lc '
dig web-ok.lab.local
curl -I http://web-ok.lab.local
dig web-slow.lab.local
curl -I http://web-slow.lab.local
'
```

Wiederhole den Block optional ein zweites Mal, damit im Capture mehrere Vergleichswerte entstehen.

## Aufgabe 4: Capture stoppen

Stoppe den Capture mit:

```text
Ctrl + C
```

Öffne die Datei:

```bash
wireshark pcaps/generated/lab-advanced-030-performance-analyse.pcapng
```

## Aufgabe 5: Grobe Orientierung

Prüfe:

```text
Statistics > Protocol Hierarchy
```

```text
Statistics > Conversations
```

Beantworte:

- Welche Protokolle sind sichtbar?
- Welche IP-Adressen sind beteiligt?
- Welche TCP-Conversations existieren?
- Welche Conversation gehört zu `web-ok`?
- Welche Conversation gehört zu `web-slow`?

## Aufgabe 6: Zeitdarstellung vorbereiten

Stelle eine sinnvolle Zeitdarstellung ein.

Beispiele:

```text
View > Time Display Format > Seconds Since Beginning of Capture
```

oder:

```text
View > Time Display Format > Seconds Since Previous Displayed Packet
```

Setze optional eine Time Reference auf:

- die DNS Query zu `web-ok.lab.local`
- den HTTP Request zu `web-ok.lab.local`
- den HTTP Request zu `web-slow.lab.local`

Notiere, welche Darstellung du verwendest.

## Aufgabe 7: DNS-Zeit prüfen

Filter für DNS:

```text
dns
```

Queries:

```text
dns.flags.response == 0
```

Responses:

```text
dns.flags.response == 1
```

Beantworte:

- Sind DNS Query und Response sichtbar?
- Gibt es auffällig lange DNS-Zeiten?
- Welche Frame-Nummern gehören zusammen?
- Ist DNS wahrscheinlich der Grund für die sichtbare Wartezeit?

## Aufgabe 8: TCP-Verbindungsaufbau prüfen

Filter für `web-ok`:

```text
ip.addr == 172.28.50.10 and tcp
```

Filter für `web-slow`:

```text
ip.addr == 172.28.50.20 and tcp
```

Beantworte:

- Ist der TCP Handshake vollständig sichtbar?
- Gibt es zwischen SYN und SYN/ACK auffällige Wartezeit?
- Welche Frame-Nummern bilden den Handshake?
- Ist TCP-Verbindungsaufbau wahrscheinlich der Grund für die sichtbare Wartezeit?

## Aufgabe 9: HTTP Request/Response-Zeit vergleichen

Filter für HTTP:

```text
http
```

Für `web-ok`:

```text
ip.addr == 172.28.50.10 and http
```

Für `web-slow`:

```text
ip.addr == 172.28.50.20 and http
```

Beantworte:

- Welche Frames enthalten HTTP Requests?
- Welche Frames enthalten HTTP Responses?
- Wie groß ist der Abstand zwischen Request und Response ungefähr?
- Welcher Server ist langsamer?
- Wo entsteht die sichtbare Wartezeit?

## Aufgabe 10: I/O Graph verwenden

Öffne:

```text
Statistics > I/O Graphs
```

Nutze optional Filter:

```text
ip.addr == 172.28.50.10
```

```text
ip.addr == 172.28.50.20
```

oder:

```text
http
```

Beantworte:

- Sind Pausen oder Peaks sichtbar?
- Hilft der Graph bei der Orientierung?
- Was kann der Graph nicht beweisen?

## Aufgabe 11: TShark-Auswertung

Setze:

```bash
PCAP="pcaps/generated/lab-advanced-030-performance-analyse.pcapng"
```

DNS-Zeiten:

```bash
tshark -r "$PCAP" \
  -Y "dns" \
  -T fields \
  -e frame.number \
  -e frame.time_relative \
  -e ip.src \
  -e ip.dst \
  -e dns.flags.response \
  -e dns.qry.name
```

HTTP Request/Response:

```bash
tshark -r "$PCAP" \
  -Y "http.request or http.response" \
  -T fields \
  -e frame.number \
  -e frame.time_relative \
  -e ip.src \
  -e ip.dst \
  -e http.request.method \
  -e http.host \
  -e http.response.code \
  -e http.response.phrase
```

TCP Handshakes:

```bash
tshark -r "$PCAP" \
  -Y "tcp.flags.syn == 1" \
  -T fields \
  -e frame.number \
  -e frame.time_relative \
  -e ip.src \
  -e tcp.srcport \
  -e ip.dst \
  -e tcp.dstport \
  -e tcp.flags.syn \
  -e tcp.flags.ack \
  -e tcp.stream
```

## Aufgabe 12: Check-Skript ausführen

```bash
bash labs/advanced/lab-advanced-030-performance-analyse/check_tshark.sh "$PCAP"
```

## Aufgabe 13: Kurzbericht schreiben

Schreibe einen Bericht:

```text
Capture-Punkt:
<wo wurde mitgeschnitten?>

DNS:
<kurze Bewertung>

TCP:
<kurze Bewertung>

HTTP:
<kurze Bewertung>

Vergleich:
web-ok.lab.local: <Zeitabstand Request/Response>
web-slow.lab.local: <Zeitabstand Request/Response>

Bewertung:
<wo ist die Wartezeit sichtbar?>

Einschränkungen:
<was ist nicht bewiesen?>
```

## Aufgabe 14: Lab stoppen

```bash
docker compose -f docker/compose/lab-basic-dns-http/compose.yml down
```
