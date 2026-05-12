# HTTP und TLS

HTTP und TLS sind in Wireshark besonders wichtig, weil sehr viele moderne Anwendungen darüber kommunizieren.

Gleichzeitig ist dieser Bereich eine häufige Quelle für Fehlinterpretationen.

Bei HTTP ohne TLS kannst du viel sehen.

Bei HTTPS siehst du zwar weiterhin Verbindungsaufbau, Zeitverhalten und TLS-Metadaten, aber normalerweise nicht den eigentlichen HTTP-Inhalt.

## Ziel

Nach diesem Abschnitt solltest du können:

- HTTP Requests und Responses erkennen
- HTTP-Methoden, Statuscodes und Header einordnen
- Redirects erkennen
- HTTP ohne TLS von HTTPS unterscheiden
- TLS Handshake und TLS Application Data einordnen
- Client Hello, Server Hello und SNI finden, wenn sichtbar
- Zertifikatsinformationen finden, wenn sie im Capture enthalten sind
- ALPN und HTTP/2 grob einordnen
- verschlüsselte Nutzdaten korrekt bewerten
- typische Web- und TLS-Fehlerbilder sauber beschreiben

## HTTP in einem Satz

HTTP ist ein Anwendungsprotokoll.

Es beschreibt, wie ein Client Anfragen an einen Server stellt und wie der Server antwortet.

Vereinfacht:

```text
Client -> Server: GET /index.html
Server -> Client: HTTP/1.1 200 OK
```

HTTP läuft klassisch über TCP.

Typische Ports:

| Protokoll | Port | Sichtbarkeit |
|---|---:|---|
| HTTP | 80 | Inhalt meist sichtbar |
| HTTPS | 443 | Inhalt durch TLS verschlüsselt |
| HTTP Proxy | 3128 / 8080 | abhängig von Umgebung |
| HTTP/3 | UDP 443 | QUIC, nicht klassisches TCP/TLS |

AHA:

> HTTP ist die Anwendungsebene. TCP transportiert. TLS verschlüsselt.

## HTTP ohne TLS

HTTP ohne TLS ist in Wireshark sehr gut lesbar.

Filter:

```text
http
```

Typische Paketdetails:

```text
Hypertext Transfer Protocol
    GET / HTTP/1.1
    Host: example.org
    User-Agent: curl/...
```

Response:

```text
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: ...
```

Hier kannst du oft sehen:

- Methode
- Pfad
- Host
- Header
- Statuscode
- Content-Type
- Server-Header
- Redirect-Ziel
- teilweise Nutzdaten

## HTTP Request

Ein HTTP Request ist die Anfrage des Clients.

Wichtige Bestandteile:

| Bestandteil | Beispiel | Bedeutung |
|---|---|---|
| Methode | `GET` | Ressource abrufen |
| Pfad | `/index.html` | angefragter Pfad |
| Host | `example.org` | Zielname |
| User-Agent | `curl/...` | Client-Software |
| Accept | `text/html` | gewünschte Inhalte |
| Authorization | `Bearer ...` | Anmeldedaten oder Token |

!!! warning "Sensible Daten"
    HTTP ohne TLS kann sensible Daten im Klartext enthalten, zum Beispiel Cookies, Tokens, Formulardaten oder Basic-Auth.  
    Captures mit HTTP-Inhalten müssen besonders vorsichtig behandelt werden.

## HTTP Response

Eine HTTP Response ist die Antwort des Servers.

Wichtige Bestandteile:

| Bestandteil | Beispiel | Bedeutung |
|---|---|---|
| Statuscode | `200` | Anfrage erfolgreich |
| Statuscode | `301` / `302` | Weiterleitung |
| Statuscode | `401` | Authentifizierung nötig |
| Statuscode | `403` | verboten |
| Statuscode | `404` | nicht gefunden |
| Statuscode | `500` | Serverfehler |
| Content-Type | `text/html` | Inhaltstyp |
| Location | `https://...` | Redirect-Ziel |
| Set-Cookie | `session=...` | Cookie wird gesetzt |

## Wichtige HTTP-Filter

Alle HTTP-Pakete:

```text
http
```

HTTP Requests:

```text
http.request
```

HTTP Responses:

```text
http.response
```

Bestimmte Methode:

```text
http.request.method == "GET"
```

Bestimmter Host:

```text
http.host contains "example"
```

Statuscode:

```text
http.response.code == 200
```

Redirects:

```text
http.response.code >= 300 and http.response.code < 400
```

Serverfehler:

```text
http.response.code >= 500
```

## Redirects erkennen

Redirects sind HTTP-Antworten, die den Client auf eine andere URL verweisen.

Typische Statuscodes:

| Statuscode | Bedeutung |
|---|---|
| 301 | dauerhaft verschoben |
| 302 | temporär verschoben |
| 307 | temporäre Weiterleitung, Methode bleibt erhalten |
| 308 | dauerhafte Weiterleitung, Methode bleibt erhalten |

Wichtiger Header:

```text
Location
```

AHA:

> Ein Redirect ist nicht automatisch ein Fehler.  
> Viele Webseiten leiten absichtlich von HTTP auf HTTPS oder von einer alten URL auf eine neue URL um.

Filter:

```text
http.response.code >= 300 and http.response.code < 400
```

## Follow TCP Stream bei HTTP

Bei unverschlüsseltem HTTP ist `Follow TCP Stream` sehr hilfreich.

In Wireshark:

```text
Right Click > Follow > TCP Stream
```

Du siehst dann oft Request und Response im Zusammenhang.

Nutze das vorsichtig, weil sensible Daten sichtbar sein können.

AHA:

> Follow TCP Stream ist bei HTTP sehr mächtig. Bei HTTPS siehst du dort normalerweise verschlüsselte Daten.

## HTTPS: HTTP in TLS

HTTPS ist vereinfacht:

```text
HTTP
in TLS
in TCP
in IP
in Ethernet
```

In Wireshark siehst du bei HTTPS typischerweise:

```text
Transmission Control Protocol
Transport Layer Security
```

Filter:

```text
tls
```

oder auf den Port:

```text
tcp.port == 443
```

Wichtig:

> HTTPS bedeutet nicht, dass nichts sichtbar ist.  
> HTTPS bedeutet, dass der HTTP-Inhalt normalerweise nicht sichtbar ist.

## Was bei HTTPS sichtbar bleibt

Auch bei HTTPS kannst du viel analysieren:

- IP-Adressen
- TCP-Ports
- TCP-Handshake
- TLS-Handshake
- Zeitverhalten
- Paketgrößen
- SNI, wenn sichtbar
- ALPN, wenn sichtbar
- Zertifikatsinformationen, je nach TLS-Version und Capture
- Verbindungsabbrüche
- TCP-Probleme
- TLS Alerts

Was du normalerweise nicht siehst:

- vollständige URL inklusive Pfad
- HTTP Header
- Cookies
- Formulardaten
- API-Payload
- Antwortinhalt

## TLS Handshake

Der TLS Handshake baut die gesicherte Verbindung auf.

Vereinfacht:

```text
Client Hello
Server Hello
Zertifikat / Parameter
Schlüsselmaterial wird ausgehandelt
verschlüsselte Kommunikation beginnt
```

In Wireshark siehst du zum Beispiel:

```text
Client Hello
Server Hello
Application Data
Alert
```

Wichtige Filter:

```text
tls.handshake
```

Client Hello:

```text
tls.handshake.type == 1
```

Server Hello:

```text
tls.handshake.type == 2
```

TLS Alerts:

```text
tls.alert_message
```

## Client Hello

Der Client Hello ist oft besonders interessant.

Darin können sichtbar sein:

- unterstützte TLS-Versionen
- Cipher Suites
- Extensions
- SNI
- ALPN
- Supported Groups
- Signature Algorithms

AHA:

> Der Client Hello sagt viel darüber, was der Client anbietet und welchen Namen er erreichen möchte.

## SNI

SNI steht für Server Name Indication.

Damit teilt der Client dem Server im TLS Handshake mit, welchen Hostnamen er erreichen möchte.

Das ist wichtig, weil mehrere HTTPS-Webseiten auf derselben IP-Adresse laufen können.

Filter:

```text
tls.handshake.extensions_server_name
```

oder:

```text
tls.handshake.extensions_server_name contains "example"
```

Je nach TLS-Version, Client, Server oder neueren Schutzmechanismen ist SNI nicht immer sichtbar.

!!! note "SNI ist hilfreich, aber nicht garantiert"
    Wenn du kein SNI siehst, heißt das nicht automatisch, dass kein Hostname verwendet wurde.  
    Prüfe TLS-Version, Clientverhalten, Capture-Punkt und ob neuere Mechanismen im Spiel sind.

## ALPN

ALPN steht für Application-Layer Protocol Negotiation.

Damit wird im TLS Handshake ausgehandelt, welches Anwendungsprotokoll über TLS gesprochen wird.

Beispiele:

```text
http/1.1
h2
```

`h2` steht für HTTP/2.

Filter können je nach Wireshark-Version variieren, oft findest du ALPN im Client Hello oder Server Hello unter TLS Extensions.

AHA:

> ALPN hilft dir zu verstehen, ob über TLS zum Beispiel HTTP/1.1 oder HTTP/2 verwendet wird.

## Zertifikate in Wireshark

Je nach TLS-Version und Verbindung kannst du Zertifikatsinformationen sehen.

Mögliche Informationen:

- Subject
- Issuer
- Gültigkeitszeitraum
- Subject Alternative Names
- Zertifikatskette

Filter:

```text
tls.handshake.certificate
```

Zertifikatsprobleme sind in Wireshark aber nicht immer eindeutig sichtbar.

Die eigentliche Validierung macht der Client.

Wenn ein Browser ein Zertifikat ablehnt, kann Wireshark Hinweise liefern, aber du brauchst oft zusätzlich:

- Browser-Fehlermeldung
- OpenSSL-Test
- Systemzeit
- Zertifikatskette
- Trust Store
- Serverkonfiguration

## TLS Alerts

TLS Alerts zeigen Probleme oder Zustandsmeldungen innerhalb von TLS.

Filter:

```text
tls.alert_message
```

Typische Beobachtungen:

- Handshake Failure
- Bad Certificate
- Unknown CA
- Close Notify
- Protocol Version
- Internal Error

AHA:

> Ein TLS Alert ist ein starker Hinweis, aber die genaue Ursache muss im Kontext geprüft werden.

`Close Notify` ist oft ein normaler sauberer TLS-Abschluss.

## HTTP/2

HTTP/2 wird häufig über TLS verwendet und per ALPN als `h2` ausgehandelt.

In Wireshark kann HTTP/2 sichtbar sein, wenn die Daten entschlüsselt werden oder wenn Klartextvarianten im Spiel sind.

Ohne Entschlüsselung siehst du bei normalem HTTPS meistens TLS Application Data.

Wichtig für die Analyse:

- HTTP/2 kann mehrere Streams über eine TCP-Verbindung multiplexen
- ein TCP-Problem kann mehrere HTTP/2-Streams beeinflussen
- ohne Entschlüsselung siehst du die einzelnen HTTP/2-Requests normalerweise nicht

## HTTP/3 und QUIC

HTTP/3 verwendet QUIC über UDP, meistens UDP-Port 443.

Das sieht anders aus als klassisches HTTPS über TCP.

Filter:

```text
udp.port == 443
```

oder je nach Erkennung:

```text
quic
```

AHA:

> Wenn du bei einer modernen Webseite keinen TCP-Port 443 Stream findest, prüfe UDP 443 und QUIC.

HTTP/3 ist für diesen Abschnitt nur als Orientierung wichtig. Tiefer behandeln wir es später oder in einem eigenen Referenzartikel.

## Zeitverhalten bei HTTP und TLS

Bei Webproblemen zerlege die Verbindung:

1. DNS Query bis DNS Response
2. TCP SYN bis SYN/ACK
3. TLS Client Hello bis Server Hello / Abschluss
4. Request bis erste Response oder Application Data
5. Datenübertragung
6. Verbindungsende

Mögliche Aussagen:

| Beobachtung | Mögliche Richtung |
|---|---|
| DNS langsam | DNS-Server, Upstream, Netzweg |
| TCP Handshake langsam | RTT, Routing, Firewall, Server-Erreichbarkeit |
| TLS Handshake langsam | TLS, Server, Paketverlust, Zertifikats-/Policy-Themen |
| Request bis Response langsam | Anwendung, Backend, Serverlast |
| Retransmissions | Paketverlust oder Capture-Thema |
| Zero Window | Empfänger kann nicht schnell genug lesen |

## HTTP-Fehler vs. Netzwerkfehler

HTTP-Statuscodes sind Anwendungsebene.

Beispiel:

```text
HTTP/1.1 404 Not Found
```

Das ist kein Netzwerkfehler.

Es bedeutet:

- TCP funktioniert
- HTTP funktioniert
- Server hat geantwortet
- die angefragte Ressource wurde nicht gefunden

Beispiel:

```text
HTTP/1.1 500 Internal Server Error
```

Auch das ist nicht automatisch Netzwerk.

Es bedeutet:

- Server hat geantwortet
- Anwendung oder Backend meldet Fehler

AHA:

> Ein HTTP-Fehlercode beweist oft eher, dass Netzwerk und Transport grundsätzlich funktioniert haben.

## Typische Analysefragen

Bei HTTP:

- Welche URL oder welcher Host wurde angefragt?
- Welche Methode wurde verwendet?
- Welcher Statuscode kam zurück?
- Gab es Redirects?
- Wie lange dauerte es bis zur Response?
- Gibt es mehrere Requests?
- Gibt es Serverfehler?
- Sind sensible Daten im Klartext sichtbar?

Bei HTTPS:

- Gibt es DNS?
- Gibt es TCP Handshake?
- Gibt es TLS Client Hello?
- Ist SNI sichtbar?
- Ist ALPN sichtbar?
- Gibt es TLS Alerts?
- Gibt es Application Data?
- Gibt es TCP-Probleme?
- Wo entsteht Wartezeit?

## TShark-Beispiele

HTTP Requests ausgeben:

```bash
tshark -r capture.pcapng \
  -Y "http.request" \
  -T fields \
  -e frame.number \
  -e frame.time_relative \
  -e ip.src \
  -e ip.dst \
  -e http.request.method \
  -e http.host \
  -e http.request.uri
```

HTTP Responses ausgeben:

```bash
tshark -r capture.pcapng \
  -Y "http.response" \
  -T fields \
  -e frame.number \
  -e frame.time_relative \
  -e ip.src \
  -e ip.dst \
  -e http.response.code \
  -e http.response.phrase
```

Redirects finden:

```bash
tshark -r capture.pcapng \
  -Y "http.response.code >= 300 and http.response.code < 400" \
  -T fields \
  -e frame.number \
  -e http.response.code \
  -e http.location
```

TLS Client Hello mit SNI ausgeben:

```bash
tshark -r capture.pcapng \
  -Y "tls.handshake.type == 1" \
  -T fields \
  -e frame.number \
  -e frame.time_relative \
  -e ip.src \
  -e ip.dst \
  -e tls.handshake.extensions_server_name
```

TLS Alerts ausgeben:

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

QUIC/UDP 443 prüfen:

```bash
tshark -r capture.pcapng -Y "udp.port == 443 or quic"
```

## Mini-Aufgabe: HTTP ohne TLS

Erzeuge einen Capture.

1. Starte Wireshark oder TShark.
2. Führe aus:

```bash
curl -v http://example.org
```

3. Stoppe den Mitschnitt.
4. Speichere ihn als:

```text
pcaps/generated/advanced-http-01.pcapng
```

5. Öffne ihn in Wireshark.

Beantworte:

- Welche DNS-Anfrage wurde gestellt?
- Welche TCP-Verbindung wurde aufgebaut?
- Welcher HTTP Request wurde gesendet?
- Welcher HTTP Statuscode kam zurück?
- Gibt es einen Redirect?
- Welche Header sind sichtbar?
- Welche sensiblen Informationen könnten bei HTTP grundsätzlich sichtbar sein?

## Mini-Aufgabe: HTTPS mit TLS

Erzeuge einen Capture.

1. Starte Wireshark oder TShark.
2. Führe aus:

```bash
curl -v https://example.org
```

3. Stoppe den Mitschnitt.
4. Speichere ihn als:

```text
pcaps/generated/advanced-tls-01.pcapng
```

5. Öffne ihn in Wireshark.

Beantworte:

- Welche TCP-Verbindung gehört zum Aufruf?
- Siehst du TLS Client Hello?
- Ist SNI sichtbar?
- Siehst du Server Hello?
- Siehst du TLS Application Data?
- Siehst du HTTP-Inhalte?
- Gibt es TLS Alerts?
- Welche Aussage kannst du trotz Verschlüsselung treffen?

## Analysebericht: HTTP

```text
Symptom:
<kurze Beschreibung>

Capture-Punkt:
<Client / Server / Gateway / unbekannt>

DNS:
<kurze Bewertung>

TCP:
<Handshake und Stream>

HTTP Request:
Frame <nummer>: <Methode> <Host><URI>

HTTP Response:
Frame <nummer>: Status <code> <phrase>

Redirect:
ja/nein, Location: <ziel>

Bewertung:
<fachliche Einordnung>

Verwendete Filter:
http
http.request
http.response
```

## Analysebericht: TLS

```text
Symptom:
<kurze Beschreibung>

Capture-Punkt:
<Client / Server / Gateway / unbekannt>

TCP Stream:
tcp.stream == <nummer>

TLS Handshake:
Client Hello: Frame <nummer>
Server Hello: Frame <nummer>
SNI: <sichtbar / nicht sichtbar>
ALPN: <sichtbar / nicht sichtbar>
Zertifikat: <sichtbar / nicht sichtbar>
TLS Alert: <ja/nein>

Application Data:
sichtbar / nicht sichtbar

Bewertung:
<fachliche Einordnung>

Nicht sichtbar:
HTTP-Pfad, HTTP-Header und Payload sind ohne Entschlüsselung nicht lesbar.

Verwendete Filter:
tls
tls.handshake
tls.alert_message
```

## Typische Fehlinterpretationen

| Beobachtung | Falscher Schluss | Bessere Bewertung |
|---|---|---|
| kein HTTP bei HTTPS sichtbar | Wireshark funktioniert nicht | HTTP ist durch TLS verschlüsselt |
| TLS Application Data | unbekanntes Protokoll | verschlüsselte Nutzdaten |
| HTTP 404 | Netzwerkfehler | Server antwortet, Ressource fehlt |
| HTTP 500 | Netzwerkfehler | Anwendung oder Backend meldet Fehler |
| Redirect | Fehler | oft normales Verhalten |
| kein SNI sichtbar | kein Hostname | SNI kann fehlen oder verborgen sein |
| TLS Alert | immer kritisch | Alert-Typ und Kontext prüfen |
| UDP 443 sichtbar | komisch | kann QUIC/HTTP/3 sein |

## WCA-Bezug

Dieser Abschnitt übt WCA-nahe Fähigkeiten:

- Anwendungsprotokolle in Captures erkennen
- HTTP Request und Response analysieren
- Statuscodes und Header einordnen
- TLS Handshake und TLS-Metadaten erkennen
- Verschlüsselungsgrenzen korrekt bewerten
- Zeitverhalten von DNS, TCP, TLS und Anwendung unterscheiden
- Display Filter und TShark für HTTP/TLS verwenden
- Beobachtungen sauber dokumentieren

## Merksatz

> Bei HTTP siehst du oft den Inhalt.  
> Bei HTTPS siehst du meistens die Verbindung, den Handshake, das Zeitverhalten und Metadaten — aber nicht den eigentlichen Inhalt.
