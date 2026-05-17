# Advanced Lab 050: Interface Counter Triage

Dieses Lab ist bewusst kein reines Wireshark-Klick-Lab.

Es trainiert die wichtigste Fähigkeit bei Interface Errors und Discards:

> Vor dem Capture die richtige Frage stellen.

Du bekommst ein generisches Monitoring-Symptom, einen vereinfachten Geräte-Counter-Auszug und eine Topologie-Beschreibung.

Deine Aufgabe ist, zu entscheiden:

- ob Wireshark helfen kann
- wo ein Capture sinnvoll wäre
- welche anderen Prüfungen wichtiger sind
- welche Aussagen belegt sind
- welche Aussagen zu stark wären

## Lab-Pfad

```text
labs/advanced/lab-advanced-050-interface-counter-triage/
```

## Ziel

Du übst:

- Errors und Discards zu unterscheiden
- In-/Out-Richtung zu bewerten
- Monitoring-Daten nicht zu überinterpretieren
- Wireshark-Grenzen bei CRC/FCS zu verstehen
- Capture-Punkte sinnvoll auszuwählen
- reale Troubleshooting-Schritte zu planen
- einen kurzen Triage-Bericht zu schreiben

## Besonderheit

Dieses Lab erzeugt keinen eigenen PCAP.

Das ist Absicht.

Nicht jedes Netzwerkproblem beginnt mit einem Capture.

Manchmal ist die richtige Analyseentscheidung:

```text
Wireshark ist hier nicht der erste Schritt.
```

## WCA-/Praxisbezug

Dieses Lab trainiert:

- Troubleshooting-Methodik
- Capture-Punkt-Auswahl
- Grenzen von Wireshark
- TCP-Symptome vs. Interface-Counter
- Beobachtung vs. Ursache
- reale Arbeitsweise mit Monitoring und Switch-/Routerdaten
