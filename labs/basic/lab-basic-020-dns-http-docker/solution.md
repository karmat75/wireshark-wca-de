# Musterlösung

Die genauen Frame-Nummern hängen von deinem Capture ab.

Die fachlichen Beobachtungen sollten aber ähnlich sein.

## Erwartete DNS-Beobachtungen

Filter:

```text
dns
```

Erwartete Namen:

```text
web-ok.lab.local
web-slow.lab.local
does-not-exist.lab.local
```

Erwartete Antworten:

| Name | Erwartung |
|---|---|
| `web-ok.lab.local` | A Record `172.28.50.10` |
| `web-slow.lab.local` | A Record `172.28.50.20` |
| `does-not-exist.lab.local` | NXDOMAIN |

NXDOMAIN-Filter:

```text
dns.flags.rcode == 3
```

Beispielbewertung:

```text
Der Name `does-not-exist.lab.local` wird vom Lab-DNS-Server mit NXDOMAIN beantwortet. Damit ist belegt, dass der DNS-Server diesen Namen nicht kennt.
```

## Erwartete HTTP-Beobachtungen

Filter:

```text
http
```

Erwartete Requests:

```text
HEAD / HTTP/1.1
```

zu:

```text
web-ok.lab.local
web-slow.lab.local
```

Erwartete Responses:

```text
HTTP/1.1 200 OK
```

oder je nach Server:

```text
HTTP/1.0 200 OK
```

## Normaler Webserver

Filter:

```text
ip.addr == 172.28.50.10 and http
```

Erwartung:

- Request sichtbar
- Response kommt schnell
- Statuscode 200

Bewertung:

```text
Der normale Webserver antwortet erfolgreich und ohne absichtliche Verzögerung.
```

## Langsamer Webserver

Filter:

```text
ip.addr == 172.28.50.20 and http
```

Erwartung:

- Request sichtbar
- Response kommt etwa 2 Sekunden später
- Statuscode 200
- Header `X-WWCA-Lab: slow-response` kann sichtbar sein

Bewertung:

```text
Die Wartezeit entsteht zwischen HTTP Request und HTTP Response. Im Lab ist diese Verzögerung absichtlich serverseitig eingebaut. Im Capture zeigt sie sich als Zeitabstand zwischen Anfrage und Antwort.
```

## Beispiel-Kurzbericht

```text
Capture-Punkt:
Host-System, Interface any, Filter net 172.28.50.0/24

DNS:
Der Client 172.28.50.100 fragt den Lab-DNS-Server 172.28.50.53 nach web-ok.lab.local, web-slow.lab.local und does-not-exist.lab.local.
web-ok.lab.local wird mit 172.28.50.10 beantwortet.
web-slow.lab.local wird mit 172.28.50.20 beantwortet.
does-not-exist.lab.local wird mit NXDOMAIN beantwortet.

HTTP:
Der Client sendet HTTP Requests an 172.28.50.10 und 172.28.50.20.
Beide Server antworten mit 200 OK.
Beim langsamen Server liegt zwischen Request und Response eine Verzögerung von ungefähr 2 Sekunden.

Bewertung:
DNS und HTTP funktionieren grundsätzlich. Der beobachtete Zeitunterschied beim langsamen Webserver entsteht im Lab auf Anwendungsebene, nicht durch sichtbaren Paketverlust.

Verwendete Filter:
dns
dns.flags.rcode == 3
http
ip.addr == 172.28.50.10 and http
ip.addr == 172.28.50.20 and http
```

## Einschränkungen

Dieses Lab beweist nicht:

- reale Internet-Erreichbarkeit
- Verhalten echter DNS-Resolver
- TLS-Verhalten
- produktive Netzwerkperformance

Es trainiert kontrolliert:

- DNS
- NXDOMAIN
- HTTP
- Zeitabstand zwischen Request und Response
