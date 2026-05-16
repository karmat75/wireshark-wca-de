# Aufgaben

## Aufgabe 1: Docker-Lab starten

Aus dem Repository-Root:

```bash
docker compose -f docker/compose/lab-advanced-security-basics/compose.yml up -d --build
```

Status prüfen:

```bash
docker compose -f docker/compose/lab-advanced-security-basics/compose.yml ps
```

## Aufgabe 2: Capture starten

Ordner vorbereiten:

```bash
mkdir -p pcaps/generated
```

Capture starten:

```bash
sudo tshark -i any -f "net 172.28.80.0/24" \
  -w pcaps/generated/lab-advanced-040-security-basics.pcapng
```

Stoppen später mit:

```text
Ctrl + C
```

Alternativ kannst du Wireshark verwenden und als Capture Filter setzen:

```text
net 172.28.80.0/24
```

## Aufgabe 3: Testtraffic erzeugen

In einem zweiten Terminal:

```bash
docker compose -f docker/compose/lab-advanced-security-basics/compose.yml exec lab-client sh -lc '
curl --noproxy "*" -A "WWCA-LabClient/1.0" http://172.28.80.10/
curl --noproxy "*" -u labuser:LabPassword123 http://172.28.80.10/basic
curl --noproxy "*" -X POST -d "username=labuser&password=LabPassword123&token=LAB-TOKEN-12345" http://172.28.80.10/login
for i in 1 2 3 4 5; do
  curl --noproxy "*" -A "WWCA-BeaconSimulator/1.0" "http://172.28.80.10/beacon?id=training-node-01&seq=$i"
  sleep 1
done
'
```

## Aufgabe 4: Capture stoppen

Stoppe den Capture mit:

```text
Ctrl + C
```

Öffne die Datei:

```bash
wireshark pcaps/generated/lab-advanced-040-security-basics.pcapng
```

## Aufgabe 5: Grobe Orientierung

Prüfe:

```text
Statistics > Protocol Hierarchy
```

```text
Statistics > Conversations
```

Beantworte:

- Welche Protokolle sind sichtbar?
- Welche IP-Adressen sind beteiligt?
- Gibt es nur HTTP oder auch TLS?
- Welche TCP Conversation ist relevant?

## Aufgabe 6: HTTP Requests anzeigen

Teste:

```text
http.request
```

Dann:

```text
http.request.method == "GET"
```

```text
http.request.method == "POST"
```

Beantworte:

- Welche URIs wurden angefragt?
- Welche Methoden sind sichtbar?
- Welche Host-/User-Agent-Informationen sind sichtbar?
- Welche Frame-Nummern sind relevant?

## Aufgabe 7: Basic Auth finden

Teste:

```text
http.authorization
```

oder:

```text
http contains "Authorization"
```

Beantworte:

- In welchem Frame ist der Authorization Header sichtbar?
- Ist der Wert im Klartext übertragbar?
- Warum ist das bei HTTP problematisch?
- Warum sollten echte Captures mit solchen Daten besonders geschützt werden?

## Aufgabe 8: Formularwerte finden

Teste:

```text
http.request.method == "POST"
```

und suche im Paketdetail oder Follow TCP Stream nach:

```text
username
password
token
```

TShark-Alternative:

```bash
tshark -r pcaps/generated/lab-advanced-040-security-basics.pcapng \
  -Y "http.request.method == \"POST\"" \
  -T fields \
  -e frame.number \
  -e http.file_data
```

Beantworte:

- Sind Benutzername, Passwort oder Token sichtbar?
- Welche Werte sind synthetische Lab-Werte?
- Wie wäre das in einer echten Umgebung zu bewerten?

## Aufgabe 9: Beacon-ähnliche Requests untersuchen

Teste:

```text
http.request.uri contains "/beacon"
```

und:

```text
http.user_agent contains "Beacon"
```

Beantworte:

- Wie viele Beacon-Requests sind sichtbar?
- In welchem Zeitabstand ungefähr?
- Welche Query-Parameter sind sichtbar?
- Ist damit Malware bewiesen?
- Welche Formulierung wäre vorsichtiger?

## Aufgabe 10: Follow TCP Stream verwenden

Wähle einen HTTP-Request mit Basic Auth oder Formularwerten.

Nutze:

```text
Follow > TCP Stream
```

Beantworte:

- Welche Inhalte sind im Klartext sichtbar?
- Warum ist das hilfreich für Analyse?
- Warum ist das gleichzeitig sensibel?

## Aufgabe 11: TShark-Auswertung

Setze:

```bash
PCAP="pcaps/generated/lab-advanced-040-security-basics.pcapng"
```

HTTP Requests:

```bash
tshark -r "$PCAP" \
  -Y "http.request" \
  -T fields \
  -e frame.number \
  -e frame.time_relative \
  -e ip.src \
  -e ip.dst \
  -e http.request.method \
  -e http.host \
  -e http.request.uri \
  -e http.user_agent
```

Authorization Header:

```bash
tshark -r "$PCAP" \
  -Y "http.authorization" \
  -T fields \
  -e frame.number \
  -e http.authorization
```

Beacon-Requests:

```bash
tshark -r "$PCAP" \
  -Y "http.request.uri contains \"/beacon\"" \
  -T fields \
  -e frame.number \
  -e frame.time_relative \
  -e http.request.uri \
  -e http.user_agent
```

## Aufgabe 12: Check-Skript ausführen

```bash
bash labs/advanced/lab-advanced-040-security-basics/check_tshark.sh "$PCAP"
```

## Aufgabe 13: Kurzbericht schreiben

Schreibe einen Bericht:

```text
Capture-Punkt:
<wo wurde mitgeschnitten?>

Klartext:
<sichtbare Zugangsdaten oder Tokens>

Beacon-Muster:
<Anzahl, Abstand, URI, User-Agent>

Bewertung:
<was ist belegt?>

Einschränkungen:
<was ist nicht bewiesen?>

Schutzbedarf:
<wie müsste man mit so einem echten Capture umgehen?>
```

## Aufgabe 14: Lab stoppen

```bash
docker compose -f docker/compose/lab-advanced-security-basics/compose.yml down
```
