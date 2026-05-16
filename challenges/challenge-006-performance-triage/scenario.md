# Szenario

Ein Benutzer meldet:

```text
web-slow.lab.local ist viel langsamer als web-ok.lab.local.
```

Beide Dienste sind grundsätzlich erreichbar.

Du sollst im Capture prüfen:

- ob DNS auffällig langsam ist
- ob der TCP Handshake auffällig langsam ist
- ob die sichtbare Wartezeit nach dem HTTP Request entsteht
- wie groß der Unterschied ungefähr ist
- was durch den Capture belegt ist
- was ohne weitere Daten nicht belegt ist

## Lab-Netz

```text
172.28.50.0/24
```

## Systeme

| System | IP | Rolle |
|---|---:|---|
| `lab-client` | `172.28.50.100` | Client |
| `lab-dns` | `172.28.50.53` | DNS |
| `web-ok.lab.local` | `172.28.50.10` | normaler Webserver |
| `web-slow.lab.local` | `172.28.50.20` | langsamer Webserver |

## Wichtig

Die sichtbare Wartezeit soll methodisch eingegrenzt werden.

Nicht gesucht ist eine Bauchgefühl-Aussage wie:

```text
Das Netzwerk ist langsam.
```

Gesucht ist eine belegbare Aussage wie:

```text
Im Capture liegt die auffällige Wartezeit zwischen HTTP Request und HTTP Response.
```
