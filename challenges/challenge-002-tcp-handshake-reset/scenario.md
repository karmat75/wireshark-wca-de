# Szenario

Ein Benutzer meldet:

```text
Der Webserver funktioniert auf der normalen Adresse, aber ein anderer Port ist nicht erreichbar.
```

Du sollst im Capture prüfen:

- ob der Webserver auf TCP-Port 80 erreichbar ist
- ob HTTP funktioniert
- was beim Verbindungsversuch zu TCP-Port 81 passiert
- ob ein Timeout oder eine aktive Ablehnung sichtbar ist

## Lab-Netz

```text
172.28.50.0/24
```

## Systeme

| System | IP | Rolle |
|---|---:|---|
| `lab-client` | `172.28.50.100` | Client |
| `web-ok.lab.local` | `172.28.50.10` | Webserver auf TCP 80 |

## Wichtige Unterscheidung

Ein Timeout und ein Reset sind nicht dasselbe.

| Beobachtung | mögliche Bedeutung |
|---|---|
| SYN ohne Antwort, mehrere Wiederholungen | keine Antwort sichtbar |
| SYN gefolgt von RST/RST-ACK | aktive Ablehnung oder geschlossener Port |
| vollständiger Handshake | TCP-Verbindung aufgebaut |
| HTTP Response | Anwendung hat geantwortet |
