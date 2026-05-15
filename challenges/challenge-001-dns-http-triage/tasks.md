# Aufgaben

## Aufgabe 1: Lab starten

Aus dem Repository-Root:

```bash
docker compose -f docker/compose/lab-basic-dns-http/compose.yml up -d
```

Prüfen:

```bash
docker compose -f docker/compose/lab-basic-dns-http/compose.yml ps
```

## Aufgabe 2: Capture starten

Ordner vorbereiten:

```bash
mkdir -p pcaps/generated
```

Capture starten:

```bash
sudo tshark -i any -f "net 172.28.50.0/24" -w pcaps/generated/challenge-001-dns-http-triage.pcapng
```

## Aufgabe 3: Testtraffic erzeugen

In einem zweiten Terminal:

```bash
docker compose -f docker/compose/lab-basic-dns-http/compose.yml exec lab-client sh -lc '
dig web-ok.lab.local
dig web-slow.lab.local
dig does-not-exist.lab.local
curl -I http://web-ok.lab.local
curl -I http://web-slow.lab.local
'
```

## Aufgabe 4: Capture stoppen

Stoppe TShark mit:

```text
Ctrl + C
```

Öffne den Capture:

```bash
wireshark pcaps/generated/challenge-001-dns-http-triage.pcapng
```

## Aufgabe 5: Grobe Orientierung

Prüfe:

```text
Statistics > Protocol Hierarchy
```

```text
Statistics > Conversations
```

Beantworte:

- Welche Protokolle sind sichtbar?
- Welche IPs sind beteiligt?
- Gibt es DNS?
- Gibt es HTTP?
- Gibt es auffällige Zeitabstände?

## Aufgabe 6: DNS-Fragen

Beantworte mit Frame-Nummern:

- Welche DNS-Namen wurden abgefragt?
- Welche Namen wurden erfolgreich aufgelöst?
- Welche IP-Adressen wurden zurückgegeben?
- Welcher Name liefert NXDOMAIN?
- Welche Filter hast du verwendet?

## Aufgabe 7: HTTP-Fragen

Beantworte mit Frame-Nummern:

- Welche HTTP Requests wurden gesendet?
- Welche HTTP Responses kamen zurück?
- Welche Statuscodes sind sichtbar?
- Welcher Server antwortet langsamer?
- Wie groß ist der Zeitabstand ungefähr?
- Welche Filter hast du verwendet?

## Aufgabe 8: Bewertung

Formuliere eine kurze Bewertung:

- DNS funktioniert grundsätzlich: ja/nein/teilweise?
- HTTP funktioniert grundsätzlich: ja/nein/teilweise?
- Welche konkrete Beobachtung erklärt „funktioniert teilweise nicht“?
- Welche konkrete Beobachtung erklärt „fühlt sich langsam an“?
- Was kann der Capture nicht beweisen?

## Aufgabe 9: TShark-Check ausführen

```bash
bash challenges/challenge-001-dns-http-triage/check_tshark.sh pcaps/generated/challenge-001-dns-http-triage.pcapng
```

## Aufgabe 10: Lab stoppen

```bash
docker compose -f docker/compose/lab-basic-dns-http/compose.yml down
```
