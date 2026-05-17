# Challenge 007: Discards und Retransmission-Korrelation

## Kurzbeschreibung

Ein Monitoring-System meldet in einem Zeitfenster OutDiscards auf einem Interface.

Im selben Zeitraum wirkt ein HTTP-Download langsam oder unruhig.

Du sollst mit Wireshark prüfen, ob im Capture passende TCP-Symptome sichtbar sind und wie weit die Aussage belastbar ist.

## Voraussetzungen

- Docker
- Docker Compose
- Wireshark
- TShark
- vorhandenes Docker-Lab `lab-advanced-tcp-loss`

## Ergebnis-PCAP

```text
pcaps/generated/challenge-007-discards-retransmission-correlation.pcapng
```

## Geschätzte Dauer

```text
60 Minuten
```

## Wichtiger Punkt

Die Challenge ist bewusst generisch.

Das Monitoring-System kann Checkmk, LibreNMS, Zabbix, PRTG, Prometheus, Grafana, Observium, ein NMS oder ein Hersteller-Tool sein.

Entscheidend ist nicht das Produkt.

Entscheidend ist die Korrelation aus:

```text
Counter + Zeitfenster + Topologie + Capture-Punkt + PCAP-Beobachtung
```
