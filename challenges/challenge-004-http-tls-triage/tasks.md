# Aufgaben

## Aufgabe 1: Lab starten

Aus dem Repository-Root:

```bash
docker compose -f docker/compose/lab-advanced-http-tls/compose.yml up -d --build
```

Prüfen:

```bash
docker compose -f docker/compose/lab-advanced-http-tls/compose.yml ps
```

## Aufgabe 2: Capture starten

Ordner vorbereiten:

```bash
mkdir -p pcaps/generated
```

Capture starten:

```bash
sudo tshark -i any -f "net 172.28.70.0/24" \
  -w pcaps/generated/challenge-004-http-tls-triage.pcapng
```

## Aufgabe 3: Testtraffic erzeugen

In einem zweiten Terminal:

```bash
docker compose -f docker/compose/lab-advanced-http-tls/compose.yml exec lab-client sh -lc '
curl --noproxy "*" -I http://172.28.70.10/
curl --noproxy "*" http://172.28.70.10/ >/tmp/http-page.html
curl --noproxy "*" -k --resolve secure.lab.local:443:172.28.70.10 -I https://secure.lab.local/
curl --noproxy "*" -k --resolve secure.lab.local:443:172.28.70.10 https://secure.lab.local/ >/tmp/https-page.html
curl --noproxy "*" --connect-timeout 3 --max-time 5 --resolve secure.lab.local:443:172.28.70.10 -I https://secure.lab.local/ || true
'
```

## Aufgabe 4: Capture stoppen

Stoppe TShark mit:

```text
Ctrl + C
```

Öffne den Capture:

```bash
wireshark pcaps/generated/challenge-004-http-tls-triage.pcapng
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
- Welche TCP-Ports sind beteiligt?
- Welche Conversations gehören zu HTTP?
- Welche Conversations gehören zu TLS?

## Aufgabe 6: HTTP analysieren

Nutze passende Filter, zum Beispiel:

```text
http
```

```text
http.request
```

```text
http.response
```

Beantworte mit Frame-Nummern:

- Welche HTTP Requests sind sichtbar?
- Welche HTTP Responses sind sichtbar?
- Welche Statuscodes sind sichtbar?
- Sind Header im Klartext sichtbar?
- Ist der HTML-Inhalt im Klartext sichtbar?

## Aufgabe 7: TLS analysieren

Nutze passende Filter, zum Beispiel:

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

Beantworte mit Frame-Nummern:

- Wo ist der TLS Client Hello?
- Ist SNI sichtbar?
- Welcher Hostname ist sichtbar?
- Ist ALPN sichtbar?
- Sind TLS Alerts sichtbar?
- Wo ist TLS Application Data sichtbar?

## Aufgabe 8: Vergleich formulieren

Schreibe eine kurze Bewertung:

- Was ist bei HTTP im Klartext sichtbar?
- Was ist bei HTTPS/TLS geschützt?
- Welche Metadaten bleiben sichtbar?
- Was bedeutet ein TLS Alert im Lab?
- Welche Aussage wäre zu stark?

## Aufgabe 9: TShark-Check ausführen

```bash
bash challenges/challenge-004-http-tls-triage/check_tshark.sh \
  pcaps/generated/challenge-004-http-tls-triage.pcapng
```

## Aufgabe 10: Lab stoppen

```bash
docker compose -f docker/compose/lab-advanced-http-tls/compose.yml down
```
