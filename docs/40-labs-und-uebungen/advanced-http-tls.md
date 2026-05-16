# Advanced Lab 020: HTTP und TLS

Dieses Lab zeigt den Unterschied zwischen HTTP im Klartext und HTTPS/TLS.

Es erzeugt in Docker einen Webserver mit:

- HTTP auf Port 80
- HTTPS auf Port 443
- selbstsigniertem Zertifikat
- sichtbarem TLS Client Hello
- SNI durch `secure.lab.local`
- optional sichtbarem TLS Alert bei Zertifikatsprüfung

## Lab-Pfad

```text
labs/advanced/lab-advanced-020-http-tls/
```

## Docker-Pfad

```text
docker/compose/lab-advanced-http-tls/
```

## Ziel

Du übst:

- HTTP Request und Response im Klartext zu lesen
- TLS-Verkehr zu erkennen
- SNI im Client Hello zu finden
- ALPN zu prüfen
- TLS Alerts zu erkennen
- HTTPS-Inhalte von TLS-Metadaten zu unterscheiden
- TShark-Ausgaben für HTTP und TLS zu erzeugen
- Analyseergebnisse vorsichtig zu formulieren

## Ergebnisdatei

Lokal erzeugter Capture:

```text
pcaps/generated/lab-advanced-020-http-tls.pcapng
```

Diese Datei ist lokal und wird nicht committed.

## WCA-Bezug

Dieses Lab trainiert:

- HTTP-Analyse
- TLS-Analyse
- TCP Port 80 und 443
- SNI / ALPN
- TLS Alert
- Display Filter
- TShark
- Security-Basics und Methodik
