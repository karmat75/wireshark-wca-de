# Szenario

Ein Benutzer meldet:

```text
Die interne Lab-Webseite funktioniert teilweise nicht.
Eine andere Seite funktioniert, fühlt sich aber langsam an.
```

Die Umgebung nutzt die Domain:

```text
lab.local
```

Bekannte Systeme:

| System | IP | Rolle |
|---|---:|---|
| `lab-client` | `172.28.50.100` | Client |
| `lab-dns` | `172.28.50.53` | DNS |
| `web-ok.lab.local` | `172.28.50.10` | normaler Webserver |
| `web-slow.lab.local` | `172.28.50.20` | langsamer Webserver |

Zusätzlich wird ein Name abgefragt, der nicht existieren soll:

```text
does-not-exist.lab.local
```

## Deine Aufgabe

Erstelle einen Capture und finde heraus:

- ob DNS grundsätzlich funktioniert
- welcher Name nicht existiert
- ob HTTP grundsätzlich funktioniert
- welche Webanfrage langsam ist
- ob die sichtbare Verzögerung eher DNS, TCP oder HTTP/Anwendung betrifft
