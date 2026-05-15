# Szenario

Du hast deine Lernumgebung eingerichtet und möchtest prüfen, ob Wireshark und TShark korrekt funktionieren.

Dazu erzeugst du einen kleinen, kontrollierten Mitschnitt.

Der Mitschnitt soll enthalten:

- DNS-Auflösung
- ICMP durch `ping`
- TCP/TLS-Verbindung durch `curl`

Der Capture muss keine perfekte Analyse liefern. Es geht um den ersten praktischen Kontakt mit einem selbst erzeugten Mitschnitt.

## Ausgangslage

Du arbeitest auf deinem Lernsystem.

Du hast Zugriff auf ein Terminal und kannst Wireshark starten.

Du erzeugst bewusst nur wenig Traffic, damit der Capture übersichtlich bleibt.

## Wichtige Einschränkung

In deinem System kann trotzdem Hintergrundtraffic auftreten.

Beispiele:

- Browser
- Updates
- Messenger
- Cloud-Sync
- IPv6 Neighbor Discovery
- mDNS
- Docker-Netzwerke

Das ist normal.

Die Aufgabe besteht darin, den relevanten Traffic mit Filtern zu finden.
