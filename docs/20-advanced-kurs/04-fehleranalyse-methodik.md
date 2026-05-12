# Fehleranalyse-Methodik

Wireshark zeigt Pakete.

Die Analyse entsteht aber nicht automatisch dadurch, dass man viele Pakete sieht.

Gute Netzwerkanalyse ist eine Methode:

- Problem sauber beschreiben
- Capture-Punkt bewusst wählen
- relevante Pakete finden
- Beobachtungen belegen
- Hypothesen prüfen
- Alternativen ausschließen
- Ergebnis verständlich dokumentieren

Dieser Abschnitt verbindet die bisherigen technischen Kapitel zu einer strukturierten Vorgehensweise.

## Ziel

Nach diesem Abschnitt solltest du können:

- ein unscharfes Symptom in prüfbare Fragen übersetzen
- Capture-Punkte bewusst auswählen
- Beobachtung, Bewertung und Ursache trennen
- Hypothesen mit Paketen prüfen
- Frame-Nummern und Filter als Belege nutzen
- Netzwerk-, Client-, Server- und Applikationsprobleme abgrenzen
- Analyseberichte nachvollziehbar formulieren
- typische Denkfehler vermeiden

## Der wichtigste Unterschied

Es gibt drei Ebenen:

| Ebene | Beispiel |
|---|---|
| Symptom | „Die Anwendung ist langsam.“ |
| Beobachtung | „Zwischen HTTP Request und erster Response liegen 4,2 Sekunden.“ |
| Bewertung | „Im Capture sind keine Retransmissions sichtbar. Die Wartezeit entsteht wahrscheinlich nach Eingang der Anfrage am Server oder im Backend.“ |

AHA:

> Eine Beobachtung ist etwas, das du im Capture belegen kannst.  
> Eine Bewertung ist deine fachliche Einordnung dieser Beobachtung.

Vermische diese Ebenen nicht.

## Gute Analyse beginnt vor dem Capture

Bevor du Wireshark öffnest, kläre:

- Wer meldet das Problem?
- Wann tritt es auf?
- Seit wann tritt es auf?
- Ist es reproduzierbar?
- Betrifft es einen Benutzer, mehrere Benutzer oder alle?
- Betrifft es eine Anwendung oder viele?
- Gibt es ein funktionierendes Gegenbeispiel?
- Welche Systeme sind beteiligt?
- Welche IPs, Namen und Ports sind relevant?
- Wo kann sinnvoll mitgeschnitten werden?

Je besser diese Fragen beantwortet sind, desto gezielter wird der Capture.

## Aus Symptomen werden Analysefragen

Schlecht:

```text
Netzwerk prüfen.
```

Besser:

```text
Kommt der Client per TCP bis zum Server auf Port 443?
```

Noch besser:

```text
Ist im Client-Capture ein vollständiger TCP Handshake zu 10.20.30.40:443 sichtbar, und wie lange dauert er?
```

Weitere Beispiele:

| Symptom | Analysefrage |
|---|---|
| Webseite lädt nicht | Gibt es DNS, TCP, TLS und eine Serverantwort? |
| Login langsam | Wo entsteht Wartezeit: DNS, TCP, TLS, Serverantwort oder Datenübertragung? |
| Verbindung bricht ab | Wer sendet FIN oder RST? |
| Client bekommt keine IP | Gibt es DHCP Discover, Offer, Request und ACK? |
| Name wird nicht gefunden | Welcher DNS Response Code kommt zurück? |
| Download langsam | Gibt es Retransmissions, Window-Probleme oder Serverpausen? |

## Capture-Punkt bewusst wählen

Der Capture-Punkt bestimmt, welche Aussage möglich ist.

| Capture-Punkt | Aussage |
|---|---|
| Client | „Aus Sicht des Clients passiert X.“ |
| Server | „Aus Sicht des Servers kommt X an oder wird X gesendet.“ |
| Gateway | „Am Übergang zwischen Netzen ist X sichtbar.“ |
| Firewall | „Vor oder nach Regelwerk/NAT ist X sichtbar.“ |
| Mirror/TAP | „An diesem Netzwerkpunkt ist X sichtbar.“ |

AHA:

> Ein Capture beweist immer nur, was an diesem Punkt sichtbar war.

Wenn ein Paket im Client-Capture fehlt, kann das bedeuten:

- Paket wurde nicht gesendet
- Paket wurde vorher verworfen
- Paket kam auf anderem Weg zurück
- Capture hat es nicht erfasst
- Filter blendet es aus
- falsches Interface wurde gewählt

## Ein Capture ist kein Weltbild

Ein Capture ist eine Perspektive.

Deshalb gehört in jeden Analysebericht:

```text
Capture-Punkt:
Client / Server / Gateway / Firewall / Mirror / unbekannt
```

und wenn möglich:

```text
Interface:
wlp2s0 / eth0 / any / mirror-port / ...
```

Ohne Capture-Punkt ist die Aussage oft zu stark.

Schlecht:

```text
Der Server antwortet nicht.
```

Besser:

```text
Im Client-Capture ist auf drei SYN-Pakete zu 10.20.30.40:443 keine SYN/ACK-Antwort sichtbar.
```

Das ist präziser und ehrlicher.

## Methodik: Vom Groben zum Konkreten

Eine bewährte Reihenfolge:

1. Capture-Punkt und Zeitraum prüfen
2. relevante Endpunkte identifizieren
3. DNS prüfen
4. Layer 3 prüfen
5. TCP oder UDP prüfen
6. TLS oder Anwendung prüfen
7. Zeitverhalten prüfen
8. Analysehinweise prüfen
9. alternative Erklärungen prüfen
10. Ergebnis formulieren

Nicht sofort mit dem auffälligsten roten Paket beginnen.

## Grobe Orientierung im Capture

Nutze zuerst:

```text
Statistics > Protocol Hierarchy
```

```text
Statistics > Conversations
```

```text
Statistics > Endpoints
```

```text
Analyze > Expert Information
```

Diese Ansichten helfen bei der Orientierung.

Sie ersetzen aber nicht die Paketprüfung.

AHA:

> Statistiken zeigen dir, wo du suchen kannst. Die Pakete zeigen dir, was passiert ist.

## Relevante Endpunkte finden

Typische Wege:

- DNS-Namen aus dem Symptom ableiten
- IP-Adresse per DNS finden
- Conversations nach großem Traffic sortieren
- TCP Streams prüfen
- bekannte Ports filtern
- Client-IP als Ausgangspunkt nehmen

Beispiele:

```text
ip.addr == <client-ip>
```

```text
dns.qry.name contains "<name>"
```

```text
tcp.port == 443
```

```text
tcp.stream == <nummer>
```

## Hypothesen bilden

Eine Hypothese ist eine prüfbare Vermutung.

Schlecht:

```text
Die Firewall ist schuld.
```

Besser:

```text
Die Firewall könnte TCP 443 blockieren. Im Client-Capture würde ich dann SYN-Pakete ohne SYN/ACK erwarten oder eine aktive Ablehnung sehen.
```

Gute Hypothesen enthalten:

- vermutete Ursache
- erwartbares Paketmuster
- Gegenbeweis

Beispiel:

```text
Hypothese:
DNS ist die Ursache.

Erwartung:
DNS Query ist sichtbar, aber keine Antwort oder ein Fehler-RCODE.

Prüfung:
Filter `dns` und `dns.flags.rcode != 0`.

Gegenbeweis:
DNS Response enthält passende IP, danach startet TCP-Verbindung.
```

## Beobachtung vs. Ursache

Nicht jede Beobachtung ist schon eine Ursache.

Beispiele:

| Beobachtung | Mögliche Ursache |
|---|---|
| SYN ohne Antwort | Firewall, Routing, Server down, Capture-Punkt, asymmetrischer Weg |
| RST vom Server | Port geschlossen, Dienst lehnt ab, Loadbalancer, Policy |
| Retransmissions | Paketverlust, ACK-Verlust, Capture-Lücke, Überlast |
| Zero Window | Empfängeranwendung liest nicht schnell genug |
| DNS NXDOMAIN | Name existiert nicht, falscher DNS, falsche Suchdomäne |
| HTTP 500 | Anwendung oder Backendfehler |

AHA:

> Wireshark zeigt häufig das Symptom der Ursache, nicht die Ursache selbst.

## Belege mit Frame-Nummern

Eine belastbare Analyse nennt Frame-Nummern.

Schlecht:

```text
Es gab Retransmissions.
```

Besser:

```text
Im Stream `tcp.stream == 4` sind Retransmissions in Frame 128, 145 und 169 sichtbar.
```

Noch besser:

```text
Frame 120 bis 169 zeigen wiederholte Duplicate ACKs für dieselbe ACK Number, gefolgt von einer Fast Retransmission in Frame 169.
```

Frame-Nummern machen deine Analyse überprüfbar.

## Filter dokumentieren

Dokumentiere verwendete Filter.

Beispiele:

```text
dns
dns.flags.rcode != 0
tcp.stream == 4
tcp.analysis.retransmission
tcp.flags.reset == 1
tls.alert_message
```

Warum?

- andere können deine Analyse nachvollziehen
- du kannst später selbst zurückfinden
- Filter zeigen, wie du zur Beobachtung gekommen bist
- es verhindert Bauchgefühl-Diagnosen

## TShark als Belegmaschine

TShark ist stark, um Ergebnisse reproduzierbar auszugeben.

Beispiel: TCP-Analysehinweise mit Frame-Nummern:

```bash
tshark -r capture.pcapng \
  -Y "tcp.analysis.flags" \
  -T fields \
  -e frame.number \
  -e frame.time_relative \
  -e tcp.stream \
  -e ip.src \
  -e ip.dst \
  -e _ws.col.Info
```

DNS-Fehler:

```bash
tshark -r capture.pcapng \
  -Y "dns.flags.response == 1 and dns.flags.rcode != 0" \
  -T fields \
  -e frame.number \
  -e frame.time_relative \
  -e ip.src \
  -e ip.dst \
  -e dns.qry.name \
  -e dns.flags.rcode
```

HTTP-Statuscodes:

```bash
tshark -r capture.pcapng \
  -Y "http.response" \
  -T fields \
  -e frame.number \
  -e frame.time_relative \
  -e http.response.code \
  -e http.response.phrase
```

## Schichtenorientierte Analyse

Nutze das OSI-/TCP-IP-Modell als Ordnungshilfe.

### Layer 2

Fragen:

- Gibt es Ethernet?
- Gibt es ARP?
- Ist das Gateway per MAC erreichbar?
- Sind VLAN-Tags sichtbar oder nicht sichtbar?
- Ist Broadcast/Multicast auffällig?

Filter:

```text
arp
eth.addr == <mac>
vlan
```

### Layer 3

Fragen:

- Stimmen Quell- und Ziel-IP?
- Gibt es ICMP-Fehler?
- Gibt es Fragmentierung?
- Ist NAT relevant?
- Ist der Weg plausibel?

Filter:

```text
ip.addr == <ip>
icmp
icmpv6
ip.flags.mf == 1 or ip.frag_offset > 0
```

### Layer 4

Fragen:

- Gibt es TCP Handshake?
- Gibt es UDP-Anfrage und Antwort?
- Gibt es RST?
- Gibt es Retransmissions?
- Gibt es Window-Probleme?

Filter:

```text
tcp
udp
tcp.stream == <nummer>
tcp.analysis.flags
tcp.flags.reset == 1
```

### Anwendung

Fragen:

- Gibt es DNS?
- Gibt es HTTP Statuscodes?
- Gibt es TLS Alerts?
- Ist der Inhalt verschlüsselt?
- Antwortet die Anwendung langsam oder fehlerhaft?

Filter:

```text
dns
http
tls
tls.alert_message
```

## Entscheidungsbaum: Webanwendung lädt nicht

```text
Start
 |
 |-- DNS sichtbar?
 |      |-- nein: Cache/DoH/DoT/Capture-Punkt prüfen
 |      |-- ja: Response Code und Antwortdaten prüfen
 |
 |-- TCP Handshake zum Ziel sichtbar?
 |      |-- nein: SYN/SYN-ACK/RST/Timeout prüfen
 |      |-- ja: weiter
 |
 |-- TLS Handshake sichtbar?
 |      |-- nein: Port/Protokoll/Abbruch prüfen
 |      |-- ja: Alerts und Application Data prüfen
 |
 |-- HTTP sichtbar?
 |      |-- ja: Statuscode, Header, Redirects prüfen
 |      |-- nein: bei HTTPS normal, Zeitverhalten prüfen
 |
 |-- TCP-Auffälligkeiten?
        |-- Retransmissions/Dup ACK/Zero Window prüfen
        |-- keine: Server-/Anwendungszeit prüfen
```

## Abgrenzung: Netzwerk, Client, Server, Anwendung

Eine gute Analyse sagt nicht nur „geht nicht“, sondern grenzt ein.

### Eher Netzwerk / Transport

Hinweise:

- SYN ohne Antwort
- ICMP Destination Unreachable
- viele Retransmissions
- Duplicate ACKs mit Fast Retransmit
- Fragmentation Needed
- starke RTT-Schwankungen
- asymmetrische Sicht

### Eher Server / Dienst

Hinweise:

- SYN/ACK kommt zurück, aber später RST vom Server
- TCP Handshake erfolgreich, aber Anwendung antwortet spät
- HTTP 500
- TLS Alert vom Server
- Server sendet Zero Window

### Eher Client

Hinweise:

- Client sendet keinen Request nach erfolgreichem Handshake
- Client schließt Verbindung früh
- Client sendet RST
- Client nutzt falschen DNS-Server
- Client fragt falschen Namen
- Client kann Daten nicht aufnehmen

### Eher Anwendung / Backend

Hinweise:

- Request kommt an, Antwort kommt spät
- HTTP 4xx oder 5xx
- TLS und TCP sauber, aber Anwendung liefert Fehler
- kleine Datenmengen, aber lange Pausen
- Backend-spezifische Fehler in Antwort sichtbar

## Der Satz „Das Netzwerk ist es nicht“

Diesen Satz solltest du vorsichtig verwenden.

Besser:

```text
Im vorliegenden Client-Capture sind keine Hinweise auf TCP-Retransmissions, Paketverlust oder Verbindungsabbrüche sichtbar. DNS, TCP Handshake und TLS Handshake erfolgen ohne erkennbare Verzögerung. Die beobachtete Wartezeit liegt zwischen Request und erster Serverantwort.
```

Das ist präziser und belastbarer.

AHA:

> Formuliere, was der Capture zeigt. Nicht mehr und nicht weniger.

## Negative Beweise sind schwierig

Wenn du etwas nicht siehst, kann das mehrere Gründe haben:

- es ist wirklich nicht passiert
- du schneidest am falschen Punkt mit
- der Filter blendet es aus
- Capture ist unvollständig
- Traffic ist verschlüsselt
- Traffic läuft über anderes Interface
- Traffic lief vor oder nach dem Capture

Schlecht:

```text
Es gibt kein DNS.
```

Besser:

```text
Im vorliegenden Client-Capture sind während des analysierten Zeitfensters keine klassischen DNS-Pakete auf UDP/TCP 53 sichtbar.
```

Das lässt Raum für Cache, DoH, DoT oder falschen Capture-Punkt.

## Mehrere Captures vergleichen

Manchmal brauchst du zwei Captures:

- Client und Server gleichzeitig
- vor und nach Firewall
- funktionierender und fehlerhafter Fall
- vor und nach Änderung
- internes und externes Netz

Wichtig:

- Uhren synchronisieren
- gleiche Testaktion ausführen
- Start- und Endzeit notieren
- Capture-Punkte dokumentieren
- gleiche Filter verwenden

AHA:

> Zwei mittelmäßige Captures mit guter Dokumentation sind oft wertvoller als ein riesiger Capture ohne Kontext.

## Zeitstempel und Uhren

Wenn du mehrere Captures vergleichst, sind Zeitstempel wichtig.

Prüfe:

- sind Systeme per NTP synchron?
- welche Zeitzone wird angezeigt?
- nutzt Wireshark relative oder absolute Zeit?
- ist die Capture-Zeit plausibel?
- gibt es Lücken im Capture?

Für Analyseberichte ist oft gut:

```text
Frame-Zeit relativ zum Capture-Start: 12,345 Sekunden
```

und bei Log-Abgleich:

```text
UTC-Zeit: 2026-...
```

## Saubere Sprache im Analysebericht

Vermeide absolute Aussagen, wenn der Capture sie nicht belegt.

Schlecht:

```text
Die Firewall blockiert.
```

Besser:

```text
Im Client-Capture sind wiederholte SYN-Pakete zum Zielport sichtbar, aber keine SYN/ACK-Antwort. Das Muster passt zu Drop durch Firewall, Routingproblem, nicht erreichbarem Ziel oder unvollständiger Capture-Sicht.
```

Schlecht:

```text
Der Server ist langsam.
```

Besser:

```text
Zwischen HTTP Request in Frame 120 und erster HTTP Response in Frame 148 liegen 3,8 Sekunden. Im gleichen TCP Stream sind keine Retransmissions sichtbar. Das spricht eher für Verzögerung auf Server-/Anwendungsseite als für sichtbaren Paketverlust im Netzwerk.
```

## Minimaler Analysebericht

```text
Symptom:
<was wurde gemeldet?>

Zeitpunkt:
<wann trat es auf?>

Capture-Punkt:
<wo wurde mitgeschnitten?>

Beteiligte Systeme:
Client: <ip/name>
Server: <ip/name>
Port/Protokoll: <port/protokoll>

Beobachtungen:
- Frame <nummer>: <Beobachtung>
- Frame <nummer>: <Beobachtung>
- Frame <nummer>: <Beobachtung>

Verwendete Filter:
<filter>

Bewertung:
<fachliche Einordnung>

Einschränkungen:
<was zeigt der Capture nicht?>

Nächster sinnvoller Schritt:
<was sollte als nächstes geprüft werden?>
```

## Ausführlicher Analysebericht

```text
## Zusammenfassung

<kurze Management-/Operations-taugliche Aussage>

## Ausgangslage

Symptom:
Betroffene Benutzer/Systeme:
Zeitfenster:
Erwartetes Verhalten:
Tatsächliches Verhalten:

## Capture-Informationen

Datei:
Capture-Punkt:
Interface:
Start/Ende:
Besonderheiten:

## Analyse

### DNS

Beobachtung:
Frames:
Filter:
Bewertung:

### TCP/UDP

Beobachtung:
Frames:
Filter:
Bewertung:

### TLS/Anwendung

Beobachtung:
Frames:
Filter:
Bewertung:

### Performance

Beobachtung:
Frames/Zeitbereiche:
Filter/Graph:
Bewertung:

## Gesamtbewertung

<was ist wahrscheinlich?>
<was ist unwahrscheinlich?>
<was ist nicht belegbar?>

## Empfehlungen

1. <nächster Schritt>
2. <nächster Schritt>
3. <nächster Schritt>
```

## Typische Denkfehler

| Denkfehler | Warum problematisch |
|---|---|
| „Wireshark zeigt rot, also Fehler“ | Farben und Expert Infos sind Hinweise |
| „Ich sehe kein Paket, also wurde keins gesendet“ | falscher Capture-Punkt oder Filter möglich |
| „Ping geht, also Netzwerk ok“ | ICMP beweist nicht TCP/TLS/HTTP |
| „Retransmission bedeutet Netzwerk schuld“ | Capture-Lücken oder ACK-Verlust möglich |
| „HTTP 500 ist Netzwerkproblem“ | Anwendung hat geantwortet |
| „Kein DNS sichtbar, also kein DNS“ | Cache, DoH, DoT, falscher Zeitpunkt |
| „Ein Capture reicht immer“ | manchmal braucht es Client- und Server-Sicht |

## Mini-Aufgabe: Symptom übersetzen

Formuliere aus diesen Symptomen je zwei prüfbare Analysefragen:

1. „Webseite ist langsam.“
2. „Client bekommt keine IP.“
3. „SSH geht nicht.“
4. „Login dauert ewig.“
5. „Nur Standort A hat Probleme.“

Beispiel:

```text
Symptom:
SSH geht nicht.

Analysefrage 1:
Ist ein TCP SYN vom Client zum Server auf Port 22 sichtbar?

Analysefrage 2:
Antwortet der Server mit SYN/ACK, RST oder gar nicht?
```

## Mini-Aufgabe: Bericht aus Capture

Nutze einen vorhandenen Capture aus den vorherigen Übungen.

Erstelle einen kurzen Analysebericht mit:

- Symptom
- Capture-Punkt
- beteiligte IPs
- relevante Frames
- verwendete Filter
- Bewertung
- Einschränkungen
- nächster Schritt

Wichtig:

> Schreibe nicht mehr, als der Capture belegt.

## TShark-Checkliste

Nützliche Startbefehle:

Protocol Overview grob über Wireshark-GUI:

```text
Statistics > Protocol Hierarchy
```

TCP Streams per TShark:

```bash
tshark -r capture.pcapng \
  -Y "tcp" \
  -T fields \
  -e tcp.stream \
  -e ip.src \
  -e tcp.srcport \
  -e ip.dst \
  -e tcp.dstport | sort -u
```

DNS-Fehler:

```bash
tshark -r capture.pcapng \
  -Y "dns.flags.response == 1 and dns.flags.rcode != 0"
```

TCP-Analysehinweise:

```bash
tshark -r capture.pcapng \
  -Y "tcp.analysis.flags"
```

Resets:

```bash
tshark -r capture.pcapng \
  -Y "tcp.flags.reset == 1"
```

TLS Alerts:

```bash
tshark -r capture.pcapng \
  -Y "tls.alert_message"
```

HTTP-Fehler:

```bash
tshark -r capture.pcapng \
  -Y "http.response.code >= 400"
```

## WCA-Bezug

Dieser Abschnitt übt WCA-nahe Fähigkeiten:

- Analyse strukturiert aufbauen
- Capture-Punkte bewerten
- Protokolle und Schichten einordnen
- Filter und Frame-Nummern als Belege verwenden
- Wireshark-Statistiken und Expert Informationen sinnvoll nutzen
- TCP-, DNS-, HTTP- und TLS-Beobachtungen fachlich einordnen
- reproduzierbare TShark-Auswertungen verwenden
- Aussagen auf das begrenzen, was der Capture wirklich zeigt

## Merksatz

> Gute Wireshark-Analyse ist nicht: „Ich habe ein auffälliges Paket gefunden.“  
> Gute Wireshark-Analyse ist: „Ich kann zeigen, was passiert ist, wo ich es gesehen habe und welche Schlussfolgerung daraus belastbar ist.“
