# Musterlösung

Die genaue Lösung hängt von deinem Netzwerk ab.

Deshalb sind IP-Adressen, Interface-Namen und Paketnummern bei dir wahrscheinlich anders.

## Erwartete Beobachtungen

Der Capture sollte ungefähr enthalten:

- DNS-Pakete für `example.org`
- ICMP Echo Request und Echo Reply durch `ping`
- TCP-Verbindung zu einer IP von `example.org`
- TLS-Pakete durch `curl -I https://example.org`

## Interface

Beispiel:

```text
Interface: wlp2s0
```

oder:

```text
Interface: enp0s3
```

## DNS

Display Filter:

```text
dns
```

Erwartete Beobachtung:

```text
Standard query A example.org
Standard query response A <ip>
```

Je nach System können auch AAAA-Abfragen sichtbar sein.

TShark:

```bash
tshark -r pcaps/generated/lab-foundation-001-first-capture.pcapng \
  -Y "dns.flags.response == 0" \
  -T fields \
  -e frame.number \
  -e ip.src \
  -e dns.qry.name
```

Beispielhafte Bewertung:

```text
Im Capture sind DNS-Anfragen für example.org sichtbar. Damit ist belegt, dass während des Captures klassische DNS-Auflösung beobachtet wurde.
```

## ICMP

Display Filter:

```text
icmp
```

Erwartete Beobachtung:

```text
Echo request
Echo reply
```

Beispielhafte Bewertung:

```text
ICMP Echo Request und Echo Reply sind sichtbar. Damit ist ICMP-Erreichbarkeit für das Ziel im Capture belegt.
```

Wichtig:

```text
Ping beweist nicht, dass HTTP oder HTTPS funktioniert.
```

## TCP/TLS

Display Filter:

```text
tcp
```

und:

```text
tls
```

Erwartete Beobachtung:

- TCP-Verbindungsaufbau zu Port 443
- TLS Client Hello
- TLS Server Hello oder TLS Application Data

Beispielhafte Bewertung:

```text
Der Client baut eine TCP-Verbindung zu Port 443 auf. Danach ist TLS-Verkehr sichtbar. HTTP-Inhalte sind bei HTTPS ohne Entschlüsselung nicht lesbar.
```

## Beispiel für einen kurzen Analysebericht

```text
Capture-Punkt:
Client-System, Interface <interface>

Aktion:
dig example.org
ping -c 4 example.org
curl -I https://example.org

Beobachtungen:
- DNS-Anfragen für example.org sind sichtbar.
- ICMP Echo Request und Echo Reply sind sichtbar.
- TCP-Verkehr zu Port 443 ist sichtbar.
- TLS-Verkehr ist sichtbar.

Verwendete Filter:
dns
icmp
tcp
tls

Bewertung:
Die Lernumgebung kann Captures erstellen, speichern und analysieren. DNS, ICMP, TCP und TLS sind im Mitschnitt sichtbar. Der Capture eignet sich als Ausgangspunkt für weitere Übungen.
```

## Was nicht zwingend ein Fehler ist

| Beobachtung | Bewertung |
|---|---|
| viele zusätzliche Pakete | Hintergrundtraffic ist normal |
| keine VLAN-Tags | am Client-Interface meist normal |
| keine HTTP-Inhalte bei HTTPS | TLS verschlüsselt den Inhalt |
| andere IP-Adresse für example.org | DNS/CDN-Antworten können variieren |
| keine AAAA-Antwort | abhängig von DNS und Netzwerk |
