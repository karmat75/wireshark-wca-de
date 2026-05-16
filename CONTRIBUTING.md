# Contributing

Danke, dass du zu **Wireshark WCA DE** beitragen möchtest.

Dieses Projekt ist ein deutschsprachiger Open-Source-Selbstlernkurs zur Netzwerkanalyse mit Wireshark und TShark, ausgerichtet an WCA-101.

## Grundsätze

Beiträge sollen:

- fachlich korrekt sein
- auf Deutsch geschrieben sein
- verständlich und didaktisch sauber sein
- keine produktiven oder personenbezogenen Daten enthalten
- keine echten Zugangsdaten, Tokens oder privaten PCAPs enthalten
- mit lokalen Checks geprüft werden
- in kleinen, nachvollziehbaren Pull Requests erfolgen

## Was willkommen ist

Willkommen sind insbesondere:

- Korrekturen an bestehenden Kapiteln
- zusätzliche Erklärungen
- neue Labs
- neue PCAP-Challenges
- neue Quizfragen
- bessere Hinweise und Musterlösungen
- neue Referenzen zu offiziellen oder hochwertigen Quellen
- bessere Screenshots, sofern sie keine sensiblen Daten enthalten
- Verbesserungen an Tools und CI

## Sprache und Stil

Bitte schreibe:

- sachlich
- direkt
- ohne unnötiges Fachchinesisch
- mit deutschen Erklärungen für Lernende
- technische Begriffe nur dort eingedeutscht, wo es sinnvoll ist
- mit klarer Trennung zwischen Beobachtung, Bewertung und Vermutung

Beispiel:

```text
Im Capture sind TCP Retransmissions sichtbar.
```

Besser als:

```text
Das Netzwerk ist kaputt.
```

## Branches

Empfohlen:

```text
feature/<kurzer-name>
fix/<kurzer-name>
docs/<kurzer-name>
lab/<kurzer-name>
challenge/<kurzer-name>
```

Beispiele:

```text
feature/tshark-cheatsheet
lab/dhcp-basics
challenge/tls-alert-triage
fix/display-filter-typo
```

## Commit Messages

Gute Commit Messages:

```text
Add TCP retransmission PCAP challenge
```

```text
Fix markdown fence in TShark cheatsheet
```

```text
Add display filter quiz questions
```

Weniger hilfreich:

```text
update
```

```text
stuff
```

```text
fix
```

## Lokale Prüfung

Vor einem Pull Request bitte ausführen:

```bash
source .venv/bin/activate
bash tools/quality/run_quality_checks.sh
```

Mindestens sollte funktionieren:

```bash
mkdocs build --strict
python3 tools/wwca/wwca.py quiz validate
python3 tools/wwca/wwca.py exam validate
```

## PCAP-Regeln

Nicht committen:

- produktive PCAPs
- PCAPs mit personenbezogenen Daten
- PCAPs mit echten IPs aus sensiblen Umgebungen
- PCAPs mit echten Zugangsdaten
- PCAPs mit echten Tokens, Session-Cookies oder API-Keys
- unklare fremde PCAPs ohne Lizenz

Erlaubt:

- synthetische PCAPs
- selbst erzeugte Docker-Lab-PCAPs, sofern sie bewusst freigegeben werden
- öffentliche PCAPs mit klarer Lizenz und Quellenangabe
- lokale generated PCAPs nur zur eigenen Bearbeitung, nicht als Standard-Commit

Standardpfad für lokale Captures:

```text
pcaps/generated/
```

## Screenshots

Screenshots dürfen keine sensiblen Daten enthalten.

Vor dem Commit prüfen:

- keine echten Hostnamen
- keine echten Benutzer
- keine internen IPs, wenn nicht ausdrücklich erlaubt
- keine Tokens
- keine Passwörter
- keine privaten Notizen
- keine personenbezogenen Daten

Details siehe:

```text
docs/90-referenz/screenshot-styleguide.md
```

## Labs

Neue Labs sollten enthalten:

```text
README.md
scenario.md
tasks.md
hints.md
solution.md
metadata.yml
```

Optional:

```text
check_tshark.sh
```

Wenn ein Lab Docker benötigt, sollte es unterhalb von `docker/compose/` eine eigene Umgebung oder eine dokumentierte Wiederverwendung geben.

## Challenges

Neue PCAP-Challenges sollten enthalten:

```text
README.md
scenario.md
tasks.md
hints.md
solution.md
metadata.yml
check_tshark.sh
```

Eine Challenge soll weniger führen als ein Lab und mehr Eigenleistung verlangen.

## Quizzes

Quizfragen sollen:

- eindeutig sein
- eine klare richtige Antwort haben
- falsche Antworten plausibel, aber nicht unfair machen
- mit einer kurzen Erklärung versehen sein
- keine reinen Fangfragen sein

Nach Änderungen:

```bash
python3 tools/wwca/wwca.py quiz validate
```

## Pull Requests

Ein Pull Request sollte enthalten:

- kurze Beschreibung
- betroffene Bereiche
- durchgeführte Checks
- Hinweise zu Screenshots, PCAPs oder Docker-Labs
- offene Punkte

Bitte die Pull-Request-Vorlage verwenden.

## Review-Kriterien

Ein Review prüft mindestens:

- baut MkDocs sauber?
- sind Links und Navigation plausibel?
- sind Formulierungen fachlich sauber?
- wird zwischen Beobachtung und Bewertung getrennt?
- sind keine sensiblen Daten enthalten?
- sind Labs/Challenges reproduzierbar?
- sind Check-Skripte ungefährlich und nachvollziehbar?

## Lizenz und Quellen

Bei neuen Quellen:

- offizielle Quellen bevorzugen
- Lizenz beachten
- keine geschützten Inhalte kopieren
- nur kurze Zitate verwenden, wenn nötig
- lieber verlinken und zusammenfassen

## Merksatz

> Dieses Projekt soll Lernenden helfen, echte Analysefähigkeit aufzubauen.  
> Jeder Beitrag sollte dieses Ziel unterstützen.
