# IPv4, IPv6 und ICMP

IPv4, IPv6 und ICMP gehören zu Layer 3.

Hier geht es nicht mehr nur darum, welches Gerät im lokalen Netzwerk angesprochen wird, sondern welche IP-Adresse über lokale Netzwerkgrenzen hinweg erreicht werden soll.

In Wireshark ist dieser Abschnitt wichtig, weil viele Fehlerbilder auf Layer 3 beginnen oder dort sichtbar werden:

- falsche Zieladresse
- falsches Gateway
- Routing-Probleme
- TTL-/Hop-Limit-Effekte
- ICMP-Fehlermeldungen
- Fragmentierung
- MTU-Probleme
- IPv6 Neighbor Discovery und Router Advertisements

## Ziel

Nach diesem Abschnitt solltest du können:

- IPv4- und IPv6-Pakete in Wireshark erkennen
- Quell- und Ziel-IP-Adressen einordnen
- TTL und Hop Limit verstehen
- ICMP Echo Request und Echo Reply erkennen
- wichtige ICMP-Fehlermeldungen grob einordnen
- einfache Fragmentierungs- und MTU-Hinweise erkennen
- sinnvolle Display Filter und TShark-Befehle für Layer 3 verwenden

## Layer 2 vs. Layer 3

Layer 2 arbeitet mit MAC-Adressen im lokalen Segment.

Layer 3 arbeitet mit IP-Adressen über Netzgrenzen hinweg.

AHA:

> Die MAC-Adresse bringt ein Paket zum nächsten Hop.  
> Die IP-Adresse beschreibt das eigentliche logische Ziel.

Wenn ein Client einen Server in einem anderen Subnetz anspricht, sieht man im Client-Capture typischerweise:

| Feld | Bedeutung |
|---|---|
| Ethernet Destination | MAC-Adresse des Gateways |
| IP Destination | IP-Adresse des Zielservers |

Das ist kein Widerspruch. Das ist Routing.

## IPv4 in Wireshark

In den Paketdetails findest du IPv4 meist als:

```text
Internet Protocol Version 4
```

Wichtige Felder:

| Feld | Bedeutung |
|---|---|
| Source Address | Quell-IP-Adresse |
| Destination Address | Ziel-IP-Adresse |
| Time to Live | TTL |
| Protocol | nächstes Protokoll, zum Beispiel TCP, UDP oder ICMP |
| Header Checksum | Prüfsumme des IPv4-Headers |
| Identification | Kennung, relevant bei Fragmentierung |
| Flags | unter anderem Don't Fragment |
| Fragment Offset | Position eines Fragments |

Display Filter:

```text
ip
```

Eine bestimmte Adresse als Quelle oder Ziel:

```text
ip.addr == 192.168.1.10
```

Nur Quelle:

```text
ip.src == 192.168.1.10
```

Nur Ziel:

```text
ip.dst == 192.168.1.10
```

## Private IPv4-Adressen

Häufige private IPv4-Bereiche:

| Bereich | Typische Nutzung |
|---|---|
| `10.0.0.0/8` | größere interne Netze |
| `172.16.0.0/12` | interne Netze |
| `192.168.0.0/16` | Heim- und kleinere Netze |

In Wireshark ist das wichtig, weil du schnell erkennst:

- kommuniziert ein System intern?
- geht Traffic ins Internet?
- wird NAT wahrscheinlich eine Rolle spielen?
- passt die Adresse zum erwarteten Netz?

## TTL verstehen

TTL steht für Time To Live.

Der Name ist etwas historisch. Praktisch ist TTL bei IPv4 ein Hop-Zähler.

Jeder Router reduziert die TTL um 1.

Wenn TTL bei 0 ankommt, wird das Paket verworfen.

Typische Beobachtung:

```text
Time to Live: 64
```

AHA:

> TTL zeigt nicht die Zeit. TTL begrenzt die Anzahl der Router-Hops.

Warum ist das hilfreich?

- sehr kleine TTL kann auf lange Wege oder absichtlich begrenzte Pakete hinweisen
- unterschiedliche TTL-Werte können auf unterschiedliche Betriebssysteme oder Wege hindeuten
- Traceroute nutzt genau dieses Verhalten aus

## ICMP in IPv4

ICMP steht für Internet Control Message Protocol.

ICMP ist kein „Ping-Protokoll“, auch wenn Ping ICMP verwendet.

ICMP wird genutzt für:

- Echo Request
- Echo Reply
- Destination Unreachable
- Time Exceeded
- Fragmentation Needed
- weitere Kontroll- und Fehlermeldungen

Display Filter:

```text
icmp
```

## Ping in Wireshark

Ein klassischer Ping erzeugt:

```text
Echo request
Echo reply
```

Auf Linux:

```bash
ping -c 4 example.org
```

In Wireshark:

```text
icmp
```

Typische Felder:

| Feld | Bedeutung |
|---|---|
| Type | ICMP-Nachrichtentyp |
| Code | genauere Bedeutung |
| Identifier | Zuordnung zusammengehöriger Pakete |
| Sequence Number | Reihenfolge der Echo-Pakete |

Echo Request:

```text
icmp.type == 8
```

Echo Reply:

```text
icmp.type == 0
```

## Ping ist kein vollständiger Netzwerkbeweis

Wenn Ping funktioniert, heißt das nur:

- DNS hat vielleicht funktioniert, wenn du einen Namen verwendet hast
- ICMP Echo Request wurde gesendet
- ICMP Echo Reply kam zurück

Es heißt nicht automatisch:

- TCP-Port 443 funktioniert
- DNS funktioniert grundsätzlich
- TLS funktioniert
- die Anwendung funktioniert
- keine Firewall greift ein

Wenn Ping nicht funktioniert, heißt das ebenfalls nicht automatisch, dass das Ziel offline ist.

ICMP kann blockiert, begrenzt oder anders behandelt werden.

!!! warning "Ping ist ein Werkzeug, kein Urteil"
    Ping ist hilfreich, aber nicht ausreichend. Für Anwendungsprobleme musst du auch TCP, UDP, DNS, TLS oder HTTP betrachten.

## Wichtige ICMP-Fehlermeldungen

### Destination Unreachable

Display Filter:

```text
icmp.type == 3
```

Das bedeutet grob:

> Das Ziel oder ein bestimmter Dienst konnte nicht erreicht werden.

Der `Code` sagt genauer, warum.

### Time Exceeded

Display Filter:

```text
icmp.type == 11
```

Das tritt auf, wenn die TTL abgelaufen ist.

Traceroute nutzt solche Antworten.

### Fragmentation Needed

Bei IPv4 gehört diese Meldung zu Destination Unreachable.

Sie ist für MTU-Probleme wichtig.

Display Filter:

```text
icmp.type == 3 and icmp.code == 4
```

AHA:

> Wenn „Fragmentation Needed“ blockiert wird, können Path-MTU-Probleme schwer sichtbar werden.

## Traceroute und TTL

Traceroute arbeitet vereinfacht so:

1. Paket mit TTL 1 senden
2. erster Router verwirft es und antwortet mit ICMP Time Exceeded
3. Paket mit TTL 2 senden
4. zweiter Router antwortet
5. so weiter bis zum Ziel

Linux:

```bash
traceroute example.org
```

Falls `traceroute` fehlt:

```bash
sudo apt install -y traceroute
```

In Wireshark kannst du dann zum Beispiel filtern:

```text
icmp.type == 11
```

Je nach System und Option kann Traceroute UDP, ICMP oder TCP verwenden.

## IPv4-Fragmentierung

Fragmentierung bedeutet:

> Ein IP-Paket wird in mehrere kleinere IP-Fragmente aufgeteilt.

Das kann passieren, wenn ein Paket größer ist als die Maximum Transmission Unit auf dem Weg.

In Wireshark können Hinweise sein:

- `More fragments`
- `Fragment offset`
- gleiche `Identification`
- mehrere Pakete gehören zu einem ursprünglichen IP-Paket

Display Filter:

```text
ip.flags.mf == 1
```

```text
ip.frag_offset > 0
```

Alle fragmentierten IPv4-Pakete:

```text
ip.flags.mf == 1 or ip.frag_offset > 0
```

!!! note "Fragmentierung ist nicht automatisch ein Fehler"
    Fragmentierung kann normal sein, ist aber oft ein Hinweis, genauer hinzuschauen.  
    Besonders bei Performanceproblemen, VPNs oder ungewöhnlichen MTU-Werten ist sie interessant.

## Don't Fragment

IPv4 kann das Flag `Don't Fragment` setzen.

In Wireshark:

```text
Don't fragment
```

Display Filter:

```text
ip.flags.df == 1
```

Wenn `Don't Fragment` gesetzt ist und ein Paket zu groß für den Weg ist, sollte eine ICMP-Meldung „Fragmentation Needed“ zurückkommen.

Wenn diese ICMP-Meldung blockiert wird, kann Kommunikation scheinbar hängen oder unvollständig funktionieren.

## Header Checksum und Offloading

In lokalen Captures kann Wireshark manchmal scheinbar fehlerhafte Checksums anzeigen.

Das kann durch Hardware Offloading entstehen.

Dann berechnet die Netzwerkkarte die Prüfsumme später, nachdem Wireshark das Paket bereits gesehen hat.

AHA:

> Eine rote Checksum-Warnung im ausgehenden lokalen Capture ist nicht automatisch ein Netzwerkfehler.

Für den Einstieg reicht:

- Checksum-Hinweise nicht blind ignorieren
- aber auch nicht sofort als Fehler bewerten
- Capture-Punkt und Offloading berücksichtigen

## IPv6 in Wireshark

IPv6 findest du als:

```text
Internet Protocol Version 6
```

Wichtige Felder:

| Feld | Bedeutung |
|---|---|
| Source Address | Quell-IPv6-Adresse |
| Destination Address | Ziel-IPv6-Adresse |
| Hop Limit | ähnlich wie TTL bei IPv4 |
| Next Header | nächstes Protokoll |
| Traffic Class | Klassifizierung |
| Flow Label | Flusskennzeichnung |

Display Filter:

```text
ipv6
```

IPv6-Adresse als Quelle oder Ziel:

```text
ipv6.addr == 2001:db8::1
```

Nur Quelle:

```text
ipv6.src == 2001:db8::1
```

Nur Ziel:

```text
ipv6.dst == 2001:db8::1
```

## Hop Limit

IPv6 verwendet kein Feld namens TTL.

Stattdessen heißt es:

```text
Hop Limit
```

Die Idee ist ähnlich:

> Jeder Router reduziert den Wert. Bei 0 wird das Paket verworfen.

Display Filter:

```text
ipv6.hlim <= 5
```

## Link-Local-Adressen

IPv6-Link-Local-Adressen beginnen mit:

```text
fe80::
```

Sie gelten nur auf dem lokalen Link.

In Wireshark tauchen sie häufig bei lokalen IPv6-Protokollen auf.

AHA:

> `fe80::` bedeutet nicht Internet. Es bedeutet lokale IPv6-Kommunikation auf dem Link.

## ICMPv6

IPv6 nutzt ICMPv6 sehr intensiv.

Display Filter:

```text
icmpv6
```

ICMPv6 ist nicht nur „Ping für IPv6“.

Es ist wichtig für:

- Neighbor Discovery
- Router Solicitation
- Router Advertisement
- Duplicate Address Detection
- Path MTU Discovery
- Echo Request und Echo Reply

Wichtige Filter:

```text
icmpv6.type == 128
```

Echo Request.

```text
icmpv6.type == 129
```

Echo Reply.

Neighbor Solicitation:

```text
icmpv6.type == 135
```

Neighbor Advertisement:

```text
icmpv6.type == 136
```

Router Solicitation:

```text
icmpv6.type == 133
```

Router Advertisement:

```text
icmpv6.type == 134
```

## IPv6 ersetzt ARP nicht direkt sichtbar durch ARP

IPv6 verwendet kein ARP.

Stattdessen nutzt IPv6 Neighbor Discovery über ICMPv6.

Wenn du also IPv6 analysierst, suche nicht nach:

```text
arp
```

sondern nach:

```text
icmpv6
```

und besonders:

```text
icmpv6.type == 135 or icmpv6.type == 136
```

## NAT und Capture-Punkte

NAT verändert IP-Adressen.

Das ist für Capture-Punkte wichtig.

Beispiel:

| Capture-Punkt | Mögliche sichtbare Quell-IP |
|---|---|
| Client intern | private Client-IP |
| vor NAT | private Client-IP |
| nach NAT | öffentliche oder andere übersetzte IP |
| Zielserver | NAT-Adresse, nicht ursprüngliche Client-IP |

AHA:

> Bei NAT ist die Frage „Wo wurde mitgeschnitten?“ entscheidend.

Wenn ein Server eine andere Quell-IP sieht als der Client verwendet, ist das nicht automatisch falsch.

Es kann NAT sein.

## Wichtige Display Filter

IPv4:

```text
ip
```

IPv6:

```text
ipv6
```

ICMP:

```text
icmp
```

ICMPv6:

```text
icmpv6
```

IPv4-Adresse:

```text
ip.addr == 192.168.1.10
```

IPv6-Adresse:

```text
ipv6.addr == 2001:db8::1
```

Niedrige TTL:

```text
ip.ttl <= 5
```

Niedriges Hop Limit:

```text
ipv6.hlim <= 5
```

IPv4 fragmentiert:

```text
ip.flags.mf == 1 or ip.frag_offset > 0
```

ICMP Destination Unreachable:

```text
icmp.type == 3
```

ICMP Time Exceeded:

```text
icmp.type == 11
```

ICMPv6 Neighbor Discovery:

```text
icmpv6.type == 135 or icmpv6.type == 136
```

## TShark-Beispiele

IPv4-Pakete zählen:

```bash
tshark -r pcaps/generated/basic-capture-01.pcapng -Y "ip" | wc -l
```

IPv6-Pakete zählen:

```bash
tshark -r pcaps/generated/basic-capture-01.pcapng -Y "ipv6" | wc -l
```

Quell- und Ziel-IPv4-Adressen ausgeben:

```bash
tshark -r pcaps/generated/basic-capture-01.pcapng \
  -Y "ip" \
  -T fields \
  -e frame.number \
  -e ip.src \
  -e ip.dst \
  -e ip.ttl \
  -e ip.proto
```

ICMP-Pakete ausgeben:

```bash
tshark -r pcaps/generated/basic-capture-01.pcapng \
  -Y "icmp" \
  -T fields \
  -e frame.number \
  -e ip.src \
  -e ip.dst \
  -e icmp.type \
  -e icmp.code
```

IPv6 und ICMPv6 ausgeben:

```bash
tshark -r pcaps/generated/basic-capture-01.pcapng \
  -Y "ipv6 or icmpv6" \
  -T fields \
  -e frame.number \
  -e ipv6.src \
  -e ipv6.dst \
  -e ipv6.hlim \
  -e icmpv6.type
```

Fragmentierte IPv4-Pakete suchen:

```bash
tshark -r capture.pcapng \
  -Y "ip.flags.mf == 1 or ip.frag_offset > 0"
```

## Mini-Aufgabe

Erzeuge einen kleinen Capture.

1. Starte Wireshark oder TShark.
2. Erzeuge Traffic:

```bash
ping -c 4 example.org
traceroute example.org
curl -I https://example.org
```

Falls `traceroute` fehlt:

```bash
sudo apt install -y traceroute
```

3. Stoppe den Mitschnitt.
4. Speichere ihn als:

```text
pcaps/generated/basic-layer3-01.pcapng
```

5. Öffne ihn in Wireshark.

Beantworte:

- Welche IPv4-Adressen siehst du?
- Siehst du IPv6-Pakete?
- Welche TTL- oder Hop-Limit-Werte findest du?
- Siehst du ICMP Echo Request oder Echo Reply?
- Siehst du ICMP Time Exceeded vom Traceroute?
- Gibt es fragmentierte IPv4-Pakete?
- Welche Display Filter hast du verwendet?

## Analysebericht: kleine Vorlage

Nutze diese Struktur für deine Notizen:

```text
Beobachtung:
Im Capture wurden IPv4-Pakete zwischen <client-ip> und <ziel-ip> gefunden.

Relevante Pakete:
Frame <nummer>: ICMP Echo Request
Frame <nummer>: ICMP Echo Reply

Bewertung:
Der Client erhält ICMP-Antworten vom Ziel. Das beweist ICMP-Erreichbarkeit, aber nicht automatisch die Funktion von TCP, TLS oder HTTP.

Verwendete Filter:
icmp
ip.addr == <ziel-ip>
```

## Typische Fehlinterpretationen

| Beobachtung | Falscher Schluss | Bessere Bewertung |
|---|---|---|
| Ping funktioniert | alles ist erreichbar | nur ICMP wurde erfolgreich getestet |
| Ping funktioniert nicht | Ziel ist offline | ICMP kann blockiert sein |
| keine IPv6-Pakete | IPv6 ist kaputt | IPv6 wird eventuell nicht genutzt |
| keine ARP bei IPv6 | Layer 2 fehlt | IPv6 nutzt Neighbor Discovery über ICMPv6 |
| Checksum-Warnung | Paket ist defekt | Offloading am Capture-Punkt prüfen |
| andere Quell-IP am Server | falscher Client | NAT oder Proxy berücksichtigen |

## WCA-Bezug

Dieser Abschnitt übt WCA-nahe Grundlagen:

- IPv4- und IPv6-Pakete erkennen
- Quell- und Zieladressen einordnen
- TTL und Hop Limit verstehen
- ICMP und ICMPv6 bewerten
- Fragmentierung und MTU-Hinweise erkennen
- Display Filter und TShark auf Layer 3 anwenden
- Capture-Punkte bei Routing und NAT richtig bewerten

## Merksatz

> Layer 3 zeigt dir, wohin ein Paket logisch gehen soll.  
> Ob es dort ankommt, hängt vom Weg, vom Routing, von Filtern, von NAT und vom Capture-Punkt ab.
