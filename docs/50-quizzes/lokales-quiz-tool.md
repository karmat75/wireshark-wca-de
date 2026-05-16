# Lokales Quiz-Tool

Das lokale Quiz-Tool macht die YAML-Fragen aus `quizzes/questions/` im Terminal nutzbar.

Es ist bewusst einfach gehalten.

Es soll helfen, Fragen lokal zu beantworten und Fortschritt zu speichern, ohne einen zentralen Server zu benötigen.

## Speicherort

Tool:

```text
tools/wwca/wwca.py
```

Wrapper:

```text
tools/wwca/wwca
```

Fragen:

```text
quizzes/questions/
```

Fortschritt:

```text
~/.local/share/wireshark-wca-de/progress.json
```

## Voraussetzung

Du brauchst Python 3.

Zusätzlich wird PyYAML benötigt.

Prüfen:

```bash
python3 -c "import yaml; print('PyYAML OK')"
```

Falls PyYAML fehlt:

```bash
python3 -m pip install PyYAML
```

Oder innerhalb der Kurs-venv:

```bash
source .venv/bin/activate
python -m pip install PyYAML
```

## Quizzes auflisten

```bash
python3 tools/wwca/wwca.py quiz list
```

Oder über den Wrapper:

```bash
tools/wwca/wwca quiz list
```

## Fragen validieren

```bash
python3 tools/wwca/wwca.py quiz validate
```

Das prüft grob:

- YAML-Dateien lesbar
- Fragen vorhanden
- IDs eindeutig
- Antwortoptionen vorhanden
- richtige Antworten vorhanden
- Referenzen gesetzt

## Quiz ausführen

Foundation:

```bash
python3 tools/wwca/wwca.py quiz run foundation
```

Basic:

```bash
python3 tools/wwca/wwca.py quiz run basic
```

## Anzahl begrenzen

```bash
python3 tools/wwca/wwca.py quiz run basic --limit 10
```

## Fragen mischen

```bash
python3 tools/wwca/wwca.py quiz run basic --shuffle
```

## Fortschritt anzeigen

```bash
python3 tools/wwca/wwca.py progress
```

## Fortschritt exportieren

```bash
python3 tools/wwca/wwca.py progress export ./mein-fortschritt.json
```

## Fortschritt zurücksetzen

```bash
python3 tools/wwca/wwca.py progress reset
```

Das fragt zur Sicherheit nach Bestätigung.

## Bedienung im Quiz

Bei Single-Choice-Fragen:

```text
Antwort: 1
```

Bei Multiple-Choice-Fragen:

```text
Antwort: 1,3,4
```

Leer lassen zählt als nicht beantwortet und falsch.

## Bewertung

Das Tool zeigt am Ende:

- Anzahl Fragen
- richtige Antworten
- Prozentwert
- grobe Bewertung

| Ergebnis | Bedeutung |
|---:|---|
| 90–100 % | sehr sicher |
| 80–89 % | prüfungsnah gut |
| 70–79 % | solide, Lücken prüfen |
| 60–69 % | Grundlagen wiederholen |
| unter 60 % | Thema erneut durcharbeiten |

## Grenzen

Das Tool ist ein erster Schritt.

Es unterstützt aktuell:

- `single-choice`
- `multiple-choice`
- einfache Fortschrittsspeicherung
- JSON-Export

Noch nicht enthalten:

- PCAP-Fragen
- Zeitlimit
- Modulprüfungen
- Import von Fortschritt
- gewichtete Bewertung
- Weboberfläche

## Merksatz

> Das Quiz-Tool ersetzt keine Analyse-Labs.  
> Es hilft, Wissen und Denkfehler regelmäßig zu prüfen.
