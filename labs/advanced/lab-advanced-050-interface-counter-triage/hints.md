# Hinweise

## Hinweis 1: Errors und Discards trennen

Errors sind häufig näher an Layer 1/2.

Discards sind häufig näher an Queue, Buffer, QoS, Policy oder Ressourcen.

Das ist nur eine erste Einordnung, keine endgültige Ursache.

## Hinweis 2: CRC/FCS

Bei CRC/FCS-Fehlern ist Wireshark selten das erste Werkzeug.

Prüfe eher:

- Kabel
- Patchfeld
- SFP
- Optikwerte
- Port
- Gegenstelle
- Speed/Duplex
- Gerätelog

## Hinweis 3: OutDiscards

OutDiscards passen oft zu:

- Egress-Queue voll
- Congestion
- Microbursts
- QoS Drops
- Oversubscription
- zu langsamer Ausgangsport

Wireshark kann Symptome zeigen, aber nicht immer den Drop selbst.

## Hinweis 4: Uplink ist anders als Access-Port

Auf einem Uplink können viele VLANs und viele Flows zusammenlaufen.

Ein Capture dort kann groß und schwer auszuwerten sein.

Conversations und Top Talker werden wichtiger.

## Hinweis 5: Capture-Punkt ist Teil der Aussage

Eine Analyse ohne Capture-Punkt ist unvollständig.

Sauber:

```text
Aus Sicht dieses Capture-Punkts sind Retransmissions sichtbar.
```

Nicht sauber:

```text
Das Paket ging auf dem Switch verloren.
```

## Hinweis 6: Monitoring ist ein Zeitfenster

Counter ohne Zeitbezug sind gefährlich.

Immer fragen:

```text
Wann stieg der Counter?
```

```text
Was passierte gleichzeitig?
```

```text
Wie stark war die Last?
```
