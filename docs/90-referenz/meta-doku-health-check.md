# Meta-Doku-Health-Check

Diese Seite hilft dabei, sekundär relevante Projektdateien regelmäßig auf Aktualität zu prüfen.

Ziel ist nicht Perfektion, sondern ein stabiler, wiederholbarer Mindeststandard.

## Wann prüfen?

Empfohlen:

- bei jedem Release
- nach größeren Strukturänderungen im Repository
- nach neuen Labs, Challenges oder Quizpaketen
- vor längeren Beitragsphasen mit mehreren Mitwirkenden

## Welche Dateien zuerst?

Priorität A:

- `README.md`
- `AGENTS.md`
- `CONTRIBUTING.md`
- `mkdocs.yml`

Priorität B:

- `PACKAGE_CONTENTS.md` (falls Paket-Workflow genutzt wurde)
- `tools/README.md`
- `docs/90-referenz/beitragen-und-review.md`
- `.github/pull_request_template.md`

Priorität C:

- Kapitel-Indexseiten unter `docs/**/index.md`
- Übersichtsseiten zu Labs, Quizzes und Challenges

## Schnellcheck in 10 Minuten

1. Stimmen die in `README.md` genannten Ordner noch mit der realen Struktur überein?
2. Verweisen Doku und Contributor-Hinweise auf vorhandene Dateien und Skripte?
3. Sind Namenskonventionen konsistent (z. B. `check_tshark.sh` statt veralteter Varianten)?
4. Sind neue Docs-Seiten in `mkdocs.yml` und in passenden Indexseiten eingehängt?
5. Sind Status- und Roadmap-Texte noch realistisch oder inzwischen überholt?
6. Sind Sicherheits- und Datenschutzhinweise unverändert klar und korrekt?

## Typische Drift-Muster

Achte besonders auf diese wiederkehrenden Probleme:

- Strukturblöcke mit veralteten Ordnern
- falsche Dateinamen durch Groß-/Kleinschreibung
- Hinweise auf nicht vorhandene Dev-Umgebungen
- alte Befehle nach Tool-Refactoring
- fehlende Navigationseinträge für neue Seiten

## Empfohlener Ablauf

1. Struktur prüfen:

```bash
find . -maxdepth 2 -type d | sort
```

2. Potenziell veraltete Begriffe suchen:

```bash
grep -nE "geplant|im Aufbau|TODO|Milestone|DevContainer" README.md AGENTS.md CONTRIBUTING.md
```

3. Referenzpfade verifizieren:

```bash
for p in README.md AGENTS.md CONTRIBUTING.md mkdocs.yml .github/pull_request_template.md; do
  [[ -e "$p" ]] && echo "OK   $p" || echo "MISS $p"
done
```

4. Dokumentation bauen:

```bash
mkdocs build --strict
```

5. Qualitätscheck ausführen:

```bash
bash tools/quality/run_quality_checks.sh
```

## Entscheidungsregel bei Abweichungen

Wenn die Doku dem Code widerspricht, gilt:

1. Erst reale Repo-Struktur verifizieren.
2. Dann Doku auf den Ist-Zustand anpassen.
3. Nur dann Strukturen umbauen, wenn das bewusstes Ziel des Changes ist.

## Definition von "aktuell genug"

Eine Meta-Datei gilt als aktuell genug, wenn:

- alle referenzierten Pfade existieren
- Beispiele den tatsächlichen Konventionen entsprechen
- die Beschreibung weder irreführend noch historisch veraltet ist
- neue Hauptbereiche in Navigation und Übersichten auftauchen

## Mini-Checkliste für Pull Requests

- [ ] Meta-Dateien bei Strukturänderungen mitgepflegt
- [ ] keine toten Links oder tote Pfadreferenzen
- [ ] `mkdocs build --strict` erfolgreich
- [ ] Qualitätschecks erfolgreich

## Merksatz

> Inhalt driftet schnell, Meta-Doku driftet schneller.  
> Ein kurzer Health-Check verhindert später große Aufräumarbeiten.
