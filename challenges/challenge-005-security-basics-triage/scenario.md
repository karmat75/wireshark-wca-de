# Szenario

Ein Security-Team bittet um eine schnelle Triage eines HTTP-Captures.

Es gibt drei Fragen:

1. Werden Zugangsdaten oder Tokens im Klartext übertragen?
2. Gibt es regelmäßige Requests, die wie ein Beaconing-Muster aussehen?
3. Welche Aussagen sind wirklich durch den Capture belegt?

## Lab-Netz

```text
172.28.80.0/24
```

## Systeme

| System | IP | Rolle |
|---|---:|---|
| `lab-client` | `172.28.80.100` | Client |
| `lab-web-security` | `172.28.80.10` | HTTP-Server |

## Synthetische Lab-Werte

In dieser Challenge können sichtbar werden:

```text
labuser
LabPassword123
LAB-TOKEN-12345
WWCA-LabClient/1.0
WWCA-BeaconSimulator/1.0
training-node-01
```

Diese Werte sind absichtlich im Lab enthalten.

In echten Captures wären vergleichbare Werte schutzbedürftig.
