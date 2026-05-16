# Aufgaben

## Aufgabe 1: PCAP vorbereiten

Prüfe, ob bereits eine passende PCAP existiert:

```bash
ls -lh pcaps/generated/lab-basic-020-dns-http-docker.pcapng
```

Wenn ja, nutze diese Datei.

Wenn nein, erzeuge eine neue Datei.

Docker-Lab starten:

```bash
docker compose -f docker/compose/lab-basic-dns-http/compose.yml up -d
```

Capture starten:

```bash
mkdir -p pcaps/generated

sudo tshark -i any -f "net 172.28.50.0/24" \
  -w pcaps/generated/lab-basic-010-display-filter.pcapng
```

In einem zweiten Terminal Traffic erzeugen:

```bash
docker compose -f docker/compose/lab-basic-dns-http/compose.yml exec lab-client sh -lc '
dig web-ok.lab.local
dig web-slow.lab.local
dig does-not-exist.lab.local
curl -I http://web-ok.lab.local
curl -I http://web-slow.lab.local
'
```

Capture mit `Ctrl + C` stoppen.

Lab stoppen:

```bash
docker compose -f docker/compose/lab-basic-dns-http/compose.yml down
```

## Aufgabe 2: PCAP öffnen

Öffne die PCAP in Wireshark.

Beispiel:

```bash
wireshark pcaps/generated/lab-basic-020-dns-http-docker.pcapng
```

oder:

```bash
wireshark pcaps/generated/lab-basic-010-display-filter.pcapng
```

## Aufgabe 3: einfache Protokollfilter testen

Teste:

```text
dns
```

```text
tcp
```

```text
http
```

Notiere:

- Filter
- Trefferanzahl
- was der Filter zeigt
- was der Filter nicht zeigt

## Aufgabe 4: IP-Filter testen

Nutze bekannte Lab-IP-Adressen:

```text
ip.addr == 172.28.50.100
```

```text
ip.src == 172.28.50.100
```

```text
ip.dst == 172.28.50.100
```

Beantworte:

- Was ist der Unterschied zwischen `ip.addr`, `ip.src` und `ip.dst`?
- Wann wäre welcher Filter sinnvoll?

## Aufgabe 5: Portfilter testen

Teste:

```text
tcp.port == 80
```

```text
udp.port == 53
```

```text
tcp.dstport == 80
```

```text
tcp.srcport == 80
```

Beantworte:

- Welcher Filter zeigt beide Richtungen?
- Welcher Filter zeigt nur Anfragen zum Serverport?
- Welcher Filter zeigt Antworten vom Serverport?

## Aufgabe 6: DNS Query und Response trennen

Teste:

```text
dns.flags.response == 0
```

```text
dns.flags.response == 1
```

Beantworte:

- Welche Pakete sind Queries?
- Welche Pakete sind Responses?
- Welche Namen wurden abgefragt?

## Aufgabe 7: DNS NXDOMAIN finden

Teste:

```text
dns.flags.rcode == 3
```

Zusätzlich:

```text
dns.qry.name contains "does-not-exist"
```

Beantworte:

- Welcher Name liefert NXDOMAIN?
- Welche Frame-Nummer belegt das?
- Warum ist NXDOMAIN kein HTTP-Fehler?

## Aufgabe 8: HTTP Request und Response trennen

Teste:

```text
http.request
```

```text
http.response
```

```text
http.response.code == 200
```

Beantworte:

- Welche Requests sind sichtbar?
- Welche Responses sind sichtbar?
- Welche Statuscodes sind sichtbar?

## Aufgabe 9: `contains` verwenden

Teste:

```text
dns.qry.name contains "web"
```

```text
http.host contains "lab.local"
```

Beantworte:

- Welche Treffer liefert `contains`?
- Warum ist `contains` praktisch?
- Warum sollte man es nicht blind überall verwenden?

## Aufgabe 10: logische Operatoren verwenden

Teste:

```text
dns or http
```

```text
dns and ip.addr == 172.28.50.53
```

```text
http and ip.addr == 172.28.50.20
```

```text
(dns or http) and ip.addr == 172.28.50.100
```

Beantworte:

- Was bewirkt `or`?
- Was bewirkt `and`?
- Warum helfen Klammern?

## Aufgabe 11: Negation verwenden

Teste:

```text
not dns
```

```text
tcp and not http
```

```text
ip.addr == 172.28.50.100 and not dns
```

Beantworte:

- Was blendet Negation aus?
- Warum kann Negation zu Fehlinterpretationen führen?
- Warum sollte man Negation immer bewusst formulieren?

## Aufgabe 12: TCP Stream Filter

Suche ein HTTP-Paket und ermittle den TCP Stream Index.

Filtere dann:

```text
tcp.stream == <nummer>
```

Beantworte:

- Welche Pakete gehören zu diesem Stream?
- Sind DNS-Pakete im TCP Stream enthalten?
- Warum nicht?

## Aufgabe 13: TShark Gegenprüfung

Setze die PCAP-Variable passend:

```bash
PCAP="pcaps/generated/lab-basic-020-dns-http-docker.pcapng"
```

oder:

```bash
PCAP="pcaps/generated/lab-basic-010-display-filter.pcapng"
```

Treffer zählen:

```bash
tshark -r "$PCAP" -Y "dns" | wc -l
tshark -r "$PCAP" -Y "http" | wc -l
tshark -r "$PCAP" -Y "dns.flags.rcode == 3" | wc -l
```

DNS-Namen ausgeben:

```bash
tshark -r "$PCAP" \
  -Y "dns.flags.response == 0" \
  -T fields \
  -e frame.number \
  -e dns.qry.name
```

HTTP-Responses ausgeben:

```bash
tshark -r "$PCAP" \
  -Y "http.response" \
  -T fields \
  -e frame.number \
  -e ip.src \
  -e http.response.code \
  -e http.response.phrase
```

## Aufgabe 14: Check-Skript ausführen

```bash
bash labs/basic/lab-basic-010-display-filter/check_tshark.sh "$PCAP"
```

## Aufgabe 15: Filtertabelle erstellen

Erstelle eine Tabelle:

```text
Filter | Treffer | Zweck | Beobachtung
```

Mindestens enthalten:

- `dns`
- `dns.flags.response == 0`
- `dns.flags.response == 1`
- `dns.flags.rcode == 3`
- `http`
- `http.request`
- `http.response`
- `tcp.port == 80`
- `ip.addr == 172.28.50.100`
- ein kombinierter Filter mit `and`
- ein kombinierter Filter mit `or`
- ein Filter mit `not`
- ein Filter mit `contains`
