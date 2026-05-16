# Lab Advanced 040: Security Basics

## Ziel

In diesem Lab analysierst du kontrollierten HTTP-Traffic aus defensiver Security-Sicht.

Du suchst:

- HTTP Basic Auth
- Formularwerte im Klartext
- synthetische Tokens
- Beacon-ähnliche regelmäßige Requests
- auffällige User-Agents
- Host- und URI-Informationen

## Voraussetzungen

Du brauchst:

- Docker
- Docker Compose
- Wireshark
- TShark
- Capture-Rechte auf dem Host

Prüfen:

```bash
docker --version
docker compose version
tshark --version
```

## Ergebnisdatei

Speichere den Capture lokal als:

```text
pcaps/generated/lab-advanced-040-security-basics.pcapng
```

Diese Datei soll nicht committed werden.

## Geschätzte Dauer

```text
60 Minuten
```

## Wichtiger Hinweis

Alle verwendeten Zugangsdaten sind synthetische Lab-Werte.

```text
labuser
LabPassword123
LAB-TOKEN-12345
```

Keine echten Zugangsdaten verwenden.
