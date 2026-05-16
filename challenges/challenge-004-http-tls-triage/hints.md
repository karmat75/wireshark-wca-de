# Hinweise

## Hinweis 1: HTTP und TLS trennen

HTTP:

```text
tcp.port == 80
```

TLS:

```text
tcp.port == 443
```

## Hinweis 2: HTTP ist Klartext

Beginne mit:

```text
http
```

und prüfe:

```text
http.request
http.response
```

## Hinweis 3: SNI finden

SNI steckt im TLS Client Hello.

Filter:

```text
tls.handshake.extensions_server_name
```

Erwarteter Wert:

```text
secure.lab.local
```

## Hinweis 4: ALPN ist optional

ALPN kann sichtbar sein, muss aber je nach Client/Handshake nicht immer Treffer liefern.

Filter:

```text
tls.handshake.extensions_alpn_str
```

## Hinweis 5: TLS Alert

Der Aufruf ohne `-k` kann einen Zertifikatsfehler erzeugen.

Filter:

```text
tls.alert_message
```

Ein TLS Alert ist zunächst eine Beobachtung. Die genaue Bedeutung hängt von Alert-Beschreibung und Kontext ab.

## Hinweis 6: Nicht zu stark formulieren

Falsch:

```text
Bei HTTPS sieht man nichts.
```

Besser:

```text
Bei HTTPS sind Inhalte geschützt, aber Metadaten wie IPs, Ports, Zeitverhalten und häufig SNI bleiben sichtbar.
```
