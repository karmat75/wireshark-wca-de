# Szenario

Du hast einen Capture aus einem Lab erstellt.

Jetzt sollst du die Datei nicht nur anschauen, sondern professionell als Analyseobjekt vorbereiten.

Ein Kollege oder eine Kollegin soll später nachvollziehen können:

- welche Datei analysiert wurde
- wie groß der Capture ist
- welche Pakete wichtig sind
- welche Filter verwendet wurden
- welcher Zeitraum relevant ist
- welche Pakete exportiert wurden
- welche Kommentare du gesetzt hast

Dieses Lab ist damit ein Brückenschritt von „ich klicke durch Wireshark“ zu „ich dokumentiere eine Analyse nachvollziehbar“.

## Ausgangslage

Du verwendest eine lokale PCAP-Datei aus einem vorherigen Lab.

Beispiele:

```text
pcaps/generated/lab-basic-020-dns-http-docker.pcapng
pcaps/generated/lab-basic-030-tcp-handshake-reset.pcapng
```

## Erwartete Arbeit

Du sollst mit Wireshark-Funktionen arbeiten, nicht nur mit Display Filtern.

Wichtig:

> Notiere jeden verwendeten Arbeitsschritt so, dass er später wiederholbar ist.
