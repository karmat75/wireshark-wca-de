# Display-Filter-Cheatsheet

Diese Seite ist eine kompakte Arbeitsreferenz für häufige Wireshark Display Filter.

Display Filter wirken auf bereits vorhandene Pakete.

Sie verändern den Capture nicht.

## Grundregel

Ein guter Filter beantwortet eine konkrete Analysefrage.

Nicht:

```text
Irgendwas mit Netzwerk.
```

Besser:

```text
Zeige mir DNS-Antworten mit NXDOMAIN.
```

## Display Filter vs. Capture Filter

| Zweck | Beispiel | Zeitpunkt |
|---|---|---|
| Display Filter | `dns` | nach oder während der Anzeige |
| Capture Filter | `udp port 53` | beim Mitschnitt |

!!! warning "Syntax nicht verwechseln"
    `dns` ist ein Display Filter.  
    `udp port 53` ist ein Capture Filter.

## Protokolle

| Frage | Filter |
|---|---|
| DNS anzeigen | `dns` |
| TCP anzeigen | `tcp` |
| UDP anzeigen | `udp` |
| HTTP anzeigen | `http` |
| TLS anzeigen | `tls` |
| ICMP anzeigen | `icmp` |
| ARP anzeigen | `arp` |

## IP-Adressen

| Frage | Filter |
|---|---|
| IP als Quelle oder Ziel | `ip.addr == 192.0.2.10` |
| IP als Quelle | `ip.src == 192.0.2.10` |
| IP als Ziel | `ip.dst == 192.0.2.10` |
| zwei Systeme | `ip.addr == 192.0.2.10 and ip.addr == 192.0.2.20` |
| IPv6-Adresse | `ipv6.addr == 2001:db8::10` |

## Ports

| Frage | Filter |
|---|---|
| TCP-Port in beide Richtungen | `tcp.port == 80` |
| TCP-Zielport | `tcp.dstport == 80` |
| TCP-Quellport | `tcp.srcport == 80` |
| UDP-Port in beide Richtungen | `udp.port == 53` |
| DNS klassisch über UDP | `udp.port == 53 and dns` |
| HTTPS-TCP-Verkehr | `tcp.port == 443` |

## DNS

| Frage | Filter |
|---|---|
| DNS Queries | `dns.flags.response == 0` |
| DNS Responses | `dns.flags.response == 1` |
| DNS NXDOMAIN | `dns.flags.rcode == 3` |
| bestimmter Name | `dns.qry.name == "example.org"` |
| Name enthält Text | `dns.qry.name contains "example"` |
| DNS mit Server-IP | `dns and ip.addr == 192.0.2.53` |

## HTTP

| Frage | Filter |
|---|---|
| HTTP Requests | `http.request` |
| HTTP Responses | `http.response` |
| HTTP GET | `http.request.method == "GET"` |
| HTTP POST | `http.request.method == "POST"` |
| HTTP Status 200 | `http.response.code == 200` |
| HTTP Fehler 500 | `http.response.code == 500` |
| Host enthält Text | `http.host contains "lab.local"` |
| URI enthält Text | `http.request.uri contains "/api"` |
| User-Agent enthält Text | `http.user_agent contains "curl"` |
| Authorization Header | `http.authorization` |

## TLS

| Frage | Filter |
|---|---|
| TLS anzeigen | `tls` |
| TLS Client Hello | `tls.handshake.type == 1` |
| TLS Server Hello | `tls.handshake.type == 2` |
| SNI sichtbar | `tls.handshake.extensions_server_name` |
| SNI enthält Hostname | `tls.handshake.extensions_server_name contains "example.org"` |
| ALPN sichtbar | `tls.handshake.extensions_alpn_str` |
| TLS Alert | `tls.alert_message` |
| TLS Application Data | `tls.app_data` |
| Port 443 | `tcp.port == 443` |

## TCP Flags

| Frage | Filter |
|---|---|
| SYN ohne ACK | `tcp.flags.syn == 1 and tcp.flags.ack == 0` |
| SYN/ACK | `tcp.flags.syn == 1 and tcp.flags.ack == 1` |
| RST | `tcp.flags.reset == 1` |
| FIN | `tcp.flags.fin == 1` |
| ACK | `tcp.flags.ack == 1` |
| Port 80 Handshake-Kandidaten | `tcp.port == 80 and tcp.flags.syn == 1` |

## TCP Analysefelder

| Frage | Filter |
|---|---|
| alle TCP-Analysehinweise | `tcp.analysis.flags` |
| Retransmission | `tcp.analysis.retransmission` |
| Fast Retransmission | `tcp.analysis.fast_retransmission` |
| Duplicate ACK | `tcp.analysis.duplicate_ack` |
| Lost Segment Hinweis | `tcp.analysis.lost_segment` |
| Out of Order | `tcp.analysis.out_of_order` |
| Zero Window | `tcp.analysis.zero_window` |
| Window Update | `tcp.analysis.window_update` |

!!! note "Analysefelder"
    `tcp.analysis.*` Felder sind Wireshark-Interpretationen.  
    Sie sind sehr nützlich, müssen aber im Kontext geprüft werden.

## Logische Operatoren

| Zweck | Beispiel |
|---|---|
| UND | `dns and ip.addr == 192.0.2.53` |
| ODER | `dns or http` |
| NICHT | `not dns` |
| Klammern | `(dns or http) and ip.addr == 192.0.2.10` |

## Typische Kombinationsfilter

| Frage | Filter |
|---|---|
| DNS oder HTTP eines Clients | `(dns or http) and ip.addr == 192.0.2.10` |
| HTTP zu bestimmtem Server | `http and ip.addr == 192.0.2.20` |
| TLS Client Hello zu Server | `tls.handshake.type == 1 and ip.dst == 192.0.2.20` |
| TCP-Problemhinweise in Stream | `tcp.stream == 5 and tcp.analysis.flags` |
| RST zu bestimmtem Port | `tcp.port == 81 and tcp.flags.reset == 1` |

## Häufige Fallen

| Falle | Besser |
|---|---|
| `not dns` ohne Kontext | genau beschreiben, was ausgeschlossen wird |
| `contains` überall verwenden | lieber konkrete Felder filtern |
| HTTP in HTTPS erwarten | bei HTTPS nach `tls` und Metadaten suchen |
| Capture Filter und Display Filter mischen | Syntax bewusst trennen |
| Farbe als Diagnose verwenden | Paketdetails und Kontext prüfen |

## Merksatz

> Ein Filter ist keine Diagnose.  
> Ein Filter ist ein Werkzeug, um die relevanten Pakete zu finden.
