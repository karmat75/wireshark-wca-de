# Hinweise

## Hinweis 1: Interface finden

Wenn du unsicher bist, welches Interface du nutzen sollst:

```bash
ip route
```

Die Zeile mit `default` zeigt meist dein aktives Interface.

## Hinweis 2: Keine DNS-Pakete sichtbar

Wenn du keine DNS-Pakete siehst, kann das mehrere Gründe haben:

- DNS-Antwort kam aus Cache
- Browser oder System nutzt DoH/DoT
- falsches Interface
- Capture wurde zu spät gestartet
- Filter ist falsch
- `dig` wurde nicht während des Captures ausgeführt

Wiederhole den Capture und starte ihn vor dem `dig`.

## Hinweis 3: Zu viel Traffic

Wenn sehr viel Traffic sichtbar ist, nutze Display Filter.

Beginne mit:

```text
dns
```

Dann:

```text
icmp
```

Dann:

```text
tcp
```

## Hinweis 4: Client-IP herausfinden

Prüfe deine IP-Adressen:

```bash
ip addr
```

Oder einfacher für die Default-Route:

```bash
ip route get 1.1.1.1
```

Dort steht meist die verwendete Quell-IP.

## Hinweis 5: TShark findet keine Datei

Prüfe den Pfad:

```bash
ls -l pcaps/generated/
```

Die Datei sollte heißen:

```text
lab-foundation-001-first-capture.pcapng
```

## Hinweis 6: Capture-Rechte fehlen

Wenn Wireshark oder TShark keine Interfaces mitschneiden darf, prüfe:

```bash
groups
tshark -D
```

Wenn die Gruppe `wireshark` fehlt, siehe Kursabschnitt zur Wireshark-Installation und Rechtevergabe.
