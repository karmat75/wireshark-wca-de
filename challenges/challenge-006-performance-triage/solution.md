# Musterlösung

Die genauen Frame-Nummern hängen von deinem lokal erzeugten Capture ab.

## Grundbeobachtung

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
DNS Query und Response sind sichtbar. In diesem Lab ist DNS nicht die auffällige Hauptwartezeit.
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

- vollständiger TCP Handshake zu Port 80 bei beiden Servern
- keine auffällige lange Wartezeit zwischen SYN und SYN/ACK
- HTTP folgt nach dem TCP-Verbindungsaufbau

Bewertung:

```text
Der TCP-Verbindungsaufbau ist zu beiden Servern erfolgreich. Die sichtbare Hauptwartezeit liegt nicht im Handshake.
```

## HTTP

Filter:

```text
http
```

Schneller Server:

```text
ip.addr == 172.28.50.10 and http
```

Langsamer Server:

```text
ip.addr == 172.28.50.20 and http
```

Erwartung:

- `web-ok` antwortet schnell
- `web-slow` antwortet deutlich später
- beide liefern HTTP 200

Bewertung:

```text
Die auffällige Wartezeit liegt bei web-slow.lab.local zwischen HTTP Request und HTTP Response. Das passt zu serverseitiger oder anwendungsseitiger Verarbeitung.
```

## Was belegt ist

Belegt ist:

- beide Namen werden aufgelöst
- beide TCP-Verbindungen werden aufgebaut
- beide Webserver antworten mit HTTP
- `web-slow.lab.local` antwortet sichtbar später als `web-ok.lab.local`
- die Wartezeit liegt im Capture zwischen HTTP Request und HTTP Response

## Was nicht belegt ist

Nicht automatisch belegt ist:

- dass das Netzwerk insgesamt langsam ist
- dass DNS die Ursache ist
- dass TCP die Ursache ist
- dass ein Switch oder eine Firewall verantwortlich ist
- welcher Prozess auf dem Server die Verzögerung erzeugt
- wie sich ein Produktivsystem verhält

## Beispielbericht

```text
Capture-Punkt:
Host-System, Interface any, Capture Filter net 172.28.50.0/24

DNS:
web-ok.lab.local und web-slow.lab.local werden erfolgreich aufgelöst. Query und Response sind sichtbar. Es gibt keine auffällige DNS-Wartezeit.

TCP:
Zu beiden Servern wird eine TCP-Verbindung auf Port 80 aufgebaut. Die Handshakes sind vollständig sichtbar und zeigen keine auffällige Verzögerung.

HTTP:
Bei web-ok.lab.local folgt die HTTP Response schnell auf den Request.
Bei web-slow.lab.local liegt zwischen HTTP Request und HTTP Response eine deutlich sichtbare Wartezeit. Beide Antworten liefern HTTP 200.

Bewertung:
Die sichtbare Wartezeit entsteht nicht bei DNS und nicht beim TCP-Verbindungsaufbau, sondern zwischen HTTP Request und HTTP Response von web-slow.lab.local. Das Muster passt zu serverseitiger oder anwendungsseitiger Verarbeitung.

Einschränkungen:
Der Capture zeigt nur die Lab-Umgebung und den Capture-Punkt. Er beweist nicht, welcher Prozess oder welche Serverkomponente die Wartezeit erzeugt.

Nächste Schritte:
In einer echten Umgebung wären Serverlogs, Applikationslogs, Reverse-Proxy-Logs, Backend-Latenzen und ein Gegen-Capture auf Serverseite sinnvoll.
```

## Merksatz

> Performanceanalyse heißt: Zeitabschnitte trennen.  
> Erst danach darf man über Ursachen sprechen.
