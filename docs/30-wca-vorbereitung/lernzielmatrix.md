# Lernzielmatrix

Die Lernzielmatrix verbindet die offiziellen WCA-Kompetenzbereiche mit den Inhalten dieses Kurses.

Sie ist bewusst pragmatisch aufgebaut.

Der Status sagt nicht nur, ob ein Thema irgendwo erwähnt wird. Entscheidend ist, ob es auch praktisch trainiert wird.

## Statuswerte

| Status | Bedeutung |
|---|---|
| Offen | Thema fehlt weitgehend |
| Erklärt | Thema ist im Kurs erklärt |
| Teilweise trainiert | Übungen oder Aufgaben vorhanden, aber noch nicht vollständig |
| Trainiert | Lab, Quiz und Lösung vorhanden |
| Prüfungsnah | Thema hat Lab, Quiz, Challenge und Wiederholung |

## Übersicht nach WCA-Bereichen

| WCA-Bereich | Gewichtung laut Objectives | Kursabdeckung | Status |
|---|---:|---|---|
| Wireshark-Funktionen | 10 % | erster Kontakt, Profile, TShark, Performanceanalyse | Erklärt |
| Capture-Methoden | 10 % | Lernumgebung, Capture-Grundlagen, TShark Headless | Erklärt |
| Capture- und Display Filter | 12 % | Display Filter, TShark, Basis-Kurs | Erklärt |
| Oberfläche und Profile | 5 % | Oberfläche, Profile und Spalten | Erklärt |
| Protokolle | 43 % | Ethernet, ARP, IPv4, IPv6, ICMP, UDP, DHCP, DNS, TCP | Erklärt |
| Troubleshooting | 20 % | TCP Deep Dive, Performanceanalyse, Fehleranalyse-Methodik | Erklärt |

!!! important "Aktueller Stand"
    Der Kurs erklärt viele WCA-Themen bereits gut.  
    Für echte Prüfungsnähe brauchen wir als nächstes Labs, Quizzes, PCAP-Challenges und Screenshots.

## 1. Wireshark-Funktionen

| Lernziel | Kursinhalt | Lab | Quiz | Status |
|---|---|---|---|---|
| Capture-Dateien öffnen, speichern und schließen | erster Kontakt, Capture-Grundlagen | fehlt | fehlt | Erklärt |
| pcap und pcapng unterscheiden | Capture-Grundlagen | fehlt | fehlt | Teilweise |
| Pakete oder Paketbereiche exportieren | fehlt | fehlt | fehlt | Offen |
| Objekte aus Captures exportieren | HTTP/TLS, Security-Basics | fehlt | fehlt | Teilweise |
| Find Packet verwenden | fehlt | fehlt | fehlt | Offen |
| Packet Comments und File Comments verwenden | fehlt | fehlt | fehlt | Offen |
| Time Reference setzen und entfernen | Performanceanalyse | fehlt | fehlt | Teilweise |
| Zeitformate anwenden | Performanceanalyse | fehlt | fehlt | Erklärt |
| Name Resolution verstehen und konfigurieren | Profile und Spalten | fehlt | fehlt | Teilweise |
| Decode As verwenden | fehlt | fehlt | fehlt | Offen |
| Capture File Properties auswerten | fehlt | fehlt | fehlt | Offen |
| Protocol Hierarchy verwenden | Performanceanalyse, Methodik, Security | fehlt | fehlt | Erklärt |
| Conversations verwenden | Methodik, Security | fehlt | fehlt | Erklärt |
| Endpoints verwenden | Methodik, Security | fehlt | fehlt | Erklärt |
| I/O Graph erstellen und interpretieren | Performanceanalyse | fehlt | fehlt | Erklärt |
| echte Capture-Bytes von generierten Feldern unterscheiden | TCP Deep Dive | fehlt | fehlt | Teilweise |
| Follow TCP/UDP Stream verwenden | TCP-Grundlagen, HTTP/TLS | fehlt | fehlt | Erklärt |

## 2. Capture-Methoden

| Lernziel | Kursinhalt | Lab | Quiz | Status |
|---|---|---|---|---|
| Endpunkt-Capture bewerten | Capture-Grundlagen, Methodik | fehlt | fehlt | Erklärt |
| TAP, Mirror Port und Infrastruktur-Capture vergleichen | Capture-Grundlagen | fehlt | fehlt | Teilweise |
| Multi-Point Capture einordnen | Fehleranalyse-Methodik | fehlt | fehlt | Teilweise |
| richtiges Interface auswählen | erstes Capture, Capture-Grundlagen | fehlt | fehlt | Erklärt |
| Capture starten, stoppen und neu starten | erstes Capture | fehlt | fehlt | Erklärt |
| Capture nach Größe, Paketanzahl oder Dauer begrenzen | fehlt | fehlt | fehlt | Offen |
| Ring Buffer verwenden | fehlt | fehlt | fehlt | Offen |
| Capture speichern | erstes Capture, Capture-Grundlagen | fehlt | fehlt | Erklärt |
| Pakete in neue Datei exportieren | fehlt | fehlt | fehlt | Offen |
| Command Line Capture verwenden | TShark, TShark Headless | fehlt | fehlt | Erklärt |
| Promiscuous Mode und Monitor Mode einordnen | Ethernet/ARP/VLAN | fehlt | fehlt | Teilweise |

## 3. Filter

| Lernziel | Kursinhalt | Lab | Quiz | Status |
|---|---|---|---|---|
| Capture Filter und Display Filter unterscheiden | Capture-Grundlagen, Display Filter | fehlt | fehlt | Erklärt |
| Capture Filter für Protokoll/IP/MAC/Port verwenden | Display Filter, Capture-Grundlagen | fehlt | fehlt | Teilweise |
| Display Filter manuell erstellen | Display Filter | fehlt | fehlt | Erklärt |
| Display Filter per Rechtsklick erstellen | Display Filter | fehlt | fehlt | Erklärt |
| Display Filter per Drag/Drop erstellen | fehlt | fehlt | fehlt | Offen |
| Membership Filter verwenden | fehlt | fehlt | fehlt | Offen |
| logische Operatoren verwenden | Display Filter | fehlt | fehlt | Erklärt |
| Display Filter Buttons erstellen | fehlt | fehlt | fehlt | Offen |
| unvollständige Filterergebnisse erkennen | Display Filter, HTTP/TLS | fehlt | fehlt | Teilweise |
| Negation und any/all-Fallen verstehen | fehlt | fehlt | fehlt | Offen |
| Filter aus Conversations/Endpoints anwenden | Methodik | fehlt | fehlt | Teilweise |
| Filter mit generierten Feldern erstellen | Display Filter, TCP Deep Dive | fehlt | fehlt | Teilweise |

## 4. Oberfläche und Profile

| Lernziel | Kursinhalt | Lab | Quiz | Status |
|---|---|---|---|---|
| GUI-Bereiche benennen | Oberfläche verstehen | fehlt | fehlt | Erklärt |
| Layout anpassen | fehlt | fehlt | fehlt | Offen |
| Wert von Profilen erklären | Profile und Spalten | fehlt | fehlt | Erklärt |
| Profile erstellen, kopieren und ändern | Profile und Spalten | fehlt | fehlt | Erklärt |
| Spalten für Troubleshooting nutzen | Profile und Spalten | fehlt | fehlt | Erklärt |
| Spalten auf mehrere Arten hinzufügen | Profile und Spalten | fehlt | fehlt | Teilweise |
| Coloring Rules nutzen | Profile und Spalten | fehlt | fehlt | Teilweise |
| Minimap / farbige Seitenleiste nutzen | fehlt | fehlt | fehlt | Offen |
| Colorize Conversation verwenden | fehlt | fehlt | fehlt | Offen |
| Protocol Preferences verstehen | HTTP/TLS, TCP Deep Dive | fehlt | fehlt | Teilweise |
| Pakete markieren und entmarkieren | fehlt | fehlt | fehlt | Offen |

## 5. Protokolle

| Protokollbereich | Kursinhalt | Lab | Quiz | Status |
|---|---|---|---|---|
| Ethernet | Ethernet, ARP und VLAN | fehlt | fehlt | Erklärt |
| ARP | Ethernet, ARP und VLAN | fehlt | fehlt | Erklärt |
| IPv4 | IPv4, IPv6 und ICMP | fehlt | fehlt | Erklärt |
| ICMPv4 | IPv4, IPv6 und ICMP | fehlt | fehlt | Erklärt |
| IPv6 | IPv4, IPv6 und ICMP | fehlt | fehlt | Erklärt |
| ICMPv6 | IPv4, IPv6 und ICMP | fehlt | fehlt | Erklärt |
| UDP | UDP, DNS und DHCP | fehlt | fehlt | Erklärt |
| DHCPv4 | UDP, DNS und DHCP | fehlt | fehlt | Erklärt |
| DNS | UDP, DNS und DHCP | fehlt | fehlt | Erklärt |
| TCP | TCP-Grundlagen, TCP Deep Dive | fehlt | fehlt | Erklärt |

## 6. Troubleshooting

| Lernziel | Kursinhalt | Lab | Quiz | Status |
|---|---|---|---|---|
| Topologie aus Capture ableiten | OSI-Referenz, Methodik | fehlt | fehlt | Teilweise |
| TCP Sequence und ACK analysieren | TCP Deep Dive | fehlt | fehlt | Erklärt |
| Server Performance von langsamer Übertragung unterscheiden | Performanceanalyse, HTTP/TLS | fehlt | fehlt | Erklärt |
| hohe RTT bei Request/Response-Protokollen bewerten | Performanceanalyse | fehlt | fehlt | Erklärt |
| niedrige Window Size und hohe RTT einordnen | TCP Deep Dive, Performanceanalyse | fehlt | fehlt | Teilweise |
| ARP-, DHCP- und ICMP-Probleme erkennen | Basis-Kurs | fehlt | fehlt | Erklärt |

## Priorisierte Lücken

| Priorität | Thema | Warum wichtig? |
|---:|---|---|
| 1 | Labs zu Display Filter, DNS, TCP und HTTP/TLS | zentrale Prüfungskompetenz |
| 2 | Wireshark-Funktionen wie Find Packet, Comments, Export, Decode As | aktuell noch zu wenig behandelt |
| 3 | Capture-Begrenzung und Ring Buffer | WCA-relevant und praxisnah |
| 4 | Filter-Fallen: Membership, Negation, any/all | WCA-relevant und fehleranfällig |
| 5 | Screenshots zur Oberfläche, Filterleiste, Conversations, I/O Graphs | für Lernende sehr hilfreich |
| 6 | Modulprüfungen und Quizfragen | Prüfungsvorbereitung braucht Wiederholung |
| 7 | PCAP-Challenges | echte Analysefähigkeit trainieren |

## Nächster Ausbau

Der nächste sinnvolle Ausbauschritt nach dieser Matrix:

```text
1. externe Ressourcen-Matrix
2. Lab-Templates
3. erstes Foundation-Lab
4. erstes Docker-Lab
5. erste Quizfragen
6. Screenshot-Styleguide
```
