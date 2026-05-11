# Wireshark installieren

Wireshark ist das zentrale Werkzeug dieses Kurses.

Zusätzlich installieren wir TShark und tcpdump, weil beide Werkzeuge für Labs, Automatisierung und spätere Prüfskripte wichtig sind.

## Installation

```bash
sudo apt update
sudo apt install -y wireshark tshark tcpdump
```

Während der Installation kann eine Frage erscheinen:

```text
Should non-superusers be able to capture packets?
```

Für ein persönliches Lernsystem sollte hier `Yes` beziehungsweise `Ja` gewählt werden.

Damit wird vorbereitet, dass normale Benutzer über die Gruppe `wireshark` Pakete mitschneiden dürfen.

## Falls die Abfrage nicht erschienen ist

Die Konfiguration kann nachträglich erneut aufgerufen werden:

```bash
sudo dpkg-reconfigure wireshark-common
```

Dort `Yes` beziehungsweise `Ja` wählen.

Danach den eigenen Benutzer zur Gruppe `wireshark` hinzufügen:

```bash
sudo usermod -aG wireshark "$USER"
```

Anschließend vollständig abmelden und wieder anmelden.

## Berechtigungen prüfen

Nach dem erneuten Login:

```bash
groups
```

Die Gruppe `wireshark` sollte enthalten sein.

Zusätzlich prüfen:

```bash
getcap /usr/bin/dumpcap
```

Typische Ausgabe:

```text
/usr/bin/dumpcap cap_net_admin,cap_net_raw=eip
```

## Versionen prüfen

```bash
wireshark --version
tshark --version
tcpdump --version
```

## Interfaces anzeigen

```bash
tshark -D
```

oder:

```bash
dumpcap -D
```

Wenn Interfaces angezeigt werden, ist die Grundkonfiguration einsatzbereit.

## Erster kurzer Capture-Test

Für einen sehr kurzen Test:

```bash
tshark -a duration:5 -w /tmp/wwca-test.pcapng
```

In einem zweiten Terminal währenddessen etwas Traffic erzeugen:

```bash
curl -I https://www.wireshark.org/
```

Danach prüfen:

```bash
capinfos /tmp/wwca-test.pcapng
```

## Wireshark starten

```bash
wireshark
```

Oder über das Anwendungsmenü.

## Zielzustand

Wireshark ist bereit, wenn:

- Wireshark als grafische Anwendung startet
- `tshark -D` Interfaces anzeigt
- ein kurzer Capture mit TShark möglich ist
- der Benutzer Mitglied der Gruppe `wireshark` ist
