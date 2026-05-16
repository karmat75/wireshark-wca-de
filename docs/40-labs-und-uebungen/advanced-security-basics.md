# Advanced Lab 040: Security Basics

Dieses Lab trainiert defensive Security-Basics mit Wireshark.

Es erzeugt kontrollierten HTTP-Traffic mit synthetischen Lab-Werten:

- HTTP Basic Auth
- Formular-Login per POST
- regelmäßige Beacon-ähnliche Requests
- Host-Header, User-Agent und URI-Auswertung

## Lab-Pfad

```text
labs/advanced/lab-advanced-040-security-basics/
```

## Docker-Pfad

```text
docker/compose/lab-advanced-security-basics/
```

## Ziel

Du übst:

- Klartext-Risiken in HTTP zu erkennen
- Authorization Header zu finden
- Formulardaten im HTTP Body zu finden
- regelmäßige Requests als Muster zu beschreiben
- User-Agent und Host-Header auszuwerten
- nicht vorschnell „Malware“ zu behaupten
- Security-Beobachtungen sauber zu dokumentieren

## Ergebnisdatei

Lokal erzeugter Capture:

```text
pcaps/generated/lab-advanced-040-security-basics.pcapng
```

Diese Datei ist lokal und wird nicht committed.

## WCA-Bezug

Dieses Lab trainiert:

- HTTP
- Display Filter
- Follow TCP Stream
- Security-Basics
- TShark
- Methodik
- Datenschutz und sichere Dokumentation
