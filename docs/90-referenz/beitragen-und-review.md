# Beitragen und Review

Dieses Projekt soll offen, nachvollziehbar und sicher weiterentwickelt werden.

Dafür braucht es klare Regeln für Beiträge, Pull Requests, Reviews und Inhalte.

## Ziel

Diese Seite beantwortet:

- Wie sollen Beiträge vorbereitet werden?
- Was muss vor einem Pull Request geprüft werden?
- Welche Inhalte dürfen nicht ins Repository?
- Wie gehen wir mit PCAPs und Screenshots um?
- Wie werden Labs, Challenges und Quizzes ergänzt?
- Was sollte ein Review prüfen?

## Schnellstart für Beiträge

```bash
git checkout -b feature/mein-beitrag
```

Änderungen durchführen.

Dann prüfen:

```bash
source .venv/bin/activate
bash tools/quality/run_quality_checks.sh
```

Commit:

```bash
git add <dateien>
git commit -m "Add meaningful description"
git push
```

Dann Pull Request öffnen.

## Grundsätze

Beiträge sollen:

- fachlich korrekt sein
- auf Deutsch geschrieben sein
- didaktisch verständlich sein
- mit möglichst wenig Annahmen arbeiten
- Quellen sauber behandeln
- keine sensiblen Daten enthalten
- lokal geprüft werden
- nicht unnötig groß sein

## Schreibstil

Gut:

```text
Im Capture sind Retransmissions im TCP Stream sichtbar.
```

Nicht gut:

```text
Das Netzwerk ist kaputt.
```

Gut:

```text
Das Muster ist Beacon-ähnlich, beweist ohne Hostkontext aber keine Malware.
```

Nicht gut:

```text
Das ist Malware.
```

## Branch-Namen

Empfohlen:

```text
feature/<name>
fix/<name>
docs/<name>
lab/<name>
challenge/<name>
quiz/<name>
```

Beispiele:

```text
lab/dhcp-basics
challenge/tls-alert-triage
quiz/tcp-flags
fix/mkdocs-navigation
```

## Commit Messages

Gute Commit Messages beschreiben die Änderung.

Gut:

```text
Add HTTP TLS PCAP challenge
```

```text
Fix TShark command in DNS lab
```

```text
Add quiz questions for TCP flags
```

Nicht gut:

```text
update
```

```text
fix
```

```text
more stuff
```

## Pull Request Checkliste

Vor einem Pull Request:

- [ ] Änderung ist thematisch abgeschlossen
- [ ] `mkdocs build --strict` läuft
- [ ] `bash tools/quality/run_quality_checks.sh` läuft
- [ ] Quiz-/Exam-Validierung läuft, falls betroffen
- [ ] keine echten PCAPs enthalten
- [ ] keine Zugangsdaten enthalten
- [ ] keine echten Tokens enthalten
- [ ] Screenshots geprüft
- [ ] Navigation aktualisiert, falls neue Seiten ergänzt wurden
- [ ] `PACKAGE_CONTENTS.md` nur verwenden, wenn ein Paket eingespielt wurde

## PCAP-Regeln

Nicht erlaubt:

- produktive Captures
- Captures mit echten Zugangsdaten
- Captures mit Session-Cookies
- Captures mit API-Keys
- Captures mit personenbezogenen Daten
- Captures aus Kundensystemen
- fremde Captures ohne klare Lizenz

Erlaubt:

- synthetische Captures
- bewusst erzeugte Lab-Captures
- öffentliche Captures mit klarer Lizenz
- lokale Captures unter `pcaps/generated/`, wenn sie nicht committed werden

!!! warning "PCAPs sind oft sensibler als sie aussehen"
    Auch scheinbar harmlose Captures können interne Namen, IPs, Tokens, Cookies, Benutzer oder Anwendungsdaten enthalten.

## Screenshot-Regeln

Screenshots dürfen keine sensiblen Daten enthalten.

Vor dem Commit prüfen:

- Hostnamen
- Benutzernamen
- IP-Adressen
- URLs
- Tokens
- Cookies
- Session-IDs
- Pfade
- private Notizen
- personenbezogene Daten

Wenn nötig:

- neu mit synthetischen Daten erstellen
- sauber maskieren
- lieber Diagramm statt Screenshot verwenden

## Labs ergänzen

Neue Labs sollten unter `labs/` liegen und mindestens enthalten:

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

Ein Lab soll Lernende führen.

Das heißt:

- klare Ausgangslage
- konkrete Aufgaben
- Hinweise bei Bedarf
- Musterlösung
- saubere Bewertung
- keine echten Daten

## PCAP-Challenges ergänzen

Neue Challenges sollten unter `challenges/` liegen und mindestens enthalten:

```text
README.md
scenario.md
tasks.md
hints.md
solution.md
metadata.yml
check_tshark.sh
```

Eine Challenge soll weniger führen als ein Lab.

Sie soll prüfen, ob Lernende selbst:

- relevante Pakete finden
- Filter auswählen
- Frames belegen
- sauber bewerten
- nicht überinterpretieren

## Quizzes ergänzen

Quizfragen sollen:

- eindeutig sein
- eine klare richtige Antwort haben
- eine Erklärung enthalten
- zu einem Lernziel passen
- keine unnötigen Fangfragen sein

Nach Änderungen:

```bash
python3 tools/wwca/wwca.py quiz validate
```

## Review-Kriterien

Ein Review prüft:

| Bereich | Prüffrage |
|---|---|
| Build | läuft `mkdocs build --strict`? |
| Struktur | liegen Dateien am richtigen Ort? |
| Navigation | ist `mkdocs.yml` aktualisiert? |
| Sprache | ist der Text verständlich und deutsch? |
| Fachlichkeit | sind Aussagen korrekt und vorsichtig? |
| Didaktik | hilft der Abschnitt wirklich beim Lernen? |
| Sicherheit | sind keine sensiblen Daten enthalten? |
| Reproduzierbarkeit | lassen sich Labs/Challenges nachvollziehen? |
| Tools | laufen Check-Skripte ohne riskante Nebeneffekte? |

## Was nicht in ein Review gehört

Nicht jedes Review muss den Kurs neu erfinden.

Nicht hilfreich:

```text
Ich hätte alles anders strukturiert.
```

Hilfreich:

```text
In Aufgabe 6 fehlt der Hinweis, wie der TCP Stream Index gefunden wird.
```

Nicht hilfreich:

```text
Das ist schlecht.
```

Hilfreich:

```text
Die Aussage „Firewall blockt“ ist zu stark. Besser wäre: „Aus Sicht des Capture-Punkts ist keine Antwort sichtbar.“
```

## Umgang mit externen Quellen

Bevorzugt:

- offizielle Wireshark-Dokumentation
- Wireshark Wiki
- hochwertige Fachartikel
- seriöse Videos mit fachlichem Bezug
- RFCs, wenn sie Lernenden wirklich helfen

Nicht erwünscht:

- kopierte Inhalte
- unklare Lizenzen
- lange Zitate
- tote Links ohne Mehrwert
- SEO-Spam

## Umgang mit Fehlern

Fehler sind normal.

Wichtig ist:

- nachvollziehbar beschreiben
- kleine Korrektur erstellen
- lokale Checks laufen lassen
- PR öffnen
- Review ernst nehmen

## Merksatz

> Beiträge sollen den Kurs besser, sicherer und verständlicher machen.  
> Nicht größer um jeden Preis.
