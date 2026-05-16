# Hinweise

## Hinweis 1: Relevante Conversation finden

Nutze:

```text
Statistics > Conversations > TCP
```

Der Download-Stream hat typischerweise die meisten Bytes vom Server zum Client.

## Hinweis 2: Server und Client

Server:

```text
172.28.60.10
```

Client:

```text
172.28.60.100
```

HTTP-Port:

```text
80
```

## Hinweis 3: Analysefelder

Beginne mit:

```text
tcp.analysis.flags
```

Dann gezielter:

```text
tcp.analysis.retransmission or tcp.analysis.fast_retransmission
```

und:

```text
tcp.analysis.duplicate_ack
```

## Hinweis 4: Duplicate ACKs einordnen

Wenn Daten vom Server zum Client fehlen, sendet häufig der Client Duplicate ACKs zurück zum Server.

Das bedeutet nicht automatisch:

```text
Der Client ist schuld.
```

Es bedeutet zunächst:

```text
Der Client bestätigt wiederholt dasselbe erwartete nächste Byte.
```

## Hinweis 5: Wireshark-Analysefelder sind Interpretationen

`tcp.analysis.*` Felder sind von Wireshark berechnete Hinweise.

Sie sind hilfreich, aber kein Ersatz für Kontext.

Prüfe den Stream, die Richtung und die umliegenden Frames.

## Hinweis 6: Keine voreilige Ursache

Nicht sauber:

```text
Der Switch verliert Pakete.
```

Besser:

```text
Im untersuchten TCP Stream sind Retransmissions und Duplicate ACKs sichtbar. Das Muster passt zu Paketverlust oder fehlenden Segmenten aus Sicht dieses Capture-Punkts.
```
