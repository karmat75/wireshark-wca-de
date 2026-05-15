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

## Aufgabe 2: Funktion prüfen

```bash
docker compose -f docker/compose/lab-basic-dns-http/compose.yml exec lab-client dig web-ok.lab.local
docker compose -f docker/compose/lab-basic-dns-http/compose.yml exec lab-client dig web-slow.lab.local
docker compose -f docker/compose/lab-basic-dns-http/compose.yml exec lab-client dig does-not-exist.lab.local
```

HTTP testen:

```bash
docker compose -f docker/compose/lab-basic-dns-http/compose.yml exec lab-client curl -I http://web-ok.lab.local
docker compose -f docker/compose/lab-basic-dns-http/compose.yml exec lab-client curl -I http://web-slow.lab.local
```

## Aufgabe 3: Capture starten

Ordner vorbereiten:

```bash
mkdir -p pcaps/generated
```

Starte auf dem Host einen Capture.

Variante mit TShark:

```bash
sudo tshark -i any -f "net 172.28.50.0/24" -w pcaps/generated/lab-basic-020-dns-http-docker.pcapng
```

Stoppen später mit:

```text
Ctrl + C
```

Alternativ kannst du Wireshark verwenden und als Capture Filter setzen:

```text
net 172.28.50.0/24
```

## Aufgabe 4: Traffic erzeugen

In einem zweiten Terminal:

```bash
docker compose -f docker/compose/lab-basic-dns-http/compose.yml exec lab-client sh -lc '
dig web-ok.lab.local
dig web-slow.lab.local
dig does-not-exist.lab.local
curl -I http://web-ok.lab.local
curl -I http://web-slow.lab.local
'
```

## Aufgabe 5: Capture stoppen

Stoppe den Capture mit:

```text
Ctrl + C
```

Öffne die Datei:

```bash
wireshark pcaps/generated/lab-basic-020-dns-http-docker.pcapng
```

## Aufgabe 6: DNS analysieren

Teste Filter:

```text
dns
```

```text
dns.flags.response == 0
```

```text
dns.flags.response == 1
```

```text
dns.flags.rcode == 3
```

Beantworte:

- Welche Namen wurden abgefragt?
- Welche Namen wurden erfolgreich aufgelöst?
- Welche IP-Adressen wurden geliefert?
- Welcher Name liefert NXDOMAIN?
- Welche Frame-Nummern belegen das?

## Aufgabe 7: HTTP analysieren

Teste Filter:

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
ip.addr == 172.28.50.10
```

```text
ip.addr == 172.28.50.20
```

Beantworte:

- Welche HTTP Requests wurden gesendet?
- Welche HTTP Statuscodes kamen zurück?
- Welcher Server antwortet langsam?
- Wie groß ist der Abstand zwischen Request und Response ungefähr?
- Welche Frame-Nummern belegen das?

## Aufgabe 8: TShark-Auswertung

DNS Queries:

```bash
tshark -r pcaps/generated/lab-basic-020-dns-http-docker.pcapng \
  -Y "dns.flags.response == 0" \
  -T fields \
  -e frame.number \
  -e frame.time_relative \
  -e ip.src \
  -e dns.qry.name
```

DNS Responses:

```bash
tshark -r pcaps/generated/lab-basic-020-dns-http-docker.pcapng \
  -Y "dns.flags.response == 1" \
  -T fields \
  -e frame.number \
  -e frame.time_relative \
  -e ip.src \
  -e ip.dst \
  -e dns.qry.name \
  -e dns.flags.rcode \
  -e dns.a
```

HTTP Responses:

```bash
tshark -r pcaps/generated/lab-basic-020-dns-http-docker.pcapng \
  -Y "http.response" \
  -T fields \
  -e frame.number \
  -e frame.time_relative \
  -e ip.src \
  -e http.response.code \
  -e http.response.phrase
```

## Aufgabe 9: Kurzbericht schreiben

Schreibe einen kurzen Bericht mit:

- Capture-Punkt
- DNS-Beobachtungen
- HTTP-Beobachtungen
- Frame-Nummern
- verwendete Filter
- Bewertung
- Einschränkungen

## Aufgabe 10: Lab stoppen

```bash
docker compose -f docker/compose/lab-basic-dns-http/compose.yml down
```
