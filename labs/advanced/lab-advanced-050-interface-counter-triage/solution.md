# Musterlösung

Es gibt nicht die eine perfekte Lösung.

Wichtig ist die saubere Einordnung.

## Beispielhafte Counter-Klassifikation

| Interface | Counter | Erste Einordnung | Wireshark hilfreich? | Nächster Schritt |
|---|---|---|---|---|
| sw-core-01 uplink-01 | OutDiscards | möglicher Queue-/Congestion-/QoS-Drop auf Uplink | ja, indirekt | Last, Queue-Counter, Top Talker, ggf. SPAN/TAP |
| sw-access-12 port-24 | InErrors CRC/FCS | wahrscheinlich physikalisch oder Link-Layer | eher nein als erster Schritt | Kabel, Patchfeld, AP-Port, SFP/PHY, Counter am Port |
| sw-access-07 port-10 | OutDiscards | Switch verwirft beim Senden zum Server | ja, wenn Benutzerbeschwerden zeitlich passen | Queue/Buffer, Serverport, Host-Capture, Gegen-Capture |
| sw-dist-02 trunk-03 | InErrors Giants | MTU/Jumbo/VLAN/Fehlkonfiguration möglich | eingeschränkt | MTU, Trunk-Konfig, Gegenstelle, VLANs, Geräte-Counter |

## Wireshark-Eignung

### CRC/FCS

Gute Bewertung:

```text
Wireshark ist hier nicht das Primärwerkzeug. Normale Captures sehen CRC-/FCS-fehlerhafte Frames oft nicht, weil diese vorher verworfen werden.
```

### OutDiscards auf Uplink

Gute Bewertung:

```text
Wireshark kann helfen, die Auswirkungen zu sehen, zum Beispiel Retransmissions oder auffällige Top Talker. Der eigentliche Queue-Drop muss über Switch-/Router-Counter und Zeitkorrelation geprüft werden.
```

### OutDiscards zum Server

Gute Bewertung:

```text
Ein Host-Capture auf dem Server und ein Capture am Switch/SPAN können helfen, Sichtweisen zu vergleichen. Wenn der Server Pakete nicht sieht, die an anderer Stelle sichtbar sind, kann der Pfad weiter eingegrenzt werden.
```

### Giants auf Trunk

Gute Bewertung:

```text
Wireshark kann bei MTU- oder Fragmentierungshinweisen helfen. Zuerst sollten aber MTU, Trunk-Konfiguration, VLANs und Gegenstellen-Counter geprüft werden.
```

## Gute Fragen an das Monitoring

- Wann genau steigen die Counter?
- Wie stark steigen sie?
- Ist es ein absoluter Counter oder eine Rate?
- Ist die Interface-Auslastung gleichzeitig hoch?
- Sind beide Richtungen betroffen?
- Sind mehrere Interfaces betroffen?
- Betrifft es ein VLAN oder viele?
- Gibt es zeitgleich Alarme auf Nachbarports?
- Gibt es zeitgleich Applikationsbeschwerden?
- Gibt es Muster nach Uhrzeit?
- Gibt es Top Talker?
- Ist der Counter seit Wochen alt oder aktuell aktiv?

## Gute Geräteprüfungen

- Interface-Details prüfen
- Error-Unterzähler prüfen
- Discard-/Queue-Unterzähler prüfen
- QoS-/Policy-Counter prüfen
- SFP-/Optik-Werte prüfen
- Speed/Duplex/Autonegotiation prüfen
- MTU prüfen
- Trunk-/VLAN-Konfiguration prüfen
- STP-/Loop-Hinweise prüfen
- Logs zum Zeitfenster prüfen
- Port-Channel/LACP prüfen
- Gegenstelle prüfen

## Vorsichtige Formulierungen

| Original | Besser |
|---|---|
| Der Switch ist kaputt. | Auf dem Interface steigen Counter. Der konkrete Fehlerort ist noch nicht belegt. |
| Das Netzwerk verliert Pakete. | Im Capture sind Symptome sichtbar, die zu Paketverlust oder fehlenden Segmenten passen. |
| Die Firewall blockt. | Aus Sicht des Capture-Punkts ist keine Antwort sichtbar beziehungsweise ein Reset sichtbar. |
| Wireshark zeigt nichts, also gibt es kein Problem. | Der Capture zeigt keine Auffälligkeit; bestimmte Layer-1/2-Fehler sind damit nicht ausgeschlossen. |
| Der Server ist schuld. | Die sichtbare Wartezeit oder Richtung muss mit Hostdaten und Gegen-Capture geprüft werden. |

## Beispiel-Kurzbericht

```text
Ausgangslage:
Das Monitoring meldet auf mehreren Switch-Interfaces steigende Errors und Discards.

Einordnung:
CRC/FCS-Errors auf dem Access-Port zum AP sprechen eher für eine physikalische oder Link-Layer-Prüfung. OutDiscards auf Uplink und Serverport sprechen eher für Queue, Buffer, QoS oder Lastspitzen und können Auswirkungen im Datenverkehr erzeugen.

Wireshark:
Wireshark ist bei CRC/FCS nicht das erste Werkzeug. Bei OutDiscards kann Wireshark helfen, Retransmissions, Duplicate ACKs, Top Talker oder betroffene Flows sichtbar zu machen. Der Drop selbst ist damit aber nicht automatisch bewiesen.

Nächste Schritte:
Zeitfenster definieren, Counter direkt am Gerät prüfen, Queue-/QoS-Counter auswerten, Topologie und betroffene VLANs klären, bei Bedarf gezielte Captures an Host, SPAN oder TAP erstellen.

Bewertung:
Das Monitoring belegt steigende Counter. Die Ursache ist noch nicht belegt.

Einschränkungen:
Ohne Geräte-Counter, Topologie und passenden Capture-Punkt ist keine belastbare Ursachenzuordnung möglich.
```

## Merksatz

> Die beste Wireshark-Analyse beginnt manchmal damit, Wireshark noch nicht zu starten.
