# Analysebericht-Vorlage

Diese Seite beschreibt eine einfache Struktur für nachvollziehbare Wireshark-Analyseberichte.

Eine Markdown-Vorlage liegt zusätzlich unter:

```text
templates/analysis-report-template.md
```

## Warum eine Vorlage?

Gute Analyseberichte sind nicht lang, sondern nachvollziehbar.

Sie beantworten:

- Was wurde untersucht?
- Wo wurde mitgeschnitten?
- Welche Pakete sind relevant?
- Welche Filter wurden verwendet?
- Was ist belegt?
- Was ist nur eine Hypothese?
- Was sollte als Nächstes geprüft werden?

## Minimalstruktur

```text
# Analysebericht: <Titel>

## Zusammenfassung

## Ausgangslage

## Capture-Informationen

## Vorgehen

## Beobachtungen

## Bewertung

## Einschränkungen

## Nächste Schritte

## Anhang: Filter und TShark-Befehle
```

## Zusammenfassung

Kurz und klar.

Beispiel:

```text
Im Capture ist sichtbar, dass die Verbindung zu web-ok.lab.local erfolgreich aufgebaut wird. Bei web-slow.lab.local liegt die auffällige Wartezeit zwischen HTTP Request und HTTP Response. DNS und TCP Handshake zeigen in diesem Capture keine auffällige Verzögerung.
```

## Capture-Informationen

Mindestens dokumentieren:

| Punkt | Beispiel |
|---|---|
| Datei | `pcaps/generated/challenge-006-performance-triage.pcapng` |
| Capture-Punkt | Host-System, Interface `any` |
| Capture Filter | `net 172.28.50.0/24` |
| Zeitraum | Start/Ende aus Capture File Properties |
| Analysewerkzeuge | Wireshark, TShark |
| Einschränkungen | lokaler Lab-Capture, keine Gegen-Captures |

## Beobachtungen

Beobachtungen sollten Frame-Nummern enthalten.

Beispiel:

```text
Frame <n>: DNS Query für web-slow.lab.local
Frame <n>: DNS Response mit 172.28.50.20
Frame <n>: TCP SYN zu 172.28.50.20:80
Frame <n>: TCP SYN/ACK von 172.28.50.20:80
Frame <n>: HTTP Request
Frame <n>: HTTP Response 200 nach ungefähr 2 Sekunden
```

## Bewertung

Bewertung ist die Einordnung der Beobachtungen.

Gut:

```text
Die sichtbare Wartezeit liegt zwischen HTTP Request und HTTP Response. Das passt zu serverseitiger oder anwendungsseitiger Verarbeitung.
```

Zu stark:

```text
Der Server ist kaputt.
```

## Einschränkungen

Jeder Capture hat Grenzen.

Beispiele:

```text
Der Capture zeigt nur die Sicht am Capture-Punkt.
```

```text
Ohne Gegen-Capture auf Client- oder Serverseite ist der genaue Fehlerort nicht sicher belegbar.
```

```text
TLS-Inhalte sind ohne Entschlüsselung nicht als HTTP-Inhalt lesbar.
```

## Nächste Schritte

Beispiele:

```text
Serverlogs prüfen.
```

```text
Gegen-Capture auf der Serverseite erstellen.
```

```text
Switch-/Firewall-Interface-Counter prüfen.
```

```text
DNS-Server-Logs prüfen.
```

```text
Applikations- und Reverse-Proxy-Logs korrelieren.
```

## Formulierungshilfe

| Unscharf | Besser |
|---|---|
| Das Netzwerk ist langsam. | Im Capture liegt die sichtbare Wartezeit zwischen HTTP Request und Response. |
| Die Firewall blockt. | Auf SYN ist keine SYN/ACK-Antwort sichtbar. |
| Der Server ist down. | Der Verbindungsversuch wird mit RST/ACK beantwortet. |
| HTTPS zeigt nichts. | HTTPS schützt Inhalte, aber Metadaten wie IP, Port, Zeitverhalten und SNI bleiben sichtbar. |
| Das ist Malware. | Das Muster ist Beacon-ähnlich, beweist ohne Hostkontext aber keine Malware. |

## Merksatz

> Eine gute Analyse trennt Beobachtung, Bewertung und Vermutung.
