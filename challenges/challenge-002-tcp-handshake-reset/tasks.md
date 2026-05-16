# Aufgaben

## Aufgabe 1: Lab starten

Aus dem Repository-Root:

```bash
docker compose -f docker/compose/lab-basic-dns-http/compose.yml up -d
```

Prüfen:

```bash
docker compose -f docker/compose/lab-basic-dns-http/compose.yml ps
```

## Aufgabe 2: Capture starten

Ordner vorbereiten:

```bash
mkdir -p pcaps/generated
```

Capture starten:

```bash
sudo tshark -i any -f "net 172.28.50.0/24" \
  -w pcaps/generated/challenge-002-tcp-handshake-reset.pcapng
```

## Aufgabe 3: Testtraffic erzeugen

In einem zweiten Terminal:

```bash
docker compose -f docker/compose/lab-basic-dns-http/compose.yml exec lab-client sh -lc '
curl -I http://web-ok.lab.local
curl -v --connect-timeout 3 --max-time 5 http://172.28.50.10:81 || true
'
```

## Aufgabe 4: Capture stoppen

Stoppe TShark mit:

```text
Ctrl + C
```

Öffne den Capture:

```bash
wireshark pcaps/generated/challenge-002-tcp-handshake-reset.pcapng
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
- Welche TCP-Ports sind sichtbar?
- Gibt es HTTP?
- Gibt es RST-Pakete?
- Welche TCP Streams sind relevant?

## Aufgabe 6: Erfolgreichen Handshake belegen

Finde die Verbindung zu Port 80.

Nutze passende Filter, zum Beispiel:

```text
tcp.port == 80
```

```text
tcp.flags.syn == 1
```

Beantworte mit Frame-Nummern:

- Welcher Frame ist SYN?
- Welcher Frame ist SYN/ACK?
- Welcher Frame ist das abschließende ACK?
- Welcher `tcp.stream` gehört dazu?
- Ist danach HTTP sichtbar?

## Aufgabe 7: Geschlossenen Port analysieren

Finde den Verbindungsversuch zu Port 81.

Filter:

```text
tcp.port == 81
```

und:

```text
tcp.flags.reset == 1
```

Beantworte mit Frame-Nummern:

- Gibt es SYN zu Port 81?
- Gibt es RST oder RST/ACK?
- Wer sendet das Reset?
- Ist das eher Timeout oder aktive Ablehnung?
- Welche Aussage ist belegbar?

## Aufgabe 8: Kurzbewertung schreiben

Schreibe eine kurze Bewertung:

- Port 80: erreichbar ja/nein?
- HTTP: Antwort sichtbar ja/nein?
- Port 81: Timeout oder aktive Ablehnung?
- Was ist belegt?
- Was ist nicht belegt?
- Welche nächste Prüfung wäre in einer echten Umgebung sinnvoll?

## Aufgabe 9: TShark-Check ausführen

```bash
bash challenges/challenge-002-tcp-handshake-reset/check_tshark.sh \
  pcaps/generated/challenge-002-tcp-handshake-reset.pcapng
```

## Aufgabe 10: Lab stoppen

```bash
docker compose -f docker/compose/lab-basic-dns-http/compose.yml down
```
