# Paket 41: Interface Errors, Discards und Monitoring-Triage

Dieses Paket ergänzt den Kurs um einen praxisnahen Advanced-Block zu Interface-Countern, Discards, Errors und der Frage, wann Wireshark helfen kann.

## Enthaltene Dateien

```text
mkdocs.yml
docs/20-advanced-kurs/index.md
docs/20-advanced-kurs/06-interface-errors-discards.md
docs/40-labs-und-uebungen/index.md
docs/40-labs-und-uebungen/advanced-interface-counter-triage.md
docs/50-quizzes/index.md
docs/50-quizzes/modulpruefungen.md
docs/50-quizzes/interface-counter-quiz.md
docs/60-pcap-challenges/index.md
docs/60-pcap-challenges/challenge-007-discards-retransmission-correlation.md
docs/90-referenz/index.md
docs/90-referenz/interface-counter-cheatsheet.md
labs/advanced/lab-advanced-050-interface-counter-triage/README.md
labs/advanced/lab-advanced-050-interface-counter-triage/scenario.md
labs/advanced/lab-advanced-050-interface-counter-triage/tasks.md
labs/advanced/lab-advanced-050-interface-counter-triage/hints.md
labs/advanced/lab-advanced-050-interface-counter-triage/solution.md
labs/advanced/lab-advanced-050-interface-counter-triage/metadata.yml
challenges/challenge-007-discards-retransmission-correlation/README.md
challenges/challenge-007-discards-retransmission-correlation/scenario.md
challenges/challenge-007-discards-retransmission-correlation/tasks.md
challenges/challenge-007-discards-retransmission-correlation/hints.md
challenges/challenge-007-discards-retransmission-correlation/solution.md
challenges/challenge-007-discards-retransmission-correlation/metadata.yml
challenges/challenge-007-discards-retransmission-correlation/check_tshark.sh
quizzes/questions/interface-counters.yml
quizzes/exams/module-interface-counters.yml
```

## Ziel

Der neue Block macht das Monitoring-Thema bewusst generisch:

- Monitoring-Systeme zeigen Interface-Counter und Zeitfenster.
- Switches/Router klassifizieren Counter genauer.
- Wireshark zeigt Traffic-Muster und Auswirkungen.
- Die Ursache entsteht erst durch Korrelation aus Zeit, Counter, Topologie und Capture-Punkt.

Der Block trainiert besonders:

- Interface Errors und Discards unterscheiden
- In-/Out-Richtung korrekt bewerten
- Wireshark-Grenzen bei CRC/FCS/physikalischen Fehlern verstehen
- Retransmissions und Duplicate ACKs als Symptome einordnen
- SPAN/TAP/Host-Capture realistisch bewerten
- reale Troubleshooting-Methodik anwenden
- keine vorschnellen Ursachen behaupten
