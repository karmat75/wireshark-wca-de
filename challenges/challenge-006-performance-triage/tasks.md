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
  -w pcaps/generated/challenge-006-performance-triage.pcapng
```

## Aufgabe 3: Testtraffic erzeugen

In einem zweiten Terminal:

```bash
docker compose -f docker/compose/lab-basic-dns-http/compose.yml exec lab-client sh -lc '
dig web-ok.lab.local
curl -I http://web-ok.lab.local
dig web-slow.lab.local
curl -I http://web-slow.lab.local
'
```

Wiederhole den Block optional ein zweites Mal, falls du mehrere Vergleichswerte möchtest.

## Aufgabe 4: Capture stoppen

Stoppe TShark mit:

```text
Ctrl + C
```

Öffne den Capture:

```bash
wireshark pcaps/generated/challenge-006-performance-triage.pcapng
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
- Welche IPs sind beteiligt?
- Welche TCP-Conversations gehören zu `web-ok` und `web-slow`?
- Welche Conversation wirkt zeitlich oder fachlich relevant?

## Aufgabe 6: DNS bewerten

Nutze passende Filter:

```text
dns
```

```text
dns.flags.response == 0
```

```text
dns.flags.response == 1
```

Beantworte mit Frame-Nummern:

- Wann wird `web-ok.lab.local` abgefragt?
- Wann kommt die DNS Response?
- Wann wird `web-slow.lab.local` abgefragt?
- Wann kommt die DNS Response?
- Ist DNS die auffällige Wartezeit?

## Aufgabe 7: TCP bewerten

Nutze passende Filter:

```text
tcp.flags.syn == 1
```

```text
ip.addr == 172.28.50.10 and tcp
```

```text
ip.addr == 172.28.50.20 and tcp
```

Beantworte mit Frame-Nummern:

- Ist der TCP Handshake zu beiden Servern sichtbar?
- Gibt es zwischen SYN und SYN/ACK eine auffällige Wartezeit?
- Ist TCP-Verbindungsaufbau die auffällige Wartezeit?

## Aufgabe 8: HTTP Request/Response bewerten

Nutze passende Filter:

```text
http
```

```text
ip.addr == 172.28.50.10 and http
```

```text
ip.addr == 172.28.50.20 and http
```

Beantworte mit Frame-Nummern:

- Wann geht der HTTP Request zu `web-ok` raus?
- Wann kommt die HTTP Response von `web-ok`?
- Wann geht der HTTP Request zu `web-slow` raus?
- Wann kommt die HTTP Response von `web-slow`?
- Wie groß ist der Unterschied ungefähr?
- Wo liegt die sichtbare Wartezeit?

## Aufgabe 9: Kurzbewertung schreiben

Schreibe eine kurze Performance-Triage:

```text
Capture-Punkt:
<wo wurde mitgeschnitten?>

DNS:
<kurze Bewertung mit Frames>

TCP:
<kurze Bewertung mit Frames>

HTTP:
<kurze Bewertung mit Frames>

Bewertung:
<wo entsteht die sichtbare Wartezeit?>

Einschränkungen:
<was ist nicht belegt?>

Nächste Schritte:
<was wäre in einer echten Umgebung sinnvoll?>
```

## Aufgabe 10: TShark-Check ausführen

```bash
bash challenges/challenge-006-performance-triage/check_tshark.sh \
  pcaps/generated/challenge-006-performance-triage.pcapng
```

## Aufgabe 11: Lab stoppen

```bash
docker compose -f docker/compose/lab-basic-dns-http/compose.yml down
```
