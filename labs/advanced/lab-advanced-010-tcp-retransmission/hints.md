# Hinweise

## Hinweis 1: keine Retransmissions sichtbar

Wiederhole den Download während der Capture läuft:

```bash
docker compose -f docker/compose/lab-advanced-tcp-loss/compose.yml exec lab-client sh -lc '
rm -f /tmp/bigfile.bin
curl -o /tmp/bigfile.bin http://172.28.60.10/bigfile.bin
'
```

Wenn weiterhin keine Retransmissions sichtbar sind, prüfe die Logs:

```bash
docker compose -f docker/compose/lab-advanced-tcp-loss/compose.yml logs lab-web-loss
```

Dort sollte `tc qdisc` mit `netem` sichtbar sein.

## Hinweis 2: passenden Stream finden

Nutze:

```text
tcp.port == 80
```

Dann öffne:

```text
Statistics > Conversations > TCP
```

Der Download-Stream hat typischerweise viele Bytes vom Server zum Client.

## Hinweis 3: Retransmission Filter

Nutze:

```text
tcp.analysis.retransmission
```

und:

```text
tcp.analysis.fast_retransmission
```

Gemeinsam:

```text
tcp.analysis.retransmission or tcp.analysis.fast_retransmission
```

## Hinweis 4: Duplicate ACKs

Duplicate ACKs kommen vom Empfänger.

Wenn Serverdaten verloren gehen, kommen Duplicate ACKs häufig vom Client in Richtung Server.

Filter:

```text
tcp.analysis.duplicate_ack
```

## Hinweis 5: Wireshark Analysefelder

Felder wie diese sind Wireshark-Interpretationen:

```text
tcp.analysis.retransmission
tcp.analysis.duplicate_ack
tcp.analysis.lost_segment
```

Sie stehen nicht als solche im Paket auf dem Kabel.

Das heißt nicht, dass sie wertlos sind. Es heißt nur:

> Kontext prüfen.

## Hinweis 6: nicht zu stark formulieren

Schlecht:

```text
Das Netzwerk ist kaputt.
```

Besser:

```text
Im untersuchten TCP Stream sind Retransmissions und Duplicate ACKs sichtbar. Das Muster passt zu Paketverlust oder fehlenden Segmenten aus Sicht dieses Capture-Punkts.
```
