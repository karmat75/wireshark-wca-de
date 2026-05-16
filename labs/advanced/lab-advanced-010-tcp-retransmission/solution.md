# Musterlösung

Die genauen Frame-Nummern hängen von deinem lokal erzeugten Capture ab.

Durch den absichtlich eingebauten Paketverlust sollten aber TCP Analysehinweise sichtbar werden.

## Erwartete Grundbeobachtung

Beteiligte Systeme:

| Rolle | IP |
|---|---:|
| Client | `172.28.60.100` |
| Webserver | `172.28.60.10` |

Filter:

```text
ip.addr == 172.28.60.10 and tcp.port == 80
```

Erwartung:

- TCP Handshake
- HTTP Request
- großer Datentransfer vom Server zum Client
- TCP Analysehinweise
- Retransmissions und/oder Fast Retransmissions
- Duplicate ACKs möglich

## TCP Stream

Filter:

```text
tcp.stream == <nummer>
```

Bewertung:

```text
Der TCP Stream isoliert die Download-Verbindung. Dadurch können Retransmissions, ACKs und Datenfluss ohne Vermischung mit anderen Verbindungen betrachtet werden.
```

## Retransmissions

Filter:

```text
tcp.analysis.retransmission
```

oder:

```text
tcp.analysis.fast_retransmission
```

Gemeinsam:

```text
tcp.analysis.retransmission or tcp.analysis.fast_retransmission
```

Beispielbewertung:

```text
Im TCP Stream sind Retransmissions sichtbar. Das bedeutet, dass Daten erneut übertragen wurden. In diesem Lab ist Paketverlust absichtlich eingebaut. In einem echten Fall wäre damit noch nicht automatisch bewiesen, wo genau ein Paket verloren ging.
```

## Duplicate ACKs

Filter:

```text
tcp.analysis.duplicate_ack
```

Beispielbewertung:

```text
Duplicate ACKs zeigen, dass der Empfänger wiederholt dasselbe nächste erwartete Byte bestätigt. Das passt zu fehlenden Segmenten im Datenstrom und kann Fast Retransmit auslösen.
```

## Wireshark Analysefelder richtig bewerten

Wichtig:

```text
tcp.analysis.* sind von Wireshark generierte Analysefelder.
```

Sie sind sehr hilfreich, aber sie sind keine Felder, die genauso im Paket übertragen wurden.

Gute Formulierung:

```text
Wireshark interpretiert die Paketfolge als Retransmission.
```

oder:

```text
Im Capture ist eine Paketfolge sichtbar, die Wireshark als Duplicate ACK und Retransmission einordnet.
```

Zu stark:

```text
Wireshark hat rot markiert, also ist das Netzwerk definitiv kaputt.
```

## Beispielbericht

```text
Capture-Punkt:
Host-System, Interface any, Capture Filter net 172.28.60.0/24

TCP Stream:
tcp.stream == <nummer>

Beobachtungen:
- Der Client 172.28.60.100 baut eine TCP-Verbindung zum Webserver 172.28.60.10:80 auf.
- Im Stream ist ein HTTP-Download von /bigfile.bin sichtbar.
- Der Webserver sendet den größeren Datenanteil zum Client.
- Im Stream sind TCP Retransmissions sichtbar.
- Zusätzlich sind Duplicate ACKs sichtbar.

Verwendete Filter:
ip.addr == 172.28.60.10 and tcp.port == 80
tcp.stream == <nummer>
tcp.analysis.flags
tcp.analysis.retransmission
tcp.analysis.fast_retransmission
tcp.analysis.duplicate_ack

Bewertung:
Das Muster passt zu Paketverlust oder fehlenden Segmenten im TCP-Datenstrom. Im Lab ist dieser Paketverlust absichtlich durch netem auf der Serverseite erzeugt. In einer echten Umgebung müsste der Capture-Punkt, der Pfad und ggf. ein Gegen-Capture auf Server- oder Client-Seite geprüft werden.

Einschränkungen:
Der Capture zeigt die Sicht am Host-Capture-Punkt. Er beweist ohne weitere Daten nicht, welches physische oder virtuelle Segment in einer echten Umgebung verantwortlich wäre.
```

## Nächster Schritt in einem echten Fall

Sinnvolle nächste Schritte wären:

- Client- und Server-Capture vergleichen
- Switch-/Firewall-Interface-Counter prüfen
- Paketverlust auf dem Pfad messen
- TCP Offloading und Capture-Punkt prüfen
- Systemlast auf Client und Server prüfen
- prüfen, ob nur ein Ziel oder viele Ziele betroffen sind

## Merksatz

> Retransmissions sind ein starkes Symptom.  
> Die Ursache entsteht erst durch Kontext, Capture-Punkt und zusätzliche Belege.
