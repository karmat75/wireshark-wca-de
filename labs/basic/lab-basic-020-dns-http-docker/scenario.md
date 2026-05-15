# Szenario

Du betreibst eine kleine Lab-Umgebung.

Ein Client greift auf zwei interne Webserver zu:

- `web-ok.lab.local`
- `web-slow.lab.local`

Zusätzlich wird ein nicht existierender Name abgefragt:

- `does-not-exist.lab.local`

Deine Aufgabe ist es, den Traffic mitzuschneiden und zu zeigen:

- welche DNS-Anfragen gestellt werden
- welche DNS-Antworten erfolgreich sind
- welcher Name mit NXDOMAIN beantwortet wird
- welcher Webserver normal antwortet
- welcher Webserver langsam antwortet
- wie sich die Verzögerung im Capture zeigt

## Lab-Netz

```text
172.28.50.0/24
```

## Systeme

| System | IP | Rolle |
|---|---:|---|
| `lab-client` | `172.28.50.100` | Client |
| `lab-dns` | `172.28.50.53` | DNS |
| `lab-web-ok` | `172.28.50.10` | normaler Webserver |
| `lab-web-slow` | `172.28.50.20` | langsamer Webserver |
