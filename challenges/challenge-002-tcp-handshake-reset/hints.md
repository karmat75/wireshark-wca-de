# Hinweise

## Hinweis 1: erfolgreiche Verbindung

Beginne mit:

```text
tcp.port == 80
```

Suche:

```text
[SYN]
[SYN, ACK]
[ACK]
```

## Hinweis 2: HTTP

Nach dem Handshake sollte HTTP sichtbar sein:

```text
http
```

oder:

```text
ip.addr == 172.28.50.10 and http
```

## Hinweis 3: geschlossener Port

Der Testport ist:

```text
81
```

Filter:

```text
tcp.port == 81
```

## Hinweis 4: Reset

RST findest du mit:

```text
tcp.flags.reset == 1
```

Ein RST/RST-ACK ist keine Zeitüberschreitung.

## Hinweis 5: nicht zu stark formulieren

Sauber:

```text
Der Verbindungsversuch zu Port 81 wird aktiv zurückgesetzt beziehungsweise abgelehnt.
```

Im Lab wahrscheinlich:

```text
Auf Port 81 lauscht kein Dienst.
```

Zu stark ohne weiteren Kontext:

```text
Die Firewall ist schuld.
```

oder:

```text
Der Server ist offline.
```
