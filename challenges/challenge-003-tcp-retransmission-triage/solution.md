# Musterlösung

Die genauen Frame-Nummern hängen von deinem lokal erzeugten Capture ab.

## Relevante Verbindung

Beteiligte Systeme:

| Rolle | IP |
|---|---:|
| Client | `172.28.60.100` |
| Webserver | `172.28.60.10` |

Filter:

```text
ip.addr == 172.28.60.10 and tcp.port == 80
```

oder nach Ermittlung:

```text
tcp.stream == <nummer>
```

Erwartung:

- TCP Handshake
- HTTP Request auf `/bigfile.bin`
- großer Datentransfer vom Server zum Client
- TCP Analysehinweise im Stream

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
Im relevanten TCP Stream sind Retransmissions sichtbar. Das bedeutet, dass Daten erneut übertragen wurden. In diesem Lab ist Paketverlust absichtlich eingebaut. In einer echten Umgebung wäre damit noch nicht automatisch belegt, wo genau ein Paket verloren ging.
```

## Duplicate ACKs

Filter:

```text
tcp.analysis.duplicate_ack
```

Beispielbewertung:

```text
Duplicate ACKs zeigen, dass der Empfänger wiederholt dasselbe nächste erwartete Byte bestätigt. Das passt zu fehlenden Segmenten im TCP-Datenstrom und kann Fast Retransmit auslösen.
```

## Richtung

Typischerweise:

- Webserver `172.28.60.10` sendet große Datenmengen zum Client
- Client `172.28.60.100` sendet ACKs
- Duplicate ACKs kommen häufig vom Client
- Retransmissions kommen häufig vom Server

Sauber formuliert:

```text
Die erneuten Übertragungen betreffen Daten in der Richtung Server zu Client. Der Client bestätigt wiederholt dasselbe erwartete nächste Byte.
```

## Was belegt ist

Belegt ist:

- der Download-Stream
- TCP-Kommunikation zwischen Client und Server
- HTTP-Download
- Wireshark erkennt TCP Analysehinweise
- Retransmissions sind sichtbar
- Duplicate ACKs sind möglich oder sichtbar
- das Muster passt zu Paketverlust oder fehlenden Segmenten

## Was nicht belegt ist

Nicht automatisch belegt ist:

- welches physische Segment verantwortlich ist
- ob Client, Server, Docker-Netz oder Host-Netz Ursache ist
- ob ein Switch oder eine Firewall Pakete verwirft
- ob das gleiche Verhalten in Produktion auftritt
- ob ein einzelner Capture-Punkt die komplette Wahrheit zeigt

## Beispielbericht

```text
Capture-Punkt:
Host-System, Interface any, Capture Filter net 172.28.60.0/24

Relevanter Stream:
tcp.stream == <nummer>

Beobachtungen:
Der Client 172.28.60.100 baut eine TCP-Verbindung zum Webserver 172.28.60.10:80 auf.
Im Stream ist ein HTTP-Download von /bigfile.bin sichtbar.
Der Webserver sendet den größeren Datenanteil.
Im Stream sind TCP Retransmissions sichtbar.
Zusätzlich sind Duplicate ACKs sichtbar.

Bewertung:
Das Muster passt zu Paketverlust oder fehlenden Segmenten aus Sicht dieses Capture-Punkts. Im Lab ist Paketverlust absichtlich eingebaut. In einer echten Umgebung müsste geprüft werden, wo auf dem Weg die Pakete verloren gehen oder ob der Capture-Punkt selbst unvollständig ist.

Einschränkungen:
Ein einzelner Capture beweist nicht automatisch den konkreten Fehlerort. Dafür wären Gegen-Captures, Interface-Counter, Hostmetriken und Netzkomponenten-Logs sinnvoll.

Nächste Schritte:
Client- und Server-Capture vergleichen, Interface-Counter prüfen, Docker-/Host-Netzwerk prüfen, TCP Offloading berücksichtigen, betroffene Strecke eingrenzen.
```

## Merksatz

> Retransmission ist eine Beobachtung.  
> Der Fehlerort ist eine Hypothese, die weitere Belege braucht.
