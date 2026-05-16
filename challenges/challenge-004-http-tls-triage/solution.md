# Musterlösung

Die genauen Frame-Nummern hängen von deinem lokal erzeugten Capture ab.

## HTTP

Filter:

```text
http
```

Erwartete Beobachtung:

- HTTP Request zu `172.28.70.10`
- HTTP Response mit Statuscode 200
- Header im Klartext
- je nach Request sichtbarer HTML-Inhalt

Beispielbewertung:

```text
Die HTTP-Verbindung auf Port 80 ist im Klartext sichtbar. Methode, Header, Statuscode und Teile der Nutzdaten können im Capture gelesen werden.
```

## TLS / HTTPS

Filter:

```text
tls
```

Erwartete Beobachtung:

- TLS Client Hello
- TLS Handshake-Pakete
- TLS Application Data
- optional TLS Alert durch Zertifikatsprüfung

Beispielbewertung:

```text
Die HTTPS-Verbindung läuft über TLS auf Port 443. Der HTTP-Inhalt ist nicht als Klartext-HTTP sichtbar. Stattdessen erscheinen TLS-Handshakes und TLS Application Data.
```

## SNI

Filter:

```text
tls.handshake.extensions_server_name
```

Erwarteter Wert:

```text
secure.lab.local
```

Bewertung:

```text
SNI zeigt den Hostnamen, den der Client im TLS Handshake anfragt. Das ist ein sichtbares TLS-Metadatum und keine Entschlüsselung des HTTP-Inhalts.
```

## ALPN

Filter:

```text
tls.handshake.extensions_alpn_str
```

Mögliche Beobachtung:

- `http/1.1`
- kein Treffer

Bewertung:

```text
ALPN kann Hinweise auf das über TLS genutzte Anwendungsprotokoll geben. Wenn kein Treffer sichtbar ist, muss das im Kontext bewertet werden.
```

## TLS Alert

Filter:

```text
tls.alert_message
```

Mögliche Beobachtung:

```text
TLS Alert im Zusammenhang mit dem Aufruf ohne -k
```

Bewertung:

```text
Der TLS Alert passt im Lab zum erwarteten Zertifikatsproblem durch das selbstsignierte Zertifikat. In einer echten Analyse müsste die genaue Alert-Beschreibung und Client-/Server-Konfiguration geprüft werden.
```

## Vergleich HTTP und HTTPS

| Beobachtung | HTTP | HTTPS/TLS |
|---|---|---|
| TCP-Port | 80 | 443 |
| HTTP-Methode sichtbar | ja | normalerweise nein |
| HTTP-Statuscode sichtbar | ja | normalerweise nein |
| Header sichtbar | ja | normalerweise nein |
| Nutzdaten sichtbar | ja | normalerweise nein |
| TLS Client Hello | nein | ja |
| SNI möglich | nein | ja |
| TLS Application Data | nein | ja |

## Beispielbericht

```text
Capture-Punkt:
Host-System, Interface any, Capture Filter net 172.28.70.0/24

HTTP:
Auf Port 80 sind HTTP Request und HTTP Response sichtbar. Statuscode und Header sind im Klartext lesbar.

TLS:
Auf Port 443 ist TLS sichtbar. Im Client Hello ist SNI mit secure.lab.local sichtbar. Danach erscheinen TLS Application Data Pakete. Der HTTP-Inhalt ist nicht im Klartext sichtbar.

TLS Alert:
Beim Aufruf ohne -k ist ein TLS Alert sichtbar beziehungsweise möglich. Im Lab passt das zum selbstsignierten Zertifikat.

Bewertung:
HTTP überträgt Inhalte im Klartext. HTTPS schützt den Inhalt, lässt aber Metadaten wie IP-Adressen, Ports, Zeitverhalten und SNI sichtbar. Der Capture belegt keine Entschlüsselung des HTTPS-Inhalts.

Einschränkungen:
Ohne TLS-Schlüssel oder andere Entschlüsselungsmethode kann der HTTP-Inhalt der HTTPS-Verbindung nicht gelesen werden.
```

## Merksatz

> HTTPS versteckt nicht alles.  
> Es schützt Inhalte, während viele Verbindungsmetadaten weiterhin analysierbar bleiben.
