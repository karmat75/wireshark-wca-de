# Aufgaben

## Aufgabe 1: Lab starten

Aus dem Repository-Root:

```bash
docker compose -f docker/compose/lab-advanced-security-basics/compose.yml up -d --build
```

Prüfen:

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
  -w pcaps/generated/challenge-005-security-basics-triage.pcapng
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

Stoppe TShark mit:

```text
Ctrl + C
```

Öffne den Capture:

```bash
wireshark pcaps/generated/challenge-005-security-basics-triage.pcapng
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

- Welche IPs sind beteiligt?
- Ist TLS sichtbar?
- Ist HTTP sichtbar?
- Welche TCP Conversation ist relevant?
- Welche Methoden sind sichtbar?

## Aufgabe 6: HTTP Requests analysieren

Nutze passende Filter:

```text
http.request
```

```text
http.request.method == "POST"
```

```text
http.request.uri contains "/beacon"
```

Beantworte mit Frame-Nummern:

- Welche URIs wurden angefragt?
- Welche HTTP-Methoden wurden verwendet?
- Welche User-Agents sind sichtbar?
- Gibt es regelmäßige Requests?

## Aufgabe 7: Zugangsdaten und Tokens suchen

Nutze passende Filter:

```text
http.authorization
```

```text
http contains "LabPassword123"
```

```text
http contains "LAB-TOKEN-12345"
```

Beantworte:

- Ist ein Authorization Header sichtbar?
- Sind Formularwerte sichtbar?
- Ist ein Token sichtbar?
- Warum ist das bei HTTP möglich?
- Wie wäre ein echter Capture zu behandeln?

## Aufgabe 8: Beacon-Muster bewerten

Nutze:

```text
http.request.uri contains "/beacon"
```

und:

```text
http.user_agent contains "BeaconSimulator"
```

Beantworte:

- Wie viele Beacon-Requests sind sichtbar?
- Welche Query-Parameter sind sichtbar?
- Wie groß ist der Abstand ungefähr?
- Ist Malware dadurch bewiesen?
- Welche vorsichtige Formulierung ist besser?

## Aufgabe 9: Kurzbewertung schreiben

Schreibe eine kurze Triage:

```text
Capture-Punkt:
<wo wurde mitgeschnitten?>

Klartext:
<sichtbare Header/Formulardaten/Tokens>

Beacon-Muster:
<Anzahl, Abstand, URI, User-Agent>

Bewertung:
<was ist belegt?>

Einschränkungen:
<was ist nicht belegt?>

Schutzbedarf:
<wie müsste ein echter Capture behandelt werden?>
```

## Aufgabe 10: TShark-Check ausführen

```bash
bash challenges/challenge-005-security-basics-triage/check_tshark.sh \
  pcaps/generated/challenge-005-security-basics-triage.pcapng
```

## Aufgabe 11: Lab stoppen

```bash
docker compose -f docker/compose/lab-advanced-security-basics/compose.yml down
```
