# Musterlösung

Die genauen Frame-Nummern hängen von deinem lokal erzeugten Capture ab.

## Relevanter Stream

Beteiligte Systeme:

| Rolle | IP |
|---|---:|
| Client | `172.28.60.100` |
| Webserver | `172.28.60.10` |

Filter:

```text
ip.addr == 172.28.60.10 and tcp.port == 80
```

oder:

```text
tcp.stream == <nummer>
```

Erwartung:

- TCP-Verbindung zum Webserver
- HTTP Request auf `/bigfile.bin`
- großer Datentransfer vom Server zum Client
- TCP Analysehinweise

## TCP-Symptome

Erwartete Filter:

```text
tcp.analysis.flags
```

```text
tcp.analysis.retransmission or tcp.analysis.fast_retransmission
```

```text
tcp.analysis.duplicate_ack
```

Gute Beobachtung:

```text
Im relevanten TCP Stream sind Retransmissions sichtbar. Zusätzlich können Duplicate ACKs sichtbar sein. Das Muster passt zu fehlenden Segmenten im Datenstrom.
```

## Monitoring-Korrelation

Monitoring-Meldung:

```text
OutDiscards auf Interface sw-access-07 port-10 im Zeitraum der Beschwerde.
```

Saubere Einordnung:

```text
OutDiscards können zu Paketverlustsymptomen passen, besonders wenn der betroffene Datenstrom über dieses Interface läuft und das Zeitfenster übereinstimmt.
```

Aber:

```text
Der Capture allein beweist nicht, dass genau dieses Interface die Pakete verworfen hat.
```

Dazu braucht man weitere Belege:

- genaue Topologie
- Queue-/QoS-Counter
- Last im Zeitfenster
- Gegen-Capture
- Geräte-Logs
- ggf. TAP oder Capture an mehreren Punkten

## Was belegt ist

Belegt ist:

- der Download-Stream
- TCP-Verkehr zwischen Client und Webserver
- HTTP-Download von `/bigfile.bin`
- Retransmissions im Capture
- ggf. Duplicate ACKs
- das Muster passt zu Paketverlust oder fehlenden Segmenten
- Monitoring meldet im Szenario OutDiscards im passenden Zeitfenster

## Was nicht belegt ist

Nicht belegt ist:

- der exakte Drop-Ort
- dass der Switch allein verantwortlich ist
- dass der physische Port defekt ist
- dass das Problem in Produktion identisch wäre
- dass alle Benutzer betroffen sind
- dass die Ursache ohne weitere Counter feststeht

## Beispielbericht

```text
Capture-Punkt:
Host-System, Interface any, Capture Filter net 172.28.60.0/24

Monitoring:
Das Monitoring meldet OutDiscards auf sw-access-07 port-10 im Zeitraum 10:14-10:18.

PCAP:
Der relevante TCP Stream zeigt einen HTTP-Download von 172.28.60.10 zu 172.28.60.100. Im Stream sind Retransmissions und Duplicate ACKs sichtbar.

Korrelation:
Die PCAP-Symptome passen fachlich zu fehlenden Segmenten oder Paketverlust. Die Monitoring-Meldung mit OutDiscards im passenden Zeitfenster stützt diese Hypothese.

Bewertung:
Es ist plausibel, dass Paketverlust oder Verwerfungen im Pfad eine Rolle spielen. Der konkrete Drop-Ort ist durch diesen Capture allein nicht bewiesen.

Einschränkungen:
Es fehlt ein Gegen-Capture, eine genaue Topologiezuordnung und detaillierte Queue-/QoS-Counter des betroffenen Interfaces.

Nächste Schritte:
Queue-/QoS-Counter prüfen, Interface-Last im Zeitfenster prüfen, Gegen-Capture auf Client/Server, Top Talker prüfen, Port-/Uplink-Kapazität prüfen, Geräte-Logs und Nachbarinterfaces kontrollieren.
```

## Merksatz

> Korrelation macht eine Hypothese stärker.  
> Sie ersetzt nicht den Beweis des Fehlerorts.
