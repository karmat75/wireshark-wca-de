# Ethernet, ARP und VLAN

Ethernet, ARP und VLAN gehören zu den Grundlagen, die man in Wireshark sehr früh sieht.

Sie wirken oft unspektakulär, sind aber wichtig: Ohne Layer 2 gibt es keine sinnvolle Kommunikation im lokalen Netzwerk.

In diesem Abschnitt geht es darum, die sichtbaren Layer-2-Informationen in Wireshark zu verstehen.

## Ziel

Nach diesem Abschnitt solltest du können:

- Ethernet-Frames in Wireshark erkennen
- Quell- und Ziel-MAC-Adressen einordnen
- Broadcast- und Multicast-Verkehr erkennen
- ARP Request und ARP Reply unterscheiden
- VLAN-Tags erkennen, wenn sie im Capture sichtbar sind
- einfache Layer-2-Filter anwenden
- typische Fehlinterpretationen vermeiden

## Ethernet im Capture

Ein Ethernet-Frame ist die lokale Transporthülle auf Layer 2.

In Wireshark findest du Ethernet meistens im mittleren Paketdetailbereich:

```text
Ethernet II
```

Typische Felder:

| Feld | Bedeutung |
|---|---|
| Destination | Ziel-MAC-Adresse |
| Source | Quell-MAC-Adresse |
| Type | nächstes Protokoll, zum Beispiel IPv4, IPv6 oder ARP |

Beispiel:

```text
Ethernet II
    Destination: 52:54:00:12:34:56
    Source: 08:00:27:aa:bb:cc
    Type: IPv4 (0x0800)
```

Wichtig:

> Ethernet-Adressen gelten nur im lokalen Layer-2-Segment.  
> Über Router hinweg ändern sich die MAC-Adressen.

## MAC-Adressen verstehen

Eine MAC-Adresse sieht zum Beispiel so aus:

```text
08:00:27:aa:bb:cc
```

Sie besteht aus 48 Bit und wird meistens hexadezimal dargestellt.

Die ersten Bytes können auf den Hersteller oder die Organisation hinweisen. Wireshark kann dafür Namen anzeigen, wenn die Namensauflösung aktiv ist.

!!! note "Namensauflösung kann helfen, aber auch ablenken"
    Wenn Wireshark statt `08:00:27:aa:bb:cc` einen Hersteller oder Namen anzeigt, kann das nützlich sein.  
    Für saubere Analysen solltest du aber verstehen, dass im Paket die MAC-Adresse steht, nicht der angezeigte Name.

## Broadcast

Ein Broadcast geht an alle Geräte im lokalen Layer-2-Segment.

Die Broadcast-MAC-Adresse lautet:

```text
ff:ff:ff:ff:ff:ff
```

Typische Broadcast-Beispiele:

- ARP Request
- DHCP Discover
- manche lokale Erkennungsprotokolle

Display Filter:

```text
eth.dst == ff:ff:ff:ff:ff:ff
```

oder kürzer:

```text
eth.addr == ff:ff:ff:ff:ff:ff
```

## Multicast

Multicast richtet sich an eine Gruppe von Empfängern.

Du siehst Multicast oft bei:

- IPv6 Neighbor Discovery
- mDNS
- LLMNR
- anderen lokalen Discovery-Protokollen

Beispiele für Multicast-nahe Adressen:

```text
01:00:5e:...
33:33:...
```

Für den Einstieg reicht:

> Broadcast ist an alle.  
> Multicast ist an eine Gruppe.

## EtherType

Das Ethernet-Feld `Type` sagt, welches Protokoll im Ethernet-Frame folgt.

Häufige Werte:

| EtherType | Bedeutung |
|---|---|
| `0x0800` | IPv4 |
| `0x0806` | ARP |
| `0x86dd` | IPv6 |
| `0x8100` | VLAN Tagging / IEEE 802.1Q |

Display Filter:

```text
eth.type == 0x0800
```

```text
eth.type == 0x0806
```

In Wireshark ist meistens der Protokollfilter einfacher:

```text
ip
```

```text
arp
```

```text
ipv6
```

## ARP: Wofür ist das da?

ARP bedeutet Address Resolution Protocol.

ARP beantwortet im IPv4-Netz eine einfache Frage:

> Welche MAC-Adresse gehört zu dieser IPv4-Adresse?

Beispiel:

Ein Client will mit seinem Gateway sprechen.

Der Client kennt die IP-Adresse des Gateways:

```text
192.168.1.1
```

Aber für die lokale Ethernet-Kommunikation braucht er die MAC-Adresse.

Also fragt er per ARP:

```text
Who has 192.168.1.1? Tell 192.168.1.50
```

Das Gerät mit `192.168.1.1` antwortet:

```text
192.168.1.1 is at 52:54:00:12:34:56
```

## ARP Request und ARP Reply

ARP Request:

- meistens Broadcast
- fragt nach einer MAC-Adresse
- Ziel-MAC ist oft `ff:ff:ff:ff:ff:ff`

ARP Reply:

- meistens Unicast
- liefert die passende MAC-Adresse
- geht zurück an den Fragesteller

Display Filter:

```text
arp
```

Nur ARP Requests:

```text
arp.opcode == 1
```

Nur ARP Replies:

```text
arp.opcode == 2
```

## ARP in Wireshark lesen

Typische Felder:

| Feld | Bedeutung |
|---|---|
| Sender MAC address | MAC-Adresse des Absenders |
| Sender IP address | IPv4-Adresse des Absenders |
| Target MAC address | gesuchte oder angesprochene MAC-Adresse |
| Target IP address | gesuchte oder angesprochene IPv4-Adresse |

Nützliche Filter:

```text
arp.src.proto_ipv4 == 192.168.1.50
```

```text
arp.dst.proto_ipv4 == 192.168.1.1
```

```text
arp.src.hw_mac == 08:00:27:aa:bb:cc
```

## ARP-Cache prüfen

Auf dem Linux-System kannst du den Neighbor-Cache anzeigen:

```bash
ip neigh
```

Beispiel:

```text
192.168.1.1 dev wlp2s0 lladdr 52:54:00:12:34:56 REACHABLE
```

Das ist kein Wireshark-Befehl, hilft aber beim Abgleich.

## ARP und IPv6

ARP gehört zu IPv4.

IPv6 verwendet dafür nicht ARP, sondern Neighbor Discovery.

Wenn du also in einem reinen IPv6-Szenario nach ARP suchst, wirst du nichts Sinnvolles finden.

Das IPv6-Gegenstück behandeln wir später im Abschnitt zu IPv6 und ICMPv6.

## VLANs im Capture

VLANs trennen Layer-2-Netze logisch voneinander.

In Ethernet-Frames kann ein VLAN-Tag stehen.

In Wireshark sieht das zum Beispiel so aus:

```text
802.1Q Virtual LAN
    Priority
    DEI
    ID
```

Der wichtige Wert ist meistens:

```text
VLAN ID
```

Display Filter:

```text
vlan
```

```text
vlan.id == 10
```

## Warum sehe ich keine VLAN-Tags?

Das ist ein wichtiger Praxispunkt.

Nur weil ein Netzwerk mit VLANs arbeitet, heißt das nicht, dass du im Capture VLAN-Tags siehst.

Gründe:

- du schneidest auf einem Access-Port mit untagged Traffic mit
- die Netzwerkkarte oder der Treiber entfernt VLAN-Tags
- das Betriebssystem zeigt die Tags nicht an
- du schneidest an der falschen Stelle mit
- der Switch-Port liefert keine getaggten Frames
- du siehst nur Traffic innerhalb eines bereits enttaggten Interfaces

!!! important "AHA!"
    Wenn du keine VLAN-Tags siehst, bedeutet das nicht automatisch, dass keine VLANs im Spiel sind.  
    Es bedeutet nur, dass an deinem Capture-Punkt keine VLAN-Tags sichtbar sind.

## Access-Port und Trunk-Port

Vereinfacht:

| Porttyp | Beschreibung |
|---|---|
| Access-Port | ein VLAN, Frames meist untagged am Endgerät |
| Trunk-Port | mehrere VLANs, Frames meist mit VLAN-Tag |

Ein normaler Client hängt meist an einem Access-Port.

Deshalb sieht ein Client-Capture oft keine VLAN-Tags.

An einem Trunk-Port oder Mirror-Port können VLAN-Tags sichtbar sein, wenn die Hardware und der Treiber sie nicht entfernen.

## Promiscuous Mode

Im Promiscuous Mode nimmt ein Interface mehr Pakete an, als nur die, die direkt an die eigene MAC-Adresse gerichtet sind.

Das heißt aber nicht, dass du plötzlich den gesamten Switch-Verkehr siehst.

Auf einem modernen Switch bekommst du normalerweise trotzdem nur:

- Traffic zu deinem Gerät
- Broadcast
- Multicast
- eventuell gespiegelten Traffic, wenn ein Mirror-Port eingerichtet ist

!!! warning "Promiscuous Mode ist kein Zaubertrick"
    Auf einem geswitchten Netzwerk sieht ein normaler Client nicht automatisch den Verkehr anderer Geräte.  
    Dafür brauchst du einen geeigneten Capture-Punkt, zum Beispiel Mirror-Port, TAP oder Capture auf dem Zielsystem.

## Typische Layer-2-Beobachtungen

### Viele ARP Requests

Kann normal sein, kann aber auch auffällig sein.

Mögliche Ursachen:

- Gerät sucht Gateway
- Gerät sucht viele Ziele im lokalen Netz
- ARP-Cache läuft ab
- Netzwerkscanner
- fehlerhafte Konfiguration
- IP-Adresskonflikt

### ARP Request ohne Antwort

Mögliche Ursachen:

- Ziel-IP existiert nicht
- Ziel ist offline
- falsches VLAN
- falsche Netzmaske
- Firewall ist hier selten die Ursache, weil ARP unterhalb von IP liegt

### Gleiche IP mit unterschiedlichen MAC-Adressen

Das kann auf einen IP-Adresskonflikt hinweisen.

Es kann aber auch durch Cluster, Loadbalancer, VRRP/HSRP-ähnliche Mechanismen oder MAC-Wechsel erklärbar sein.

Also nicht sofort urteilen.

### Viele Broadcasts

Broadcasts sind normal, aber zu viele Broadcasts können ein Hinweis auf Probleme sein.

Bewerte immer im Kontext:

- Wie groß ist das Netz?
- Welche Protokolle erzeugen die Broadcasts?
- Tritt das dauerhaft auf?
- Gibt es ein konkretes Symptom?

## Wichtige Display Filter

Ethernet-Adresse als Quelle oder Ziel:

```text
eth.addr == 08:00:27:aa:bb:cc
```

Nur Quelle:

```text
eth.src == 08:00:27:aa:bb:cc
```

Nur Ziel:

```text
eth.dst == 08:00:27:aa:bb:cc
```

ARP:

```text
arp
```

ARP Request:

```text
arp.opcode == 1
```

ARP Reply:

```text
arp.opcode == 2
```

Broadcast:

```text
eth.dst == ff:ff:ff:ff:ff:ff
```

VLAN:

```text
vlan
```

Bestimmte VLAN ID:

```text
vlan.id == 10
```

## TShark-Beispiele

Alle ARP-Pakete anzeigen:

```bash
tshark -r pcaps/generated/basic-capture-01.pcapng -Y "arp"
```

ARP Requests zählen:

```bash
tshark -r pcaps/generated/basic-capture-01.pcapng -Y "arp.opcode == 1" | wc -l
```

ARP-Felder ausgeben:

```bash
tshark -r pcaps/generated/basic-capture-01.pcapng \
  -Y "arp" \
  -T fields \
  -e frame.number \
  -e arp.opcode \
  -e arp.src.proto_ipv4 \
  -e arp.src.hw_mac \
  -e arp.dst.proto_ipv4 \
  -e arp.dst.hw_mac
```

VLAN-IDs ausgeben, wenn sichtbar:

```bash
tshark -r capture.pcapng \
  -Y "vlan" \
  -T fields \
  -e frame.number \
  -e vlan.id
```

## Mini-Aufgabe

Erzeuge einen kleinen Capture auf deinem Lernsystem.

1. Starte Wireshark oder TShark.
2. Erzeuge etwas lokalen Netzwerkverkehr:

```bash
ip neigh
ping -c 4 "$(ip route | awk '/default/ {print $3; exit}')"
```

3. Stoppe den Mitschnitt.
4. Speichere ihn als:

```text
pcaps/generated/basic-layer2-01.pcapng
```

5. Öffne ihn in Wireshark.

Beantworte:

- Siehst du ARP-Pakete?
- Welche MAC-Adresse hat dein Gateway?
- Gibt es Broadcast-Pakete?
- Siehst du VLAN-Tags?
- Falls nicht: warum ist das nicht automatisch ein Fehler?
- Welche Display Filter hast du verwendet?

## Analysebericht: kleine Vorlage

```markdown
## Beobachtung

Im Capture wurden ARP-Pakete zwischen `<client-ip>` und `<gateway-ip>` gefunden.

## Relevante Pakete

- Frame `<nummer>`: ARP Request
- Frame `<nummer>`: ARP Reply

## Bewertung

Der Client konnte die MAC-Adresse des Gateways ermitteln.  
Layer-2-Kommunikation zum Gateway ist damit grundsätzlich sichtbar.

## Verwendete Filter

```text
arp
arp.opcode == 1
arp.opcode == 2
```
```

## Typische Fehlinterpretationen

| Beobachtung | Falscher Schluss | Bessere Bewertung |
|---|---|---|
| keine VLAN-Tags sichtbar | es gibt keine VLANs | Tags sind am Capture-Punkt eventuell nicht sichtbar |
| ARP Broadcast sichtbar | Broadcast-Sturm | ein einzelner ARP Request ist normal |
| viele MAC-Adressen | Netzwerkproblem | erst Kontext und Capture-Punkt prüfen |
| keine ARP-Pakete | ARP funktioniert nicht | Cache kann bereits gefüllt sein |
| Promiscuous Mode aktiv | ich sehe alles | auf Switches weiterhin nur sichtbarer Traffic |

## WCA-Bezug

Dieser Abschnitt übt WCA-nahe Grundlagen:

- Ethernet-Frames erkennen
- MAC-Adressen einordnen
- ARP verstehen
- Broadcast/Multicast unterscheiden
- VLAN-Tags erkennen
- Capture-Punkt korrekt bewerten
- Display Filter und TShark auf Layer 2 anwenden

## Merksatz

> Layer 2 ist lokal. Wenn du Ethernet, ARP oder VLANs analysierst, musst du immer fragen: Wo wurde mitgeschnitten und was kann an dieser Stelle überhaupt sichtbar sein?
