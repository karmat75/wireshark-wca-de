# Quizzes

Dieser Bereich sammelt Wiederholungsfragen und später auch Modulprüfungen.

Die Quizzes sind keine echten WCA-Prüfungsfragen.

Sie sind eigene Kursfragen, die helfen sollen, Wissen, Bedienung und Analysefähigkeit zu festigen.

## Ziel

Quizzes sollen helfen:

- Begriffe zu wiederholen
- typische Denkfehler zu erkennen
- Display Filter sicherer zu verwenden
- Protokolle besser einzuordnen
- Analysefragen prüfungsnah zu beantworten
- Lücken vor Labs und PCAP-Challenges sichtbar zu machen

## Aktuelle Quizbereiche

| Quiz | Inhalt | Datei |
|---|---|---|
| [Foundation-Quiz](foundation-quiz.md) | Umgebung, Wireshark-Oberfläche, TShark, Linux-Grundlagen | `quizzes/questions/foundation.yml` |
| [Basic-Quiz](basic-quiz.md) | Display Filter, Ethernet, ARP, IP, ICMP, UDP, DNS, DHCP, TCP | `quizzes/questions/basic.yml` |

## Lokales Quiz-Tool

Die YAML-Fragen können jetzt lokal im Terminal ausgeführt werden.

Siehe:

```text
docs/50-quizzes/lokales-quiz-tool.md
```

Beispiel:

```bash
python3 tools/wwca/wwca.py quiz run foundation
```

## Arbeitsweise

Die Fragen liegen maschinenlesbar unter:

```text
quizzes/questions/
```

Das lokale Tool liest diese Dateien ein, stellt Fragen im Terminal und speichert Fortschritt lokal.

## Keine Exam Dumps

!!! warning "Keine echten Prüfungsfragen"
    Dieser Kurs enthält keine echten WCA-Prüfungsfragen und keine Exam Dumps.  
    Die Fragen sind eigene Lernfragen, die auf Verständnis und Analysefähigkeit zielen.

## Geplante Ausbaustufen

| Stufe | Ziel |
|---|---|
| 1 | YAML-Fragen sammeln |
| 2 | einfache lokale Auswertung per Python |
| 3 | Modulprüfungen definieren |
| 4 | Fortschritt lokal speichern |
| 5 | PCAP-basierte Fragen einbinden |
| 6 | WCA-nahe Probeprüfung erstellen |
