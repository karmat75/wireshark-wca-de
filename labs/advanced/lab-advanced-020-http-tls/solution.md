# Musterlösung

Die genauen Frame-Nummern hängen von deinem lokal erzeugten Capture ab.

Die fachlichen Beobachtungen sollten aber ähnlich sein.

## HTTP im Klartext

Filter:

```text
http
```

Erwartete Beobachtung:

- HTTP Request
- HTTP Response
- Statuscode 200
- Header `X-WWCA-Lab: http-cleartext`
- je nach Request sichtbarer HTML-Inhalt

Beispielbewertung:

```text
Bei HTTP sind Methode, Header, Statuscode und Nutzdaten im Capture im Klartext sichtbar. Das macht HTTP für Analysezwecke einfach, ist aber für sensible Daten ein Sicherheitsrisiko.
```

## TLS / HTTPS

Filter:

```text
tls
```

Erwartete Beobachtung:

- TLS Client Hello
- TLS Server Hello oder TLS 1.3 Handshake-Pakete
- TLS Application Data
- optional TLS Alert durch Zertifikatsfehler

## SNI

Filter:

```text
tls.handshake.extensions_server_name
```

Erwartung:

```text
secure.lab.local
```

Bewertung:

```text
SNI zeigt, welchen Hostnamen der Client im TLS Handshake anfragt. Der HTTP-Inhalt ist dadurch nicht entschlüsselt, aber ein wichtiges Metadatum bleibt sichtbar.
```

## ALPN

Filter:

```text
tls.handshake.extensions_alpn_str
```

Mögliche Beobachtung:

```text
http/1.1
```

oder:

```text
kein Treffer
```

Bewertung:

```text
ALPN kann zeigen, welches Anwendungsprotokoll über TLS ausgehandelt werden soll. Je nach Client und Aushandlung ist das Feld sichtbar oder nicht.
```

## TLS Alert

Filter:

```text
tls.alert_message
```

Mögliche Beobachtung:

```text
TLS Alert durch Zertifikatsprüfung
```

Bewertung:

```text
Der Alert entsteht im Lab erwartungsgemäß, wenn der Client das selbstsignierte Zertifikat ohne `-k` nicht akzeptiert. In einer echten Analyse müsste die genaue Alert-Beschreibung und Client-Ausgabe geprüft werden.
```

## HTTP vs. HTTPS

| Beobachtung | HTTP | HTTPS |
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
Der Client 172.28.70.100 greift per HTTP auf 172.28.70.10:80 zu.
Im Capture sind HTTP Request und HTTP Response sichtbar.
Der Statuscode 200 und Header sind im Klartext lesbar.

TLS:
Der Client greift per HTTPS auf secure.lab.local zu.
Im TLS Client Hello ist SNI mit secure.lab.local sichtbar.
Danach sind TLS Application Data Pakete sichtbar.
Der HTTP-Inhalt ist nicht als Klartext-HTTP sichtbar.

TLS Alert:
Beim Aufruf ohne `-k` entsteht erwartungsgemäß ein Zertifikatsfehler. Im Capture kann ein TLS Alert sichtbar sein.

Bewertung:
HTTP ist vollständig im Klartext analysierbar. HTTPS schützt den Inhalt, lässt aber Verbindungsmetadaten wie IP, Port, Zeitverhalten und häufig SNI sichtbar.

Einschränkungen:
Der Capture enthält keine Entschlüsselung des TLS-Inhalts. Es kann daher nicht aus dem HTTP-Inhalt der HTTPS-Verbindung gelesen werden.
```

## Merksatz

> HTTPS bedeutet nicht, dass keine Analyse möglich ist.  
> Es bedeutet, dass Inhalte geschützt sind und Metadaten sauber interpretiert werden müssen.
