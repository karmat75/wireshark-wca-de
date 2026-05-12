# Performanceanalyse

Performanceanalyse mit Wireshark beginnt selten mit einer fertigen Antwort.

Meist beginnt sie mit einer unscharfen Aussage:

```text
Die Anwendung ist langsam.
```

Das ist als Symptom verständlich, aber für Analyse noch zu ungenau.

Wireshark hilft dir, dieses Symptom in messbare Abschnitte zu zerlegen:

- DNS-Auflösung
- TCP-Verbindungsaufbau
- TLS-Handshake
- Anwendungsanfrage
- Serverantwortzeit
- Datenübertragung
- Paketverlust
- Window-Probleme
- Client- oder Serververzögerung

## Ziel

Nach diesem Abschnitt solltest du können:

- „langsam“ in messbare Bestandteile zerlegen
- DNS-, TCP-, TLS- und Anwendungszeit unterscheiden
- Round Trip Time grob einschätzen
- Retransmissions und Paketverlust in Performancekontext setzen
- Zero Window und Window Update bewerten
- I/O Graphs und TCP Stream Graphs nutzen
- Capture-Punkt und Baseline berücksichtigen
- Analyseergebnisse nachvollziehbar dokumentieren

## Die wichtigste Regel

> „Langsam“ ist keine Ursache. „Langsam“ ist ein Symptom.

Bevor du analysierst, brauchst du eine genauere Frage.

Schlecht:

```text
Warum ist die Anwendung langsam?
```

Besser:

```text
Wo entsteht die Wartezeit zwischen DNS-Auflösung, TCP-Handshake, TLS-Handshake, Request und Response?
```

Noch besser:

```text
Der Client wartet nach dem HTTP Request etwa 2,8 Sekunden auf die erste Serverantwort. Im gleichen Stream sind keine Retransmissions sichtbar.
```

## Performance ist eine Zeitfrage

Für Performanceanalyse ist die Zeitachse entscheidend.

In Wireshark solltest du deshalb bewusst mit Zeitdarstellung arbeiten.

Menü:

```text
View > Time Display Format
```

Nützliche Optionen:

| Option | Nutzen |
|---|---|
| Seconds Since Beginning of Capture | gut für Ablaufanalyse |
| Seconds Since Previous Captured Packet | zeigt Abstand zum vorherigen Paket |
| Seconds Since Previous Displayed Packet | zeigt Abstand zum vorherigen angezeigten Paket |
| UTC Date and Time of Day | gut für Abgleich mit Logs |

AHA:

> Für Performanceanalyse ist `Displayed Packet` oft nützlicher als `Captured Packet`, wenn du mit Filtern arbeitest.

## Capture-Punkt festhalten

Performance sieht je nach Capture-Punkt unterschiedlich aus.

| Capture-Punkt | Was du gut sehen kannst |
|---|---|
| Client | Benutzerperspektive, DNS, Verbindungsaufbau, Wartezeit |
| Server | Ankunft der Anfrage, Serverantwort, lokale Verzögerung |
| Gateway/Firewall | Übergang zwischen Netzen, NAT, Drops, Verzögerungen |
| Mirror Port | Netzsicht, aber abhängig von Spiegelung und Richtung |
| TAP | saubere Netzsicht, aber nicht immer verfügbar |

Ein Client-Capture kann zeigen:

> Aus Sicht des Clients kam die Antwort spät.

Ein Server-Capture kann zeigen:

> Die Anfrage kam spät an oder der Server hat spät geantwortet.

Beides sind unterschiedliche Aussagen.

## Baseline statt Bauchgefühl

Ohne Vergleich ist „langsam“ schwer zu bewerten.

Eine Baseline beantwortet:

> Wie sieht es aus, wenn es normal funktioniert?

Beispiele:

| Messpunkt | Normalfall | Problemfall |
|---|---:|---:|
| DNS-Antwort | 5 ms | 1200 ms |
| TCP-Handshake | 20 ms | 800 ms |
| TLS-Handshake | 50 ms | 2 s |
| Serverantwort nach Request | 80 ms | 5 s |
| Download | 40 MB/s | 500 KB/s |

Du brauchst nicht immer perfekte Werte.

Aber du brauchst Vergleichswerte, Logs oder wiederholbare Tests.

## Analyse-Reihenfolge bei langsamer Webanwendung

Für HTTP/HTTPS ist diese Reihenfolge hilfreich:

1. DNS prüfen
2. TCP Handshake prüfen
3. TLS Handshake prüfen
4. Request finden
5. erste Serverantwort finden
6. Datenübertragung bewerten
7. TCP-Analysehinweise prüfen
8. Window-Probleme prüfen
9. Capture-Punkt bewerten
10. Ergebnis formulieren

AHA:

> Bei Webproblemen ist die Frage oft nicht „Netz oder Anwendung?“, sondern „welcher Abschnitt der Verbindung kostet Zeit?“

## DNS-Zeit

DNS kann ein großer Teil gefühlter Wartezeit sein.

Filter:

```text
dns
```

Nur Anfragen:

```text
dns.flags.response == 0
```

Nur Antworten:

```text
dns.flags.response == 1
```

Ablauf:

1. DNS Query finden
2. passende DNS Response finden
3. Zeitdifferenz prüfen
4. Response Code und Antwortdaten bewerten

Mögliche Beobachtungen:

- schnelle Antwort mit IP
- verzögerte Antwort
- mehrere DNS-Server werden gefragt
- NXDOMAIN
- SERVFAIL
- erst IPv6, dann IPv4
- keine DNS-Pakete sichtbar, weil Cache oder DoH/DoT

## TCP-Handshake-Zeit

Ein TCP-Handshake zeigt, wie schnell der Verbindungsaufbau auf Transportebene klappt.

Filter für SYN ohne ACK:

```text
tcp.flags.syn == 1 and tcp.flags.ack == 0
```

Filter für SYN/ACK:

```text
tcp.flags.syn == 1 and tcp.flags.ack == 1
```

Im Stream:

```text
tcp.stream == <nummer>
```

Messpunkt:

```text
Zeit zwischen SYN und SYN/ACK
```

Das ist grob ein Hinweis auf Round Trip Time und Erreichbarkeit.

AHA:

> Wenn der TCP-Handshake schon langsam ist, brauchst du die Anwendung noch nicht zu beschuldigen.

## Round Trip Time

Round Trip Time, kurz RTT, ist die Zeit für Hin- und Rückweg.

In TCP-Analysen ist RTT wichtig, weil sie beeinflusst:

- Handshake-Dauer
- ACK-Verhalten
- Durchsatz
- Retransmission-Timer
- gefühlte Reaktionszeit

Wireshark kann RTT-Schätzungen anzeigen, zum Beispiel in TCP-Analysefeldern oder TCP Stream Graphs.

Praktisch für den Einstieg:

- SYN bis SYN/ACK als grober RTT-Hinweis
- Datenpaket bis ACK als weiterer Hinweis
- starke Schwankungen ernst nehmen

## TLS-Handshake-Zeit

Bei HTTPS kommt nach TCP meist TLS.

Filter:

```text
tls
```

Wichtige Beobachtungen:

- Client Hello
- Server Hello
- Zertifikatsinformationen, je nach TLS-Version und Sichtbarkeit
- Change Cipher / Finished, je nach Version
- Application Data

Wenn die Verzögerung zwischen TCP Handshake und TLS-Abschluss liegt, ist das Problem nicht im reinen TCP-Verbindungsaufbau.

Mögliche Ursachen:

- Server langsam
- Zertifikatsprüfung oder externe Abhängigkeiten
- TLS-Parameter
- Paketverlust
- Client- oder Serverlast

## Zeit bis zur ersten Anwendungsantwort

Bei HTTP ohne TLS kannst du oft direkt sehen:

```text
GET /...
HTTP/1.1 200 OK
```

Interessanter Messpunkt:

```text
Zeit zwischen Request und erster Response
```

Wenn dieser Abstand groß ist und TCP sauber aussieht, spricht das eher für:

- Anwendung verarbeitet langsam
- Backend wartet
- Datenbank langsam
- Server ausgelastet
- Proxy oder Loadbalancer wartet

AHA:

> Wenn der Request beim Server angekommen ist und lange keine Antwort kommt, ist das nicht automatisch ein Netzwerkproblem.

Bei HTTPS siehst du den HTTP-Inhalt normalerweise nicht, aber du kannst trotzdem Zeitabstände zwischen TLS Application Data Paketen bewerten.

## Datenübertragung und Throughput

Throughput beschreibt, wie viele Daten pro Zeit übertragen werden.

In Wireshark kannst du das über Statistiken und Graphen sichtbar machen.

Nützliche Menüs:

```text
Statistics > I/O Graphs
```

```text
Statistics > Conversations
```

```text
Statistics > TCP Stream Graphs
```

Mögliche Beobachtungen:

- gleichmäßiger Datenfluss
- lange Pausen
- Sägezahnmuster
- Retransmission-Spitzen
- kurze Bursts mit langen Wartezeiten
- sehr kleine Pakete statt großer Segmente

## I/O Graphs

I/O Graphs zeigen Paket- oder Byte-Mengen über die Zeit.

Menü:

```text
Statistics > I/O Graphs
```

Nützlich für:

- Traffic-Spitzen
- Übertragungspausen
- Vergleich von gefilterten Streams
- Erkennen von Bursts
- grobe Durchsatzbetrachtung

Beispiel-Filter für einen Stream:

```text
tcp.stream == 3
```

Beispiel-Filter für Retransmissions:

```text
tcp.analysis.retransmission
```

AHA:

> I/O Graphs zeigen Muster. Die Ursache musst du danach im Paketdetail prüfen.

## TCP Stream Graphs

Wireshark bietet für TCP Streams mehrere Graphen.

Typisch interessant:

| Graph | Nutzen |
|---|---|
| Time Sequence | zeigt Sequenznummern über Zeit |
| Throughput | zeigt Übertragungsrate |
| Round Trip Time | zeigt RTT-Entwicklung |
| Window Scaling | hilft bei Fensteranalyse |

Je nach Wireshark-Version können Namen leicht abweichen.

Die Idee bleibt:

> Graphen helfen, Muster zu sehen. Pakete erklären die Muster.

## Retransmissions und Performance

Retransmissions können Performance stark beeinflussen.

Filter:

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

Wichtig:

- einzelne Retransmission kann unkritisch sein
- gehäufte Retransmissions sind relevant
- Retransmissions am Anfang können Handshake oder TLS verzögern
- Retransmissions während großer Transfers reduzieren Durchsatz
- Capture-Lücken können wie Retransmissions wirken

## Paketverlust oder Capture-Problem?

Nicht jede Lücke im Capture ist echter Paketverlust.

Hinweise auf Capture-Probleme:

- `ACKed unseen segment`
- `Previous segment not captured`
- sehr hohe Capture-Last
- Mitschnitt auf falschem Interface
- SPAN/Mirror-Port überlastet
- nur eine Richtung sichtbar
- Capture startet zu spät
- viele Drops im Capture-Tool

AHA:

> Bevor du Paketverlust diagnostizierst, prüfe, ob dein Capture zuverlässig ist.

## Window-Probleme

Window-Probleme zeigen, dass eine Seite nicht schnell genug Daten aufnehmen kann.

Wichtige Filter:

```text
tcp.analysis.zero_window
```

```text
tcp.analysis.window_update
```

```text
tcp.analysis.window_full
```

Zero Window bedeutet:

> Der Empfänger kann aktuell keine weiteren Daten aufnehmen.

Das spricht eher für:

- Anwendung liest zu langsam
- Empfänger überlastet
- Buffer voll
- Client- oder Serverproblem

Es ist nicht der klassische Beweis für ein Netzwerkproblem.

## Kleine Pakete und Nagle/Delayed ACK

Manchmal wirken viele kleine Pakete oder Wartezeiten auffällig.

Mögliche Themen:

- kleine Writes der Anwendung
- Nagle-Algorithmus
- Delayed ACK
- interaktive Protokolle
- Anwendung wartet bewusst
- TLS Records
- Proxy-Verhalten

Für den Kurs reicht zunächst:

> Viele kleine Pakete sind nicht automatisch falsch. Prüfe, ob sie zum Protokoll und zur Anwendung passen.

## Server Delay vs. Network Delay

Ein wichtiger Unterschied:

| Beobachtung | Mögliche Richtung |
|---|---|
| SYN bis SYN/ACK langsam | Netzweg, Server-Erreichbarkeit, Firewall, Last |
| Request kommt an, Antwort spät | Anwendung oder Serververarbeitung |
| Retransmissions und Dup ACKs | Paketverlust oder Capture-Thema |
| Zero Window | Empfänger kann nicht aufnehmen |
| DNS Response spät | DNS-Server, Upstream, Netzweg zum DNS |
| TLS Handshake verzögert | TLS, Server, Paketverlust, Client-/Serverlast |

AHA:

> Nicht jede Verzögerung zwischen zwei Paketen ist Netzwerkverzögerung. Manchmal wartet die Anwendung.

## Expert Information vorsichtig nutzen

Wireshark bietet:

```text
Analyze > Expert Information
```

Das ist hilfreich, aber keine endgültige Diagnose.

Expert Information zeigt Hinweise wie:

- Errors
- Warnings
- Notes
- Chats

Verwende es als Einstieg, nicht als Urteil.

Sinnvolle Reihenfolge:

1. Expert Information öffnen
2. betroffene Pakete prüfen
3. Stream isolieren
4. zeitlichen Kontext prüfen
5. Capture-Punkt bewerten

## TShark-Beispiele

TCP-Analysehinweise pro Stream zählen:

```bash
tshark -r capture.pcapng \
  -Y "tcp.analysis.flags" \
  -T fields \
  -e tcp.stream | sort -n | uniq -c
```

Retransmissions mit Zeit ausgeben:

```bash
tshark -r capture.pcapng \
  -Y "tcp.analysis.retransmission" \
  -T fields \
  -e frame.number \
  -e frame.time_relative \
  -e tcp.stream \
  -e ip.src \
  -e ip.dst
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

DNS-Antwortzeiten grob vorbereiten:

```bash
tshark -r capture.pcapng \
  -Y "dns" \
  -T fields \
  -e frame.number \
  -e frame.time_relative \
  -e dns.id \
  -e dns.flags.response \
  -e dns.qry.name \
  -e dns.flags.rcode
```

TCP-Streams anzeigen:

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

## Mini-Aufgabe: Webaufruf zeitlich zerlegen

Erzeuge einen Capture.

1. Starte Wireshark oder TShark.
2. Führe aus:

```bash
curl -v https://example.org
```

3. Stoppe den Mitschnitt.
4. Speichere ihn als:

```text
pcaps/generated/advanced-performance-web-01.pcapng
```

5. Öffne ihn in Wireshark.

Beantworte:

- Gibt es DNS?
- Wie lange dauert DNS ungefähr?
- Welche TCP-Verbindung gehört zum Webaufruf?
- Wie lange dauert der TCP-Handshake ungefähr?
- Gibt es TLS-Pakete?
- Gibt es Retransmissions?
- Gibt es Zero Window?
- Gibt es auffällige Wartezeiten?
- Welche Aussage kannst du wirklich belegen?

## Mini-Aufgabe: I/O Graph

Nutze den gleichen Capture.

1. Öffne:

```text
Statistics > I/O Graphs
```

2. Setze als Filter:

```text
tcp.stream == <nummer>
```

3. Prüfe:

- Gibt es lange Pausen?
- Gibt es gleichmäßige Datenübertragung?
- Gibt es Traffic-Spitzen?
- Passt das Muster zu dem, was du in der Paketliste siehst?

Dokumentiere mindestens eine Beobachtung mit Zeitbereich.

## Analysebericht: Performance

```text
Symptom:
<kurze Beschreibung>

Capture-Punkt:
<Client / Server / Gateway / unbekannt>

Betroffener Flow/Stream:
tcp.stream == <nummer>

DNS:
<kurze Bewertung mit Frame-Nummern>

TCP Handshake:
<kurze Bewertung mit Frame-Nummern und Zeitabstand>

TLS:
<kurze Bewertung, falls sichtbar>

Anwendungsantwort:
<Zeit bis zur ersten Antwort oder Application Data>

TCP-Auffälligkeiten:
Retransmissions: ja/nein
Duplicate ACKs: ja/nein
Zero Window: ja/nein
RST/FIN: ja/nein

Graphen:
<I/O Graph oder TCP Stream Graph Beobachtung>

Bewertung:
<fachliche Einordnung>

Nicht belegbar:
<was der Capture nicht zeigt>

Nächster sinnvoller Schritt:
<z. B. Server-Capture, DNS-Test, Log-Abgleich, Vergleich mit Baseline>
```

## Typische Fehlinterpretationen

| Beobachtung | Falscher Schluss | Bessere Bewertung |
|---|---|---|
| Anwendung langsam | Netzwerkproblem | erst Zeitabschnitte zerlegen |
| lange Pause | Paketverlust | kann Server- oder Anwendungspause sein |
| Retransmission | Netz ist schuld | Capture-Punkt und Muster prüfen |
| Zero Window | Netzwerk langsam | Empfänger kann nicht aufnehmen |
| DNS fehlt | DNS nicht genutzt | Cache, DoH, DoT oder falscher Capture-Punkt prüfen |
| I/O Graph hat Lücken | Fehler | Paketdetails und Anwendungskontext prüfen |
| Expert Information zeigt Warnungen | Ursache gefunden | Hinweis prüfen, nicht blind übernehmen |

## WCA-Bezug

Dieser Abschnitt übt WCA-nahe Fähigkeiten:

- TCP-Performancehinweise erkennen
- Zeitverhalten in Captures bewerten
- TCP-Analysefelder sinnvoll nutzen
- DNS-, TCP-, TLS- und Anwendungsabschnitte trennen
- Graphen zur Mustererkennung verwenden
- Capture-Punkte und Capture-Qualität bewerten
- Beobachtungen reproduzierbar dokumentieren

## Merksatz

> Performanceanalyse mit Wireshark bedeutet nicht, eine rote Zeile zu finden.  
> Es bedeutet, Wartezeit sichtbar zu machen und sauber einzugrenzen.
