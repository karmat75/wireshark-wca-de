# Musterlösung

Die genauen Frame-Nummern hängen von deinem lokal erzeugten Capture ab.

## HTTP-Klartext

Filter:

```text
http
```

Erwartung:

- HTTP Requests
- HTTP Responses
- sichtbare URIs
- sichtbare Header
- sichtbare Body-Daten bei POST

Bewertung:

```text
Der Capture zeigt HTTP-Verkehr im Klartext. Dadurch sind Header und Teile der Nutzdaten direkt analysierbar.
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

Bewertung:

```text
Ein Authorization Header ist im HTTP Request sichtbar. Basic Auth ist Base64-kodiert, aber nicht sicher verschlüsselt. Bei HTTP kann dieser Wert aus dem Capture extrahiert werden.
```

## Formularwerte und Token

Filter:

```text
http.request.method == "POST"
```

und:

```text
http contains "LAB-TOKEN-12345"
```

Erwartete sichtbare Werte:

```text
username=labuser
password=LabPassword123
token=LAB-TOKEN-12345
```

Bewertung:

```text
Der POST Body enthält synthetische Lab-Zugangsdaten und einen synthetischen Token im Klartext. In einer echten Umgebung wäre das ein Sicherheits- und Datenschutzrisiko.
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

User-Agent:

```text
WWCA-BeaconSimulator/1.0
```

Bewertung:

```text
Die Requests sind regelmäßig und enthalten fortlaufende Sequenzwerte. Das Muster ist Beacon-ähnlich. Es beweist ohne weiteren Kontext aber keine Malware.
```

## Was belegt ist

Belegt ist:

- HTTP im Klartext
- sichtbarer Authorization Header
- sichtbare synthetische Formularwerte
- sichtbarer synthetischer Token
- mehrere ähnliche `/beacon` Requests
- User-Agent `WWCA-BeaconSimulator/1.0`
- Query-Parameter mit `training-node-01` und `seq`

## Was nicht belegt ist

Nicht belegt ist:

- Malware
- echte Kompromittierung
- echter Datenabfluss
- Prozess auf dem Client
- Benutzerkontext
- Verhalten außerhalb der Lab-Umgebung

## Beispielbericht

```text
Capture-Punkt:
Host-System, Interface any, Capture Filter net 172.28.80.0/24

Klartext:
Im Capture ist HTTP-Verkehr zwischen 172.28.80.100 und 172.28.80.10 sichtbar.
Ein Request zu /basic enthält einen Authorization Header.
Der POST zu /login enthält username=labuser, password=LabPassword123 und token=LAB-TOKEN-12345 im Klartext.

Beacon-Muster:
Es sind fünf GET Requests zu /beacon sichtbar. Die Requests enthalten id=training-node-01 und fortlaufende seq-Werte. Der User-Agent lautet WWCA-BeaconSimulator/1.0. Der Abstand liegt ungefähr bei einer Sekunde.

Bewertung:
Der Capture belegt Klartextübertragung synthetischer sensibler Werte und ein regelmäßiges HTTP-Request-Muster. Das Muster ist Beacon-ähnlich, beweist aber ohne Host-, Prozess- und Kontextdaten keine Malware.

Einschränkungen:
Es handelt sich um eine kontrollierte Lab-Umgebung. In einer echten Umgebung müssten Hostdaten, Prozessinformationen, Proxy-Logs, DNS-Logs, EDR/AV und Serverlogs geprüft werden.

Schutzbedarf:
Ein echter Capture mit Authorization Headern, Passwörtern oder Tokens dürfte nicht öffentlich geteilt oder committed werden. Betroffene Zugangsdaten müssten rotiert werden.
```

## Merksatz

> Ein Capture kann starke Hinweise liefern.  
> Eine Security-Bewertung braucht trotzdem Kontext.
