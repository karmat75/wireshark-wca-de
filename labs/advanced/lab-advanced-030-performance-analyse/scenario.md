# Szenario

Ein Benutzer meldet:

```text
Die interne Webseite web-slow.lab.local fühlt sich deutlich langsamer an als web-ok.lab.local.
```

Beide Dienste sind grundsätzlich erreichbar.

Du sollst herausfinden:

- ob DNS langsam ist
- ob der TCP-Verbindungsaufbau langsam ist
- ob die Verzögerung nach dem HTTP Request entsteht
- wie groß der Unterschied zwischen den beiden Webservern ungefähr ist
- welche Aussagen durch den Capture belegbar sind

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

In diesem Lab ist die Verzögerung bewusst im langsamen Webserver eingebaut.

In einer echten Analyse würdest du das aber nicht vorher wissen.

Deshalb sollst du so formulieren, dass die Aussage durch den Capture belegbar bleibt.
