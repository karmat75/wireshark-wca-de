# Display Filter

Display Filter sind eines der wichtigsten Werkzeuge in Wireshark.

Sie entscheiden, welche Pakete in einem geöffneten Mitschnitt angezeigt werden.

Der Mitschnitt selbst wird dadurch nicht verändert.

## Grundidee

Ein Display Filter beantwortet eine Frage an die Capture-Datei.

Beispiele:

| Frage | Display Filter |
|---|---|
| Welche DNS-Pakete gibt es? | `dns` |
| Welche TCP-Pakete gibt es? | `tcp` |
| Welche Pakete betreffen eine IP-Adresse? | `ip.addr == 1.1.1.1` |
| Welche Pakete gehen zu TCP-Port 443? | `tcp.port == 443` |
| Welche HTTP-Pakete gibt es? | `http` |

## Einfache Protokollfilter

Zeige DNS:

```text
dns
```

Zeige TCP:

```text
tcp
```

Zeige UDP:

```text
udp
```

Zeige ICMP:

```text
icmp
```

Zeige ARP:

```text
arp
```

Diese Filter sind gut für den Einstieg, aber oft zu breit.

## IP-Adressen filtern

Eine bestimmte IP-Adresse als Quelle oder Ziel:

```text
ip.addr == 1.1.1.1
```

Nur als Quelle:

```text
ip.src == 1.1.1.1
```

Nur als Ziel:

```text
ip.dst == 1.1.1.1
```

Für IPv6 gibt es entsprechende Felder:

```text
ipv6.addr == 2606:4700:4700::1111
```

## Ports filtern

TCP-Port als Quelle oder Ziel:

```text
tcp.port == 443
```

Nur Zielport:

```text
tcp.dstport == 443
```

Nur Quellport:

```text
tcp.srcport == 443
```

UDP-Port:

```text
udp.port == 53
```

## Bedingungen kombinieren

Und-Verknüpfung:

```text
ip.addr == 1.1.1.1 and tcp.port == 443
```

Oder-Verknüpfung:

```text
dns or icmp
```

Negation:

```text
not arp
```

Klammern helfen bei komplexeren Filtern:

```text
(ip.addr == 1.1.1.1 or ip.addr == 8.8.8.8) and dns
```

## Enthält Text

DNS-Namen enthalten einen Text:

```text
dns.qry.name contains "example"
```

HTTP Host enthält einen Text:

```text
http.host contains "example"
```

!!! note "Groß-/Kleinschreibung"
    Einige Vergleiche sind abhängig vom Feldtyp und der verwendeten Funktion.  
    Prüfe bei unerwarteten Ergebnissen den Filter und das Feld genau.

## Filter aus Paketdetails erzeugen

Du musst nicht jeden Feldnamen auswendig kennen.

Praktischer Weg:

1. Paket auswählen
2. im mittleren Bereich ein Feld suchen
3. Rechtsklick auf das Feld
4. `Apply as Filter`
5. passenden Filter auswählen

Das ist eine sehr gute Lernmethode.

So lernst du die tatsächlichen Wireshark-Feldnamen.

## Filter validieren

Die Filterleiste zeigt an, ob ein Filter gültig ist.

Typisch:

- grün: gültiger Filter
- rot: ungültiger Filter
- gelb oder Hinweis: Filter ist syntaktisch gültig, aber möglicherweise nicht ideal

Wenn ein Filter keine Pakete zeigt, heißt das nicht automatisch, dass er falsch ist.

Es kann auch bedeuten:

- solche Pakete sind im Capture nicht vorhanden
- du filterst auf das falsche Feld
- die Adresse oder der Port stimmt nicht
- der Traffic ist verschlüsselt oder anders erkannt
- das Protokoll wurde nicht dissektiert

## Display Filter mit TShark

TShark verwendet ebenfalls Display Filter.

Beispiel:

```bash
tshark -r pcaps/generated/basic-capture-01.pcapng -Y "dns"
```

DNS-Anfragen ausgeben:

```bash
tshark -r pcaps/generated/basic-capture-01.pcapng \
  -Y "dns.flags.response == 0" \
  -T fields \
  -e frame.number \
  -e ip.src \
  -e dns.qry.name
```

Das ist wichtig, weil du Filter damit reproduzierbar testen und dokumentieren kannst.

## Häufige Anfängerfehler

### Capture Filter und Display Filter verwechseln

Falsch als Display Filter:

```text
host 1.1.1.1
```

Richtig als Display Filter:

```text
ip.addr == 1.1.1.1
```

`host 1.1.1.1` ist Capture-Filter-Syntax, nicht Display-Filter-Syntax.

### Einzelnes Gleichheitszeichen verwenden

Falsch:

```text
ip.addr = 1.1.1.1
```

Richtig:

```text
ip.addr == 1.1.1.1
```

### Falsches Feld verwenden

Beispiel:

```text
ip.src == 1.1.1.1
```

zeigt nur Pakete, bei denen `1.1.1.1` die Quelle ist.

Wenn du Quelle oder Ziel meinst:

```text
ip.addr == 1.1.1.1
```

### Zu früh zu eng filtern

Wenn du sofort sehr eng filterst, übersiehst du leicht den Kontext.

Besser:

1. erst grob filtern
2. relevante Pakete finden
3. dann enger filtern

## Kleine Filter-Reihenfolge

Für einen unbekannten Capture ist oft diese Reihenfolge sinnvoll:

```text
dns
```

```text
ip.addr == <client-ip>
```

```text
tcp
```

```text
tcp.stream == <nummer>
```

```text
tcp.analysis.flags
```

Nicht jeder Filter passt zu jedem Fall.

Aber diese Reihenfolge hilft, vom Groben zum Konkreten zu kommen.

## Mini-Aufgabe

Öffne deinen Capture aus dem vorherigen Abschnitt:

```text
pcaps/generated/basic-capture-01.pcapng
```

Teste diese Filter:

```text
dns
```

```text
tcp
```

```text
udp
```

```text
icmp
```

```text
ip.addr == <deine-client-ip>
```

Beantworte:

1. Welche Filter zeigen Pakete?
2. Welche Filter zeigen keine Pakete?
3. Welche DNS-Namen findest du?
4. Welche TCP-Ports tauchen auf?
5. Welche Filter würdest du in einem Analysebericht dokumentieren?

## WCA-Bezug

Dieser Abschnitt übt WCA-nahe Grundlagen:

- Display Filter anwenden
- relevante Pakete isolieren
- Protokolle erkennen
- Feldnamen verwenden
- Filter mit Wireshark und TShark nutzen
- Analyse nachvollziehbar dokumentieren
