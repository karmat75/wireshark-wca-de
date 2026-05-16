# Szenario

Ein interner Webdienst ist sowohl über HTTP als auch über HTTPS erreichbar.

Du sollst zeigen:

- was bei HTTP im Capture sichtbar ist
- was bei HTTPS/TLS noch sichtbar ist
- ob SNI im TLS Client Hello erkennbar ist
- ob ALPN sichtbar ist
- wie ein Zertifikatsproblem im Capture aussehen kann
- welche Inhalte bei TLS nicht mehr im Klartext lesbar sind

## Lab-Netz

```text
172.28.70.0/24
```

## Systeme

| System | IP | Rolle |
|---|---:|---|
| `lab-client` | `172.28.70.100` | Client |
| `lab-web-tls` | `172.28.70.10` | HTTP/HTTPS Webserver |

## Hostname für TLS

```text
secure.lab.local
```

Der Hostname wird im Client über `curl --resolve` auf die IP `172.28.70.10` gemappt.

Dadurch ist SNI im TLS Client Hello möglich, ohne einen eigenen DNS-Server zu betreiben.
