# TCP Deep Dive

TCP ist der Bereich, in dem Wireshark besonders viel Mehrwert liefert.

Im Basis-Kurs hast du gelernt, TCP-Verbindungen, Handshakes, FIN, RST und TCP Streams zu erkennen.

Jetzt gehen wir tiefer.

In diesem Abschnitt geht es darum, TCP nicht nur zu sehen, sondern zu lesen:

- Welche Daten wurden gesendet?
- Welche Daten wurden bestätigt?
- Wo fehlen Segmente?
- Gibt es Retransmissions?
- Reagiert der Empfänger mit Duplicate ACKs?
- Ist das Capture vollständig?
- Gibt es Hinweise auf Paketverlust?
- Wird die Verbindung durch Window-Probleme gebremst?

## Ziel

Nach diesem Abschnitt solltest du können:

- TCP Streams systematisch analysieren
- Sequence Number und ACK Number praktisch interpretieren
- Retransmissions, Duplicate ACKs und Fast Retransmit unterscheiden
- Out-of-Order und Previous Segment Not Captured einordnen
- SACK grundsätzlich verstehen
- Window Size und Window Scaling erkennen
- Zero Window und Window Update erkennen
- Wireshark-TCP-Analysehinweise kritisch bewerten
- TShark für TCP-Deep-Dive-Abfragen einsetzen

## TCP-Analyse ist Kontextarbeit

Ein einzelnes TCP-Paket reicht selten für eine Diagnose.

TCP ist ein Gespräch.

Du musst deshalb meistens einen Stream betrachten, nicht nur ein Paket.

Wichtige Fragen:

- Wer ist Client?
- Wer ist Server?
- Welcher TCP Stream ist betroffen?
- Ist der Capture einseitig oder sieht er beide Richtungen?
- Wo wurde mitgeschnitten?
- Sind Pakete verloren gegangen oder fehlen sie nur im Capture?
- Tritt das Problem einmalig oder dauerhaft auf?

AHA:

> TCP-Analyse beginnt nicht mit `tcp.analysis.flags`.  
> TCP-Analyse beginnt mit dem richtigen Stream und der richtigen Frage.

## TCP Stream sauber isolieren

Ein guter Start ist:

1. Relevantes Paket finden
2. TCP Stream ermitteln
3. Stream isolieren

Display Filter:

```text
tcp.stream == 0
```

Die Stream-Nummer hängt vom Capture ab.

Du findest sie im TCP-Paketdetailbereich:

```text
Transmission Control Protocol
    Stream index: 0
```

Oder über:

```text
Right Click > Conversation Filter > TCP
```

oder:

```text
Follow > TCP Stream
```

## Warum `tcp.stream` so wichtig ist

Ein Capture enthält oft viele TCP-Verbindungen gleichzeitig.

Ohne Stream-Filter vermischst du schnell:

- DNS over TCP
- HTTPS
- Updates
- Browser-Verbindungen
- Hintergrunddienste
- Docker- oder Systemverkehr

AHA:

> Erst den Stream isolieren, dann bewerten.

## Sequence Number

Die Sequence Number beschreibt die Position im TCP-Datenstrom.

Vereinfacht:

> Dieses Segment beginnt an Position X meines Datenstroms.

Wireshark zeigt standardmäßig relative Sequenznummern.

Das ist gut für die Analyse.

Beispiel:

```text
Seq=1 Len=517
```

Das bedeutet vereinfacht:

- Daten beginnen bei relativer Sequenznummer 1
- das Segment enthält 517 Bytes Nutzdaten
- das nächste erwartete Byte wäre 518

## ACK Number

Die ACK Number bestätigt empfangene Daten.

Vereinfacht:

> Ich habe alles bis vor diese Nummer erhalten und erwarte als nächstes diese Nummer.

Beispiel:

```text
Ack=518
```

Das bedeutet:

> Ich habe Daten bis einschließlich 517 erhalten und erwarte jetzt Byte 518.

!!! note "ACK bestätigt das nächste erwartete Byte"
    Eine ACK Number bestätigt nicht „dieses Paket“, sondern den Datenstrom bis zum nächsten erwarteten Byte.

## Sequence und ACK zusammen lesen

Nehmen wir vereinfacht an:

```text
Client -> Server  Seq=1   Len=100
Server -> Client  Ack=101
```

Das bedeutet:

- Client sendet 100 Bytes ab Position 1
- Server bestätigt den Empfang bis Byte 100
- Server erwartet als nächstes Byte 101

Wenn danach nochmal kommt:

```text
Client -> Server  Seq=1   Len=100
```

ist das wahrscheinlich eine erneute Übertragung desselben Datenbereichs.

## Relative und absolute Sequenznummern

Wireshark verwendet standardmäßig relative Sequenznummern.

Du kannst das ändern unter:

```text
Edit > Preferences > Protocols > TCP
```

Option:

```text
Relative sequence numbers
```

Für den Kurs bleiben relative Nummern aktiviert.

Warum?

- besser lesbar
- leichter zu erklären
- für Analyse meist ausreichend

Absolute Werte sind wichtig, wenn du mit anderen Tools oder Rohdaten vergleichst.

## Len ist wichtig

In der Info-Spalte zeigt Wireshark häufig:

```text
Len=0
```

oder:

```text
Len=1460
```

`Len=0` bedeutet:

- kein TCP-Nutzdatenanteil
- häufig ACK, SYN, FIN oder reine Steuerpakete

`Len>0` bedeutet:

- dieses Segment enthält Nutzdaten

AHA:

> Nicht jedes TCP-Paket transportiert Anwendungsdaten.

## Retransmission

Eine Retransmission ist eine erneute Übertragung von Daten.

Wireshark markiert sie häufig als:

```text
[TCP Retransmission]
```

Display Filter:

```text
tcp.analysis.retransmission
```

Eine Retransmission bedeutet:

> Der Sender überträgt Daten erneut, weil er annimmt, dass sie nicht angekommen oder nicht bestätigt wurden.

Mögliche Ursachen:

- Paketverlust im Netzwerk
- ACK ging verloren
- Capture unvollständig
- Out-of-Order wurde fehlinterpretiert
- sehr hohe Verzögerung
- Paket wurde am Capture-Punkt nicht gesehen

!!! warning "Retransmission ist ein Symptom, keine fertige Ursache"
    Eine Retransmission zeigt, dass TCP erneut sendet.  
    Sie beweist allein noch nicht, wo der Verlust entstanden ist.

## Duplicate ACK

Ein Duplicate ACK ist eine wiederholte Bestätigung desselben nächsten erwarteten Bytes.

Wireshark markiert häufig:

```text
[TCP Dup ACK]
```

Display Filter:

```text
tcp.analysis.duplicate_ack
```

Typisches Muster:

```text
Server -> Client  Seq=1    Len=1460
Server -> Client  Seq=1461 Len=1460
Server -> Client  Seq=4381 Len=1460
Client -> Server  Ack=2921
Client -> Server  Ack=2921
Client -> Server  Ack=2921
```

Der Client sagt mehrfach:

> Ich erwarte weiterhin Byte 2921.

Das kann bedeuten, dass ein Segment fehlt.

## Fast Retransmit

Wenn ein Sender mehrere Duplicate ACKs erhält, kann er schnell erneut senden, ohne auf einen Timeout zu warten.

Wireshark markiert das häufig als:

```text
[TCP Fast Retransmission]
```

Display Filter:

```text
tcp.analysis.fast_retransmission
```

AHA:

> Fast Retransmit ist TCPs schnelle Reaktion auf wahrscheinlich fehlende Daten.

## Out-of-Order

Out-of-Order bedeutet, dass Pakete nicht in der erwarteten Reihenfolge gesehen wurden.

Wireshark markiert häufig:

```text
[TCP Out-Of-Order]
```

Display Filter:

```text
tcp.analysis.out_of_order
```

Mögliche Ursachen:

- echte Umordnung im Netzwerk
- mehrere Wege
- Capture-Punkt sieht Pakete in anderer Reihenfolge
- Timestamp-/Capture-Effekt
- Paketverlust und spätere Nachlieferung

Out-of-Order ist nicht automatisch schlimm.

Entscheidend ist:

- folgen Duplicate ACKs?
- folgt eine Retransmission?
- gibt es sichtbare Anwendungsauswirkungen?
- ist das Capture zuverlässig?

## Previous Segment Not Captured

Wireshark markiert manchmal:

```text
[TCP Previous segment not captured]
```

Display Filter:

```text
tcp.analysis.lost_segment
```

Das bedeutet:

> Wireshark sieht eine Lücke in der Sequenznummernfolge.

Wichtig: Die Meldung heißt bewusst nicht „Paket wurde im Netzwerk verloren“.

Sie sagt:

> Im Capture fehlt dieses Segment.

Mögliche Ursachen:

- Paketverlust im Netzwerk
- Paket wurde vor dem Capture-Punkt verloren
- Capture hat Paket nicht erfasst
- Capture wurde zu spät gestartet
- Capture-System war überlastet
- Offloading oder Capture-Bedingungen verfälschen die Sicht

AHA:

> „Not captured“ ist ehrlicher als „lost“. Erst der Kontext entscheidet, ob es echter Paketverlust war.

## Spurious Retransmission

Wireshark kann markieren:

```text
[TCP Spurious Retransmission]
```

Display Filter:

```text
tcp.analysis.spurious_retransmission
```

Das bedeutet vereinfacht:

> Es wurde erneut gesendet, obwohl Wireshark Hinweise sieht, dass die ursprünglichen Daten bereits angekommen waren.

Mögliche Ursachen:

- ACK kam zu spät
- senderseitiger Timeout war zu aggressiv
- Capture-Punkt sieht zeitliche Reihenfolge ungünstig
- Netzwerkverzögerung
- Analyseheuristik

Auch hier gilt:

> Kontext prüfen, nicht blind urteilen.

## SACK: Selective Acknowledgment

SACK steht für Selective Acknowledgment.

Damit kann ein Empfänger mitteilen:

> Mir fehlt ein bestimmter Bereich, aber spätere Bereiche habe ich bereits erhalten.

Ohne SACK kann TCP nur kumulativ bestätigen:

> Ich habe alles bis X.

Mit SACK kann TCP genauer sagen:

> Mir fehlt X bis Y, aber A bis B habe ich schon.

In Wireshark findest du SACK in TCP Options.

Display Filter können je nach Version und Feld variieren, häufig hilfreich:

```text
tcp.options.sack_perm
```

```text
tcp.options.sack
```

SACK ist besonders relevant bei Paketverlust, weil TCP dadurch effizienter erneut senden kann.

## Window Size

TCP verwendet ein Empfangsfenster.

Das Fenster sagt vereinfacht:

> So viele Bytes kann ich aktuell noch empfangen.

In Wireshark siehst du Felder wie:

```text
Window
Calculated window size
Window size scaling factor
```

Wichtig ist meistens die berechnete Fenstergröße:

```text
Calculated window size
```

## Window Scaling

Ohne Window Scaling wäre das TCP-Fenster stark begrenzt.

Window Scaling wird im TCP Handshake ausgehandelt.

Du findest es in den TCP Options der SYN-Pakete.

AHA:

> Wenn du Window-Probleme analysierst, prüfe den Handshake. Dort wird Window Scaling ausgehandelt.

## Zero Window

Zero Window bedeutet:

> Der Empfänger kann aktuell keine weiteren Daten aufnehmen.

Wireshark markiert häufig:

```text
[TCP ZeroWindow]
```

Display Filter:

```text
tcp.analysis.zero_window
```

Das ist ein wichtiger Hinweis.

Mögliche Ursachen:

- Anwendung liest Daten nicht schnell genug
- Empfänger ist überlastet
- Buffer voll
- Server oder Client kann nicht nachkommen

Zero Window ist eher ein Hinweis auf Empfänger-/Anwendungsseite als auf klassischen Paketverlust.

## Window Update

Wenn wieder Platz im Empfangsfenster ist, folgt ein Window Update.

Display Filter:

```text
tcp.analysis.window_update
```

Das sagt:

> Der Empfänger kann wieder Daten annehmen.

## ACKed unseen segment

Wireshark kann markieren:

```text
[TCP ACKed unseen segment]
```

Das bedeutet:

> Ein ACK bestätigt Daten, die Wireshark im Capture nicht gesehen hat.

Das ist ein starker Hinweis darauf, dass der Capture unvollständig ist oder an einem Punkt erstellt wurde, der nicht alle Pakete sieht.

AHA:

> Nicht jede TCP-Anomalie ist Netzwerkproblem. Manche sind Capture-Problem.

## tcp.analysis.flags

Dieser Filter zeigt viele Wireshark-TCP-Analysehinweise:

```text
tcp.analysis.flags
```

Das ist praktisch für den Überblick.

Aber:

!!! warning "Nicht als Fehlerliste missverstehen"
    `tcp.analysis.flags` ist keine automatische Fehlerdiagnose.  
    Es ist eine Sammlung von Analysehinweisen. Du musst jeden Hinweis im Kontext bewerten.

Sinnvolle Vorgehensweise:

1. `tcp.analysis.flags` anwenden
2. betroffenen Stream isolieren
3. Reihenfolge prüfen
4. Frame-Nummern notieren
5. prüfen, ob Capture vollständig ist
6. Hypothese bilden

## Analyse-Reihenfolge für TCP-Probleme

Wenn eine TCP-Verbindung auffällig ist:

1. passenden Stream finden
2. Handshake prüfen
3. Verbindungsende prüfen
4. Datenrichtung klären
5. Retransmissions suchen
6. Duplicate ACKs suchen
7. Out-of-Order prüfen
8. Zero Window prüfen
9. RTT und Zeitabstände betrachten
10. Capture-Punkt bewerten
11. erst dann Ursache formulieren

## Praktische Display Filter

Bestimmter Stream:

```text
tcp.stream == 0
```

TCP-Analysehinweise:

```text
tcp.analysis.flags
```

Retransmissions:

```text
tcp.analysis.retransmission
```

Fast Retransmissions:

```text
tcp.analysis.fast_retransmission
```

Duplicate ACKs:

```text
tcp.analysis.duplicate_ack
```

Out-of-Order:

```text
tcp.analysis.out_of_order
```

Previous Segment Not Captured:

```text
tcp.analysis.lost_segment
```

Spurious Retransmission:

```text
tcp.analysis.spurious_retransmission
```

Zero Window:

```text
tcp.analysis.zero_window
```

Window Update:

```text
tcp.analysis.window_update
```

Resets:

```text
tcp.flags.reset == 1
```

FIN:

```text
tcp.flags.fin == 1
```

## TShark-Beispiele

TCP-Analysehinweise zählen:

```bash
tshark -r capture.pcapng -Y "tcp.analysis.flags" | wc -l
```

Retransmissions ausgeben:

```bash
tshark -r capture.pcapng \
  -Y "tcp.analysis.retransmission" \
  -T fields \
  -e frame.number \
  -e frame.time_relative \
  -e tcp.stream \
  -e ip.src \
  -e tcp.srcport \
  -e ip.dst \
  -e tcp.dstport
```

Duplicate ACKs ausgeben:

```bash
tshark -r capture.pcapng \
  -Y "tcp.analysis.duplicate_ack" \
  -T fields \
  -e frame.number \
  -e frame.time_relative \
  -e tcp.stream \
  -e ip.src \
  -e ip.dst \
  -e tcp.ack
```

TCP Streams mit Analysehinweisen anzeigen:

```bash
tshark -r capture.pcapng \
  -Y "tcp.analysis.flags" \
  -T fields \
  -e tcp.stream | sort -n | uniq -c
```

Zero Window finden:

```bash
tshark -r capture.pcapng \
  -Y "tcp.analysis.zero_window" \
  -T fields \
  -e frame.number \
  -e frame.time_relative \
  -e tcp.stream \
  -e ip.src \
  -e ip.dst
```

## Mini-Aufgabe: TCP Stream untersuchen

Nutze einen Capture mit HTTP oder HTTPS.

1. Öffne den Capture in Wireshark.
2. Suche eine TCP-Verbindung.
3. Ermittle die Stream-Nummer.
4. Filtere auf diesen Stream:

```text
tcp.stream == <nummer>
```

5. Prüfe:

- Gibt es einen vollständigen 3-Way Handshake?
- Wer ist Client?
- Wer ist Server?
- Welche Richtung sendet die meisten Daten?
- Gibt es FIN oder RST?
- Gibt es `tcp.analysis.flags`?
- Gibt es Retransmissions?
- Gibt es Duplicate ACKs?
- Gibt es Zero Window?

## Mini-Aufgabe: Analysehinweise bewerten

Wende auf einen Capture an:

```text
tcp.analysis.flags
```

Beantworte:

1. Welche Arten von Hinweisen gibt es?
2. Welche Streams sind betroffen?
3. Sind die Hinweise vereinzelt oder gehäuft?
4. Gibt es eine erkennbare Auswirkung auf die Verbindung?
5. Könnte der Capture unvollständig sein?
6. Welche Frame-Nummern würdest du in einem Bericht nennen?

## Analysebericht: TCP Deep Dive

```text
Symptom:
<kurze Beschreibung>

Capture-Punkt:
<Client / Server / Gateway / unbekannt>

Betroffener Stream:
tcp.stream == <nummer>

Endpunkte:
Client: <ip>:<port>
Server: <ip>:<port>

Handshake:
vollständig / unvollständig / nicht im Capture enthalten

Auffälligkeiten:
- Frame <nummer>: <Beobachtung>
- Frame <nummer>: <Beobachtung>
- Frame <nummer>: <Beobachtung>

Bewertung:
<fachliche Einordnung>

Alternative Erklärungen:
- Capture unvollständig?
- falscher Capture-Punkt?
- asymmetrisches Routing?
- Offloading?
- Anwendung liest zu langsam?
- echter Paketverlust?

Verwendete Filter:
tcp.stream == <nummer>
tcp.analysis.flags
...
```

## Typische Fehlinterpretationen

| Beobachtung | Falscher Schluss | Bessere Bewertung |
|---|---|---|
| Retransmission | Netzwerk ist schuld | Ursache und Capture-Punkt prüfen |
| Duplicate ACK | Paketverlust bewiesen | starker Hinweis, aber Kontext prüfen |
| Previous segment not captured | Paket im Netzwerk verloren | im Capture fehlt ein Segment |
| Zero Window | Netzwerk langsam | Empfänger kann gerade nicht aufnehmen |
| Out-of-Order | Fehler | kann normal oder Capture-bedingt sein |
| tcp.analysis.flags | Fehlerliste | Analysehinweise, keine Diagnose |
| RST | Netzwerkproblem | Verbindung wurde hart beendet, Ursache offen |

## WCA-Bezug

Dieser Abschnitt übt WCA-nahe Fähigkeiten:

- TCP Streams gezielt untersuchen
- TCP-Sequenz- und ACK-Verhalten verstehen
- Wireshark-TCP-Analysehinweise bewerten
- Retransmissions, Duplicate ACKs und Resets erkennen
- Capture-Vollständigkeit hinterfragen
- Display Filter und TShark für TCP-Analyse nutzen
- Beobachtungen mit Frame-Nummern dokumentieren

## Merksatz

> TCP erzählt eine Geschichte.  
> Lies nicht nur einzelne Pakete. Lies den Stream, die Reihenfolge und die Bestätigungen.
