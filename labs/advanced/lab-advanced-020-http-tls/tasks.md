# Aufgaben

## Aufgabe 1: Docker-Lab starten

Aus dem Repository-Root:

```bash
docker compose -f docker/compose/lab-advanced-http-tls/compose.yml up -d --build
```

Status prüfen:

```bash
docker compose -f docker/compose/lab-advanced-http-tls/compose.yml ps
```

Logs prüfen:

```bash
docker compose -f docker/compose/lab-advanced-http-tls/compose.yml logs lab-web-tls
```

## Aufgabe 2: Capture starten

Ordner vorbereiten:

```bash
mkdir -p pcaps/generated
```

Capture starten:

```bash
sudo tshark -i any -f "net 172.28.70.0/24" \
  -w pcaps/generated/lab-advanced-020-http-tls.pcapng
```

Stoppen später mit:

```text
Ctrl + C
```

Alternativ kannst du Wireshark verwenden und als Capture Filter setzen:

```text
net 172.28.70.0/24
```

## Aufgabe 3: HTTP im Klartext erzeugen

In einem zweiten Terminal:

```bash
docker compose -f docker/compose/lab-advanced-http-tls/compose.yml exec lab-client sh -lc '
curl --noproxy "*" -I http://172.28.70.10/
curl --noproxy "*" http://172.28.70.10/ >/tmp/http-page.html
'
```

## Aufgabe 4: HTTPS mit `-k` erzeugen

```bash
docker compose -f docker/compose/lab-advanced-http-tls/compose.yml exec lab-client sh -lc '
curl --noproxy "*" -k --resolve secure.lab.local:443:172.28.70.10 -I https://secure.lab.local/
curl --noproxy "*" -k --resolve secure.lab.local:443:172.28.70.10 https://secure.lab.local/ >/tmp/https-page.html
'
```

## Aufgabe 5: TLS Alert durch Zertifikatsprüfung erzeugen

Ohne `-k` sollte der Client dem selbstsignierten Zertifikat nicht vertrauen.

```bash
docker compose -f docker/compose/lab-advanced-http-tls/compose.yml exec lab-client sh -lc '
curl --noproxy "*" --connect-timeout 3 --max-time 5 --resolve secure.lab.local:443:172.28.70.10 -I https://secure.lab.local/ || true
'
```

## Aufgabe 6: Capture stoppen

Stoppe TShark mit:

```text
Ctrl + C
```

Öffne die Datei:

```bash
wireshark pcaps/generated/lab-advanced-020-http-tls.pcapng
```

## Aufgabe 7: HTTP analysieren

Teste:

```text
http
```

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

- Welche HTTP Requests sind sichtbar?
- Welche HTTP Responses sind sichtbar?
- Welche Header sind sichtbar?
- Ist der HTML-Inhalt im Klartext sichtbar?
- Welche Frame-Nummern belegen das?

## Aufgabe 8: TLS analysieren

Teste:

```text
tls
```

```text
tls.handshake.type == 1
```

```text
tls.handshake.extensions_server_name
```

```text
tls.handshake.extensions_alpn_str
```

```text
tls.alert_message
```

Beantworte:

- Welche TLS Handshake-Pakete sind sichtbar?
- Ist SNI sichtbar?
- Welcher Hostname wird per SNI angefragt?
- Ist ALPN sichtbar?
- Sind TLS Alerts sichtbar?
- Welche Inhalte sind nicht im Klartext sichtbar?

## Aufgabe 9: HTTP und HTTPS vergleichen

Vergleiche:

```text
tcp.port == 80
```

mit:

```text
tcp.port == 443
```

Beantworte:

- Wo siehst du HTTP-Methoden?
- Wo siehst du HTTP-Statuscodes?
- Wo siehst du TLS Application Data?
- Warum ist das kein Fehler?
- Welche Metadaten bleiben bei HTTPS trotzdem sichtbar?

## Aufgabe 10: TCP Streams isolieren

Isoliere einen HTTP-Stream:

```text
tcp.stream == <http-stream>
```

Isoliere einen TLS-Stream:

```text
tcp.stream == <tls-stream>
```

Beantworte:

- Was zeigt Follow TCP Stream bei HTTP?
- Was zeigt Follow TCP Stream bei TLS?
- Warum ist der Unterschied wichtig?

## Aufgabe 11: TShark-Auswertung

Setze:

```bash
PCAP="pcaps/generated/lab-advanced-020-http-tls.pcapng"
```

HTTP:

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

TLS SNI:

```bash
tshark -r "$PCAP" \
  -Y "tls.handshake.extensions_server_name" \
  -T fields \
  -e frame.number \
  -e frame.time_relative \
  -e ip.src \
  -e ip.dst \
  -e tls.handshake.extensions_server_name
```

TLS Alerts:

```bash
tshark -r "$PCAP" \
  -Y "tls.alert_message" \
  -T fields \
  -e frame.number \
  -e frame.time_relative \
  -e ip.src \
  -e ip.dst \
  -e tls.alert_message.desc
```

## Aufgabe 12: Check-Skript ausführen

```bash
bash labs/advanced/lab-advanced-020-http-tls/check_tshark.sh "$PCAP"
```

## Aufgabe 13: Kurzbericht schreiben

Schreibe einen Bericht:

```text
Capture-Punkt:
<wo wurde mitgeschnitten?>

HTTP:
<sichtbare Requests, Responses, Header>

TLS:
<SNI, ALPN, Alerts, Application Data>

Vergleich:
<was ist bei HTTP sichtbar, was bei HTTPS nicht?>

Bewertung:
<fachliche Einordnung>

Einschränkungen:
<was ist nicht bewiesen?>
```

## Aufgabe 14: Lab stoppen

```bash
docker compose -f docker/compose/lab-advanced-http-tls/compose.yml down
```
