# Szenario

Ein interner Dienst wurde teilweise von HTTP auf HTTPS umgestellt.

Das Team möchte wissen:

- ob im Capture noch Klartext-HTTP sichtbar ist
- ob HTTPS/TLS korrekt als TLS-Verkehr erkennbar ist
- ob SNI sichtbar ist
- ob ein Zertifikatsproblem sichtbar wird
- welche Inhalte geschützt sind
- welche Metadaten weiterhin sichtbar bleiben

## Lab-Netz

```text
172.28.70.0/24
```

## Systeme

| System | IP | Rolle |
|---|---:|---|
| `lab-client` | `172.28.70.100` | Client |
| `lab-web-tls` | `172.28.70.10` | HTTP/HTTPS Webserver |

## Hostname

Für TLS wird verwendet:

```text
secure.lab.local
```

Der Hostname wird per `curl --resolve` auf die IP des Webservers gemappt.
