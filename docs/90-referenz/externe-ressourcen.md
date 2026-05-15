# Externe Ressourcen

Diese Seite sammelt externe Ressourcen, die für den Kurs und die WCA-Vorbereitung besonders nützlich sind.

Sie ist bewusst als zentrale Link-Matrix gedacht.

Spätere Kapitel, Labs und Quizfragen können von hier aus gezielt auf passende Quellen verweisen.

## Grundregel

Externe Ressourcen werden verlinkt, nicht ungeprüft kopiert.

Das gilt besonders für:

- Artikel
- Videos
- Kursunterlagen
- Folien
- PCAP-Dateien
- Prüfungsunterlagen
- fremde Labs

!!! warning "Lizenz und Urheberrecht"
    Nur weil etwas im Internet verfügbar ist, darf es nicht automatisch in dieses Repository kopiert werden.  
    Wenn die Lizenz unklar ist, wird verlinkt und nicht übernommen.

## Offizielle Wireshark-Ressourcen

Diese Quellen haben die höchste Priorität, wenn es um Wireshark selbst geht.

| Ressource | Link | Wofür nutzen? |
|---|---|---|
| Wireshark Website | <https://www.wireshark.org/> | Einstieg, Downloads, Projektinformationen |
| Wireshark Resource Hub | <https://www.wireshark.org/resources> | zentrale Sammlung offizieller Ressourcen |
| Wireshark Learn | <https://www.wireshark.org/learn> | Einstieg, Grundlagen, erste Schritte |
| Wireshark Documentation | <https://www.wireshark.org/docs/> | Dokumentation, Manpages, User Guide |
| Wireshark User's Guide | <https://www.wireshark.org/docs/wsug_html/> | Bedienung, Capture, Analysefunktionen |
| Wireshark Display Filter Reference | <https://www.wireshark.org/docs/dfref/> | Feldnamen und Display-Filter |
| Wireshark Manual Pages | <https://www.wireshark.org/docs/man-pages/> | TShark, dumpcap, editcap, mergecap usw. |
| TShark Manual Page | <https://www.wireshark.org/docs/man-pages/tshark.html> | TShark-Optionen und CLI-Verhalten |
| Wireshark Wiki | <https://wiki.wireshark.org/> | Zusatzwissen, Protokollseiten, Beispiele |
| Wireshark Sample Captures | <https://wiki.wireshark.org/SampleCaptures> | Beispiel-PCAPs zum Üben |
| Wireshark Blog | <https://www.wireshark.org/blog/> | Projektneuigkeiten und Hinweise |
| Wireshark Community | <https://www.wireshark.org/community> | SharkFest, Community und Veranstaltungen |

## WCA-Ressourcen

| Ressource | Link | Wofür nutzen? |
|---|---|---|
| Wireshark Certifications | <https://www.wireshark.org/certifications/> | offizielle Zertifizierungsseite |
| WCA-101 Exam Objectives PDF | <https://www.wireshark.org/pdf/wca-objectives.pdf> | Grundlage für Lernzielmatrix und Abdeckung |

!!! important "Vor der Prüfung prüfen"
    Prüfungsdetails können sich ändern.  
    Vor Anmeldung zur Prüfung immer die offiziellen Informationen auf der Wireshark-Seite prüfen.

## Display Filter

Die Display Filter Reference ist eine Pflichtressource.

Wireshark unterstützt sehr viele Protokolle und Felder. Niemand sollte versuchen, alle Feldnamen auswendig zu lernen.

Wichtiger ist:

- passende Felder in Wireshark finden
- Rechtsklick auf Felder nutzen
- `Apply as Filter` verwenden
- offizielle Display Filter Reference nachschlagen
- Filter in TShark reproduzierbar testen

| Thema | Link |
|---|---|
| Display Filter Reference | <https://www.wireshark.org/docs/dfref/> |
| Display Filters im Wireshark Wiki | <https://wiki.wireshark.org/DisplayFilters> |
| Capture Filters im Wireshark Wiki | <https://wiki.wireshark.org/CaptureFilters> |

## TShark und Command Line

TShark ist für diesen Kurs ein Kernwerkzeug.

| Ressource | Link | Wofür nutzen? |
|---|---|---|
| TShark im User's Guide | <https://www.wireshark.org/docs/wsug_html_chunked/AppToolstshark.html> | Einordnung von TShark |
| TShark Manual Page | <https://www.wireshark.org/docs/man-pages/tshark.html> | Optionen und Verhalten |
| tshark.dev | <https://tshark.dev/> | praxisnahe TShark-Anleitungen |

## Sample Captures und PCAPs

PCAP-Dateien sind für diesen Kurs sehr wichtig.

Sie müssen aber lizenzrechtlich und datenschutztechnisch sauber behandelt werden.

| Ressource | Link | Hinweis |
|---|---|---|
| Wireshark Sample Captures | <https://wiki.wireshark.org/SampleCaptures> | offizielle Wiki-Sammlung |
| Kurose/Ross Wireshark Labs | <https://gaia.cs.umass.edu/kurose_ross/wireshark.php> | sehr gute Lehr-Labs, nicht ungeprüft kopieren |
| Stratosphere IPS Dataset | <https://www.stratosphereips.org/datasets-overview> | Security-nahe Datasets, Lizenz und Zweck prüfen |
| Malware-Traffic-Analysis.net | <https://www.malware-traffic-analysis.net/> | nur in sicherer Lab-Umgebung nutzen |

!!! warning "Security-Captures"
    Malware- oder Incident-Captures dürfen nicht leichtfertig verwendet werden.  
    Sie können schädliche Inhalte, personenbezogene Daten oder reale Infrastrukturinformationen enthalten. Für den Kurs bevorzugen wir synthetische, selbst erzeugte oder klar lizenzierte Captures.

## Kurose/Ross Wireshark Labs

Die Kurose/Ross Labs sind didaktisch sehr wertvoll, weil Lernende Netzwerkprotokolle praktisch beobachten.

Sie eignen sich besonders als ergänzende Ressource für:

- HTTP
- DNS
- TCP
- UDP
- IP
- ICMP
- Ethernet/ARP
- DHCP
- NAT

Link:

<https://gaia.cs.umass.edu/kurose_ross/wireshark.php>

Wichtig:

> Diese Labs werden verlinkt und nicht kopiert.  
> Eigene Kurslabs können sich didaktisch inspirieren lassen, müssen aber eigene Aufgaben, Texte und Captures verwenden.

## SharkFest und Videos

SharkFest ist eine sehr wertvolle Quelle für fortgeschrittene Wireshark- und Packet-Analysis-Themen.

| Ressource | Link | Wofür nutzen? |
|---|---|---|
| Wireshark Community / SharkFest | <https://www.wireshark.org/community> | Veranstaltungen und Community |
| Wireshark Resources | <https://www.wireshark.org/resources> | Verweise auf SharkFest YouTube und Ressourcen |
| Wireshark YouTube | <https://www.youtube.com/@WiresharkFoundation> | Vorträge, Tutorials, Aufzeichnungen |

Mögliche Video-Kategorien für den Kurs:

- Wireshark Einstieg
- Display Filter
- TCP Analyse
- Performanceanalyse
- TLS Analyse
- Troubleshooting-Methodik
- Security Analysis

## Deutschsprachige Ressourcen

Deutschsprachige Ressourcen sind willkommen, sollten aber fachlich geprüft werden.

Mögliche Kriterien:

- aktuell genug
- keine irreführenden Vereinfachungen
- keine offensiven Anleitungen ohne defensiven Kontext
- klare Trennung zwischen Capture Filter und Display Filter
- verantwortlicher Umgang mit Captures und Datenschutz

Beispiele für nützliche deutschsprachige Ergänzungen:

- Linux-/Ubuntu-Wikis zur Installation
- deutschsprachige Artikel zu Netzwerkgrundlagen
- deutschsprachige Vorträge oder Workshops
- eigene Kursseiten in diesem Repository

## Protokollbezogene Ressourcenzuordnung

Diese Tabelle hilft, spätere Kapitel und Labs mit externen Quellen zu verbinden.

| Kursbereich | Externe Ressourcen |
|---|---|
| Lernumgebung | Wireshark Learn, User's Guide, Ubuntu-/Pop!_OS-Dokumentation |
| Wireshark erster Kontakt | Wireshark Learn, User's Guide |
| TShark | TShark Manual Page, TShark User Guide, tshark.dev |
| Display Filter | Display Filter Reference, DisplayFilters Wiki |
| Capture Filter | CaptureFilters Wiki, TShark Manual Page |
| Ethernet/ARP/VLAN | User's Guide, Sample Captures, Kurose/Ross Ethernet/ARP Labs |
| IPv4/IPv6/ICMP | Display Filter Reference, Kurose/Ross IP/ICMP Labs |
| UDP/DNS/DHCP | Kurose/Ross DNS/UDP Labs, Sample Captures |
| TCP | Kurose/Ross TCP Lab, SharkFest/TCP-Videos, TShark |
| HTTP/TLS | Kurose/Ross HTTP Lab, Wireshark TLS-Dokumentation, Sample Captures |
| Performance | Wireshark Statistics, I/O Graphs, TCP Stream Graphs, SharkFest |
| Security-Basics | Wireshark Sample Captures, Security-Datasets, defensive Analyseartikel |
| WCA-Vorbereitung | WCA-Objectives, User's Guide, eigene Labs und Quizzes |

## Ressourcenblock für Kurskapitel

Jedes Kurskapitel kann am Ende einen Ressourcenblock bekommen.

Beispiel:

```markdown
## Weiterführende Ressourcen

- Offizielle Wireshark-Dokumentation:
  - [Wireshark User's Guide](https://www.wireshark.org/docs/wsug_html/)
  - [Display Filter Reference](https://www.wireshark.org/docs/dfref/)
- Praktische Übungen:
  - [Kurose/Ross Wireshark Labs](https://gaia.cs.umass.edu/kurose_ross/wireshark.php)
- TShark:
  - [TShark Manual Page](https://www.wireshark.org/docs/man-pages/tshark.html)
```

## Ressourcenblock für Labs

Jedes Lab sollte gezielter verlinken.

Beispiel für ein DNS-Lab:

```markdown
## Weiterführende Ressourcen

- [Wireshark Display Filter Reference: DNS](https://www.wireshark.org/docs/dfref/d/dns.html)
- [Kurose/Ross Wireshark Labs](https://gaia.cs.umass.edu/kurose_ross/wireshark.php)
- [TShark Manual Page](https://www.wireshark.org/docs/man-pages/tshark.html)
```

## Bewertung externer Quellen

Vor dem Verlinken einer Quelle prüfen:

| Frage | Bewertung |
|---|---|
| Ist die Quelle fachlich zuverlässig? | bevorzugt offizielle oder etablierte Quellen |
| Ist sie aktuell genug? | besonders wichtig bei Tools und Prüfung |
| Ist die Lizenz klar? | wichtig, wenn Inhalte übernommen werden sollen |
| Ist der Inhalt defensiv und kursgeeignet? | besonders bei Security-Themen |
| Ist der Inhalt für Lernende verständlich? | nicht zu abstrakt, nicht zu beliebig |
| Ergänzt die Quelle wirklich das Kursziel? | keine Link-Sammlung ohne Zweck |

## Was nicht in diese Ressourcensammlung gehört

Nicht aufnehmen:

- Exam Dumps
- echte Prüfungsfragen
- unseriöse Zertifizierungsseiten
- urheberrechtlich kopierte PDFs
- private PCAPs
- produktive Incident-Captures
- offensive Anleitungen ohne defensiven Lernkontext
- Links ohne klaren Nutzen für den Kurs

## Pflegehinweise

Diese Seite sollte regelmäßig aktualisiert werden.

Besonders prüfungsnahe Links müssen aktuell bleiben:

- WCA-Objectives
- Wireshark-Versionen
- TShark-Optionen
- Dokumentationslinks
- externe PCAP-Sammlungen
- Video- und Kurslinks

## Nächster Ausbauschritt

Nach dieser Ressourcenseite sollten wir die Links gezielt in die bestehenden Kapitel einbauen.

Priorität:

1. Display Filter
2. TShark
3. TCP Deep Dive
4. HTTP/TLS
5. Performanceanalyse
6. Security-Basics
7. Labs und PCAP-Challenges

## Merksatz

> Gute externe Ressourcen ersetzen den Kurs nicht.  
> Sie machen ihn stärker, überprüfbarer und anschlussfähig an die Wireshark-Community.
