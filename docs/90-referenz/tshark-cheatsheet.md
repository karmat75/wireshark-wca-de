# TShark-Cheatsheet

Diese Seite sammelt wiederverwendbare TShark-Befehle für Labs, Challenges und echte Analysen.

## Grundform

```bash
tshark -r capture.pcapng -Y "display.filter"
```

Mit Feldausgabe:

```bash
tshark -r capture.pcapng \
  -Y "display.filter" \
  -T fields \
  -e frame.number \
  -e frame.time_relative \
  -e ip.src \
  -e ip.dst
```

## Capture-Datei prüfen

```bash
capinfos capture.pcapng
```

Erste Pakete anzeigen:

```bash
tshark -r capture.pcapng | head
```

Pakete zählen:

```bash
tshark -r capture.pcapng | wc -l
```

!!! note "`wc`"
    `wc` steht für `word count`.  
    Mit `-l` zählt es Zeilen. In diesem Kurs nutzen wir es oft, um die Anzahl passender Pakete zu zählen.

## Protokolle zählen

```bash
tshark -r capture.pcapng -Y "dns" | wc -l
tshark -r capture.pcapng -Y "http" | wc -l
tshark -r capture.pcapng -Y "tls" | wc -l
tshark -r capture.pcapng -Y "tcp.analysis.flags" | wc -l
```

## DNS

DNS Queries:

```bash
tshark -r capture.pcapng \
  -Y "dns.flags.response == 0" \
  -T fields \
  -e frame.number \
  -e frame.time_relative \
  -e ip.src \
  -e ip.dst \
  -e dns.qry.name
```

DNS Responses:

```bash
tshark -r capture.pcapng \
  -Y "dns.flags.response == 1" \
  -T fields \
  -e frame.number \
  -e frame.time_relative \
  -e ip.src \
  -e ip.dst \
  -e dns.qry.name \
  -e dns.flags.rcode
```

NXDOMAIN:

```bash
tshark -r capture.pcapng \
  -Y "dns.flags.rcode == 3" \
  -T fields \
  -e frame.number \
  -e frame.time_relative \
  -e ip.src \
  -e ip.dst \
  -e dns.qry.name
```

## HTTP

HTTP Request/Response Timeline:

```bash
tshark -r capture.pcapng \
  -Y "http.request or http.response" \
  -T fields \
  -e frame.number \
  -e frame.time_relative \
  -e tcp.stream \
  -e ip.src \
  -e ip.dst \
  -e http.request.method \
  -e http.host \
  -e http.request.uri \
  -e http.response.code \
  -e http.response.phrase
```

HTTP Authorization Header:

```bash
tshark -r capture.pcapng \
  -Y "http.authorization" \
  -T fields \
  -e frame.number \
  -e frame.time_relative \
  -e ip.src \
  -e ip.dst \
  -e http.authorization
```

HTTP POST Body:

```bash
tshark -r capture.pcapng \
  -Y "http.request.method == \"POST\"" \
  -T fields \
  -e frame.number \
  -e http.file_data
```

## TLS

TLS Client Hello:

```bash
tshark -r capture.pcapng \
  -Y "tls.handshake.type == 1" \
  -T fields \
  -e frame.number \
  -e frame.time_relative \
  -e ip.src \
  -e ip.dst \
  -e tcp.stream
```

SNI:

```bash
tshark -r capture.pcapng \
  -Y "tls.handshake.extensions_server_name" \
  -T fields \
  -e frame.number \
  -e frame.time_relative \
  -e ip.src \
  -e ip.dst \
  -e tls.handshake.extensions_server_name
```

ALPN:

```bash
tshark -r capture.pcapng \
  -Y "tls.handshake.extensions_alpn_str" \
  -T fields \
  -e frame.number \
  -e tls.handshake.extensions_alpn_str
```

TLS Alerts:

```bash
tshark -r capture.pcapng \
  -Y "tls.alert_message" \
  -T fields \
  -e frame.number \
  -e frame.time_relative \
  -e ip.src \
  -e ip.dst \
  -e tls.alert_message.desc
```

## TCP

SYN-Pakete:

```bash
tshark -r capture.pcapng \
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

RST-Pakete:

```bash
tshark -r capture.pcapng \
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

TCP Analysehinweise:

```bash
tshark -r capture.pcapng \
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
tshark -r capture.pcapng \
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
tshark -r capture.pcapng \
  -Y "tcp.analysis.duplicate_ack" \
  -T fields \
  -e frame.number \
  -e frame.time_relative \
  -e tcp.stream \
  -e ip.src \
  -e ip.dst \
  -e _ws.col.Info
```

## Conversations

TCP Conversations:

```bash
tshark -r capture.pcapng -q -z conv,tcp
```

IP Conversations:

```bash
tshark -r capture.pcapng -q -z conv,ip
```

Protocol Hierarchy:

```bash
tshark -r capture.pcapng -q -z io,phs
```

## Spaltenausgabe robuster machen

Wenn Feldwerte sauber tabellarisch ausgegeben werden sollen:

```bash
tshark -r capture.pcapng \
  -Y "http.request" \
  -T fields \
  -E header=y \
  -E separator=';' \
  -E quote=d \
  -e frame.number \
  -e frame.time_relative \
  -e ip.src \
  -e ip.dst \
  -e http.host \
  -e http.request.uri
```

## Merksatz

> TShark macht Analyse wiederholbar.  
> Was du im Terminal reproduzieren kannst, kannst du auch besser dokumentieren.
