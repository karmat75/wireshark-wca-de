# Basic Lab 020: DNS und HTTP im Docker-Lab

Dieses Lab ist das erste reproduzierbare Docker-basierte Analyse-Lab.

Es erzeugt eine kleine isolierte Umgebung:

- einen DNS-Server für `lab.local`
- einen normalen Webserver
- einen absichtlich langsamen Webserver
- einen Client-Container für `dig` und `curl`

Du schneidest den Traffic auf dem Host mit und analysierst anschließend DNS, NXDOMAIN, HTTP und einfache Wartezeit.

## Lab-Pfad

```text
labs/basic/lab-basic-020-dns-http-docker/
```

## Docker-Pfad

```text
docker/compose/lab-basic-dns-http/
```

## Ziel

Du übst:

- Docker-Lab starten
- kontrollierten DNS- und HTTP-Traffic erzeugen
- Host-Capture auf Docker-Traffic erstellen
- DNS Query und Response analysieren
- NXDOMAIN erkennen
- HTTP Request und Response lesen
- einfache Serververzögerung im Capture sehen
- Beobachtungen mit Filtern und Frame-Nummern dokumentieren

## Kurzablauf

1. Docker-Lab starten
2. Capture auf dem Host starten
3. aus dem Client-Container Traffic erzeugen
4. Capture stoppen
5. DNS und HTTP analysieren
6. Wartezeit beim langsamen Webserver bewerten
7. Lab wieder stoppen

## Ergebnisdatei

Lokal erzeugter Capture:

```text
pcaps/generated/lab-basic-020-dns-http-docker.pcapng
```

Diese Datei ist lokal und wird nicht committed.

## WCA-Bezug

Dieses Lab trainiert:

- Display Filter
- DNS Query und Response
- DNS Response Codes
- HTTP Request und Response
- TCP-Port 80
- Zeitverhalten
- TShark-Auswertungen
- Analysebericht mit Belegen

## Vollständige Aufgaben

Die vollständigen Aufgaben, Hinweise und Lösungen liegen unter:

```text
labs/basic/lab-basic-020-dns-http-docker/
```
