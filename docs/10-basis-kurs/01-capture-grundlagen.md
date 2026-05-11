# Capture-Grundlagen

Ein Capture ist ein Mitschnitt von Netzwerkverkehr.

Wireshark und TShark können diesen Verkehr live erfassen oder vorhandene Capture-Dateien öffnen.

Eine Capture-Datei ist aber nur dann hilfreich, wenn sie an der richtigen Stelle und mit der richtigen Fragestellung erstellt wurde.

## Die wichtigste Frage

Bevor du mitschneidest, frage:

> Welches Problem will ich mit diesem Capture beantworten?

Beispiele:

- Kommt der Client überhaupt beim Server an?
- Wird DNS korrekt aufgelöst?
- Antwortet der Server?
- Gibt es TCP-Retransmissions?
- Bricht die Verbindung mit einem Reset ab?
- Ist das Problem vor oder hinter einem Gateway sichtbar?

Ohne Frage wird ein Capture schnell zu einer großen Paket-Sammlung ohne klare Aussage.

## Wo mitschneiden?

Der Capture-Punkt entscheidet, was du sehen kannst.

Typische Capture-Punkte:

| Ort | Vorteil | Nachteil |
|---|---|---|
| Client | zeigt die Sicht des Benutzers | sieht nicht alles im Netzwerk |
| Server | zeigt, ob Anfragen ankommen | sieht nicht, was vorher verloren ging |
| Gateway/Firewall | zeigt Übergänge zwischen Netzen | braucht Zugriff und saubere Filter |
| Switch Mirror Port | gute Netzwerksicht | muss korrekt konfiguriert sein |
| TAP | sehr sauberer Mitschnitt | zusätzliche Hardware nötig |

## Client- und Server-Sicht

Wenn ein Client sagt: „Die Anwendung ist langsam“, kann ein Client-Capture zeigen:

- DNS-Auflösung
- TCP-Verbindungsaufbau
- TLS-Handshake
- HTTP-Anfragen
- Wartezeiten aus Sicht des Clients

Ein Server-Capture zeigt dagegen:

- ob die Anfrage am Server ankommt
- wann der Server antwortet
- ob der Server die Verbindung schließt
- ob der Server Retransmissions sieht

Beide Sichtweisen können unterschiedlich aussehen.

Das ist normal und oft sehr hilfreich.

## Was ein Capture nicht zeigen kann

Ein Capture zeigt nur, was am Capture-Punkt sichtbar ist.

Wenn du am Client mitschneidest, siehst du nicht automatisch:

- interne Switch-Weiterleitung
- Firewall-Entscheidungen hinter dem Client
- Pakete, die nie beim Client ankommen
- Traffic anderer Systeme
- verschlüsselte Nutzdaten in TLS-Verbindungen

Wireshark zeigt keine Wahrheit über das gesamte Netzwerk.

Wireshark zeigt die Wahrheit am Capture-Punkt.

## Capture-Dateiformate

Wireshark verwendet heute standardmäßig `pcapng`.

Typische Dateiendungen:

| Endung | Bedeutung |
|---|---|
| `.pcapng` | modernes Capture-Format |
| `.pcap` | klassisches Capture-Format |
| `.cap` | unspezifisch, oft ebenfalls Capture-Dateien |

Für den Kurs verwenden wir bevorzugt:

```text
.pcapng
```

## Live-Capture vs. Datei-Analyse

Es gibt zwei Arbeitsweisen:

| Arbeitsweise | Beispiel |
|---|---|
| Live-Capture | direkt auf einem Interface mitschneiden |
| Datei-Analyse | vorhandene `.pcapng` öffnen und untersuchen |

Im Kurs verwenden wir beides.

Für viele Übungen ist eine Datei-Analyse besser, weil alle Lernenden dieselbe Ausgangslage haben.

Für Praxisübungen erzeugen wir auch eigene Captures.

## Capture Filter vs. Display Filter

Das ist einer der wichtigsten Unterschiede.

| Filtertyp | Zeitpunkt | Wirkung |
|---|---|---|
| Capture Filter | vor oder während der Aufnahme | entscheidet, was gespeichert wird |
| Display Filter | nach der Aufnahme | entscheidet, was angezeigt wird |

Beispiel Capture Filter:

```text
host 1.1.1.1
```

Beispiel Display Filter:

```text
ip.addr == 1.1.1.1
```

!!! warning "Wichtig"
    Ein Capture Filter kann Pakete dauerhaft ausschließen.  
    Was nicht mitgeschnitten wurde, kann später nicht analysiert werden.

Für den Anfang verwenden wir bevorzugt Display Filter.

## Warum nicht immer alles mitschneiden?

Alles mitzuschneiden klingt erstmal sicher.

Es hat aber Nachteile:

- große Dateien
- unübersichtliche Analyse
- sensible Daten
- höhere Last
- schwierigeres Teilen
- längere Suchzeit

Trotzdem ist für den Einstieg ein breiter Mitschnitt oft besser als ein zu enger Capture Filter.

Die Kunst ist, nicht zu viel und nicht zu wenig zu erfassen.

## Kleine Capture-Strategie

Für viele Fälle funktioniert diese Reihenfolge gut:

1. Problem beschreiben
2. Capture-Punkt auswählen
3. möglichst wenig Hintergrundtraffic erzeugen
4. Capture starten
5. Problem reproduzieren
6. Capture stoppen
7. Datei speichern
8. Analyse mit Display Filtern beginnen
9. Ergebnis mit Paketnummern belegen

## Beispiel: DNS-Problem

Fragestellung:

> Kann der Client den Namen `example.org` auflösen?

Capture-Punkt:

```text
Client
```

Traffic erzeugen:

```bash
dig example.org
```

Analysefilter:

```text
dns
```

Mögliche Beobachtungen:

- DNS-Anfrage vorhanden
- DNS-Antwort vorhanden
- Antwort enthält IP-Adresse
- Antwort enthält NXDOMAIN
- keine Antwort sichtbar
- Anfrage geht an unerwarteten DNS-Server

## Beispiel: Webserver langsam

Fragestellung:

> Wartet der Client auf Netzwerk, Server oder Anwendung?

Capture-Punkt:

```text
Client oder Server
```

Traffic erzeugen:

```bash
curl -v https://example.org
```

Erste Filter:

```text
dns
```

```text
tcp
```

```text
tls
```

Spätere Analyse:

- DNS-Dauer
- TCP-Handshake
- TLS-Handshake
- Serverantwortzeit
- Retransmissions
- Resets

Das kommt im erweiterten Kurs genauer.

## Mini-Aufgabe

Erzeuge einen kurzen Capture mit Wireshark oder TShark.

1. Starte einen Mitschnitt.
2. Führe aus:

```bash
dig example.org
curl -I https://example.org
```

3. Stoppe den Mitschnitt.
4. Speichere ihn als:

```text
pcaps/generated/basic-capture-01.pcapng
```

5. Öffne ihn in Wireshark.
6. Beantworte:

- Welche DNS-Anfragen siehst du?
- Welche IP-Adressen tauchen auf?
- Welche TCP-Verbindungen siehst du?
- Wie viele Pakete enthält der Mitschnitt?

## WCA-Bezug

Dieser Abschnitt übt WCA-nahe Grundlagen:

- Capture-Methoden
- Capture-Punkte
- Unterschied zwischen Erfassen und Anzeigen
- Umgang mit Capture-Dateien
- erste strukturierte Analysefragen
