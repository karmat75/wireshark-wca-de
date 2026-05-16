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
  -w pcaps/generated/challenge-003-tcp-retransmission-triage.pcapng
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

Falls der Download zu schnell war oder später keine Analysehinweise sichtbar sind, wiederhole den Download ein- bis zweimal während der Capture läuft.

## Aufgabe 4: Capture stoppen

Stoppe TShark mit:

```text
Ctrl + C
```

Öffne den Capture:

```bash
wireshark pcaps/generated/challenge-003-tcp-retransmission-triage.pcapng
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
- Welche TCP Conversation hat die meisten Bytes?
- Welcher Port wird verwendet?
- Welcher TCP Stream gehört zum Download?
- Welche Richtung sendet die meisten Daten?

## Aufgabe 6: TCP Stream isolieren

Filtere den relevanten Stream:

```text
tcp.stream == <nummer>
```

Beantworte:

- Ist der Handshake sichtbar?
- Ist HTTP sichtbar?
- Gibt es große Datenübertragung?
- Gibt es auffällige Zeitabstände?
- Gibt es Analysehinweise?

## Aufgabe 7: TCP Analysehinweise prüfen

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
- Gibt es Fast Retransmissions?
- Gibt es Duplicate ACKs?
- Von welcher Seite kommen die Duplicate ACKs?
- Welche Seite sendet erneut?

## Aufgabe 8: Belegbare Bewertung schreiben

Schreibe eine kurze Bewertung:

- Was ist im Capture sichtbar?
- Welche Richtung ist betroffen?
- Passt das Muster zu Paketverlust oder fehlenden Segmenten?
- Was ist durch einen einzelnen Capture-Punkt nicht bewiesen?
- Welche nächsten Prüfungen wären in einer echten Umgebung sinnvoll?

## Aufgabe 9: TShark-Check ausführen

```bash
bash challenges/challenge-003-tcp-retransmission-triage/check_tshark.sh \
  pcaps/generated/challenge-003-tcp-retransmission-triage.pcapng
```

## Aufgabe 10: Lab stoppen

```bash
docker compose -f docker/compose/lab-advanced-tcp-loss/compose.yml down
```
