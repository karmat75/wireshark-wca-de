# Szenario

Ein Benutzer meldet:

```text
Der Download von einem internen Webserver ist langsam und wirkt unruhig.
```

Du hast eine Lab-Umgebung, in der absichtlich Paketverlust auf der Serverseite eingebaut wird.

Deine Aufgabe ist es, im Capture zu zeigen:

- ob TCP Retransmissions sichtbar sind
- ob Duplicate ACKs sichtbar sind
- welcher TCP Stream betroffen ist
- wie sich der Paketverlust im TCP-Datenstrom zeigt
- welche Aussagen durch den Capture belegbar sind
- welche Aussagen zu stark wären

## Lab-Netz

```text
172.28.60.0/24
```

## Systeme

| System | IP | Rolle |
|---|---:|---|
| `lab-client` | `172.28.60.100` | Client |
| `lab-web-loss` | `172.28.60.10` | Webserver mit absichtlichem Paketverlust |

## Erwartete Kernbeobachtung

Der Client lädt eine größere Datei vom Webserver.

Durch den eingebauten Paketverlust sollten im Capture TCP Analysehinweise sichtbar werden, zum Beispiel:

- Retransmission
- Fast Retransmission
- Duplicate ACK
- TCP Analysis Flags
