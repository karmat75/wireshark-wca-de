# Hinweise

## Hinweis 1: Keine Pakete im Capture

Prüfe, ob das Lab läuft:

```bash
docker compose -f docker/compose/lab-basic-dns-http/compose.yml ps
```

Prüfe, ob du auf dem Host mitgeschnitten hast und nicht in einem falschen Interface.

Für den Einstieg ist `any` oft am einfachsten:

```bash
sudo tshark -i any -f "net 172.28.50.0/24"
```

## Hinweis 2: DNS funktioniert nicht

Prüfe den DNS-Server direkt:

```bash
docker compose -f docker/compose/lab-basic-dns-http/compose.yml exec lab-client dig @172.28.50.53 web-ok.lab.local
```

## Hinweis 3: NXDOMAIN finden

Nutze:

```text
dns.flags.rcode == 3
```

Der abgefragte Name steht im Feld:

```text
dns.qry.name
```

## Hinweis 4: HTTP nicht sichtbar

Prüfe, ob du wirklich HTTP verwendest:

```bash
curl -I http://web-ok.lab.local
```

Nicht HTTPS.

HTTP sollte mit dem Display Filter sichtbar sein:

```text
http
```

## Hinweis 5: langsamen Server erkennen

Vergleiche den Zeitabstand zwischen Request und Response.

Filtere zuerst auf den langsamen Server:

```text
ip.addr == 172.28.50.20 and http
```

Dann prüfe `Time` oder `Seconds Since Previous Displayed Packet`.

## Hinweis 6: Lab hängt oder Container alt

Lab stoppen und neu starten:

```bash
docker compose -f docker/compose/lab-basic-dns-http/compose.yml down
docker compose -f docker/compose/lab-basic-dns-http/compose.yml up -d
```
