# Musterlösung

Die Frame-Nummern hängen von deinem lokal erzeugten Capture ab.

Die fachlichen Beobachtungen sollten aber gleich sein.

## DNS

Filter:

```text
dns
```

Erwartete DNS-Namen:

```text
web-ok.lab.local
web-slow.lab.local
does-not-exist.lab.local
```

Erwartete Antworten:

| Name | Ergebnis |
|---|---|
| `web-ok.lab.local` | A Record `172.28.50.10` |
| `web-slow.lab.local` | A Record `172.28.50.20` |
| `does-not-exist.lab.local` | NXDOMAIN |

NXDOMAIN-Filter:

```text
dns.flags.rcode == 3
```

Bewertung:

```text
DNS funktioniert grundsätzlich für vorhandene Namen in der Zone `lab.local`.
Der Name `does-not-exist.lab.local` existiert erwartungsgemäß nicht und wird mit NXDOMAIN beantwortet.
```

Wichtig:

```text
NXDOMAIN bedeutet nicht, dass HTTP kaputt ist. Es bedeutet, dass dieser Name laut DNS-Server nicht existiert.
```

## HTTP

Filter:

```text
http
```

Erwartete HTTP-Ziele:

| Ziel | IP | Erwartung |
|---|---:|---|
| `web-ok.lab.local` | `172.28.50.10` | schnelle HTTP-Antwort |
| `web-slow.lab.local` | `172.28.50.20` | verzögerte HTTP-Antwort |

HTTP-Responses:

```text
HTTP 200 OK
```

oder je nach Serverdarstellung:

```text
Statuscode 200
```

## Langsame Antwort

Filter:

```text
ip.addr == 172.28.50.20 and http
```

Beobachtung:

```text
Zwischen HTTP Request und HTTP Response liegt ungefähr eine Verzögerung von 2 Sekunden.
```

Bewertung:

```text
Die Verzögerung liegt im Capture zwischen HTTP Request und HTTP Response. Im Lab ist diese Verzögerung absichtlich serverseitig eingebaut. Ohne Lab-Wissen wäre eine vorsichtige Bewertung: Die Wartezeit entsteht nach der Anfrage und vor der Antwort, sichtbar nicht durch DNS oder TCP-Verbindungsaufbau.
```

## Beispielbericht

```text
Capture-Punkt:
Host-System, Interface any, Capture Filter net 172.28.50.0/24

DNS:
Der Client 172.28.50.100 fragt den DNS-Server 172.28.50.53 nach web-ok.lab.local, web-slow.lab.local und does-not-exist.lab.local.
web-ok.lab.local wird mit 172.28.50.10 beantwortet.
web-slow.lab.local wird mit 172.28.50.20 beantwortet.
does-not-exist.lab.local wird mit NXDOMAIN beantwortet.

HTTP:
Der Client sendet HTTP HEAD Requests an 172.28.50.10 und 172.28.50.20.
Beide Webserver antworten mit Status 200.
Beim Ziel 172.28.50.20 liegt zwischen Request und Response ungefähr eine Verzögerung von 2 Sekunden.

Bewertung:
Das Symptom „funktioniert teilweise nicht“ passt zum nicht existierenden DNS-Namen does-not-exist.lab.local.
Das Symptom „fühlt sich langsam an“ passt zur verzögerten HTTP-Antwort von web-slow.lab.local.
Im Capture sind keine Aussagen über echte produktive Netzwerkprobleme möglich, da es sich um ein Lab handelt.

Verwendete Filter:
dns
dns.flags.rcode == 3
http
ip.addr == 172.28.50.10 and http
ip.addr == 172.28.50.20 and http
```

## Nicht belegbar

Dieser Capture beweist nicht:

- dass ein reales Unternehmensnetz langsam ist
- dass TLS funktioniert oder nicht funktioniert
- dass ein externer DNS-Resolver korrekt arbeitet
- dass es keinen Paketverlust außerhalb des Lab-Netzes gibt

Er belegt nur das Verhalten in der kontrollierten Docker-Lab-Umgebung.
