# Hinweise

## Hinweis 1: Unterschied Display Filter und Capture Filter

Display Filter wirken auf vorhandene Pakete.

Beispiel:

```text
dns
```

Capture Filter wirken beim Mitschnitt.

Beispiel:

```text
udp port 53
```

Verwechsle die Syntax nicht.

## Hinweis 2: `ip.addr` vs. `ip.src` vs. `ip.dst`

```text
ip.addr == 172.28.50.100
```

zeigt Quelle oder Ziel.

```text
ip.src == 172.28.50.100
```

zeigt nur Pakete, bei denen diese IP Quelle ist.

```text
ip.dst == 172.28.50.100
```

zeigt nur Pakete, bei denen diese IP Ziel ist.

## Hinweis 3: Portfilter

```text
tcp.port == 80
```

zeigt beide Richtungen.

```text
tcp.dstport == 80
```

zeigt typischerweise Anfragen zum Serverport.

```text
tcp.srcport == 80
```

zeigt typischerweise Antworten vom Serverport.

## Hinweis 4: DNS NXDOMAIN

NXDOMAIN ist Response Code 3:

```text
dns.flags.rcode == 3
```

## Hinweis 5: HTTP fehlt

Wenn HTTP nicht sichtbar ist, prüfe:

- wurde wirklich `http://` verwendet?
- wurde HTTPS verwendet?
- ist die PCAP aus dem richtigen Lab?
- wurde der Capture vor dem Traffic gestartet?

## Hinweis 6: TCP Stream enthält kein DNS

DNS und HTTP können in derselben Benutzeraktion vorkommen, gehören aber nicht zum gleichen TCP Stream.

DNS ist hier UDP Port 53.

HTTP ist TCP Port 80.

## Hinweis 7: Klammern

Dieser Filter:

```text
dns or http and ip.addr == 172.28.50.100
```

ist schwerer zu lesen.

Besser:

```text
(dns or http) and ip.addr == 172.28.50.100
```

Klammern machen deine Absicht klar.
