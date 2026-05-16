# Challenge 003: TCP Retransmission Triage

Diese Challenge nutzt das vorhandene Docker-Lab `lab-advanced-tcp-loss`.

Du erzeugst einen Capture und untersuchst eine Download-Verbindung mit absichtlichem Paketverlust.

## Challenge-Pfad

```text
challenges/challenge-003-tcp-retransmission-triage/
```

## Benötigtes Docker-Lab

```text
docker/compose/lab-advanced-tcp-loss/compose.yml
```

## Ergebnis-PCAP

```text
pcaps/generated/challenge-003-tcp-retransmission-triage.pcapng
```

Diese Datei wird lokal erzeugt und nicht committed.

## Ziel

Du sollst herausfinden:

- welche TCP-Verbindung den Download enthält
- welcher TCP Stream relevant ist
- ob Retransmissions sichtbar sind
- ob Duplicate ACKs sichtbar sind
- ob Fast Retransmit sichtbar ist
- welche Richtung betroffen ist
- was durch den Capture belegt ist
- was ohne weitere Daten nicht belegt ist

## WCA-Bezug

Diese Challenge trainiert:

- TCP Stream Analyse
- TCP Analysefelder
- Retransmission
- Duplicate ACK
- Fast Retransmit
- Conversations
- TShark
- Performance- und Fehleranalyse-Methodik
