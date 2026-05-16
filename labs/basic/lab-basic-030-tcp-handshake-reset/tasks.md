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

Starte auf dem Host einen Capture:

```bash
sudo tshark -i any -f "net 172.28.50.0/24" -w pcaps/generated/lab-basic-030-tcp-handshake-reset.pcapng
```

Stoppen später mit:

```text
Ctrl + C
```

Alternativ kannst du Wireshark verwenden und als Capture Filter setzen:

```text
net 172.28.50.0/24
```

## Aufgabe 3: erfolgreichen TCP/HTTP-Traffic erzeugen

In einem zweiten Terminal:

```bash
docker compose -f docker/compose/lab-basic-dns-http/compose.yml exec lab-client sh -lc '
curl -I http://web-ok.lab.local
'
```

## Aufgabe 4: geschlossenen TCP-Port testen

Im gleichen zweiten Terminal:

```bash
docker compose -f docker/compose/lab-basic-dns-http/compose.yml exec lab-client sh -lc '
curl -v --connect-timeout 3 --max-time 5 http://172.28.50.10:81 || true
'
```

## Aufgabe 5: Capture stoppen

Stoppe TShark mit:

```text
Ctrl + C
```

Öffne den Capture:

```bash
wireshark pcaps/generated/lab-basic-030-tcp-handshake-reset.pcapng
```

## Aufgabe 6: erfolgreichen Handshake finden

Nutze Filter:

```text
tcp.flags.syn == 1 and tcp.flags.ack == 0
```

```text
tcp.flags.syn == 1 and tcp.flags.ack == 1
```

```text
tcp.port == 80
```

Beantworte:

- Welche Frame-Nummer enthält SYN vom Client zum Webserver?
- Welche Frame-Nummer enthält SYN/ACK vom Webserver zum Client?
- Welche Frame-Nummer enthält das abschließende ACK?
- Welcher `tcp.stream` gehört zur Verbindung?
- Welche HTTP Response ist sichtbar?

## Aufgabe 7: TCP Stream isolieren

Ermittle den Stream Index in Wireshark oder per TShark.

Filtere dann:

```text
tcp.stream == <nummer>
```

Beantworte:

- Ist der Handshake vollständig?
- Gibt es HTTP?
- Gibt es FIN oder RST am Ende?
- Welche Richtung sendet die HTTP Response?

## Aufgabe 8: geschlossenen Port analysieren

Nutze Filter:

```text
tcp.port == 81
```

```text
tcp.flags.reset == 1
```

Beantworte:

- Gibt es SYN zum Zielport 81?
- Wer sendet RST oder RST/ACK?
- Welche Aussage ist dadurch belegbar?
- Welche Aussage wäre zu stark?

## Aufgabe 9: TShark-Auswertung

TCP SYN ohne ACK:

```bash
tshark -r pcaps/generated/lab-basic-030-tcp-handshake-reset.pcapng \
  -Y "tcp.flags.syn == 1 and tcp.flags.ack == 0" \
  -T fields \
  -e frame.number \
  -e frame.time_relative \
  -e ip.src \
  -e tcp.srcport \
  -e ip.dst \
  -e tcp.dstport \
  -e tcp.stream
```

RST-Pakete:

```bash
tshark -r pcaps/generated/lab-basic-030-tcp-handshake-reset.pcapng \
  -Y "tcp.flags.reset == 1" \
  -T fields \
  -e frame.number \
  -e frame.time_relative \
  -e ip.src \
  -e tcp.srcport \
  -e ip.dst \
  -e tcp.dstport \
  -e tcp.stream
```

HTTP Responses:

```bash
tshark -r pcaps/generated/lab-basic-030-tcp-handshake-reset.pcapng \
  -Y "http.response" \
  -T fields \
  -e frame.number \
  -e frame.time_relative \
  -e ip.src \
  -e ip.dst \
  -e http.response.code \
  -e http.response.phrase
```

## Aufgabe 10: Check-Skript ausführen

```bash
bash labs/basic/lab-basic-030-tcp-handshake-reset/check_tshark.sh \
  pcaps/generated/lab-basic-030-tcp-handshake-reset.pcapng
```

## Aufgabe 11: Kurzbericht schreiben

Schreibe einen kurzen Bericht mit:

- Capture-Punkt
- erfolgreicher TCP-Verbindung
- geschlossenem Port
- verwendeten Filtern
- relevanten Frame-Nummern
- Bewertung
- Einschränkungen

## Aufgabe 12: Lab stoppen

```bash
docker compose -f docker/compose/lab-basic-dns-http/compose.yml down
```
