# Aufgaben

## Aufgabe 1: Lab starten

Aus dem Repository-Root:

```bash
docker compose -f docker/compose/lab-advanced-tcp-loss/compose.yml up -d --build
```

Prüfen:

```bash
docker compose -f docker/compose/lab-advanced-tcp-loss/compose.yml ps
docker compose -f docker/compose/lab-advanced-tcp-loss/compose.yml logs lab-web-loss
```

## Aufgabe 2: Capture starten

Ordner vorbereiten:

```bash
mkdir -p pcaps/generated
```

Capture starten:

```bash
sudo tshark -i any -f "net 172.28.60.0/24" \
  -w pcaps/generated/challenge-007-discards-retransmission-correlation.pcapng
```

## Aufgabe 3: Download erzeugen

In einem zweiten Terminal:

```bash
docker compose -f docker/compose/lab-advanced-tcp-loss/compose.yml exec lab-client sh -lc '
rm -f /tmp/bigfile.bin
curl -o /tmp/bigfile.bin http://172.28.60.10/bigfile.bin
ls -lh /tmp/bigfile.bin
'
```

Falls später keine Analysehinweise sichtbar sind, wiederhole den Download ein- bis zweimal während der Capture läuft.

## Aufgabe 4: Capture stoppen

Stoppe TShark mit:

```text
Ctrl + C
```

Öffne den Capture:

```bash
wireshark pcaps/generated/challenge-007-discards-retransmission-correlation.pcapng
```

## Aufgabe 5: Relevanten Stream finden

Prüfe:

```text
Statistics > Conversations
```

Finde:

- die Verbindung zwischen Client und Webserver
- den TCP Port
- den TCP Stream
- die Richtung mit den meisten Bytes

Dokumentiere:

```text
tcp.stream == <nummer>
```

## Aufgabe 6: TCP-Symptome prüfen

Teste:

```text
tcp.analysis.flags
```

```text
tcp.analysis.retransmission
```

```text
tcp.analysis.fast_retransmission
```

```text
tcp.analysis.duplicate_ack
```

```text
tcp.analysis.lost_segment
```

Beantworte mit Frame-Nummern:

- Welche Analysehinweise sind sichtbar?
- Gibt es Retransmissions?
- Gibt es Duplicate ACKs?
- Welche Seite sendet erneut?
- Welche Seite sendet Duplicate ACKs?
- Passt das zu fehlenden Segmenten oder Paketverlust?

## Aufgabe 7: Monitoring-Korrelation formulieren

Beziehe die Monitoring-Meldung ein.

Beantworte:

- Passt das Zeitfenster grundsätzlich zur Beobachtung?
- Passt `OutDiscards` grundsätzlich zu Paketverlustsymptomen?
- Was ist dadurch stärker belegt?
- Was ist dadurch noch nicht bewiesen?

## Aufgabe 8: Nächste reale Prüfungen definieren

Nenne mindestens sechs nächste Schritte in einer echten Umgebung.

Beispiele:

- Queue-/QoS-Counter prüfen
- Interface-Last im Zeitfenster prüfen
- Gegen-Capture auf Client oder Server
- Top Talker prüfen
- SPAN/TAP-Capture gezielter planen
- Switch-/Router-Logs prüfen
- Port-Geschwindigkeit und Oversubscription prüfen
- Hostmetriken prüfen

## Aufgabe 9: TShark-Check ausführen

```bash
bash challenges/challenge-007-discards-retransmission-correlation/check_tshark.sh \
  pcaps/generated/challenge-007-discards-retransmission-correlation.pcapng
```

## Aufgabe 10: Kurzbericht schreiben

```text
Capture-Punkt:
<wo wurde mitgeschnitten?>

Monitoring:
<Counter, Richtung, Zeitfenster>

PCAP:
<relevanter Stream, Symptome, Frames>

Korrelation:
<was passt zusammen?>

Bewertung:
<was ist belegt?>

Einschränkungen:
<was ist nicht belegt?>

Nächste Schritte:
<reale Prüfungen>
```

## Aufgabe 11: Lab stoppen

```bash
docker compose -f docker/compose/lab-advanced-tcp-loss/compose.yml down
```
