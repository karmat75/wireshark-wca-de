# TCP-Grundlagen

TCP ist eines der wichtigsten Protokolle für Netzwerkanalyse mit Wireshark.

Viele typische Fehlermeldungen wie „Anwendung ist langsam“, „Verbindung bricht ab“ oder „Server nicht erreichbar“ werden erst verständlich, wenn du TCP sicher lesen kannst.

Dieser Abschnitt legt das Fundament.

Die tieferen Themen wie Retransmissions, Duplicate ACKs, SACK, Window Size, RTT und Performanceanalyse kommen später im erweiterten Kurs.

## Ziel

Nach diesem Abschnitt solltest du können:

- TCP-Pakete in Wireshark erkennen
- TCP von UDP unterscheiden
- Quell- und Zielports einordnen
- einen TCP 3-Way Handshake erkennen
- SYN, SYN/ACK, ACK, FIN und RST grundsätzlich verstehen
- TCP Streams in Wireshark verwenden
- einfache TCP-Verbindungsprobleme erkennen
- sinnvolle Display Filter und TShark-Befehle einsetzen

## TCP in einem Satz

TCP steht für Transmission Control Protocol.

TCP ist verbindungsorientiert.

Das bedeutet:

- vor der Datenübertragung wird eine Verbindung aufgebaut
- Pakete werden nummeriert
- empfangene Daten werden bestätigt
- verlorene Daten können erneut übertragen werden
- Verbindungen werden beendet oder abgebrochen

AHA:

> TCP ist nicht einfach „Port 443“. TCP ist die komplette Transportlogik unter vielen Anwendungen.

Typische TCP-basierte Protokolle:

| Protokoll | Typischer Port | Zweck |
|---|---:|---|
| HTTP | 80 | Web ohne TLS |
| HTTPS | 443 | Web mit TLS |
| SSH | 22 | Remote Shell |
| SMTP | 25 | Mail-Transport |
| IMAP | 143 / 993 | Mail-Zugriff |
| RDP | 3389 | Remote Desktop |
| SMB | 445 | Datei- und Windows-Netzwerkfreigaben |
| PostgreSQL | 5432 | Datenbank |
| MS SQL | 1433 | Datenbank |

## TCP in Wireshark

In den Paketdetails findest du TCP als:

```text
Transmission Control Protocol
```

Wichtige Felder:

| Feld | Bedeutung |
|---|---|
| Source Port | Quellport |
| Destination Port | Zielport |
| Stream index | Nummer des TCP-Streams |
| Sequence Number | Sequenznummer |
| Acknowledgment Number | Bestätigungsnummer |
| Header Length | Länge des TCP-Headers |
| Flags | Steuerbits wie SYN, ACK, FIN, RST |
| Window | Empfangsfenster |
| Options | Zusatzinformationen wie MSS, Window Scale, SACK Permitted |

Display Filter:

```text
tcp
```

Bestimmter TCP-Port:

```text
tcp.port == 443
```

Nur Zielport:

```text
tcp.dstport == 443
```

Nur Quellport:

```text
tcp.srcport == 443
```

## Ports verstehen

Ein TCP-Gespräch besteht aus zwei Endpunkten:

```text
Client-IP:Client-Port  ->  Server-IP:Server-Port
```

Beispiel:

```text
192.168.1.50:53124 -> 93.184.216.34:443
```

Hier ist:

| Teil | Bedeutung |
|---|---|
| `192.168.1.50` | Client-IP |
| `53124` | dynamischer Client-Port |
| `93.184.216.34` | Server-IP |
| `443` | Server-Port für HTTPS |

AHA:

> Der Serverport beschreibt meist den Dienst.  
> Der Clientport ist oft nur ein temporärer, dynamischer Port.

## TCP Flags

TCP verwendet Flags, um den Zustand einer Verbindung zu steuern.

Wichtige Flags:

| Flag | Bedeutung |
|---|---|
| SYN | Verbindungsaufbau starten |
| ACK | Daten oder Verbindungszustand bestätigen |
| FIN | Verbindung ordentlich schließen |
| RST | Verbindung hart zurücksetzen |
| PSH | Daten möglichst direkt an Anwendung geben |
| URG | Urgent Pointer relevant, heute selten wichtig |

In Wireshark siehst du Flags häufig in der Info-Spalte:

```text
[SYN]
[SYN, ACK]
[ACK]
[FIN, ACK]
[RST]
```

## Der 3-Way Handshake

Eine normale TCP-Verbindung beginnt mit drei Schritten:

```text
Client -> Server: SYN
Server -> Client: SYN, ACK
Client -> Server: ACK
```

Das ist der 3-Way Handshake.

Er bedeutet:

1. Client möchte eine Verbindung aufbauen.
2. Server bestätigt und möchte ebenfalls synchronisieren.
3. Client bestätigt die Serverantwort.

In Wireshark sieht das ungefähr so aus:

```text
1  Client -> Server  TCP  53124 > 443 [SYN]
2  Server -> Client  TCP  443 > 53124 [SYN, ACK]
3  Client -> Server  TCP  53124 > 443 [ACK]
```

## Handshake-Filter

Nur SYN ohne ACK:

```text
tcp.flags.syn == 1 and tcp.flags.ack == 0
```

SYN/ACK:

```text
tcp.flags.syn == 1 and tcp.flags.ack == 1
```

ACK:

```text
tcp.flags.ack == 1
```

Alle TCP-Pakete mit SYN:

```text
tcp.flags.syn == 1
```

## Was ein erfolgreicher Handshake zeigt

Ein erfolgreicher 3-Way Handshake zeigt:

- Client kann ein SYN zum Server senden
- Server antwortet mit SYN/ACK
- Client sieht die Antwort
- Client bestätigt mit ACK
- der TCP-Port ist grundsätzlich erreichbar

Das beweist aber noch nicht:

- dass die Anwendung korrekt funktioniert
- dass TLS erfolgreich ist
- dass HTTP korrekt antwortet
- dass die Verbindung schnell ist
- dass später keine Paketverluste auftreten

AHA:

> Ein erfolgreicher TCP-Handshake ist ein Anfang, kein vollständiger Anwendungstest.

## Typische Handshake-Fehlerbilder

### SYN ohne Antwort

Beobachtung:

```text
Client -> Server [SYN]
Client -> Server [SYN Retransmission]
Client -> Server [SYN Retransmission]
```

Mögliche Ursachen:

- Ziel nicht erreichbar
- Firewall blockiert
- Routingproblem
- Server offline
- falsche IP
- Capture-Punkt sieht Antwort nicht
- asymmetrisches Routing

### SYN, dann RST

Beobachtung:

```text
Client -> Server [SYN]
Server -> Client [RST, ACK]
```

Mögliche Ursachen:

- Port ist geschlossen
- Dienst lauscht nicht
- Host erreichbar, Dienst aber nicht
- Firewall oder System lehnt aktiv ab

### SYN/ACK sichtbar, aber kein abschließendes ACK

Beobachtung:

```text
Client -> Server [SYN]
Server -> Client [SYN, ACK]
```

aber kein ACK vom Client.

Mögliche Ursachen:

- Client sieht SYN/ACK nicht
- Capture ist unvollständig
- asymmetrisches Routing
- Paketverlust
- Filter zu eng
- Client oder Firewall verwirft Antwort

## Verbindung ordentlich schließen: FIN

Eine TCP-Verbindung kann geordnet beendet werden.

Dazu wird meist `FIN` verwendet.

Typisch:

```text
Client -> Server [FIN, ACK]
Server -> Client [ACK]
Server -> Client [FIN, ACK]
Client -> Server [ACK]
```

Das ist kein Fehler.

Es bedeutet nur:

> Eine Seite möchte keine weiteren Daten mehr senden.

## Verbindung hart abbrechen: RST

`RST` bedeutet Reset.

Ein Reset bricht eine TCP-Verbindung hart ab.

Typische Gründe:

- Port geschlossen
- Anwendung beendet Verbindung abrupt
- Firewall oder Loadbalancer setzt Verbindung zurück
- Paket passt nicht zu einer bestehenden Verbindung
- Client oder Server will sofort abbrechen

Filter:

```text
tcp.flags.reset == 1
```

AHA:

> RST ist nicht automatisch ein Fehler. Es ist ein harter Abbruch. Ob das problematisch ist, hängt vom Kontext ab.

## Sequence Number und ACK Number

TCP nummeriert Daten.

Die Sequence Number sagt vereinfacht:

> Ab welcher Position in meinem Datenstrom sende ich?

Die ACK Number sagt vereinfacht:

> Bis zu welcher Position habe ich Daten vom anderen Ende erhalten?

Wireshark zeigt standardmäßig oft relative Sequenznummern.

Das ist für Menschen lesbarer.

Beispiel:

```text
Seq=0 Ack=0
Seq=1 Ack=1
```

Die echten Werte sind viel größer, aber für die Analyse ist die relative Darstellung meist einfacher.

!!! note "Relative Sequenznummern"
    Wireshark zeigt standardmäßig relative Sequence Numbers.  
    Das ist gewollt und erleichtert die Analyse. Die echten Nummern sind weiterhin im Paket ableitbar.

## TCP Stream

Ein TCP Stream ist in Wireshark eine zusammengehörige TCP-Verbindung.

Filter:

```text
tcp.stream == 0
```

oder:

```text
tcp.stream == 1
```

Die Nummer hängt vom Capture ab.

Du findest sie im Paketdetailbereich unter TCP:

```text
Stream index
```

Oder über Rechtsklick:

```text
Follow > TCP Stream
```

## Follow TCP Stream

`Follow TCP Stream` zeigt die Nutzdaten einer TCP-Verbindung zusammenhängend an.

Das ist besonders hilfreich bei unverschlüsselten Protokollen wie HTTP.

Bei HTTPS siehst du dort normalerweise nur verschlüsselte Daten.

AHA:

> Follow TCP Stream ist stark, aber Verschlüsselung bleibt Verschlüsselung.

Nutze Follow TCP Stream vorsichtig bei echten Captures, weil dort sensible Daten sichtbar werden können.

## TCP und TLS

HTTPS ist kein eigenes Transportprotokoll.

Vereinfacht:

```text
HTTP
in TLS
in TCP
in IP
in Ethernet
```

In Wireshark siehst du bei HTTPS also zunächst TCP und dann TLS.

Filter:

```text
tcp.port == 443
```

```text
tls
```

Wenn du HTTP-Inhalte nicht lesen kannst, ist das bei HTTPS normal.

## TCP und „Connection refused“

Wenn ein Client „Connection refused“ meldet, sieht man im Capture oft:

```text
SYN
RST, ACK
```

Das bedeutet meistens:

- Zielhost erreichbar
- TCP-Antwort kommt zurück
- der angefragte Port wird aktiv abgelehnt

Das unterscheidet sich von einem Timeout.

## TCP und Timeout

Bei einem Timeout sieht man oft:

```text
SYN
SYN Retransmission
SYN Retransmission
```

aber keine Antwort.

Das bedeutet nicht automatisch, dass der Server aus ist.

Es bedeutet:

> Am Capture-Punkt ist keine passende Antwort sichtbar.

Mögliche Ursachen:

- Firewall droppt
- Routingproblem
- Server antwortet auf anderem Weg
- falscher Capture-Punkt
- Zielsystem offline

## Wichtige Display Filter

Alle TCP-Pakete:

```text
tcp
```

TCP-Port 443:

```text
tcp.port == 443
```

Nur SYN ohne ACK:

```text
tcp.flags.syn == 1 and tcp.flags.ack == 0
```

SYN/ACK:

```text
tcp.flags.syn == 1 and tcp.flags.ack == 1
```

RST:

```text
tcp.flags.reset == 1
```

FIN:

```text
tcp.flags.fin == 1
```

Bestimmter Stream:

```text
tcp.stream == 0
```

TCP-Analysehinweise von Wireshark:

```text
tcp.analysis.flags
```

!!! note "tcp.analysis.flags"
    Dieser Filter zeigt Pakete, bei denen Wireshark Analysehinweise setzt.  
    Das ist hilfreich, aber nicht jede Analysemarkierung ist automatisch ein Fehler. Kontext bleibt wichtig.

## TShark-Beispiele

Alle TCP-Pakete zählen:

```bash
tshark -r pcaps/generated/basic-capture-01.pcapng -Y "tcp" | wc -l
```

SYN ohne ACK ausgeben:

```bash
tshark -r pcaps/generated/basic-capture-01.pcapng \
  -Y "tcp.flags.syn == 1 and tcp.flags.ack == 0" \
  -T fields \
  -e frame.number \
  -e ip.src \
  -e tcp.srcport \
  -e ip.dst \
  -e tcp.dstport
```

RST-Pakete ausgeben:

```bash
tshark -r pcaps/generated/basic-capture-01.pcapng \
  -Y "tcp.flags.reset == 1" \
  -T fields \
  -e frame.number \
  -e ip.src \
  -e tcp.srcport \
  -e ip.dst \
  -e tcp.dstport
```

TCP Streams anzeigen:

```bash
tshark -r pcaps/generated/basic-capture-01.pcapng \
  -Y "tcp" \
  -T fields \
  -e tcp.stream \
  -e ip.src \
  -e tcp.srcport \
  -e ip.dst \
  -e tcp.dstport | sort -u
```

## Mini-Aufgabe

Erzeuge einen kleinen Capture.

1. Starte Wireshark oder TShark.
2. Führe aus:

```bash
curl -I https://example.org
curl -I http://example.org
```

3. Stoppe den Mitschnitt.
4. Speichere ihn als:

```text
pcaps/generated/basic-tcp-01.pcapng
```

5. Öffne ihn in Wireshark.

Beantworte:

- Welche TCP-Verbindungen siehst du?
- Welche Zielports werden verwendet?
- Findest du den 3-Way Handshake?
- Welche Pakete enthalten SYN?
- Welche Pakete enthalten SYN/ACK?
- Gibt es FIN oder RST?
- Welche `tcp.stream`-Nummern gehören zu den Verbindungen?
- Kannst du bei HTTP einen TCP Stream folgen?
- Was siehst du bei HTTPS im Stream?

## Mini-Aufgabe: geschlossener Port

Diese Aufgabe kann je nach Zielsystem unterschiedlich reagieren.

Teste auf einem ungefährlichen Ziel, zum Beispiel gegen localhost:

```bash
curl -v http://127.0.0.1:9
```

Port 9 ist auf vielen Systemen nicht offen.

Mögliche Beobachtung:

- RST
- Connection refused
- keine Antwort, abhängig von lokaler Firewall

Filter:

```text
tcp.flags.reset == 1
```

oder:

```text
tcp.port == 9
```

!!! warning "Keine Portscans gegen fremde Systeme"
    Für diesen Kurs testen wir nur gegen eigene Systeme, localhost oder explizit freigegebene Lab-Umgebungen.

## Analysebericht: TCP-Handshake

```text
Beobachtung:
Der Client baut eine TCP-Verbindung zu <server-ip>:<port> auf.

Relevante Pakete:
Frame <nummer>: SYN vom Client
Frame <nummer>: SYN/ACK vom Server
Frame <nummer>: ACK vom Client

Bewertung:
Der TCP 3-Way Handshake ist erfolgreich. Der Zielport ist grundsätzlich erreichbar.

Verwendete Filter:
tcp.stream == <nummer>
tcp.flags.syn == 1
```

## Analysebericht: TCP-Reset

```text
Beobachtung:
Der Server antwortet auf den Verbindungsversuch mit RST/ACK.

Relevante Pakete:
Frame <nummer>: SYN vom Client
Frame <nummer>: RST/ACK vom Server

Bewertung:
Das Zielsystem ist erreichbar, lehnt den angefragten TCP-Port aber aktiv ab. Der Dienst lauscht wahrscheinlich nicht oder eine Komponente setzt die Verbindung zurück.

Verwendete Filter:
tcp.flags.reset == 1
tcp.port == <port>
```

## Typische Fehlinterpretationen

| Beobachtung | Falscher Schluss | Bessere Bewertung |
|---|---|---|
| SYN sichtbar | Verbindung steht | erst SYN/ACK und ACK prüfen |
| SYN ohne Antwort | Server ist aus | Capture-Punkt, Firewall und Routing prüfen |
| RST sichtbar | Netzwerk kaputt | Ziel oder Zwischenkomponente lehnt aktiv ab |
| erfolgreicher Handshake | Anwendung funktioniert | nur TCP-Port ist erreichbar |
| kein HTTP bei HTTPS | Wireshark funktioniert nicht | Inhalt ist durch TLS verschlüsselt |
| tcp.analysis.flags | sicherer Fehler | Analysehinweis im Kontext bewerten |

## WCA-Bezug

Dieser Abschnitt übt WCA-nahe Grundlagen:

- TCP als Transportprotokoll erkennen
- Ports und Services zuordnen
- TCP Flags lesen
- 3-Way Handshake erkennen
- Verbindungsaufbau und Abbruch unterscheiden
- TCP Streams verwenden
- Display Filter und TShark für TCP einsetzen
- erste TCP-Fehlerbilder bewerten

## Merksatz

> TCP sagt dir nicht nur, dass zwei Systeme miteinander sprechen.  
> TCP zeigt dir, ob sie eine Verbindung aufbauen, bestätigen, schließen, abbrechen oder auf Antwort warten.
