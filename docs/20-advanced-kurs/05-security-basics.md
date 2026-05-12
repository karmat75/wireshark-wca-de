# Security-Basics

Wireshark ist kein SIEM, kein EDR und kein Schwachstellenscanner.

Trotzdem ist Wireshark ein sehr starkes Werkzeug für defensive Sicherheitsanalyse.

Es hilft dir zu sehen:

- welche Systeme miteinander sprechen
- welche Protokolle verwendet werden
- ob sensible Daten im Klartext übertragen werden
- ob ungewöhnliche DNS-Anfragen sichtbar sind
- ob ein System regelmäßig nach außen kommuniziert
- ob Verbindungsversuche ungewöhnlich breit gestreut sind
- ob TLS, HTTP oder DNS Hinweise auf ein Problem liefern
- ob ein Verdacht mit Paketen belegbar ist

Dieser Abschnitt bleibt bewusst defensiv.

Es geht nicht darum, Angriffe auszuführen.

Es geht darum, verdächtigen oder unerwünschten Netzwerkverkehr zu erkennen, einzuordnen und sauber zu dokumentieren.

## Ziel

Nach diesem Abschnitt solltest du können:

- Security-relevante Beobachtungen in Captures finden
- Klartext-Protokolle erkennen
- verdächtige DNS-Muster grob bewerten
- einfache Beaconing-Muster erkennen
- Portscan-ähnliches Verhalten einordnen
- HTTP- und TLS-Metadaten für defensive Analyse nutzen
- IOCs in Captures suchen
- Dateiübertragungen vorsichtig behandeln
- Grenzen und Datenschutzrisiken von PCAPs benennen
- Security-Beobachtungen sauber dokumentieren

## Grundsatz: defensiv und berechtigt

Packet Capturing kann sensible Daten sichtbar machen.

Security-Analyse mit Wireshark darf nur dort erfolgen, wo du dazu berechtigt bist.

Das gilt besonders für:

- produktive Netzwerke
- personenbezogene Daten
- Authentifizierungsdaten
- Kundendaten
- medizinische oder geschäftskritische Daten
- fremde Geräte
- fremde Netzwerke

!!! warning "Keine Analyse ohne Berechtigung"
    In diesem Kurs analysieren wir nur eigene Captures, Lab-Captures oder ausdrücklich freigegebene Mitschnitte.

## Was Wireshark in Security-Fällen leisten kann

Wireshark kann helfen bei:

- Verdacht auf unerwünschte Kommunikation
- Prüfung von Klartextübertragung
- DNS-Analyse
- HTTP-Analyse
- TLS-Metadaten
- Verbindungsabbrüchen
- ungewöhnlichen Ports
- ungewöhnlichen Zielsystemen
- einfachen Beaconing-Mustern
- IOC-Suche in PCAPs
- Validierung anderer Systeme, zum Beispiel Firewall, Proxy, IDS oder EDR

Wireshark ersetzt aber nicht:

- Endpoint-Forensik
- vollständige Malwareanalyse
- Log-Analyse
- SIEM-Korrelation
- Netzwerkflussdaten über lange Zeit
- organisatorische Incident-Response-Prozesse

AHA:

> Wireshark zeigt Netzwerkbeobachtungen. Ein Security-Fall braucht fast immer zusätzliche Datenquellen.

## Erste Orientierung in einem verdächtigen Capture

Beginne nicht direkt mit einem einzelnen Paket.

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

Fragen:

- Welche Protokolle kommen vor?
- Welche internen IPs sind beteiligt?
- Welche externen IPs sind beteiligt?
- Gibt es ungewöhnlich viele DNS-Anfragen?
- Gibt es viele fehlgeschlagene Verbindungen?
- Gibt es HTTP ohne TLS?
- Gibt es unerwartete Ports?
- Gibt es viel Traffic zu einem einzelnen Ziel?
- Gibt es regelmäßige Kommunikation?

## Interne und externe Kommunikation

Eine einfache erste Frage:

> Spricht ein System mit Zielen, die es nicht kennen sollte?

Filter für ein einzelnes internes System:

```text
ip.addr == <client-ip>
```

Wenn du die Client-IP kennst, kannst du alle Gespräche dieses Systems betrachten.

In Wireshark:

```text
Statistics > Conversations
```

Dort kannst du nach Bytes, Paketen, Dauer oder Endpunkten sortieren.

## Klartext-Protokolle erkennen

Klartext ist aus Security-Sicht wichtig, weil Inhalte sichtbar sein können.

Typische Klartext- oder potenziell sensible Protokolle:

| Protokoll | Risiko |
|---|---|
| HTTP | Header, Cookies, Formulardaten, API-Daten sichtbar |
| FTP | Benutzername und Passwort oft sichtbar |
| Telnet | komplette Sitzung sichtbar |
| POP3 ohne TLS | Mailinhalte und Zugangsdaten möglich |
| IMAP ohne TLS | Mailinhalte und Zugangsdaten möglich |
| SMTP ohne TLS | Mailinhalte sichtbar, je nach Nutzung |
| LDAP ohne TLS | Verzeichnisdaten, ggf. sensible Informationen |
| SMB alte Varianten | abhängig von Version und Signierung/Verschlüsselung |

Display Filter:

```text
http
```

```text
ftp
```

```text
telnet
```

```text
smtp
```

```text
ldap
```

AHA:

> Wenn sensible Daten im Klartext im Capture sichtbar sind, sind sie auch für jeden sichtbar, der diesen Traffic mitschneiden konnte.

## HTTP aus Security-Sicht

Bei HTTP ohne TLS kannst du unter anderem sehen:

- Host
- URI
- User-Agent
- Referer
- Cookies
- Authorization Header
- Formulardaten
- Dateidownloads
- Redirects
- Statuscodes
- Server-Header

Filter:

```text
http
```

HTTP Requests:

```text
http.request
```

HTTP Responses:

```text
http.response
```

Bestimmter Host:

```text
http.host contains "example"
```

User-Agent:

```text
http.user_agent
```

Statuscodes ab 400:

```text
http.response.code >= 400
```

!!! warning "Credentials und Tokens"
    Wenn du in HTTP-Captures Zugangsdaten, Cookies oder Tokens findest, gehören diese Informationen nicht in Tickets, Screenshots oder öffentliche Repositories.

## HTTPS aus Security-Sicht

Bei HTTPS ist der Inhalt normalerweise verschlüsselt.

Sichtbar bleiben häufig:

- Ziel-IP
- Zielport
- TCP-Verhalten
- TLS Client Hello
- SNI, wenn sichtbar
- ALPN, wenn sichtbar
- Zertifikatsinformationen, wenn sichtbar
- TLS Alerts
- Paketgrößen
- Zeitverhalten

Filter:

```text
tls
```

Client Hello:

```text
tls.handshake.type == 1
```

SNI:

```text
tls.handshake.extensions_server_name
```

TLS Alerts:

```text
tls.alert_message
```

AHA:

> Verschlüsselung verhindert nicht, dass Kommunikation sichtbar ist. Sie verhindert, dass der Inhalt einfach lesbar ist.

## DNS aus Security-Sicht

DNS ist oft sehr aufschlussreich.

Viele Anwendungen und Schadprogramme müssen Namen auflösen, bevor sie kommunizieren.

Interessante DNS-Beobachtungen:

- ungewöhnliche Domains
- sehr lange Domainnamen
- sehr viele Subdomains
- viele NXDOMAIN-Antworten
- wiederholte Anfragen in festen Abständen
- Anfragen an unerwartete DNS-Server
- direkte DNS-Anfragen ins Internet trotz internem DNS
- Wechsel zwischen vielen Domains
- auffällige TLDs oder frisch wirkende Namen

Filter:

```text
dns
```

DNS Queries:

```text
dns.flags.response == 0
```

DNS Fehler:

```text
dns.flags.response == 1 and dns.flags.rcode != 0
```

Bestimmter Name:

```text
dns.qry.name contains "example"
```

## DNS ist kein Beweis für Bösartigkeit

Eine ungewöhnliche Domain ist erstmal nur eine Beobachtung.

Sie kann bedeuten:

- legitimer Cloud-Dienst
- CDN
- Telemetrie
- Update-Mechanismus
- Werbung oder Tracking
- Fehlkonfiguration
- Schadsoftware
- Testverkehr

AHA:

> DNS ist ein starker Hinweisgeber, aber kein alleiniger Schuldspruch.

## Beaconing erkennen

Beaconing bedeutet vereinfacht:

> Ein System meldet sich regelmäßig bei einem Ziel.

Das kann legitim sein:

- Monitoring-Agent
- Update-Client
- Cloud-Sync
- VPN
- Telemetrie
- NTP

Oder verdächtig:

- Command-and-Control-Kommunikation
- unerwünschter Agent
- Malware
- exfiltrierende Software

Beobachtungen:

- gleiche Quelle
- gleiches Ziel
- ähnliche Paketgröße
- regelmäßiger Abstand
- ähnliche DNS-Namen oder SNI
- wenig Daten, aber wiederkehrend

In Wireshark helfen:

```text
Statistics > Conversations
```

```text
Statistics > I/O Graphs
```

Filter:

```text
ip.addr == <client-ip> and ip.addr == <ziel-ip>
```

oder:

```text
tls.handshake.extensions_server_name contains "<name>"
```

## Regelmäßigkeit prüfen

Zeitdarstellung:

```text
View > Time Display Format > Seconds Since Beginning of Capture
```

Dann prüfst du, ob ähnliche Verbindungen regelmäßig auftauchen.

Beispiel:

```text
12.0 s
42.0 s
72.1 s
102.1 s
```

Das wäre ein Hinweis auf ein 30-Sekunden-Intervall.

Aber:

> Regelmäßigkeit allein ist nicht automatisch bösartig.

## Portscan-ähnliches Verhalten

Ein Portscan versucht typischerweise, viele Ports oder viele Ziele zu erreichen.

In einem Capture können Hinweise sein:

- viele SYN-Pakete
- viele Zielports
- viele Ziel-IP-Adressen
- wenige oder keine vollständigen Handshakes
- viele RST-Antworten
- kurze Zeitfenster
- wiederholte Muster

Filter:

```text
tcp.flags.syn == 1 and tcp.flags.ack == 0
```

RST:

```text
tcp.flags.reset == 1
```

Viele Verbindungsversuche eines Clients:

```text
ip.src == <client-ip> and tcp.flags.syn == 1 and tcp.flags.ack == 0
```

AHA:

> Viele SYN-Pakete können ein Scan sein. Sie können aber auch ein normaler Client mit vielen Verbindungen sein. Kontext entscheidet.

## Unerwartete Ports

Ungewöhnliche Ports sind interessant, aber nicht automatisch schlecht.

Prüfe:

- gehört der Port zur Anwendung?
- ist der Zielserver bekannt?
- ist die Verbindung erfolgreich?
- welcher Prozess auf dem Client könnte das sein?
- gibt es passende DNS-Anfragen?
- ist TLS oder HTTP sichtbar?
- tritt es regelmäßig auf?

In Wireshark:

```text
Statistics > Conversations > TCP
```

Sortiere nach Port, Paketen, Bytes oder Dauer.

## IOCs in Captures suchen

IOC steht für Indicator of Compromise.

Typische IOCs:

- IP-Adresse
- Domain
- URL
- Hostname
- User-Agent
- Dateiname
- Hash, wenn bekannt
- Zertifikatsmerkmal
- SNI
- E-Mail-Adresse, je nach Protokoll

Beispiele:

IP suchen:

```text
ip.addr == 203.0.113.10
```

Domain in DNS suchen:

```text
dns.qry.name contains "example"
```

SNI suchen:

```text
tls.handshake.extensions_server_name contains "example"
```

HTTP Host suchen:

```text
http.host contains "example"
```

HTTP User-Agent suchen:

```text
http.user_agent contains "curl"
```

## Dateiübertragungen in Captures

Wireshark kann unter bestimmten Bedingungen Objekte aus Protokollen exportieren.

Zum Beispiel bei HTTP:

```text
File > Export Objects > HTTP
```

Das kann bei Analyse hilfreich sein.

Aber Vorsicht:

- exportierte Dateien können schädlich sein
- Dateien können personenbezogene oder geschäftliche Daten enthalten
- Dateien können urheberrechtlich oder vertraulich sein
- niemals unüberlegt öffnen oder weitergeben

!!! warning "Gefahr durch exportierte Dateien"
    Exportiere Objekte nur in einer sicheren Lab-Umgebung und öffne sie nicht ungeschützt auf deinem normalen Arbeitsgerät.

## Keine Malware im Kurs-Repo

Für dieses Projekt gilt:

- keine Malware-Dateien ins Repo
- keine echten Schadcode-Samples
- keine produktiven Incident-Captures
- keine Kundendaten
- keine echten Zugangsdaten
- keine privaten Captures

Security-Labs müssen mit synthetischem oder klar lizenziertem Material arbeiten.

## TLS-Zertifikate als Hinweis

TLS-Zertifikate können Hinweise liefern:

- ungewöhnlicher Aussteller
- Self-Signed-Zertifikat
- falscher Hostname
- sehr kurze Gültigkeit
- abgelaufenes Zertifikat
- unerwartete Organisation
- ungewöhnliche Subject Alternative Names

Wireshark zeigt Zertifikatsinformationen nur, wenn sie im Capture sichtbar sind.

Zusätzliche Werkzeuge sind oft sinnvoll:

```bash
openssl s_client -connect example.org:443 -servername example.org
```

Dieses Werkzeug ist ergänzend, nicht Wireshark selbst.

## Verdächtige DNS-Fehler

Viele NXDOMAIN-Antworten können interessant sein.

Filter:

```text
dns.flags.rcode == 3
```

Mögliche Ursachen:

- Tippfehler
- falsch konfigurierte Anwendung
- Suchdomänen-Effekte
- blockierte Domains
- Domain Generation Algorithm
- kaputter Dienst
- interne Namen gehen nach extern

AHA:

> Viele NXDOMAINs sind ein Hinweis. Die Ursache muss geprüft werden.

## Datenabfluss grob erkennen

Wireshark kann Hinweise auf ungewöhnliche Datenübertragung liefern.

Mögliche Beobachtungen:

- ungewöhnlich große Uploads
- viele Daten zu unbekanntem Ziel
- regelmäßige kleine Datenpakete
- Upload außerhalb erwarteter Zeiten
- Datenverkehr über unübliche Ports
- DNS mit sehr langen Namen
- HTTP POST ohne TLS
- TLS-Verbindung zu unbekanntem Ziel mit viel ausgehendem Traffic

Aber:

> Wireshark allein sagt nicht automatisch, ob Datenabfluss stattgefunden hat. Es zeigt Verkehrsverhalten.

## Nützliche Display Filter

HTTP:

```text
http
```

HTTP Requests:

```text
http.request
```

HTTP Statuscodes ab 400:

```text
http.response.code >= 400
```

TLS:

```text
tls
```

TLS Client Hello:

```text
tls.handshake.type == 1
```

TLS Alerts:

```text
tls.alert_message
```

DNS:

```text
dns
```

DNS-Fehler:

```text
dns.flags.response == 1 and dns.flags.rcode != 0
```

SYN ohne ACK:

```text
tcp.flags.syn == 1 and tcp.flags.ack == 0
```

RST:

```text
tcp.flags.reset == 1
```

Ein Host:

```text
ip.addr == <ip>
```

Ein Zielport:

```text
tcp.dstport == <port>
```

## TShark-Beispiele

DNS Queries ausgeben:

```bash
tshark -r capture.pcapng \
  -Y "dns.flags.response == 0" \
  -T fields \
  -e frame.number \
  -e frame.time_relative \
  -e ip.src \
  -e dns.qry.name
```

DNS-Fehler ausgeben:

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

TLS SNI ausgeben:

```bash
tshark -r capture.pcapng \
  -Y "tls.handshake.type == 1" \
  -T fields \
  -e frame.number \
  -e frame.time_relative \
  -e ip.src \
  -e ip.dst \
  -e tls.handshake.extensions_server_name
```

HTTP User-Agents ausgeben:

```bash
tshark -r capture.pcapng \
  -Y "http.user_agent" \
  -T fields \
  -e frame.number \
  -e ip.src \
  -e http.host \
  -e http.user_agent
```

SYN-Ziele eines Clients ausgeben:

```bash
tshark -r capture.pcapng \
  -Y "ip.src == <client-ip> and tcp.flags.syn == 1 and tcp.flags.ack == 0" \
  -T fields \
  -e frame.time_relative \
  -e ip.dst \
  -e tcp.dstport | sort | uniq -c
```

## Mini-Aufgabe: Security-Triage

Nutze einen eigenen harmlosen Capture oder einen vorbereiteten Lab-Capture.

1. Öffne den Capture in Wireshark.
2. Prüfe:

```text
Statistics > Protocol Hierarchy
```

3. Prüfe:

```text
Statistics > Conversations
```

4. Beantworte:

- Welche Protokolle kommen vor?
- Welche Hosts sprechen am meisten?
- Gibt es HTTP ohne TLS?
- Gibt es DNS-Fehler?
- Gibt es TLS-Verbindungen mit sichtbarem SNI?
- Gibt es viele SYN-Pakete?
- Gibt es viele RST-Pakete?
- Gibt es regelmäßige Kommunikation?

Dokumentiere nur Beobachtungen, keine vorschnellen Ursachen.

## Mini-Aufgabe: IOC-Suche

Wähle einen bekannten harmlosen Namen aus deinem Capture, zum Beispiel:

```text
example.org
```

Suche ihn in:

```text
dns.qry.name contains "example"
```

```text
tls.handshake.extensions_server_name contains "example"
```

```text
http.host contains "example"
```

Beantworte:

- Taucht der Name in DNS auf?
- Taucht der Name in SNI auf?
- Taucht der Name in HTTP auf?
- Gibt es eine TCP-Verbindung zur aufgelösten IP?
- Welche Filter haben Treffer geliefert?

## Analysebericht: Security-Beobachtung

```text
Verdacht:
<kurze Beschreibung>

Capture-Punkt:
<Client / Server / Gateway / Mirror / unbekannt>

Betroffenes System:
<ip/name>

Beobachtungen:
- Frame <nummer>: <Beobachtung>
- Frame <nummer>: <Beobachtung>
- Frame <nummer>: <Beobachtung>

Indikatoren:
IP: <ip>
Domain/SNI/Host: <name>
Port: <port>
Protokoll: <protokoll>

Bewertung:
<fachliche Einordnung>

Einschränkungen:
<was zeigt der Capture nicht?>

Empfohlene nächste Schritte:
- Log-Abgleich
- EDR/AV-Prüfung
- DNS-/Proxy-Logs prüfen
- Firewall-Logs prüfen
- Systemprozess identifizieren
- weiteren Capture am passenden Punkt erstellen

Verwendete Filter:
<filter>
```

## Typische Fehlinterpretationen

| Beobachtung | Falscher Schluss | Bessere Bewertung |
|---|---|---|
| unbekannte Domain | Malware | erst Kontext und Reputation prüfen |
| regelmäßiger Traffic | Beaconing durch Malware | kann legitimer Agent sein |
| HTTP im Klartext | Angriff | Risiko oder Fehlkonfiguration prüfen |
| viele SYNs | Portscan | Zielverteilung und Kontext prüfen |
| TLS verschlüsselt | keine Analyse möglich | Metadaten und Zeitverhalten bleiben sichtbar |
| DNS NXDOMAIN | DGA | auch Tippfehler oder Suchdomänen möglich |
| Datei im Capture | gefahrlos öffnen | isoliert behandeln, nicht direkt ausführen |

## WCA-Bezug

Dieser Abschnitt übt WCA-nahe Fähigkeiten:

- Protokolle in Captures erkennen
- HTTP, DNS, TLS und TCP sicher filtern
- Conversations und Endpoints nutzen
- verdächtige Muster erkennen und vorsichtig einordnen
- Display Filter und TShark für strukturierte Suche verwenden
- Analyseergebnisse mit Frame-Nummern dokumentieren
- Grenzen von Captures und Verschlüsselung benennen

## Merksatz

> Security-Analyse mit Wireshark bedeutet nicht, sofort „bösartig“ zu rufen.  
> Sie bedeutet, verdächtige Beobachtungen sauber zu belegen, einzuordnen und mit weiteren Datenquellen abzugleichen.
