# Qualitätssicherung und CI

Der Kurs ist inzwischen mehr als ein paar Markdown-Dateien.

Es gibt:

- Dokumentation
- Labs
- Docker-Compose-Umgebungen
- Quizzes
- Exams
- PCAP-Challenges
- lokale Tools
- Vorlagen

Damit Änderungen nicht versehentlich etwas kaputt machen, braucht das Repository einfache und wiederholbare Checks.

## Ziel

Qualitätssicherung soll helfen:

- MkDocs-Buildfehler früh zu finden
- kaputte Quiz- oder Exam-Dateien zu erkennen
- offensichtliche Markdown-Probleme zu finden
- wichtige Repository-Verzeichnisse zu prüfen
- Pull Requests sicherer zu machen
- lokale Prüfung und CI möglichst gleich zu halten

## Lokale Prüfung

Aus dem Repository-Root:

```bash
bash tools/quality/run_quality_checks.sh
```

Der Sammelcheck führt aktuell aus:

```text
python3 tools/quality/check_repo_structure.py
python3 tools/quality/check_markdown_fences.py
python3 tools/wwca/wwca.py quiz validate
python3 tools/wwca/wwca.py exam validate
mkdocs build --strict
```

## Einzelchecks

Repository-Struktur prüfen:

```bash
python3 tools/quality/check_repo_structure.py
```

Markdown-Code-Fences prüfen:

```bash
python3 tools/quality/check_markdown_fences.py
```

Quizfragen prüfen:

```bash
python3 tools/wwca/wwca.py quiz validate
```

Modulprüfungen prüfen:

```bash
python3 tools/wwca/wwca.py exam validate
```

MkDocs bauen:

```bash
mkdocs build --strict
```

## GitHub Actions

Der Workflow liegt unter:

```text
.github/workflows/ci.yml
```

Er läuft bei:

- Push auf `main`
- Pull Requests gegen `main`
- manueller Ausführung über `workflow_dispatch`

## Was die CI prüft

Die CI prüft:

1. Repository auschecken
2. Python einrichten
3. Python-Abhängigkeiten installieren
4. lokale Qualitätschecks ausführen
5. MkDocs-Site bauen
6. Site-Artefakt hochladen

## Warum `mkdocs build --strict`?

`--strict` sorgt dafür, dass Warnungen den Build fehlschlagen lassen.

Das ist gewollt.

Eine Kurs-Webseite sollte nicht stillschweigend mit kaputten Links, fehlenden Dateien oder fehlerhafter Navigation gebaut werden.

## Was die Checks nicht prüfen

Die Checks prüfen aktuell nicht:

- fachliche Korrektheit
- alle externen Links
- ob Docker-Labs wirklich starten
- ob PCAP-Captures in jeder Umgebung gleich aussehen
- ob Screenshots aktuell sind
- ob jede Aufgabe didaktisch perfekt ist

Das bleibt Review-Arbeit.

## Empfohlener Ablauf vor einem Commit

```bash
source .venv/bin/activate
bash tools/quality/run_quality_checks.sh
git status --short
```

Wenn alles passt:

```bash
git add <dateien>
git commit -m "<sinnvolle commit message>"
git push
```

## Empfohlener Ablauf für Pull Requests

1. kleine Änderungseinheiten erstellen
2. lokal prüfen
3. Commit erstellen
4. Push
5. CI abwarten
6. Review durchführen
7. erst dann mergen

## Gute Commit Messages

Gut:

```text
Add TCP retransmission PCAP challenge
```

```text
Fix markdown fence validation in quality tools
```

```text
Add HTTP TLS analysis lab
```

Weniger gut:

```text
update
```

```text
stuff
```

```text
fix
```

## Merksatz

> CI ersetzt kein Review.  
> CI verhindert aber, dass offensichtliche Fehler unbemerkt bleiben.
