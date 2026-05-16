# Szenario

Ein Security-Team möchte wissen, ob in einem kleinen HTTP-basierten Lab-Dienst sensible Informationen im Klartext übertragen werden.

Außerdem fällt ein regelmäßiger HTTP-Request auf, der wie ein Beaconing-Muster wirken könnte.

Deine Aufgabe ist eine defensive Triage:

- Welche Informationen sind im Capture sichtbar?
- Sind Zugangsdaten oder Tokens im Klartext sichtbar?
- Gibt es regelmäßige Requests?
- Welche User-Agents sind beteiligt?
- Welche Aussagen sind belegt?
- Welche Aussagen wären zu stark?

## Lab-Netz

```text
172.28.80.0/24
```

## Systeme

| System | IP | Rolle |
|---|---:|---|
| `lab-client` | `172.28.80.100` | Client |
| `lab-web-security` | `172.28.80.10` | HTTP-Server |

## Erwartete Muster

| Muster | Erwartung |
|---|---|
| Basic Auth | Authorization Header im HTTP-Request |
| Formularlogin | POST Body mit synthetischen Lab-Werten |
| Beacon-Simulation | mehrere ähnliche GET-Requests zu `/beacon` |
| User-Agent | `WWCA-LabClient/1.0` und `WWCA-BeaconSimulator/1.0` |
