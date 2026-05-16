# Hinweise

## Hinweis 1: HTTP ist Klartext

Beginne mit:

```text
http
```

Dann:

```text
http.request
```

Wenn du im Capture HTTP siehst, kannst du oft Header und Body lesen.

## Hinweis 2: Basic Auth

Suche nach:

```text
http.authorization
```

oder:

```text
Authorization
```

Basic Auth ist Base64-kodiert, aber nicht sicher verschlüsselt.

## Hinweis 3: Formularwerte

Formularwerte findest du häufig in:

```text
http.file_data
```

oder über:

```text
Follow TCP Stream
```

## Hinweis 4: Beaconing vorsichtig bewerten

Mehrere regelmäßige Requests können Beaconing-ähnlich wirken.

Sauber:

```text
Im Capture sind regelmäßige HTTP GET Requests zu /beacon sichtbar.
```

Zu stark:

```text
Das ist Malware.
```

## Hinweis 5: User-Agent

User-Agent kann Hinweise geben, ist aber leicht manipulierbar.

Deshalb nicht allein als Beweis verwenden.

## Hinweis 6: echte Captures schützen

Wenn echte Zugangsdaten oder Tokens sichtbar sind:

- nicht ins Repository
- nicht unverschlüsselt weitergeben
- betroffene Credentials rotieren
- Zugriff auf Capture begrenzen
- Incident-/Datenschutzprozess beachten
