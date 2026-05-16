# Musterlösung

Die genauen Frame-Nummern hängen von deinem lokal erzeugten Capture ab.

Die fachlichen Beobachtungen sollten aber gleich sein.

## HTTP Requests

Filter:

```text
http.request
```

Erwartete Requests:

- `GET /`
- `GET /basic`
- `POST /login`
- mehrere `GET /beacon?id=training-node-01&seq=<n>`

Bewertung:

```text
Der Traffic ist HTTP und damit im Klartext analysierbar.
```

## Basic Auth

Filter:

```text
http.authorization
```

Erwartung:

```text
Authorization: Basic ...
```

Beispielbewertung:

```text
Im HTTP Request zu `/basic` ist ein Authorization Header sichtbar. Bei HTTP wird dieser Header ohne TLS-Schutz übertragen. Der Wert ist zwar Base64-kodiert, aber nicht sicher verschlüsselt.
```

Wichtig:

```text
Die Lab-Werte sind synthetisch. In echten Captures wären solche Daten schutzbedürftig.
```

## Formularwerte

Filter:

```text
http.request.method == "POST"
```

oder Analyse über:

```text
Follow TCP Stream
```

Erwartete sichtbare Werte:

```text
username=labuser
password=LabPassword123
token=LAB-TOKEN-12345
```

Bewertung:

```text
Der Formularinhalt ist im HTTP Body sichtbar. In einer echten Umgebung wäre das ein klares Sicherheits- und Datenschutzrisiko.
```

## Beacon-ähnliche Requests

Filter:

```text
http.request.uri contains "/beacon"
```

Erwartung:

```text
/beacon?id=training-node-01&seq=1
/beacon?id=training-node-01&seq=2
/beacon?id=training-node-01&seq=3
/beacon?id=training-node-01&seq=4
/beacon?id=training-node-01&seq=5
```

Bewertung:

```text
Im Capture sind regelmäßige GET Requests zu `/beacon` sichtbar. Das Muster ist Beacon-ähnlich. Es beweist aber nicht automatisch Malware, da es sich auch um Telemetrie, Monitoring oder Lab-Traffic handeln kann.
```

## User-Agent

Filter:

```text
http.user_agent
```

Erwartete Werte:

```text
WWCA-LabClient/1.0
WWCA-BeaconSimulator/1.0
curl/...
```

Bewertung:

```text
Der User-Agent kann Hinweise liefern, ist aber leicht manipulierbar und daher kein alleiniger Beweis.
```

## Beispielbericht

```text
Capture-Punkt:
Host-System, Interface any, Capture Filter net 172.28.80.0/24

Klartext:
Im Capture ist HTTP-Verkehr zwischen 172.28.80.100 und 172.28.80.10 sichtbar.
Der Request zu /basic enthält einen Authorization Header.
Der POST zu /login enthält die synthetischen Lab-Werte username=labuser, password=LabPassword123 und token=LAB-TOKEN-12345 im Klartext.

Beacon-Muster:
Es sind mehrere GET Requests zu /beacon sichtbar. Die Requests enthalten id=training-node-01 und fortlaufende seq-Werte. Der Abstand beträgt ungefähr eine Sekunde.

Bewertung:
Der Capture belegt Klartextübertragung sensibler Werte im Lab und ein regelmäßiges HTTP-Request-Muster. Das Muster ist Beacon-ähnlich, beweist aber ohne Kontext keine Malware.

Einschränkungen:
Der Capture stammt aus einer kontrollierten Lab-Umgebung. In einer echten Umgebung müssten Hostkontext, Prozessinformationen, DNS, Proxy-Logs, EDR/AV und Serverlogs geprüft werden.

Schutzbedarf:
Ein echter Capture mit Authorization Headern, Passwörtern oder Tokens dürfte nicht ungeschützt geteilt oder committed werden. Betroffene Zugangsdaten müssten rotiert werden.
```

## Merksatz

> Security-Analyse mit Wireshark beginnt mit Beobachtungen.  
> Eine Bewertung wird erst mit Kontext belastbar.
