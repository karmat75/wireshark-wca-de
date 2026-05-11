# OSI-Modell für Wireshark

Das OSI-Modell ist ein Schichtenmodell für Netzwerkkommunikation.

Für diesen Kurs ist es keine akademische Pflichtübung, sondern eine praktische Orientierung:

> Auf welcher Schicht suche ich eigentlich das Problem?

Wenn du in Wireshark ein Paket öffnest, siehst du genau diese Schichtung als aufgeklappte Protokolle.

Beispiel:

```text
Frame
Ethernet II
Internet Protocol Version 4
Transmission Control Protocol
Transport Layer Security
Hypertext Transfer Protocol
```

Das ist keine zufällige Liste. Es ist die technische Verpackung des Datenverkehrs von unten nach oben.

## Warum das im Kurs wichtig ist

Viele Fehlanalysen entstehen, weil Symptome auf der falschen Schicht gesucht werden.

Beispiele:

| Symptom | Mögliche Schicht | Erste Frage |
|---|---|---|
| Zielname wird nicht gefunden | Anwendung / DNS | Gibt es DNS-Anfrage und DNS-Antwort? |
| Ziel-IP ist erreichbar, Webdienst nicht | Transport / Anwendung | Kommt TCP-Port 80 oder 443 zustande? |
| Client erreicht Gateway nicht | Layer 2 / Layer 3 | Gibt es ARP und eine passende Route? |
| HTTPS lädt langsam | Transport / Anwendung | Gibt es Retransmissions, RTT oder Server Delay? |
| VLAN wird vermutet | Layer 2 | Sind VLAN-Tags am Capture-Punkt sichtbar? |

Das OSI-Modell hilft dir, die Analyse zu sortieren.

Es ersetzt aber nicht die Paketprüfung.

## Die OSI-Schichten im Überblick

| Schicht | Name | Typische Themen im Kurs |
|---|---|---|
| 7 | Application | HTTP, DNS, DHCP, TLS-Sichtbarkeit, Anwendungsfehler |
| 6 | Presentation | Codierung, Verschlüsselung, TLS wird oft hier oder zwischen 5 und 7 eingeordnet |
| 5 | Session | Sitzungen, Dialoge, in TCP/IP oft nicht klar getrennt |
| 4 | Transport | TCP, UDP, Ports, Verbindungen, Retransmissions |
| 3 | Network | IPv4, IPv6, ICMP, Routing, TTL, Fragmentierung |
| 2 | Data Link | Ethernet, MAC-Adressen, ARP, VLAN, Broadcast |
| 1 | Physical | Kabel, Funk, Signal, Link, Duplex, physische Fehler |

!!! note "Nicht zu dogmatisch verwenden"
    Das OSI-Modell ist ein Denkmodell.  
    Moderne Protokolle passen nicht immer sauber in genau eine Schicht. Für Wireshark ist wichtiger, was im Paket tatsächlich sichtbar ist.

## Was Wireshark wirklich zeigt

Wireshark zeigt nicht einfach „Layer 1 bis 7“.

Wireshark zeigt die Protokolle, die es im Paket erkennt.

Ein einfaches DNS-Paket über IPv4 und UDP kann so aussehen:

```text
Frame
Ethernet II
Internet Protocol Version 4
User Datagram Protocol
Domain Name System
```

Das entspricht grob:

| Wireshark-Bereich | OSI-Einordnung |
|---|---|
| Frame | Metadaten zum Mitschnitt, keine echte OSI-Schicht |
| Ethernet II | Layer 2 |
| IPv4 | Layer 3 |
| UDP | Layer 4 |
| DNS | Layer 7 |

## Frame ist keine OSI-Schicht

Der Eintrag `Frame` in Wireshark ist besonders wichtig.

Er enthält Informationen über den Mitschnitt selbst, zum Beispiel:

- Paketnummer
- Paketlänge
- Zeitpunkt
- Capture-Länge
- Interface-Informationen

Das sind keine Daten, die in dieser Form „auf dem Kabel“ als OSI-Schicht übertragen wurden.

`Frame` ist Wireshark-/Capture-Metadaten.

## Layer 1: Was du meistens nicht siehst

Layer 1 ist die physische Schicht.

Dazu gehören zum Beispiel:

- Kabel
- Stecker
- Funk
- Signalqualität
- Linkstatus
- elektrische oder optische Signale
- Duplex und Geschwindigkeit

Wireshark sieht normalerweise keine echten Layer-1-Details.

Du kannst indirekte Hinweise sehen, zum Beispiel:

- viele Retransmissions
- Paketverlust
- Verbindungsabbrüche
- auffällige Latenz
- Interface geht hoch/runter, aber eher in Systemlogs als im Capture

Aber die Ursache „Kabel defekt“ steht nicht als Paket im Capture.

Dafür brauchst du andere Werkzeuge:

- Switchport-Statistiken
- Interface-Counter
- Logs
- Monitoring
- Kabeltester
- WLAN-Analysewerkzeuge

## Layer 2: Ethernet, ARP und VLAN

Layer 2 ist die lokale Verbindungsschicht.

In Wireshark siehst du hier typischerweise:

- Ethernet II
- Quell-MAC-Adresse
- Ziel-MAC-Adresse
- Broadcast
- Multicast
- ARP
- VLAN-Tags, wenn sie sichtbar sind

Wichtige Filter:

```text
eth
```

```text
arp
```

```text
vlan
```

```text
eth.addr == aa:bb:cc:dd:ee:ff
```

AHA:

> Layer 2 ist lokal. Über Router hinweg ändern sich MAC-Adressen.

Wenn du also einen Server in einem anderen Subnetz ansprichst, ist die Ziel-MAC im Client-Capture normalerweise nicht die MAC-Adresse des Servers, sondern die MAC-Adresse des Gateways.

## Layer 3: IPv4, IPv6 und ICMP

Layer 3 beschäftigt sich mit logischer Adressierung und Routing.

In Wireshark siehst du hier:

- IPv4
- IPv6
- Quell-IP
- Ziel-IP
- TTL / Hop Limit
- Fragmentierung
- ICMP
- ICMPv6

Wichtige Filter:

```text
ip
```

```text
ipv6
```

```text
icmp
```

```text
icmpv6
```

```text
ip.addr == 192.168.1.10
```

AHA:

> IP-Adressen bleiben über Router hinweg sichtbar. MAC-Adressen gelten nur lokal im jeweiligen Segment.

## Layer 4: TCP und UDP

Layer 4 ist die Transportschicht.

Hier geht es um Kommunikation zwischen Prozessen oder Diensten.

Typische Themen:

- TCP
- UDP
- Ports
- TCP Handshake
- Sequenznummern
- ACKs
- Retransmissions
- Resets
- Window Size
- UDP-Anfragen und Antworten

Wichtige Filter:

```text
tcp
```

```text
udp
```

```text
tcp.port == 443
```

```text
udp.port == 53
```

AHA:

> Eine IP-Adresse sagt, welches System gemeint ist.  
> Ein Port sagt, welcher Dienst auf diesem System gemeint ist.

## Layer 5 bis 7: Session, Presentation, Application

Im TCP/IP-Alltag werden die oberen OSI-Schichten oft nicht so sauber getrennt wie im Modell.

Für Wireshark ist meistens entscheidend:

- Welches Anwendungsprotokoll sehe ich?
- Ist der Inhalt verschlüsselt?
- Welche Metadaten bleiben sichtbar?
- Ist die Anwendung selbst langsam oder fehlerhaft?

Typische Protokolle:

| Protokoll | Einordnung im Kurs |
|---|---|
| DNS | Anwendung |
| HTTP | Anwendung |
| TLS | Verschlüsselung/Absicherung zwischen Transport und Anwendung |
| DHCP | Anwendung über UDP |
| SMB | Anwendung |
| NTP | Anwendung über UDP |

Wichtige Filter:

```text
dns
```

```text
http
```

```text
tls
```

```text
dhcp
```

oder je nach Wireshark-Version:

```text
bootp
```

## TLS ist ein gutes Beispiel für „nicht zu dogmatisch“

TLS wird oft grob in Richtung Presentation Layer eingeordnet, weil es Verschlüsselung und Aushandlung behandelt.

In Wireshark liegt TLS praktisch zwischen TCP und der Anwendung.

Du siehst zum Beispiel:

```text
Ethernet II
IPv4
TCP
TLS
```

Was du sehen kannst:

- TLS-Version
- Handshake
- SNI, wenn vorhanden und nicht durch neuere Mechanismen verborgen
- Zertifikatsinformationen, je nach Verbindung
- ALPN, je nach Verbindung
- Paketgrößen und Zeitverhalten

Was du normalerweise nicht siehst:

- HTTP-Inhalt
- Passwörter
- Formulardaten
- API-Payload

AHA:

> Verschlüsselung versteckt nicht die Existenz einer Verbindung. Sie versteckt den Inhalt.

## ARP passt nicht perfekt in eine einfache Schublade

ARP fühlt sich wie „zwischen Layer 2 und 3“ an:

- Es wird in Ethernet transportiert.
- Es löst IPv4-Adressen zu MAC-Adressen auf.
- Es ist nur im lokalen Layer-2-Segment relevant.

Für den Kurs behandeln wir ARP im Layer-2-Kontext, weil du es bei Ethernet, Broadcast und lokaler Erreichbarkeit brauchst.

Das ist für die Analyse wichtiger als eine perfekte akademische Einordnung.

## Encapsulation: Verpackung von oben nach unten

Beim Senden werden Daten schrittweise verpackt.

Vereinfacht:

```text
HTTP-Daten
in TLS
in TCP
in IP
in Ethernet
```

Beim Empfangen wird diese Verpackung wieder geöffnet.

Wireshark zeigt dir diese Schichten im Paketdetailbereich.

AHA:

> Wenn du ein Paket in Wireshark aufklappst, liest du die Verpackung von außen nach innen.

## Analyse mit Schichtenmodell

Eine einfache Troubleshooting-Reihenfolge:

1. Gibt es überhaupt Pakete?
2. Ist der Capture-Punkt richtig?
3. Siehst du Layer 2?
4. Gibt es ARP oder passende MAC-Kommunikation?
5. Gibt es IP-Kommunikation?
6. Gibt es TCP oder UDP?
7. Gibt es ein Anwendungsprotokoll?
8. Gibt es Fehler, Verzögerungen oder Abbrüche?
9. Auf welcher Schicht ist der erste sichtbare Bruch?

Diese Reihenfolge verhindert, dass du zu früh an der falschen Stelle suchst.

## Beispiel: Webseite funktioniert nicht

Symptom:

```text
https://example.org lädt nicht
```

Analysefragen nach Schichten:

| Schicht | Frage |
|---|---|
| Layer 2 | Kann der Client sein Gateway per ARP erreichen? |
| Layer 3 | Gibt es IP-Pakete zum Ziel oder zum DNS-Server? |
| Layer 4 | Wird TCP-Port 443 erreicht? |
| TLS | Gibt es einen TLS-Handshake? |
| Anwendung | Gibt es HTTP-Antworten oder Fehler? |
| Capture | Schneide ich überhaupt an der richtigen Stelle mit? |

## Beispiel: DNS funktioniert nicht

Symptom:

```text
Name kann nicht aufgelöst werden
```

Analysefragen:

| Schicht | Frage |
|---|---|
| Layer 3 | Wird der DNS-Server per IP erreicht? |
| Layer 4 | Gibt es UDP oder TCP auf Port 53? |
| Anwendung | Gibt es DNS Query und DNS Response? |
| Anwendung | Welcher Response Code kommt zurück? |
| Capture | Sehe ich Anfrage und Antwort oder nur eine Richtung? |

## Typische Fehler im Umgang mit dem OSI-Modell

### „Das ist Layer 7, also kann es kein Netzwerkproblem sein“

Falsch.

Ein Anwendungssymptom kann durch ein Transportproblem ausgelöst werden.

Beispiel:

- HTTP ist langsam
- Ursache ist Paketverlust auf TCP
- sichtbar als Retransmissions auf Layer 4

### „Ping geht, also ist das Netzwerk okay“

Falsch.

Ping zeigt nur, dass ICMP Echo in diesem Moment funktioniert.

Es sagt nicht automatisch, dass DNS, TCP 443, TLS oder HTTP funktionieren.

### „Keine VLAN-Tags sichtbar, also gibt es keine VLANs“

Falsch.

VLAN-Tags können am Capture-Punkt entfernt worden sein oder gar nicht sichtbar sein.

### „Wireshark zeigt keinen Fehler, also gibt es keinen Fehler“

Falsch.

Wireshark zeigt Pakete. Die Bewertung entsteht durch Analyse.

## WCA-Bezug

Für WCA-nahe Vorbereitung ist das Schichtenmodell wichtig, weil es hilft:

- Protokolle einzuordnen
- Header und Felder sinnvoll zu lesen
- Capture-Punkte zu bewerten
- Filter gezielt einzusetzen
- Fehler strukturiert einzugrenzen
- nicht vorschnell auf die falsche Ursache zu schließen

Du musst das OSI-Modell nicht als Definition auswendig herunterbeten.

Du solltest es als Denkwerkzeug nutzen können.

## Merksatz

> Das OSI-Modell ist kein Gesetzbuch. Es ist eine Landkarte.  
> Wireshark zeigt dir die Pakete. Das Schichtenmodell hilft dir, dich darin nicht zu verlaufen.
