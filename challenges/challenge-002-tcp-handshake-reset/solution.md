# Musterlösung

Die genauen Frame-Nummern hängen von deinem lokal erzeugten Capture ab.

## Port 80: erfolgreiche Verbindung

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

Danach sollte HTTP sichtbar sein.

Filter:

```text
http
```

Erwartung:

```text
HTTP Response 200 OK
```

Bewertung:

```text
Der TCP 3-Way Handshake zu 172.28.50.10:80 ist vollständig sichtbar. Danach folgt HTTP-Verkehr mit einer Antwort des Webservers. Damit ist belegt, dass Port 80 im Lab erreichbar ist und der Webdienst antwortet.
```

## Port 81: aktive Ablehnung

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

Bewertung:

```text
Der Client versucht, eine TCP-Verbindung zu 172.28.50.10:81 aufzubauen. Das Ziel antwortet mit RST/ACK. Das ist eine aktive Ablehnung und kein klassischer Timeout. Im Lab bedeutet das, dass auf Port 81 kein Dienst lauscht.
```

## Was nicht belegt ist

Der Capture beweist nicht automatisch:

- dass eine Firewall schuld ist
- dass der Server offline ist
- dass DNS fehlerhaft ist
- dass TLS falsch konfiguriert ist
- dass der gesamte Netzpfad fehlerfrei ist

## Beispielbericht

```text
Capture-Punkt:
Host-System, Interface any, Capture Filter net 172.28.50.0/24

Port 80:
Der Client 172.28.50.100 baut eine TCP-Verbindung zu 172.28.50.10:80 auf.
Der 3-Way Handshake ist vollständig sichtbar:
Frame <n>: SYN
Frame <n>: SYN/ACK
Frame <n>: ACK
Danach ist HTTP sichtbar und der Server antwortet mit 200 OK.

Port 81:
Der Client sendet SYN zu 172.28.50.10:81.
Das Ziel antwortet mit RST/ACK.
Damit wird der Verbindungsversuch aktiv abgelehnt.

Bewertung:
Port 80 ist erreichbar und HTTP antwortet. Port 81 ist nicht als Dienst erreichbar, sondern wird aktiv zurückgesetzt. Das ist nicht dasselbe wie ein Timeout.

Nächste Prüfung in echter Umgebung:
Prüfen, ob der Dienst auf Port 81 laufen soll, ob lokale Firewall-Regeln greifen, ob die Anwendung an den erwarteten Port gebunden ist und ob die Beobachtung aus Client- und Serversicht gleich aussieht.
```

## Merksatz

> SYN ohne Antwort, SYN/ACK und RST sind drei unterschiedliche Signale.  
> Wer sie sauber trennt, vermeidet viele falsche Diagnosen.
