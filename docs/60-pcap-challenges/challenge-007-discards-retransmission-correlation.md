# Challenge 007: Discards und Retransmission-Korrelation

Diese Challenge verbindet Monitoring-Zeitfenster mit einem TCP-Capture.

Du erzeugst mit dem vorhandenen Docker-Lab `lab-advanced-tcp-loss` einen Capture mit Paketverlustsymptomen.

Zusätzlich bekommst du ein generisches Monitoring-Szenario:

```text
Ein Monitoring-System meldet während des Downloads OutDiscards auf einem betroffenen Interface.
```

Deine Aufgabe ist nicht, den Switch als Ursache zu behaupten.

Deine Aufgabe ist, sauber zu korrelieren:

- Was zeigt das Monitoring?
- Was zeigt der Capture?
- Passt das zeitlich und fachlich zusammen?
- Was ist belegt?
- Was ist nicht belegt?

## Challenge-Pfad

```text
challenges/challenge-007-discards-retransmission-correlation/
```

## Benötigtes Docker-Lab

```text
docker/compose/lab-advanced-tcp-loss/compose.yml
```

## Ergebnis-PCAP

```text
pcaps/generated/challenge-007-discards-retransmission-correlation.pcapng
```

Diese Datei wird lokal erzeugt und nicht committed.

## Ziel

Du sollst herausfinden:

- welcher TCP Stream den Download enthält
- ob Retransmissions sichtbar sind
- ob Duplicate ACKs sichtbar sind
- ob das Muster zu Paketverlust oder fehlenden Segmenten passt
- wie die Monitoring-Meldung vorsichtig einbezogen wird
- warum der konkrete Drop-Ort nicht allein durch den Capture bewiesen ist

## WCA-/Praxisbezug

Diese Challenge trainiert:

- TCP Analyse
- Retransmissions
- Duplicate ACKs
- Capture-Punkt
- Monitoring-Korrelation
- Interface-Counter-Einordnung
- vorsichtige Troubleshooting-Bewertung
