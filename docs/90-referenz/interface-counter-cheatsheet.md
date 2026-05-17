# Interface-Counter-Cheatsheet

Diese Seite ist eine kompakte Referenz für Interface Errors, Discards und Wireshark-Einordnung.

## Grundregel

> Ein Interface-Counter ist ein Symptom, keine vollständige Ursache.

Erst die Kombination aus Counter, Richtung, Zeitfenster, Topologie, Geräteinformationen und Capture macht eine belastbare Analyse möglich.

## Schnellübersicht

| Counter / Hinweis | Erste Einordnung | Wireshark-Rolle |
|---|---|---|
| CRC Errors | physikalisch, Kabel, SFP, Optik, Port | meist gering |
| FCS Errors | fehlerhafte Ethernet-Frames | meist gering |
| Alignment Errors | Layer-1/2-Problem | gering |
| Symbol Errors | PHY/SFP/Optik | gering |
| Runts | zu kleine Frames, Kollision/Fehler/Hardware | eingeschränkt |
| Giants | MTU/Jumbo/Fehlkonfiguration möglich | eingeschränkt bis hilfreich |
| Input Errors | Sammelcounter, Unterzähler prüfen | abhängig |
| Output Errors | Sammelcounter, Unterzähler prüfen | abhängig |
| InDiscards | Empfang verworfen, Policy/Ressourcen/VLAN/Security möglich | indirekt |
| OutDiscards | Senden verworfen, Queue/Buffer/QoS/Congestion möglich | indirekt hilfreich |
| Queue Drops | Queue voll, Microburst, QoS, Oversubscription | indirekt hilfreich |
| Pause Frames | Flow Control | manchmal sichtbar |
| Broadcast Storm | L2-Problem, Loop, Fehlverhalten | sehr hilfreich |
| Multicast Flooding | IGMP/Snooping/Applikation | hilfreich |
| MTU Drops | MTU/Jumbo/MSS/PMTUD | sehr hilfreich |

## Errors

Errors bedeuten häufig:

```text
Frames sind fehlerhaft oder konnten technisch nicht korrekt verarbeitet werden.
```

Typische Prüfungen:

- Kabel
- Patchfeld
- SFP
- Glasfaser
- Optikwerte
- Port
- Gegenstelle
- Speed/Duplex
- Autonegotiation
- Gerätelog

Wireshark ist bei CRC/FCS oft nicht ausreichend, weil fehlerhafte Frames vor dem Capture verworfen werden können.

## Discards

Discards bedeuten häufig:

```text
Frames oder Pakete wurden verworfen, obwohl sie nicht zwingend defekt waren.
```

Typische Ursachen:

- Egress Queue voll
- Buffer Drops
- QoS Drops
- Microbursts
- Oversubscription
- Port-Geschwindigkeit zu gering
- Policy/ACL
- VLAN-/Security-Regeln
- Ressourcenmangel

Wireshark kann Auswirkungen zeigen:

- Retransmissions
- Duplicate ACKs
- Fast Retransmit
- Out-of-Order
- Durchsatzschwankungen
- Top Talker
- auffällige Flows

## Richtung

| Richtung | Frage |
|---|---|
| InErrors | Was empfängt das Gerät fehlerhaft? |
| OutErrors | Was kann das Gerät nicht sauber senden? |
| InDiscards | Was verwirft das Gerät beim Empfang? |
| OutDiscards | Was verwirft das Gerät beim Senden? |

Richtung immer mit Topologie verbinden.

## Capture-Punkte

| Capture-Punkt | Gut für | Grenze |
|---|---|---|
| Host | Anwendungssicht, TCP, HTTP/TLS | sieht nicht zwingend Switch-Drops |
| SPAN/Mirror | zentrale Sicht, mehrere Flows | kann selbst droppen oder Timing verfälschen |
| TAP | belastbare Leitungssicht | braucht Hardware/Zugang |
| beidseitig | Eingrenzung des Fehlerorts | organisatorisch aufwendiger |
| Uplink | viele Flows/VLANs | große Datenmenge, schwierige Filterung |

## Nützliche Wireshark-Filter

TCP-Symptome:

```text
tcp.analysis.flags
tcp.analysis.retransmission
tcp.analysis.fast_retransmission
tcp.analysis.duplicate_ack
tcp.analysis.lost_segment
tcp.analysis.out_of_order
tcp.analysis.zero_window
```

Reset/Timeout-Unterscheidung:

```text
tcp.flags.reset == 1
tcp.flags.syn == 1 and tcp.flags.ack == 0
```

Broadcast:

```text
eth.dst == ff:ff:ff:ff:ff:ff
arp
```

Multicast:

```text
eth.dst[0] & 1
igmp
```

Layer-2-Hinweise:

```text
stp
lldp
```

MTU/ICMP:

```text
icmp
icmpv6
```

## TShark-Beispiele

TCP Analysehinweise:

```bash
tshark -r capture.pcapng \
  -Y "tcp.analysis.flags" \
  -T fields \
  -e frame.number \
  -e frame.time_relative \
  -e tcp.stream \
  -e ip.src \
  -e tcp.srcport \
  -e ip.dst \
  -e tcp.dstport \
  -e _ws.col.Info
```

Top TCP Conversations:

```bash
tshark -r capture.pcapng -q -z conv,tcp
```

Broadcast-Anteil grob zählen:

```bash
tshark -r capture.pcapng -Y "eth.dst == ff:ff:ff:ff:ff:ff" | wc -l
```

Retransmissions zählen:

```bash
tshark -r capture.pcapng \
  -Y "tcp.analysis.retransmission or tcp.analysis.fast_retransmission" | wc -l
```

## Gute Fragen im Incident

- Welcher Counter steigt?
- In welche Richtung?
- Auf welchem Interface?
- In welchem Zeitfenster?
- Wie stark steigt er?
- Ist die Last zeitgleich hoch?
- Ist es Access-Port, Trunk oder Uplink?
- Welche VLANs oder Systeme hängen daran?
- Sind Nachbarinterfaces betroffen?
- Gibt es Geräte-Logs im Zeitraum?
- Gibt es Queue-/QoS-Unterzähler?
- Gibt es SFP-/Optik-Auffälligkeiten?
- Gibt es passende PCAP-Symptome?
- Gibt es einen Gegen-Capture?

## Berichtssprache

| Zu stark | Besser |
|---|---|
| Der Switch ist schuld. | Auf dem Interface steigen Counter; der Fehlerort ist noch nicht belegt. |
| Wireshark zeigt nichts, also ist alles gut. | Der Capture zeigt keine Auffälligkeit; Layer-1/2-Fehler sind damit nicht ausgeschlossen. |
| Das Kabel ist kaputt. | CRC/FCS-Fehler sprechen für eine physikalische Prüfung. |
| Das Netzwerk verliert Pakete. | Im Capture sind Retransmissions sichtbar, die zu Paketverlust oder fehlenden Segmenten passen. |
| Die Firewall blockt. | Aus Sicht des Capture-Punkts ist keine Antwort sichtbar beziehungsweise ein Reset sichtbar. |

## Merksatz

> Wireshark sieht Pakete.  
> Interface-Counter sehen Geräteereignisse.  
> Gute Analyse verbindet beides, ohne eines davon zu überschätzen.
