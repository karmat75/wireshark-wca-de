# Rechtliches und Datenschutz

Paketmitschnitte können sensible Daten enthalten. Deshalb muss der Umgang mit Wireshark, TShark, tcpdump und PCAP-Dateien verantwortungsvoll erfolgen.

!!! warning "Keine Rechtsberatung"
    Diese Seite ist keine Rechtsberatung. Sie beschreibt Grundregeln für einen verantwortungsvollen Umgang mit Paketmitschnitten im Rahmen dieses Lernprojekts.

## Nur mit Berechtigung mitschneiden

Netzwerkverkehr darf nur dort mitgeschnitten werden, wo eine entsprechende Berechtigung vorliegt.

Das kann zum Beispiel der Fall sein:

- im eigenen Lab
- im eigenen Heimnetz
- in ausdrücklich freigegebenen Testumgebungen
- in produktiven Umgebungen nur mit klarer organisatorischer Freigabe
- im Rahmen definierter Betriebs- oder Fehlersuchprozesse

Nicht akzeptabel ist das unbefugte Mitschneiden fremder Kommunikation.

## Warum PCAPs sensibel sind

Ein Paketmitschnitt kann unter anderem enthalten:

- IP-Adressen
- Hostnamen
- Benutzernamen
- Cookies
- Tokens
- URLs
- DNS-Abfragen
- Mailadressen
- Klartext-Passwörter bei unsicheren Protokollen
- interne Systemnamen
- Zeitpunkte und Kommunikationsmuster

Auch wenn Nutzdaten verschlüsselt sind, können Metadaten sensibel sein.

## Regeln für dieses Repository

Für dieses Repository gelten folgende Regeln:

- keine privaten Captures veröffentlichen
- keine produktiven Captures veröffentlichen
- keine Kundendaten veröffentlichen
- keine personenbezogenen Daten veröffentlichen
- keine Zugangsdaten veröffentlichen
- keine Tokens, Cookies oder API-Keys veröffentlichen
- bevorzugt synthetisch erzeugten Lab-Traffic verwenden
- externe PCAP-Dateien nur bei klarer Lizenzlage aufnehmen
- bei unklarer Lizenzlage nur auf die Quelle verlinken

## Selbst erzeugte Lab-Captures

Für den Kurs sollen bevorzugt eigene Lab-Captures erzeugt werden.

Vorteile:

- reproduzierbar
- keine produktiven Daten
- klare Lernziele
- kontrollierte Fehlerbilder
- einfacher zu dokumentieren
- lizenzrechtlich sauberer

Beispiele:

- DNS NXDOMAIN
- TCP Reset
- HTTP 404
- HTTP 500
- langsame Serverantwort
- Paketverlust im Lab
- TLS-Handshake mit Testzertifikat

## Umgang mit externen Ressourcen

Externe Ressourcen sind willkommen, aber sie müssen sauber behandelt werden.

Grundsatz:

> Verlinken ist besser als Kopieren.

Externe Artikel, Videos, Folien oder PCAPs werden nur dann direkt ins Repository übernommen, wenn die Lizenz das eindeutig erlaubt.

Zusätzlich gelten für externe Links auf der Kursseite folgende Regeln:

- externe Links werden als externe Verweise gekennzeichnet
- externe Links erhalten `rel="external nofollow noopener noreferrer"`
- dadurch werden keine Referrer-Daten an die Zielseite übertragen

Damit bleibt für Lernende transparent, wann ein Verweis die Kursseite verlässt.

## Transparenz zur KI-Unterstützung

Dieser Kurs wird unter Zuhilfenahme von KI-Werkzeugen erstellt und überarbeitet.

Wichtig dabei:

- die inhaltliche Verantwortung liegt bei den Maintainern
- Inhalte werden redaktionell und fachlich geprüft
- externe Quellen werden weiterhin manuell bewertet und ausgewählt
- Fehler sind möglich und sollen über Issues gemeldet werden

## Analyseberichte

Analyseberichte in diesem Kurs sollen keine realen vertraulichen Daten enthalten.

Wenn ein Beispielbericht benötigt wird, sollten neutrale Namen verwendet werden:

- `client01.lab.local`
- `web01.lab.local`
- `dns01.lab.local`
- `192.0.2.10`
- `198.51.100.20`
- `203.0.113.30`

Diese Beispielnetze sind für Dokumentationszwecke reserviert.

## Grundregel

Wenn du unsicher bist, ob ein Mitschnitt veröffentlicht werden darf, veröffentliche ihn nicht.

Erstelle stattdessen einen synthetischen Capture im Lab oder beschreibe das Problem abstrakt.
