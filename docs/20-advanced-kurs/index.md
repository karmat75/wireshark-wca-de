# Erweiterter Kurs

Der erweiterte Kurs baut auf dem Basis-Kurs auf.

Im Basis-Kurs ging es darum, Protokolle sicher zu erkennen, einfache Filter zu verwenden und erste Beobachtungen korrekt einzuordnen.

Jetzt geht es stärker um echte Analyse:

- Warum ist eine Verbindung langsam?
- Warum wird eine Verbindung abgebrochen?
- Wo entsteht Wartezeit?
- Ist Paketverlust sichtbar?
- Ist der Capture vollständig?
- Liegt das Problem eher bei Netzwerk, Client, Server oder Anwendung?

## Erwartetes Vorwissen

Du solltest vor diesem Abschnitt sicher sein bei:

- Capture-Dateien öffnen und speichern
- Display Filter verwenden
- Ethernet, ARP und VLAN grob einordnen
- IPv4, IPv6 und ICMP erkennen
- UDP, DNS und DHCP analysieren
- TCP Handshake, FIN und RST erkennen
- TShark für einfache Abfragen verwenden

## Arbeitsweise im erweiterten Kurs

Im erweiterten Kurs reicht es nicht mehr, nur einzelne Pakete zu finden.

Du musst Beobachtungen in eine nachvollziehbare Analyse bringen.

Das bedeutet:

1. Symptom beschreiben
2. Capture-Punkt benennen
3. relevante Streams oder Flows finden
4. Filter dokumentieren
5. auffällige Pakete mit Frame-Nummern nennen
6. Hypothese bilden
7. alternative Erklärungen prüfen
8. Bewertung klar formulieren

## Wichtige Denkregel

> Wireshark zeigt nicht automatisch die Ursache.  
> Wireshark zeigt Beobachtungen. Die Ursache entsteht durch saubere Einordnung.

Das ist besonders wichtig bei TCP. Viele TCP-Hinweise sehen dramatisch aus, sind aber ohne Kontext nicht eindeutig.
