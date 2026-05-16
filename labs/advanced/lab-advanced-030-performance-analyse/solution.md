# Musterlösung

Die Frame-Nummern hängen von deinem lokal erzeugten Capture ab.

Die fachliche Beobachtung sollte aber gleich sein:

> Der langsame Webserver zeigt eine deutlich größere Zeit zwischen HTTP Request und HTTP Response.

## Erwartete Grundbeobachtung

Beteiligte Systeme:

| Rolle | IP |
|---|---:|
| Client | `172.28.50.100` |
| DNS | `172.28.50.53` |
| Web OK | `172.28.50.10` |
| Web Slow | `172.28.50.20` |

## DNS

Filter:

```text
dns
```

Erwartung:

- Query für `web-ok.lab.local`
- Response mit `172.28.50.10`
- Query für `web-slow.lab.local`
- Response mit `172.28.50.20`

Bewertung:

```text
DNS Query und Response sind sichtbar. In diesem Lab sollte DNS nicht die auffällige Wartezeit verursachen.
```

## TCP

Filter:

```text
ip.addr == 172.28.50.10 and tcp
```

und:

```text
ip.addr == 172.28.50.20 and tcp
```

Erwartung:

- vollständiger TCP Handshake zu Port 80
- kein auffälliger langer Abstand zwischen SYN und SYN/ACK
- HTTP folgt nach dem TCP-Verbindungsaufbau

Bewertung:

```text
Der TCP-Verbindungsaufbau ist grundsätzlich erfolgreich. Die sichtbare Hauptwartezeit liegt nicht im Handshake.
```

## HTTP

Filter schneller Server:

```text
ip.addr == 172.28.50.10 and http
```

Filter langsamer Server:

```text
ip.addr == 172.28.50.20 and http
```

Erwartung:

- `web-ok` antwortet schnell
- `web-slow` antwortet ungefähr 2 Sekunden nach dem Request
- beide liefern HTTP 200

Bewertung:

```text
Die sichtbare Wartezeit liegt beim langsamen Server zwischen HTTP Request und HTTP Response. Das Muster passt zu serverseitiger oder anwendungsseitiger Verarbeitung.
```

## Warum das wichtig ist

Eine unscharfe Meldung wie:

```text
Die Webseite ist langsam.
```

wird durch Wireshark zerlegt in:

```text
DNS langsam?
TCP-Verbindungsaufbau langsam?
TLS langsam?
Serverantwort langsam?
Datenübertragung langsam?
```

In diesem Lab ist die Antwort:

```text
Die auffällige Wartezeit liegt nach dem HTTP Request und vor der HTTP Response.
```

## Beispielbericht

```text
Capture-Punkt:
Host-System, Interface any, Capture Filter net 172.28.50.0/24

DNS:
Die Namen web-ok.lab.local und web-slow.lab.local werden erfolgreich aufgelöst.
DNS Query und Response sind sichtbar und zeigen keine auffällige Wartezeit.

TCP:
Zu beiden Webservern wird eine TCP-Verbindung auf Port 80 aufgebaut.
Der Handshake ist vollständig sichtbar und zeigt keine auffällige Verzögerung.

HTTP:
Bei web-ok.lab.local folgt die HTTP Response schnell auf den Request.
Bei web-slow.lab.local liegt zwischen HTTP Request und HTTP Response ungefähr eine Verzögerung von 2 Sekunden.
Beide Antworten liefern HTTP 200.

Bewertung:
Die sichtbare Wartezeit entsteht im Capture nicht bei DNS und nicht beim TCP-Verbindungsaufbau, sondern zwischen HTTP Request und HTTP Response des langsamen Webservers. Das passt zu serverseitiger oder anwendungsseitiger Verarbeitung. Im Lab ist diese Verzögerung absichtlich eingebaut.

Einschränkungen:
Der Capture beweist nicht, wie sich ein echtes Produktivsystem verhält. Er zeigt nur das Verhalten dieser Lab-Umgebung.
```

## I/O Graph

Ein I/O Graph kann zeigen:

- wann Traffic auftritt
- ob längere Pausen sichtbar sind
- ob Bursts auftreten
- ob sich zwei Server unterschiedlich verhalten

Er beweist aber nicht allein:

- die konkrete Ursache
- den Zustand des Servers
- die Qualität eines gesamten Netzpfads

## Merksatz

> Performanceanalyse heißt: Wartezeit in Abschnitte zerlegen.  
> Erst danach wird über Ursachen gesprochen.
