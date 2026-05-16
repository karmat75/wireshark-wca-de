# Musterlösung

Die Frame-Nummern hängen von deinem lokal erzeugten Capture ab.

Die fachlichen Beobachtungen sollten aber ähnlich sein.

## Erfolgreiche TCP-Verbindung

Filter:

```text
tcp.port == 80
```

Erwartete Beobachtung:

```text
Client -> Server  [SYN]
Server -> Client  [SYN, ACK]
Client -> Server  [ACK]
```

Beteiligte Systeme:

| Rolle | IP |
|---|---:|
| Client | `172.28.50.100` |
| Webserver | `172.28.50.10` |

Beispielbewertung:

```text
Der TCP 3-Way Handshake zwischen dem Client 172.28.50.100 und dem Webserver 172.28.50.10 auf TCP-Port 80 ist vollständig sichtbar. Damit ist belegt, dass der Zielport grundsätzlich erreichbar ist.
```

## TCP Stream

Filter:

```text
tcp.stream == <nummer>
```

Erwartung:

- vollständiger Handshake
- HTTP Request
- HTTP Response
- je nach Verbindung FIN/ACK oder weiterer Verbindungsabschluss

Wichtig:

```text
Der erfolgreiche Handshake beweist nicht allein, dass jede Anwendung korrekt funktioniert. In diesem Lab ist zusätzlich eine HTTP Response sichtbar.
```

## HTTP

Filter:

```text
http
```

oder:

```text
ip.addr == 172.28.50.10 and http
```

Erwartung:

```text
HTTP Request
HTTP Response 200 OK
```

Beispielbewertung:

```text
Nach dem erfolgreichen TCP Handshake ist HTTP-Verkehr sichtbar. Der Webserver beantwortet die Anfrage mit Status 200. Damit funktioniert der Webdienst in diesem Lab grundsätzlich.
```

## Geschlossener Port

Filter:

```text
tcp.port == 81
```

und:

```text
tcp.flags.reset == 1
```

Erwartete Beobachtung:

```text
Client -> 172.28.50.10:81 [SYN]
172.28.50.10 -> Client [RST, ACK]
```

Beispielbewertung:

```text
Der Client versucht, eine TCP-Verbindung zu 172.28.50.10 auf Port 81 aufzubauen. Das Ziel antwortet mit RST/ACK. Damit ist belegt, dass der Verbindungsversuch aktiv abgelehnt wird. Im Lab bedeutet das: Auf Port 81 lauscht kein Dienst.
```

## Was RST nicht beweist

Ein RST beweist nicht automatisch:

- dass eine Firewall schuld ist
- dass der Server offline ist
- dass DNS fehlerhaft ist
- dass TLS falsch konfiguriert ist

Ein RST zeigt zunächst:

```text
Eine TCP-Verbindung wurde aktiv zurückgesetzt oder abgelehnt.
```

## Beispielbericht

```text
Capture-Punkt:
Host-System, Interface any, Capture Filter net 172.28.50.0/24

Erfolgreiche Verbindung:
Der Client 172.28.50.100 baut eine TCP-Verbindung zu 172.28.50.10:80 auf.
Der 3-Way Handshake ist vollständig sichtbar:
Frame <n>: SYN
Frame <n>: SYN/ACK
Frame <n>: ACK

HTTP:
Im gleichen Stream ist eine HTTP-Antwort mit Status 200 sichtbar.

Geschlossener Port:
Der Client versucht außerdem, 172.28.50.10:81 zu erreichen.
Auf den SYN folgt ein RST/ACK vom Zielsystem.
Damit wird der Zielport aktiv abgelehnt. Im Lab lauscht auf Port 81 kein Dienst.

Verwendete Filter:
tcp.port == 80
tcp.stream == <nummer>
http
tcp.port == 81
tcp.flags.reset == 1

Bewertung:
TCP zu Port 80 funktioniert. TCP zu Port 81 wird aktiv abgelehnt. Der Capture belegt damit zwei typische TCP-Zustände: erfolgreiche Verbindung und geschlossenen Port.
```

## Einschränkungen

Dieses Lab beweist nicht:

- Verhalten echter Firewalls
- Verhalten externer Netzwege
- TLS-Funktion
- echte Paketverluste
- Performance über WAN-Strecken

Es trainiert kontrolliert:

- TCP Handshake
- TCP Stream
- HTTP über TCP
- RST bei geschlossenem Port
