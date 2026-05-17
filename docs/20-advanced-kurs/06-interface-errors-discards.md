# Interface Errors, Discards und Monitoring-Triage

Monitoring-Systeme zeigen häufig Interface-Counter wie Errors, Discards oder Drops.

Das ist wertvoll, aber es ist noch keine fertige Ursache.

Ein Monitoring-System kann typischerweise sagen:

```text
Auf Interface X steigt Counter Y im Zeitraum Z.
```

Es sagt meistens nicht zuverlässig:

```text
Warum genau passiert das?
```

Dieser Abschnitt erklärt, wie du Interface-Counter einordnest, wann Wireshark helfen kann und wann andere Werkzeuge wichtiger sind.

## Kernidee

> Monitoring zeigt das Symptom.  
> Switch- oder Router-Counter klassifizieren es genauer.  
> Wireshark zeigt Traffic-Muster und Auswirkungen.  
> Die Ursache entsteht erst durch Korrelation.

## Was Wireshark leisten kann

Wireshark kann helfen, wenn sich Interface-Probleme im Datenverkehr zeigen.

Typische sichtbare Hinweise:

- TCP Retransmissions
- Duplicate ACKs
- Fast Retransmit
- Out-of-Order
- Previous Segment Not Captured
- Zero Window
- ungewöhnlich viele Broadcasts
- auffälliger Multicast
- DNS- oder HTTP-Zeitprobleme
- RST statt Timeout
- MTU- oder Fragmentierungsprobleme

Wireshark kann außerdem helfen, eine konkrete Frage zu beantworten:

```text
Gibt es im Zeitraum der Discards sichtbare TCP-Symptome?
```

```text
Welche Conversation erzeugt den größten Datenanteil?
```

```text
Ist der Effekt auf einen Flow, ein VLAN, einen Server oder viele Ziele verteilt?
```

```text
Passt das Muster zu Paketverlust, Überlast, Anwendungslatenz oder Empfängerproblemen?
```

## Was Wireshark oft nicht leisten kann

Wireshark ist kein magisches Interface-Counter-Erklärwerkzeug.

Bei bestimmten Fehlerarten ist Wireshark sogar bewusst das falsche Primärwerkzeug.

Beispiele:

- CRC Errors
- FCS Errors
- Symbol Errors
- Alignment Errors
- defekte Kabel
- defekte SFPs
- verschmutzte Glasfaser
- Port-Hardwarefehler
- viele ASIC-/Queue-Drops ohne passenden Capture-Punkt
- Microbursts im Sub-Millisekunden-Bereich

Warum?

Fehlerhafte Ethernet-Frames werden häufig schon vom Switch, vom PHY, von der Netzwerkkarte oder vom Treiber verworfen, bevor Wireshark sie sieht.

Das bedeutet:

```text
Der Switch zählt CRC Errors.
Wireshark zeigt möglicherweise nichts Auffälliges.
```

Das ist kein Widerspruch.

Es ist eine Grenze des Capture-Punkts.

## Errors vs. Discards

| Begriff | Vereinfachte Bedeutung | Typische Richtung |
|---|---|---|
| Error | Frame war fehlerhaft oder konnte technisch nicht sauber verarbeitet werden | oft physikalisch oder Layer 1/2 |
| Discard | Frame/Paket wurde verworfen, obwohl es nicht zwingend kaputt war | oft Queue, Policy, Buffer, QoS |
| Drop | generischer Begriff für Verwerfen | herstellerabhängig |
| CRC/FCS | Prüfsummenfehler auf Ethernet-Ebene | Kabel, SFP, Optik, Port |
| OutDiscard | Gerät wollte senden, hat aber verworfen | Queue, Congestion, QoS, Buffer |
| InDiscard | Gerät hat beim Empfang verworfen | Policy, Ressourcen, VLAN/Security, Buffer |

Die exakte Bedeutung hängt vom Hersteller und vom Counter ab.

Deshalb ist der zweite Schritt nach dem Monitoring fast immer:

```text
Geräte-Counter direkt am Switch oder Router prüfen.
```

## Warum Richtung wichtig ist

Ein Counter ohne Richtung ist gefährlich.

Beispiel:

```text
OutDiscards auf einem Access-Port zum Server
```

Das kann bedeuten:

```text
Der Switch wollte Pakete zum Server senden, musste aber verwerfen.
```

Beispiel:

```text
InErrors auf demselben Port
```

Das kann bedeuten:

```text
Der Switch empfängt fehlerhafte Frames aus Richtung Server, Patchkabel, SFP oder Endgerät.
```

Beides sind völlig unterschiedliche Troubleshooting-Pfade.

## Reale Vorgehensweise

### 1. Monitoring-Zeitfenster sichern

Zuerst brauchst du:

- Gerät
- Interface
- Counter
- Richtung
- Zeitpunkt
- Dauer
- Rate oder absoluter Zuwachs
- betroffene Systeme oder VLANs
- Last auf dem Interface

Gute Frage:

```text
Steigt der Counter dauerhaft oder nur während Lastspitzen?
```

### 2. Counter direkt am Gerät prüfen

Typische Prüfungen:

```text
show interface <port>
show interfaces counters errors
show interfaces counters discards
show logging
show spanning-tree interface <port>
show interface transceiver detail
show queue / qos counters
show policy-map interface
```

Die Befehle sind herstellerabhängig.

Gesucht wird nach:

- CRC
- FCS
- input errors
- output errors
- queue drops
- buffer drops
- pause frames
- storm control
- giants
- runts
- MTU drops
- QoS drops
- drops per queue
- SFP-/Optik-Werten

### 3. Counterstand oder Messfenster definieren

Alte Counterstände sind gefährlich.

Besser:

```text
Counterstand notieren
kurzes Messfenster definieren
Problem reproduzieren oder warten
Counterstand erneut prüfen
```

Wenn möglich, Counter nicht blind löschen, sondern dokumentieren.

### 4. Topologie verstehen

Vor einem Capture klären:

- Access-Port oder Uplink?
- Trunk oder einzelnes VLAN?
- Server, Access Point, Firewall, Router oder Storage?
- LACP beteiligt?
- QoS aktiv?
- Port-Security aktiv?
- Storm-Control aktiv?
- welche VLANs?
- welche Gegenstelle?
- welche Geschwindigkeit?
- welche Duplex-/Autonegotiation?
- Kupfer, Glasfaser oder DAC?

Ohne Topologie ist jede Bewertung wackelig.

### 5. Capture-Punkt wählen

Mögliche Capture-Punkte:

| Capture-Punkt | Vorteil | Grenze |
|---|---|---|
| Host-Capture | einfach, nah an Anwendung | sieht nicht alles auf dem Switch-Port |
| SPAN/Mirror-Port | praktisch, zentral | kann Pakete verlieren oder Timing verfälschen |
| TAP | sehr belastbar | nicht immer verfügbar |
| beidseitiger Capture | sehr aussagekräftig | organisatorisch aufwendiger |
| Capture vor/nach Segment | gut zum Eingrenzen | braucht Zugang zur Strecke |

SPAN ist gut für viele Analysen, aber nicht perfekt.

Ein SPAN-Port kann selbst überlasten und Fehlerframes oft nicht liefern.

### 6. Wireshark gezielt einsetzen

Nicht einfach „mal capturen“.

Besser mit konkreter Frage:

```text
Sehe ich Retransmissions im betroffenen Zeitraum?
```

```text
Gibt es viele Duplicate ACKs?
```

```text
Ist ein einzelner Flow betroffen oder viele?
```

```text
Gibt es Broadcast-/Multicast-Last?
```

```text
Gibt es RST statt Timeout?
```

```text
Gibt es Hinweise auf MTU-Probleme?
```

Nützliche Filter:

```text
tcp.analysis.flags
tcp.analysis.retransmission
tcp.analysis.fast_retransmission
tcp.analysis.duplicate_ack
tcp.analysis.lost_segment
tcp.analysis.out_of_order
tcp.analysis.zero_window
tcp.flags.reset == 1
icmp
icmpv6
arp
eth.dst == ff:ff:ff:ff:ff:ff
stp
lldp
```

### 7. Korrelation herstellen

Die stärkste Aussage entsteht durch Korrelation:

```text
Im Monitoring steigen auf Interface X im Zeitraum 10:14 bis 10:18 OutDiscards.
Im selben Zeitraum zeigt der Capture im TCP Stream zwischen Client A und Server B Retransmissions und Duplicate ACKs.
Das Muster passt zu fehlenden Segmenten oder Paketverlust aus Sicht dieses Capture-Punkts.
```

Das ist stark.

Aber noch nicht:

```text
Der Switch ist schuld.
```

Besser:

```text
Der Drop-Ort ist noch nicht eindeutig belegt. Dafür wären weitere Counter, Gegen-Captures oder Telemetrie nötig.
```

## Typische Diagnosepfade

### CRC/FCS Errors

Primär prüfen:

- Kabel
- Patchfeld
- SFP
- Glasfaser
- Optikwerte
- Port
- Gegenstelle
- Autonegotiation
- Speed/Duplex
- Gerätelog

Wireshark-Rolle:

```text
meist gering
```

Gute Aussage:

```text
CRC/FCS-Fehler sind am Switch-Counter sichtbar. Ein normaler Wireshark-Capture muss diese Fehler nicht zeigen.
```

### OutDiscards / Queue Drops

Primär prüfen:

- Queue-Counter
- QoS
- Lastspitzen
- Microbursts
- Oversubscription
- Egress-Port-Geschwindigkeit
- Flow-Verteilung
- Uplink-Kapazität

Wireshark-Rolle:

```text
indirekt hilfreich
```

Mögliche sichtbare Symptome:

- Retransmissions
- Duplicate ACKs
- Durchsatzschwankungen
- auffällige Top Talker
- viele parallele Flows

### Broadcast oder Multicast Last

Primär prüfen:

- Broadcast-Anteil
- Multicast-Gruppen
- IGMP Snooping
- STP
- Loop-Verdacht
- Storm-Control

Wireshark-Rolle:

```text
sehr hilfreich
```

Nützliche Filter:

```text
eth.dst == ff:ff:ff:ff:ff:ff
arp
stp
igmp
```

### MTU / Fragmentierung

Primär prüfen:

- MTU auf Pfad
- Jumbo Frames
- MSS
- ICMP Fragmentation Needed
- PMTUD
- Firewalls, die ICMP blocken

Wireshark-Rolle:

```text
sehr hilfreich
```

Nützliche Filter:

```text
icmp
icmpv6
tcp.analysis.retransmission
```

## Gute Berichtssprache

| Zu stark | Besser |
|---|---|
| Der Switch droppt Pakete. | Auf Interface X steigen OutDiscards; im Capture sind passende TCP-Symptome sichtbar. |
| Das Kabel ist kaputt. | Die Counter zeigen CRC/FCS-Fehler; physikalische Prüfung ist der nächste Schritt. |
| Wireshark zeigt nichts, also gibt es kein Problem. | Der Capture zeigt keine Auffälligkeit; bestimmte Layer-1/2-Fehler sind damit nicht ausgeschlossen. |
| Das ist ein Netzwerkproblem. | Die sichtbare Wartezeit oder die Retransmissions liegen im untersuchten Zeitraum; weitere Eingrenzung ist nötig. |
| Die Firewall blockt. | Aus Sicht des Capture-Punkts ist keine Antwort sichtbar beziehungsweise ein Reset sichtbar. |

## Merksatz

> Interface-Counter sind Symptome.  
> Wireshark zeigt Auswirkungen.  
> Die Ursache entsteht durch Richtung, Zeitfenster, Topologie und Gegenbelege.
