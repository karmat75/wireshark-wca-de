# Hinweise

## Hinweis 1: Handshake finden

Beginne mit:

```text
tcp.port == 80
```

Dann suche:

```text
[SYN]
[SYN, ACK]
[ACK]
```

## Hinweis 2: Stream Index finden

Klicke ein Paket der Verbindung an und öffne im Paketdetailbereich:

```text
Transmission Control Protocol
```

Dort findest du:

```text
Stream index
```

Oder nutze TShark:

```bash
tshark -r pcaps/generated/lab-basic-030-tcp-handshake-reset.pcapng \
  -Y "tcp.port == 80" \
  -T fields \
  -e frame.number \
  -e tcp.stream \
  -e _ws.col.Info
```

## Hinweis 3: HTTP sehen

Für die erfolgreiche Verbindung sollte HTTP sichtbar sein:

```text
http
```

oder:

```text
ip.addr == 172.28.50.10 and http
```

## Hinweis 4: geschlossenen Port finden

Der geschlossene Port ist:

```text
81
```

Filter:

```text
tcp.port == 81
```

Danach:

```text
tcp.flags.reset == 1
```

## Hinweis 5: RST richtig formulieren

Sauber:

```text
Das Zielsystem oder eine Komponente auf dem Weg lehnt den Verbindungsversuch aktiv ab.
```

Für dieses Docker-Lab ist sehr wahrscheinlich:

```text
Auf Port 81 lauscht am Ziel kein Dienst.
```

Zu stark ohne Kontext:

```text
Die Firewall ist schuld.
```

oder:

```text
Der Server ist offline.
```

## Hinweis 6: Keine RST-Pakete sichtbar

Falls kein RST sichtbar ist:

- Testtraffic wiederholen
- Capture früher starten
- richtigen Capture-Filter prüfen
- `curl`-Befehl erneut ausführen
- prüfen, ob Docker-Lab läuft
