# UDP, DNS und DHCP

UDP, DNS und DHCP gehören zu den Protokollen, die du in Wireshark sehr häufig sehen wirst.

Sie sind besonders wichtig, weil viele Probleme im Alltag zunächst wie „Netzwerk geht nicht“ aussehen, aber in Wirklichkeit mit Namensauflösung oder Adressvergabe beginnen.

In diesem Abschnitt geht es um drei Dinge:

- UDP als Transportprotokoll
- DNS als Namensauflösung
- DHCP als automatische IP-Konfiguration

## Ziel

Nach diesem Abschnitt solltest du können:

- UDP-Pakete in Wireshark erkennen
- UDP von TCP abgrenzen
- DNS Query und DNS Response unterscheiden
- wichtige DNS Response Codes einordnen
- DNS über UDP und TCP erkennen
- DHCP Discover, Offer, Request und ACK erkennen
- wichtige DHCP-Optionen lesen
- einfache DNS- und DHCP-Fehlerbilder bewerten
- passende Display Filter und TShark-Befehle verwenden

## UDP: kurz und direkt

UDP steht für User Datagram Protocol.

UDP ist verbindungslos.

Das bedeutet:

- kein Verbindungsaufbau
- kein 3-Way Handshake
- keine Sequenznummern wie bei TCP
- keine automatische Wiederholung verlorener Pakete
- keine eingebaute Flusskontrolle

UDP sendet Datagramme.

Ob eine Antwort kommt, ob ein Paket verloren geht oder ob eine Anwendung erneut fragt, muss die Anwendung selbst behandeln.

AHA:

> UDP ist nicht „schlecht“. UDP ist einfach bewusst schlank.

Typische UDP-Protokolle:

| Protokoll | Typischer Port | Zweck |
|---|---:|---|
| DNS | 53 | Namensauflösung |
| DHCP Server | 67 | Adressvergabe |
| DHCP Client | 68 | Adressvergabe |
| NTP | 123 | Zeitsynchronisation |
| mDNS | 5353 | lokale Namensauflösung |
| SNMP | 161 | Monitoring |
| QUIC/HTTP3 | 443 | Webverkehr über UDP |

## UDP in Wireshark

In den Paketdetails findest du UDP als:

```text
User Datagram Protocol
```

Wichtige Felder:

| Feld | Bedeutung |
|---|---|
| Source Port | Quellport |
| Destination Port | Zielport |
| Length | Länge des UDP-Datagramms |
| Checksum | Prüfsumme |

Display Filter:

```text
udp
```

Bestimmter UDP-Port:

```text
udp.port == 53
```

Nur Zielport:

```text
udp.dstport == 53
```

Nur Quellport:

```text
udp.srcport == 53
```

## UDP und „keine Antwort“

Bei UDP gibt es keine Verbindung, die aufgebaut oder sauber beendet wird.

Wenn du eine UDP-Anfrage siehst, aber keine Antwort, kann das mehrere Gründe haben:

- Antwort wurde nicht gesendet
- Antwort ging an anderem Capture-Punkt vorbei
- Antwort wurde gefiltert
- Anfrage war ungültig
- Dienst läuft nicht
- Anwendung wiederholt später
- ICMP-Fehlermeldung wurde gesendet
- ICMP-Fehlermeldung wurde blockiert

AHA:

> Bei UDP ist „keine Antwort sichtbar“ eine Beobachtung, aber noch keine fertige Diagnose.

## DNS: Namen zu Adressen

DNS steht für Domain Name System.

DNS beantwortet Fragen wie:

> Welche IP-Adresse gehört zu `example.org`?

In Wireshark findest du DNS meist als:

```text
Domain Name System
```

Häufig über UDP-Port 53:

```text
udp.port == 53
```

Einfacher Display Filter:

```text
dns
```

## DNS Query und DNS Response

Eine DNS-Abfrage besteht meistens aus:

- Query
- Response

Query:

```text
Standard query
```

Response:

```text
Standard query response
```

Wichtige Felder:

| Feld | Bedeutung |
|---|---|
| Transaction ID | Zuordnung von Anfrage und Antwort |
| Query Name | abgefragter Name |
| Query Type | Typ der Anfrage, z. B. A oder AAAA |
| Response Code | Ergebnis der Antwort |
| Answers | Antwortdatensätze |

## DNS Query Types

Häufige Query Types:

| Typ | Bedeutung |
|---|---|
| A | IPv4-Adresse |
| AAAA | IPv6-Adresse |
| CNAME | Alias |
| MX | Mailserver |
| TXT | Textdaten |
| PTR | Reverse Lookup |

Beispiele:

```text
A example.org
AAAA example.org
PTR 1.1.168.192.in-addr.arpa
```

## DNS Response Codes

Wichtige Response Codes:

| Code | Bedeutung | Typische Interpretation |
|---|---|---|
| `NoError` | Anfrage erfolgreich verarbeitet | Antwort kann Daten enthalten, muss aber nicht |
| `NXDomain` | Name existiert nicht | Name falsch oder nicht vorhanden |
| `ServFail` | Server konnte Anfrage nicht verarbeiten | Problem beim DNS-Server oder Upstream |
| `Refused` | Server lehnt Anfrage ab | Policy, falscher Client, falsche Zone |
| `NoData` | Name existiert, aber nicht für diesen Typ | z. B. A gefragt, aber kein A-Record |

!!! note "NoError bedeutet nicht immer: passende IP gefunden"
    `NoError` bedeutet nur, dass die DNS-Anfrage erfolgreich verarbeitet wurde.  
    Es kann trotzdem sein, dass keine Antwortdaten für den angefragten Typ enthalten sind.

## Wichtige DNS-Filter

Alle DNS-Pakete:

```text
dns
```

Nur DNS-Anfragen:

```text
dns.flags.response == 0
```

Nur DNS-Antworten:

```text
dns.flags.response == 1
```

DNS-Name enthält Text:

```text
dns.qry.name contains "example"
```

NXDOMAIN:

```text
dns.flags.rcode == 3
```

SERVFAIL:

```text
dns.flags.rcode == 2
```

DNS über UDP:

```text
dns and udp
```

DNS über TCP:

```text
dns and tcp
```

## DNS über TCP

DNS läuft meistens über UDP.

DNS kann aber auch TCP verwenden.

Typische Gründe:

- sehr große Antworten
- Zone Transfers
- Fallback bei abgeschnittenen Antworten
- bestimmte DNSSEC-Szenarien

Filter:

```text
tcp.port == 53
```

oder:

```text
dns and tcp
```

AHA:

> DNS ist nicht automatisch UDP. UDP ist häufig, aber TCP ist ebenfalls möglich.

## DNS ist nicht immer als DNS sichtbar

Nicht jede Namensauflösung erscheint in Wireshark als klassisches DNS.

Gründe:

- DNS over HTTPS
- DNS over TLS
- lokaler DNS-Cache
- Browser nutzt eigene DNS-Einstellungen
- Anfrage passiert vor dem Capture
- Antwort kommt aus Cache
- Name wurde bereits aufgelöst
- du schneidest am falschen Interface mit

DoH und DoT sind besonders wichtig:

| Verfahren | Typischer Transport | Sichtbarkeit |
|---|---|---|
| klassisches DNS | UDP/TCP 53 | als DNS sichtbar |
| DNS over TLS | TCP 853 | verschlüsselt |
| DNS over HTTPS | HTTPS/TCP 443 | als HTTPS sichtbar, nicht als klassisches DNS |

AHA:

> Wenn du keinen DNS-Traffic siehst, heißt das nicht automatisch, dass keine Namensauflösung stattgefunden hat.

## DNS-Analyse: sinnvolle Reihenfolge

Bei DNS-Problemen hilft diese Reihenfolge:

1. Gibt es überhaupt DNS-Pakete?
2. Wer fragt welchen DNS-Server?
3. Welcher Name wird gefragt?
4. Welcher Query Type wird gefragt?
5. Gibt es eine Antwort?
6. Welcher Response Code steht in der Antwort?
7. Enthält die Antwort passende Records?
8. Passt die zurückgegebene IP zum erwarteten Ziel?
9. Wird danach tatsächlich eine Verbindung zur IP aufgebaut?

## Beispiel: NXDOMAIN

Symptom:

```text
Benutzer kann webappl.local nicht öffnen.
```

Beobachtung:

```text
DNS Response Code: NXDomain
```

Bewertung:

> Der Client hat gefragt, aber der DNS-Server sagt, dass dieser Name nicht existiert.

Mögliche Ursachen:

- Name falsch geschrieben
- falsche DNS-Suchdomäne
- falscher DNS-Server
- Zone fehlt
- Eintrag wurde gelöscht
- Split-DNS-Problem

## Beispiel: DNS funktioniert, Anwendung nicht

Beobachtung:

- DNS Query vorhanden
- DNS Response mit IP vorhanden
- danach TCP SYN zur IP sichtbar
- keine TCP-Antwort oder Reset

Bewertung:

> DNS ist wahrscheinlich nicht die Ursache. Die Analyse muss danach auf TCP, Routing, Firewall oder Serverdienst wechseln.

## DHCP: automatische IP-Konfiguration

DHCP steht für Dynamic Host Configuration Protocol.

DHCP versorgt Clients typischerweise mit:

- IP-Adresse
- Subnetzmaske
- Standardgateway
- DNS-Server
- Lease-Zeit
- weiteren Optionen

In IPv4 läuft DHCP klassisch über UDP:

| Richtung | Port |
|---|---:|
| Client zu Server | UDP 67 |
| Server zu Client | UDP 68 |

Display Filter:

```text
dhcp
```

oder, je nach Wireshark-Version:

```text
bootp
```

!!! note "DHCP oder BOOTP?"
    In Wireshark kann DHCP je nach Version und Kontext als `dhcp` oder historisch als `bootp` gefiltert werden.  
    Wenn `dhcp` keine Pakete zeigt, teste `bootp`.

## DHCP DORA

Der klassische Ablauf wird oft als DORA bezeichnet:

| Schritt | Bedeutung |
|---|---|
| Discover | Client sucht DHCP-Server |
| Offer | Server bietet Adresse an |
| Request | Client fordert Adresse an |
| ACK | Server bestätigt Adresse |

Vereinfacht:

```text
Discover  -> Wer kann mir eine IP geben?
Offer     -> Ich biete dir diese IP an.
Request   -> Ich möchte diese IP verwenden.
ACK       -> Ja, du darfst diese IP verwenden.
```

## DHCP in Wireshark lesen

Wichtige Felder:

| Feld | Bedeutung |
|---|---|
| Message Type | Discover, Offer, Request, ACK usw. |
| Client MAC address | MAC-Adresse des Clients |
| Your client IP address | angebotene oder zugewiesene Adresse |
| Transaction ID | Zuordnung der DHCP-Nachrichten |
| Option 50 | Requested IP Address |
| Option 53 | DHCP Message Type |
| Option 54 | DHCP Server Identifier |
| Option 1 | Subnet Mask |
| Option 3 | Router / Default Gateway |
| Option 6 | DNS Server |
| Option 51 | Lease Time |

## DHCP Message Types filtern

Je nach Wireshark-Version können die Feldnamen leicht variieren.

Häufig funktioniert:

```text
dhcp.option.dhcp == 1
```

für Discover.

```text
dhcp.option.dhcp == 2
```

für Offer.

```text
dhcp.option.dhcp == 3
```

für Request.

```text
dhcp.option.dhcp == 5
```

für ACK.

Wenn dein Wireshark stattdessen BOOTP-Feldnamen verwendet, suche im Paketdetails-Bereich das Feld `DHCP Message Type`, klicke es rechts an und wähle `Apply as Filter`.

AHA:

> Feldnamen aus dem Paketdetails-Bereich sind verlässlicher als auswendig gelernte Filter.

## DHCP und Broadcast

DHCP beginnt oft mit Broadcast, weil der Client am Anfang noch keine gültige IP-Konfiguration hat.

Typisch:

- Quell-IP: `0.0.0.0`
- Ziel-IP: `255.255.255.255`
- Ziel-MAC: `ff:ff:ff:ff:ff:ff`

Das ist normal.

Display Filter für Broadcast-MAC:

```text
eth.dst == ff:ff:ff:ff:ff:ff
```

## DHCP über Router hinweg

DHCP-Broadcasts gehen normalerweise nicht einfach über Router hinweg.

Wenn Clients in einem anderen Netz einen zentralen DHCP-Server verwenden, braucht es meist einen DHCP Relay.

In der Praxis kann dieser auf einem Router, Switch, Firewall oder Server laufen.

AHA:

> Wenn ein Client keinen DHCP-Server findet, kann das Problem im lokalen VLAN, am Relay oder am DHCP-Server liegen.

## Typische DHCP-Fehlerbilder

### Discover ohne Offer

Beobachtung:

- Client sendet DHCP Discover
- kein DHCP Offer sichtbar

Mögliche Ursachen:

- DHCP-Server nicht erreichbar
- falsches VLAN
- DHCP Relay fehlt oder ist falsch
- Server hat keine freien Leases
- Firewall oder ACL blockiert
- Capture-Punkt sieht nur Client-Seite

### Offer ohne Request

Beobachtung:

- Server bietet Adresse an
- Client fordert sie nicht an

Mögliche Ursachen:

- Client akzeptiert Angebot nicht
- mehrere DHCP-Server
- falsche Option
- Client hat bereits andere Konfiguration
- Capture unvollständig

### Request ohne ACK

Beobachtung:

- Client fordert Adresse an
- keine Bestätigung sichtbar

Mögliche Ursachen:

- Server lehnt ab
- Antwort geht verloren
- falscher Capture-Punkt
- Serverproblem

### Falsches Gateway oder DNS

Beobachtung:

- DHCP läuft durch
- Client bekommt aber falsche Optionen

Mögliche Ursachen:

- falscher Scope
- falsche DHCP-Optionen
- falsches VLAN
- veraltete Konfiguration

## Wichtige Display Filter

UDP:

```text
udp
```

DNS:

```text
dns
```

DNS-Anfragen:

```text
dns.flags.response == 0
```

DNS-Antworten:

```text
dns.flags.response == 1
```

DNS-Name:

```text
dns.qry.name contains "example"
```

DNS Response Code nicht erfolgreich:

```text
dns.flags.rcode != 0
```

DNS über Port 53:

```text
udp.port == 53 or tcp.port == 53
```

DHCP:

```text
dhcp
```

Alternative:

```text
bootp
```

DHCP-Ports:

```text
udp.port == 67 or udp.port == 68
```

Broadcast:

```text
eth.dst == ff:ff:ff:ff:ff:ff
```

## TShark-Beispiele

DNS-Anfragen ausgeben:

```bash
tshark -r pcaps/generated/basic-capture-01.pcapng   -Y "dns.flags.response == 0"   -T fields   -e frame.number   -e ip.src   -e ip.dst   -e dns.qry.name   -e dns.qry.type
```

DNS-Antworten mit Response Code ausgeben:

```bash
tshark -r pcaps/generated/basic-capture-01.pcapng   -Y "dns.flags.response == 1"   -T fields   -e frame.number   -e ip.src   -e ip.dst   -e dns.qry.name   -e dns.flags.rcode
```

DNS-Fehler zählen:

```bash
tshark -r pcaps/generated/basic-capture-01.pcapng   -Y "dns.flags.response == 1 and dns.flags.rcode != 0" | wc -l
```

DHCP-Pakete anzeigen:

```bash
tshark -r capture.pcapng -Y "dhcp or bootp"
```

DHCP-relevante Felder ausgeben:

```bash
tshark -r capture.pcapng   -Y "dhcp or bootp"   -T fields   -e frame.number   -e eth.src   -e eth.dst   -e ip.src   -e ip.dst   -e udp.srcport   -e udp.dstport
```

## Mini-Aufgabe: DNS

Erzeuge einen Capture.

1. Starte Wireshark oder TShark.
2. Führe aus:

```bash
dig example.org
dig does-not-exist.example.org
dig AAAA example.org
curl -I https://example.org
```

3. Stoppe den Mitschnitt.
4. Speichere ihn als:

```text
pcaps/generated/basic-udp-dns-01.pcapng
```

5. Öffne ihn in Wireshark.

Beantworte:

- Welche DNS Query Names siehst du?
- Welche Query Types kommen vor?
- Welche Antworten enthalten IP-Adressen?
- Gibt es NXDOMAIN?
- Wird nach der DNS-Antwort eine TCP-Verbindung zur zurückgegebenen IP aufgebaut?
- Siehst du DNS nur über UDP oder auch über TCP?

## Mini-Aufgabe: DHCP beobachten

Diese Aufgabe hängt von deinem System und Netzwerk ab.

Wenn du ein Lernsystem oder eine VM hast, kannst du versuchen, DHCP-Traffic zu beobachten.

Mögliche Wege:

- Netzwerkverbindung kurz trennen und wieder verbinden
- DHCP Lease erneuern
- VM neu starten
- auf einem Testnetz arbeiten

!!! warning "Vorsicht im produktiven Netz"
    DHCP-Tests können die Netzwerkverbindung beeinflussen.  
    Führe solche Tests nicht unüberlegt auf einem produktiven Arbeitsgerät aus.

Auf Linux kann je nach Netzwerkmanager und Umgebung hilfreich sein:

```bash
nmcli device show
```

oder:

```bash
ip addr
ip route
```

Für echte DHCP-Paketmitschnitte ist ein isoliertes Lab später besser geeignet.

## Analysebericht: DNS-Vorlage

```text
Beobachtung:
Der Client fragt den Namen <name> beim DNS-Server <dns-server> ab.

Relevante Pakete:
Frame <nummer>: DNS Query
Frame <nummer>: DNS Response

Response Code:
<rcode>

Antwortdaten:
<ip-adresse oder keine Antwortdaten>

Bewertung:
Die Namensauflösung ist erfolgreich / fehlerhaft / unvollständig.

Verwendete Filter:
dns
dns.qry.name contains "<name>"
dns.flags.response == 1
```

## Analysebericht: DHCP-Vorlage

```text
Beobachtung:
Im Capture wurde ein DHCP-Ablauf gefunden.

Relevante Pakete:
Frame <nummer>: Discover
Frame <nummer>: Offer
Frame <nummer>: Request
Frame <nummer>: ACK

Zugewiesene Adresse:
<ip-adresse>

DHCP-Server:
<server-ip>

Wichtige Optionen:
Gateway: <gateway>
DNS: <dns-server>
Lease Time: <lease>

Bewertung:
Der Client erhält eine vollständige / unvollständige / fehlerhafte IP-Konfiguration.
```

## Typische Fehlinterpretationen

| Beobachtung | Falscher Schluss | Bessere Bewertung |
|---|---|---|
| UDP hat keine Antwort | Paketverlust | UDP hat keine Verbindung; Kontext prüfen |
| kein DNS sichtbar | keine Namensauflösung | Cache, DoH, DoT oder falscher Capture-Punkt prüfen |
| NXDOMAIN | DNS-Server kaputt | Name existiert laut Server nicht |
| NoError ohne IP | alles okay | Antwort kann leer für den angefragten Typ sein |
| DHCP Discover ohne Offer | Server ist aus | VLAN, Relay, Scope, Capture-Punkt prüfen |
| falsches Gateway per DHCP | Netzwerk kaputt | DHCP-Optionen und Scope prüfen |

## WCA-Bezug

Dieser Abschnitt übt WCA-nahe Grundlagen:

- UDP als Transportprotokoll erkennen
- DNS Query und Response analysieren
- DNS Response Codes bewerten
- DHCP-Abläufe erkennen
- Ports und Protokolle zuordnen
- Display Filter und TShark für UDP-basierte Protokolle nutzen
- Capture-Punkte bei Broadcast, DHCP und DNS richtig bewerten

## Merksatz

> DNS sagt dir, wohin ein Name zeigt.  
> DHCP sagt dir, wie ein Client seine Netzwerkkonfiguration bekommt.  
> UDP transportiert beides schnell und schlank — aber ohne die Sicherheiten von TCP.
