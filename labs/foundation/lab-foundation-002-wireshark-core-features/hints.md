# Hinweise

## Hinweis 1: Keine PCAP-Datei vorhanden

Erzeuge zuerst eine Datei mit einem vorherigen Lab:

```text
Foundation Lab 001
Basic Lab 020
Basic Lab 030
```

Danach sollte unter `pcaps/generated/` eine `.pcapng` liegen.

## Hinweis 2: Find Packet findet nichts

Prüfe:

- Suchmodus
- ob du nach Paketbytes, String oder Display Filter suchst
- Groß-/Kleinschreibung
- ob der Suchbegriff wirklich im Capture vorkommt

Alternativ nutze Display Filter:

```text
dns
http
tcp.flags.reset == 1
```

## Hinweis 3: Packet Comments nicht sichtbar

Je nach Wireshark-Version musst du Kommentare über Paketdetails oder Kontextmenü setzen.

Prüfe auch, ob du die Datei danach als `pcapng` speicherst.

Klassisches `pcap` kann weniger Metadaten speichern.

## Hinweis 4: Export Specified Packets

Wenn du markierte Pakete exportieren willst:

1. Pakete markieren
2. `File > Export Specified Packets`
3. Option für markierte oder angezeigte Pakete wählen
4. als `.pcapng` speichern

## Hinweis 5: Time Reference verwirrt

Time Reference ändert die Zeitdarstellung relativ zu einem gewählten Paket.

Wenn es unübersichtlich wird:

```text
Edit > Time Reference > Remove All Time References
```

oder Zeitformat wieder umstellen.

## Hinweis 6: Decode As nicht erzwingen

Decode As ist nützlich, wenn Wireshark ein Protokoll wegen ungewöhnlicher Ports nicht automatisch erkennt.

In diesem Lab musst du nichts dauerhaft ändern.

Nur ansehen, verstehen, dokumentieren.
