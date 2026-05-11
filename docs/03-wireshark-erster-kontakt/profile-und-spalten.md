# Profile und Spalten

Wireshark lässt sich stark anpassen.

Für den Kurs ist ein eigenes Profil sinnvoll, damit du die Oberfläche verändern kannst, ohne die Standardansicht zu verlieren.

## Warum Profile?

Ein Profil speichert unter anderem:

- Spalten
- Farben
- Filter-Buttons
- Protokolleinstellungen
- Darstellungseinstellungen

Damit kannst du zum Beispiel ein Kursprofil verwenden und später eigene Profile für Arbeit, Security-Analyse oder Performance-Troubleshooting erstellen.

## Neues Profil anlegen

In Wireshark:

```text
Edit > Configuration Profiles
```

Dann:

1. Profil duplizieren oder neu anlegen
2. Name vergeben
3. Profil auswählen

Empfohlener Name:

```text
wireshark-wca-de
```

## Sinnvolle Basisspalten

Die Standardspalten reichen für den Start aus, aber ein paar zusätzliche Spalten helfen später sehr.

Empfohlene Spalten:

| Spalte | Zweck |
|---|---|
| No. | Paketnummer |
| Time | Zeitpunkt/Zeitabstand |
| Source | Quelle |
| Destination | Ziel |
| Protocol | Protokoll |
| Length | Paketlänge |
| Info | Zusammenfassung |
| Delta time | Zeitabstand zum vorherigen angezeigten Paket |
| TCP Stream | Nummer des TCP-Streams |
| DNS Query | abgefragter DNS-Name |

Nicht jede Spalte ist in jedem Paket gefüllt.

Das ist normal.

## Spalte aus einem Feld erzeugen

Du kannst viele Felder direkt als Spalte hinzufügen.

Beispiel für DNS:

1. DNS-Paket auswählen
2. Im mittleren Bereich das Feld `Queries` öffnen
3. Feld mit dem DNS-Namen suchen
4. Rechtsklick auf das Feld
5. `Apply as Column`

Beispiel für TCP Stream:

1. TCP-Paket auswählen
2. TCP-Bereich öffnen
3. Feld `Stream index` suchen
4. Rechtsklick
5. `Apply as Column`

## Zeitdarstellung einstellen

Die Zeitspalte kann unterschiedlich dargestellt werden.

Für Analysen ist oft ein relativer Zeitbezug hilfreich.

Menü:

```text
View > Time Display Format
```

Sinnvolle Optionen:

- Seconds Since Beginning of Capture
- Seconds Since Previous Displayed Packet
- UTC Date and Time of Day

Für den Einstieg ist `Seconds Since Beginning of Capture` meist gut verständlich.

## Name Resolution

Wireshark kann Adressen in Namen auflösen.

Das ist manchmal hilfreich, kann aber auch verwirren oder zusätzlichen Netzwerkverkehr verursachen.

Menü:

```text
View > Name Resolution
```

Für den Anfang ist es oft besser, numerische IP-Adressen sichtbar zu lassen.

Später kannst du gezielt entscheiden, wann Namensauflösung hilfreich ist.

## Coloring Rules

Farben helfen bei der Orientierung.

Menü:

```text
View > Coloring Rules
```

Für den Anfang musst du hier nichts ändern.

Wichtig ist nur:

> Farben sind Hinweise, keine Diagnose.

## Profil sichern

Wireshark speichert Profile im Benutzerprofil.

Für den Kurs können wir später ein vorbereitetes Profil bereitstellen.

Bis dahin reicht:

- eigenes Profil anlegen
- Spalten bewusst ergänzen
- Änderungen nicht im Default-Profil vornehmen

## Mini-Aufgabe

Lege ein Profil an:

```text
wireshark-wca-de
```

Öffne deinen ersten Mitschnitt und ergänze mindestens eine zusätzliche Spalte:

- TCP Stream
- DNS Query
- Delta time

Speichere nichts Besonderes.

Wireshark speichert die Profilanpassungen automatisch.
