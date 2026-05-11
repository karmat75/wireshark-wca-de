# Netzwerkbefehle

In diesem Kurs wirst du regelmäßig einfache Netzwerkbefehle verwenden.

Sie helfen dir, Netzwerkverhalten außerhalb von Wireshark zu prüfen und gezielt Traffic zu erzeugen.

## IP-Adressen anzeigen

```bash
ip addr
```

Kurzform:

```bash
ip a
```

Wichtig sind:

- Interface-Name
- IPv4-Adresse
- IPv6-Adresse
- Status `UP` oder `DOWN`

Beispiel für ein Interface:

```text
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP>
    inet 192.168.1.50/24
```

## Routing anzeigen

```bash
ip route
```

Typische Ausgabe:

```text
default via 192.168.1.1 dev enp0s3
192.168.1.0/24 dev enp0s3 proto kernel scope link src 192.168.1.50
```

Die `default`-Route ist das Standard-Gateway.

## DNS prüfen

```bash
dig example.org
```

Kurzere Ausgabe:

```bash
dig +short example.org
```

Alternative:

```bash
nslookup example.org
```

Im Kurs bevorzugen wir meistens `dig`, weil die Ausgabe für Analysezwecke gut geeignet ist.

## Erreichbarkeit prüfen

```bash
ping example.org
```

Abbrechen mit:

```text
Ctrl + C
```

!!! note "Ping ist kein vollständiger Verbindungstest"
    Wenn `ping` funktioniert, heißt das nicht automatisch, dass HTTP, HTTPS, DNS oder eine Anwendung funktionieren. Wenn `ping` nicht funktioniert, kann ICMP auch bewusst blockiert sein.

## Route zum Ziel prüfen

```bash
traceroute example.org
```

Falls `traceroute` fehlt:

```bash
sudo apt install -y traceroute
```

## HTTP testen

Nur Header abrufen:

```bash
curl -I https://example.org
```

Ausführlicher Verbindungsaufbau:

```bash
curl -v https://example.org
```

Eine URL abrufen und Ausgabe verwerfen:

```bash
curl -o /dev/null -s -w "%{http_code}\n" https://example.org
```

## Offene Ports prüfen

Mit `ss`:

```bash
ss -ltnp
```

Bedeutung:

- `-l`: listening
- `-t`: TCP
- `-n`: numerische Ausgabe
- `-p`: Prozess anzeigen

Beispiel für Port 8000:

```bash
ss -ltnp | grep ':8000'
```

## Namen und Adressen im Kurs

Viele Labs verwenden Container-Namen, lokale Dienste oder Testdomains.

Beispiele:

```text
client
web-ok
web-slow
dns-lab
```

Diese Namen funktionieren meist nur innerhalb der jeweiligen Docker-Lab-Umgebung.

## Traffic gezielt erzeugen

Für Wireshark-Übungen brauchst du oft kontrollierten Traffic.

Beispiele:

```bash
ping -c 4 1.1.1.1
dig example.org
curl -I https://example.org
```

Diese Befehle erzeugen Pakete, die du anschließend in Wireshark sehen und analysieren kannst.

## Wichtige Kursregel

Erst prüfen, dann analysieren:

1. Was ist meine eigene IP-Adresse?
2. Welche Route wird verwendet?
3. Funktioniert DNS?
4. Funktioniert die Zielverbindung?
5. Was zeigt Wireshark dazu?
