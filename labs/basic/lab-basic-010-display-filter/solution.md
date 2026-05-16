# Musterlösung

Die Trefferzahlen hängen von deiner PCAP ab.

Die Filter und fachlichen Aussagen sollten aber ähnlich sein.

## Einfache Protokollfilter

| Filter | Erwartung |
|---|---|
| `dns` | zeigt DNS Query und DNS Response |
| `tcp` | zeigt TCP-Verkehr, unter anderem HTTP |
| `http` | zeigt HTTP Request und Response |

Bewertung:

```text
Protokollfilter sind ein guter Einstieg, aber oft zu breit für eine gezielte Analyse.
```

## IP-Filter

| Filter | Bedeutung |
|---|---|
| `ip.addr == 172.28.50.100` | Quelle oder Ziel ist der Client |
| `ip.src == 172.28.50.100` | Client ist Quelle |
| `ip.dst == 172.28.50.100` | Client ist Ziel |

Bewertung:

```text
`ip.addr` ist praktisch für beide Richtungen. `ip.src` und `ip.dst` sind genauer, wenn die Richtung wichtig ist.
```

## Portfilter

| Filter | Bedeutung |
|---|---|
| `tcp.port == 80` | TCP-Verkehr mit Port 80 in beide Richtungen |
| `tcp.dstport == 80` | typischerweise Anfragen zum Webserver |
| `tcp.srcport == 80` | typischerweise Antworten vom Webserver |
| `udp.port == 53` | klassischer DNS-Verkehr über UDP |

## DNS Query und Response

Queries:

```text
dns.flags.response == 0
```

Responses:

```text
dns.flags.response == 1
```

Erwartete Namen:

```text
web-ok.lab.local
web-slow.lab.local
does-not-exist.lab.local
```

## NXDOMAIN

Filter:

```text
dns.flags.rcode == 3
```

Erwartung:

```text
does-not-exist.lab.local
```

Bewertung:

```text
NXDOMAIN ist eine DNS-Antwort und bedeutet, dass der Name laut antwortendem DNS-Server nicht existiert. Es ist kein HTTP-Statuscode.
```

## HTTP

Requests:

```text
http.request
```

Responses:

```text
http.response
```

Statuscode 200:

```text
http.response.code == 200
```

Erwartung:

```text
HTTP Request zu web-ok.lab.local
HTTP Request zu web-slow.lab.local
HTTP Response 200 OK
```

## `contains`

Beispiele:

```text
dns.qry.name contains "web"
```

```text
http.host contains "lab.local"
```

Bewertung:

```text
`contains` ist praktisch für Textsuche in bestimmten Feldern. Es ist aber weniger präzise als ein exakter Vergleich und sollte bewusst verwendet werden.
```

## Logische Operatoren

Beispiele:

```text
dns or http
```

zeigt DNS oder HTTP.

```text
dns and ip.addr == 172.28.50.53
```

zeigt DNS-Verkehr mit dem DNS-Server.

```text
(dns or http) and ip.addr == 172.28.50.100
```

zeigt DNS oder HTTP, aber nur mit Beteiligung des Clients.

Bewertung:

```text
Klammern machen komplexe Filter lesbarer und vermeiden Missverständnisse.
```

## Negation

Beispiele:

```text
not dns
```

```text
tcp and not http
```

Bewertung:

```text
Negation blendet aus, kann aber schnell zu Fehlinterpretationen führen. Man sollte immer dokumentieren, was ausgeschlossen wurde.
```

## TCP Stream

Filter:

```text
tcp.stream == <nummer>
```

Bewertung:

```text
Ein TCP Stream isoliert eine TCP-Verbindung. DNS-Pakete aus diesem Lab sind nicht im HTTP-TCP-Stream enthalten, weil DNS hier über UDP läuft.
```

## Beispiel-Filtertabelle

| Filter | Zweck | Beobachtung |
|---|---|---|
| `dns` | DNS anzeigen | Query und Response sichtbar |
| `dns.flags.response == 0` | DNS Queries | abgefragte Namen sichtbar |
| `dns.flags.response == 1` | DNS Responses | Antworten sichtbar |
| `dns.flags.rcode == 3` | DNS Fehler NXDOMAIN | nicht existierender Name sichtbar |
| `http` | HTTP anzeigen | Requests und Responses sichtbar |
| `http.request` | HTTP Requests | HEAD/GET sichtbar |
| `http.response` | HTTP Responses | Statuscodes sichtbar |
| `tcp.port == 80` | Web-TCP-Verkehr | beide Richtungen sichtbar |
| `ip.addr == 172.28.50.100` | Client-Verkehr | Client als Quelle oder Ziel |
| `http and ip.addr == 172.28.50.20` | HTTP mit slow server | langsamer Server isoliert |
| `dns or http` | DNS und HTTP | beide Protokolle sichtbar |
| `not dns` | DNS ausblenden | alle Nicht-DNS-Pakete |
| `dns.qry.name contains "web"` | Namen mit web | web-ok und web-slow |

## Merksatz

> Display Filter sind Analysewerkzeuge.  
> Ein guter Filter beantwortet eine konkrete Frage und verändert den Capture nicht.
