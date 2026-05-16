# Szenario

Ein Client im Lab-Netz soll einen Webserver erreichen.

Der Webserver auf `web-ok.lab.local` antwortet auf Port 80.

Zusätzlich testest du einen Port, auf dem kein Dienst lauscht.

Deine Aufgabe ist es, im Capture zu zeigen:

- dass die Verbindung zum Webserver erfolgreich aufgebaut wird
- welche Pakete den 3-Way Handshake bilden
- welcher TCP Stream zur erfolgreichen Verbindung gehört
- wie ein geschlossener Port im Capture aussieht
- welche Aussage durch RST/RST-ACK wirklich belegbar ist

## Lab-Netz

```text
172.28.50.0/24
```

## Systeme

| System | IP | Rolle |
|---|---:|---|
| `lab-client` | `172.28.50.100` | Client |
| `lab-dns` | `172.28.50.53` | DNS |
| `web-ok.lab.local` | `172.28.50.10` | Webserver auf TCP 80 |
| `web-slow.lab.local` | `172.28.50.20` | Webserver auf TCP 80 |

## Erwartete Kernbeobachtungen

| Test | Erwartung |
|---|---|
| `curl -I http://web-ok.lab.local` | erfolgreicher TCP Handshake und HTTP Response |
| `curl -v --max-time 3 http://172.28.50.10:81` | aktive Ablehnung oder RST/RST-ACK für geschlossenen Port |
