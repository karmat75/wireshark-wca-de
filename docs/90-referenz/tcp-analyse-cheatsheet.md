# TCP-Analyse-Cheatsheet

Diese Seite sammelt typische TCP-Beobachtungen, passende Filter und vorsichtige Formulierungen.

## Grundidee

TCP ist ein Bytestrom zwischen zwei Endpunkten.

Für Analyse bedeutet das:

1. Verbindung finden
2. Stream isolieren
3. Handshake prüfen
4. Datenrichtung prüfen
5. Analysehinweise bewerten
6. nicht vorschnell Ursache behaupten

## Relevante Filter

| Frage | Filter |
|---|---|
| TCP anzeigen | `tcp` |
| TCP-Port | `tcp.port == 80` |
| SYN ohne ACK | `tcp.flags.syn == 1 and tcp.flags.ack == 0` |
| SYN/ACK | `tcp.flags.syn == 1 and tcp.flags.ack == 1` |
| RST | `tcp.flags.reset == 1` |
| FIN | `tcp.flags.fin == 1` |
| bestimmter Stream | `tcp.stream == <nummer>` |
| TCP Analysehinweise | `tcp.analysis.flags` |

## TCP 3-Way Handshake

Erwartetes Muster:

```text
Client -> Server  SYN
Server -> Client  SYN/ACK
Client -> Server  ACK
```

Gute Formulierung:

```text
Der TCP 3-Way Handshake ist vollständig sichtbar.
```

Vorsicht:

```text
Ein erfolgreicher TCP Handshake beweist nicht automatisch, dass die Anwendung korrekt funktioniert.
```

## SYN ohne Antwort

Muster:

```text
Client -> Server  SYN
Client -> Server  SYN
Client -> Server  SYN
```

Mögliche Bewertung:

```text
Aus Sicht dieses Capture-Punkts ist keine SYN/ACK-Antwort sichtbar.
```

Nicht vorschnell:

```text
Die Firewall ist schuld.
```

Besser:

```text
Mögliche Ursachen wären Filtering, Routing, Zielsystem nicht erreichbar oder ein ungünstiger Capture-Punkt. Weitere Daten sind nötig.
```

## RST / RST-ACK

Muster:

```text
Client -> Server  SYN
Server -> Client  RST/ACK
```

Mögliche Bewertung:

```text
Der Verbindungsversuch wird aktiv zurückgesetzt oder abgelehnt.
```

Im Lab häufig:

```text
Auf dem Zielport lauscht kein Dienst.
```

Nicht automatisch:

```text
Die Firewall ist schuld.
```

oder:

```text
Der Server ist offline.
```

## Retransmission

Filter:

```text
tcp.analysis.retransmission
```

oder:

```text
tcp.analysis.retransmission or tcp.analysis.fast_retransmission
```

Gute Formulierung:

```text
Im TCP Stream sind erneute Übertragungen sichtbar.
```

Vorsicht:

```text
Retransmissions zeigen ein Symptom. Der konkrete Fehlerort ist damit nicht automatisch bewiesen.
```

## Duplicate ACK

Filter:

```text
tcp.analysis.duplicate_ack
```

Bedeutung:

```text
Der Empfänger bestätigt wiederholt dasselbe nächste erwartete Byte.
```

Mögliche Einordnung:

```text
Das passt zu fehlenden Segmenten im Datenstrom und kann Fast Retransmit auslösen.
```

Nicht automatisch:

```text
Der Empfänger ist schuld.
```

## Fast Retransmit

Filter:

```text
tcp.analysis.fast_retransmission
```

Gute Formulierung:

```text
Wireshark interpretiert die Paketfolge als Fast Retransmit.
```

Wichtig:

```text
Die `tcp.analysis.*` Felder sind Wireshark-Analysehinweise und müssen im Stream-Kontext geprüft werden.
```

## Zero Window

Filter:

```text
tcp.analysis.zero_window
```

Bedeutung:

```text
Der Empfänger signalisiert, dass er aktuell keine weiteren Daten aufnehmen kann.
```

Mögliche Einordnung:

```text
Das kann auf Anwendung, Puffer oder Systemlast auf Empfängerseite hinweisen.
```

Nicht automatisch:

```text
Das Netzwerk verliert Pakete.
```

## Window Update

Filter:

```text
tcp.analysis.window_update
```

Bedeutung:

```text
Der Empfänger signalisiert wieder mehr verfügbares Empfangsfenster.
```

Zusammen mit Zero Window interessant.

## Previous Segment Not Captured

Filter:

```text
tcp.analysis.lost_segment
```

oder über Info-Spalte:

```text
Previous segment not captured
```

Gute Formulierung:

```text
Wireshark erkennt eine Lücke in der beobachteten Sequenz.
```

Vorsicht:

```text
Das Segment wurde am Capture-Punkt nicht gesehen. Ob es tatsächlich auf dem Netz verloren ging, muss weiter geprüft werden.
```

## Out-of-Order

Filter:

```text
tcp.analysis.out_of_order
```

Mögliche Bewertung:

```text
Pakete kommen aus Sicht des Capture-Punkts in anderer Reihenfolge an.
```

Nicht automatisch kritisch:

```text
Out-of-Order kann je nach Pfad, Capture-Punkt oder Offloading auftreten und muss im Kontext bewertet werden.
```

## Vorgehensweise bei TCP-Problemen

```text
1. Betroffene IPs und Ports identifizieren
2. Conversation oder Stream finden
3. tcp.stream isolieren
4. Handshake prüfen
5. Richtung der Datenübertragung bestimmen
6. tcp.analysis.flags prüfen
7. auffällige Frames notieren
8. Zeitabstände betrachten
9. Gegenrichtung prüfen
10. Aussage vorsichtig formulieren
```

## Berichtssprache

| Unscharf | Besser |
|---|---|
| Das Netzwerk ist kaputt. | Im Capture sind Retransmissions im Stream X sichtbar. |
| Die Firewall blockt. | Auf SYN ist aus Sicht dieses Capture-Punkts keine SYN/ACK-Antwort sichtbar. |
| Der Server ist tot. | Der Verbindungsversuch wird mit RST/ACK beantwortet. |
| Wireshark sagt Fehler. | Wireshark markiert die Paketfolge als `tcp.analysis.retransmission`. |
| Der Client ist schuld. | Duplicate ACKs kommen vom Client; das ist ein Symptom im Datenstrom, keine Ursachenfeststellung. |

## Merksatz

> TCP zeigt dir sehr viel.  
> Aber TCP sagt dir selten allein, wo genau die Ursache liegt.
