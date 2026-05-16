# Hinweise

## Hinweis 1: HTTP zeigt viel

Beginne mit:

```text
http
```

und:

```text
http.request
```

Bei HTTP sind Header und Nutzdaten häufig im Klartext sichtbar.

## Hinweis 2: Basic Auth

Filter:

```text
http.authorization
```

Basic Auth ist Base64-kodiert, aber nicht verschlüsselt.

Bei HTTP ist das ein klares Risiko.

## Hinweis 3: Formularwerte

POST Requests findest du mit:

```text
http.request.method == "POST"
```

Danach im Paketdetail oder per Follow TCP Stream prüfen.

## Hinweis 4: Token suchen

Filter:

```text
http contains "LAB-TOKEN-12345"
```

Wenn das funktioniert, ist der Wert im Capture sichtbar.

## Hinweis 5: Beaconing vorsichtig formulieren

Nicht sauber:

```text
Das ist Malware.
```

Besser:

```text
Im Capture sind regelmäßige HTTP GET Requests zu `/beacon` sichtbar. Das Muster ist Beacon-ähnlich, beweist aber ohne Host- und Prozesskontext keine Malware.
```

## Hinweis 6: echte Captures

Wenn echte Zugangsdaten sichtbar sind:

- Capture nicht öffentlich teilen
- nicht ins Repository committen
- Zugangsdaten rotieren
- Zugriff begrenzen
- Datenschutz-/Incident-Prozess beachten
