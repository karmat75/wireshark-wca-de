# Erstes Capture öffnen

In diesem Abschnitt erzeugst du einen kleinen eigenen Mitschnitt und öffnest ihn anschließend wieder.

Damit prüfst du gleichzeitig, ob Wireshark auf deinem System grundsätzlich funktioniert.

## Vorbereitung

Öffne ein Terminal und prüfe, ob grundlegende Netzwerkbefehle verfügbar sind:

```bash
ping -c 1 example.org
dig +short example.org
curl -I https://example.org
```

Wenn einer dieser Befehle fehlt, installiere die Basiswerkzeuge:

```bash
sudo apt update
sudo apt install -y curl dnsutils iputils-ping
```

## Wireshark starten

Starte Wireshark über das Anwendungsmenü oder im Terminal:

```bash
wireshark
```

Wenn Wireshark keine Interfaces anzeigt oder keine Aufnahme starten kann, prüfe die Capture-Rechte aus dem Abschnitt zur Wireshark-Installation.

## Passendes Interface auswählen

Wähle das Interface aus, über das dein normaler Netzwerkverkehr läuft.

Häufig ist das:

- ein WLAN-Interface wie `wlp...`
- ein kabelgebundenes Interface wie `enp...`, `eno...` oder `eth...`

Wenn du unsicher bist, kannst du vorher prüfen:

```bash
ip route
```

Die Zeile mit `default via` zeigt meist das aktive Interface.

Beispiel:

```text
default via 192.168.1.1 dev wlp2s0
```

In diesem Beispiel wäre `wlp2s0` das interessante Interface.

## Aufnahme starten

Starte die Aufnahme über einen Doppelklick auf das Interface.

Danach erzeugst du im Terminal etwas Traffic:

```bash
ping -c 4 example.org
dig example.org
curl -I https://example.org
```

Stoppe die Aufnahme anschließend in Wireshark mit dem roten Stop-Button.

## Mitschnitt speichern

Speichere die Datei im Repository unter:

```text
pcaps/generated/first-contact.pcapng
```

Falls der Ordner noch nicht existiert:

```bash
mkdir -p pcaps/generated
```

In Wireshark:

```text
File > Save As
```

Dateiname:

```text
first-contact.pcapng
```

## Mitschnitt wieder öffnen

Schließe den Mitschnitt oder starte Wireshark neu.

Dann öffne die Datei:

```text
File > Open
```

oder im Terminal:

```bash
wireshark pcaps/generated/first-contact.pcapng
```

## Erste Filter ausprobieren

Zeige nur DNS-Pakete:

```text
dns
```

Zeige nur ICMP-Pakete:

```text
icmp
```

Zeige nur TCP-Pakete:

```text
tcp
```

Zeige Pakete zu einer bestimmten IP-Adresse:

```text
ip.addr == 93.184.216.34
```

Die IP-Adresse kann bei dir anders sein. Prüfe sie über DNS:

```bash
dig +short example.org
```

## Was solltest du sehen?

Je nach System und Netzwerk solltest du ungefähr sehen:

- DNS-Anfragen für `example.org`
- ICMP-Pakete vom `ping`
- TCP-Verbindungen vom `curl`
- TLS-Verkehr, wenn HTTPS verwendet wurde

Nicht jedes Netzwerk sieht gleich aus.

Das ist normal.

## Wenn du sehr viel Traffic siehst

Während einer Aufnahme läuft oft mehr Netzwerkverkehr als erwartet.

Das können sein:

- Browser-Tabs
- Systemupdates
- Messenger
- Cloud-Sync
- DNS im Hintergrund
- mDNS oder IPv6 Neighbor Discovery
- Docker-Netzwerke

Für den Anfang ist das kein Problem.

Später lernst du, mit Filtern gezielt die relevanten Pakete zu finden.

## Mini-Aufgabe

Öffne deinen Mitschnitt und beantworte:

1. Wie viele Pakete enthält die Datei?
2. Welche Protokolle zeigt Wireshark in der Spalte `Protocol`?
3. Welche DNS-Anfragen findest du?
4. Welche IP-Adresse wurde für `example.org` verwendet?
5. Gibt es ICMP-Pakete?
6. Gibt es TCP-Pakete?

Nutze dafür noch keine perfekte Analyse.

Es geht nur darum, die Oberfläche zu benutzen und erste Fragen an den Mitschnitt zu stellen.
