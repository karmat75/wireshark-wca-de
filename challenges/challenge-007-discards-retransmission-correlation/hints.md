# Hinweise

## Hinweis 1: OutDiscards sind keine Pakete im PCAP

Ein OutDiscard ist ein Counter am Gerät.

Wireshark sieht nicht automatisch den Discard selbst.

Wireshark kann aber Symptome sehen, zum Beispiel:

```text
tcp.analysis.retransmission
tcp.analysis.duplicate_ack
tcp.analysis.fast_retransmission
```

## Hinweis 2: Relevante Conversation

Nutze:

```text
Statistics > Conversations > TCP
```

Die Download-Verbindung hat typischerweise viele Bytes vom Server zum Client.

## Hinweis 3: Richtung beachten

Wenn Serverdaten fehlen, kommen Duplicate ACKs oft vom Client.

Das heißt nicht:

```text
Der Client ist schuld.
```

Es heißt zunächst:

```text
Der Client bestätigt wiederholt dasselbe nächste erwartete Byte.
```

## Hinweis 4: Korrelation ist stärker als ein einzelner Hinweis

Ein Monitoring-Counter allein ist nicht genug.

Ein PCAP-Hinweis allein ist nicht genug.

Zusammen können sie eine plausible Hypothese stützen.

## Hinweis 5: Nicht zu stark formulieren

Nicht sauber:

```text
Der Switch hat die Pakete verworfen.
```

Besser:

```text
Im Zeitraum der gemeldeten OutDiscards sind im Capture TCP-Symptome sichtbar, die zu Paketverlust oder fehlenden Segmenten passen. Der genaue Drop-Ort ist noch nicht eindeutig belegt.
```
