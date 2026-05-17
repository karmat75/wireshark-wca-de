# Interface-Counter-Quiz

Dieses Quiz wiederholt den Advanced-Praxisblock zu Interface Errors, Discards und Monitoring-Triage.

## Datei

```text
quizzes/questions/interface-counters.yml
```

## Aktueller Umfang

```text
12 Fragen
```

## Themen

- Errors vs. Discards
- In-/Out-Richtung
- CRC/FCS und Wireshark-Grenzen
- OutDiscards und Queue Drops
- Capture-Punkte
- SPAN/TAP-Grenzen
- Monitoring-Korrelation
- Berichtssprache
- reale nächste Schritte

## Nutzung

```bash
python3 tools/wwca/wwca.py quiz run interface-counters
```

Mit zufälliger Reihenfolge:

```bash
python3 tools/wwca/wwca.py quiz run interface-counters --shuffle
```

Als Modulprüfung:

```bash
python3 tools/wwca/wwca.py exam run module-interface-counters
```

## Ziel

Das Quiz prüft nicht nur Begriffe.

Es prüft vor allem, ob du die wichtigste Frage beantworten kannst:

```text
Kann Wireshark hier helfen — und wenn ja, wobei genau?
```
