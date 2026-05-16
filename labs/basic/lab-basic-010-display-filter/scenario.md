# Szenario

Du hast einen Capture aus einer kleinen Lab-Umgebung.

Darin befinden sich:

- DNS-Anfragen
- DNS-Antworten
- ein nicht existierender DNS-Name
- HTTP-Anfragen
- HTTP-Antworten
- TCP-Verbindungen

Deine Aufgabe ist nicht, einen neuen Fehler zu finden.

Deine Aufgabe ist, die passenden Pakete gezielt mit Display Filtern zu finden und die Filter sauber zu dokumentieren.

## Warum dieses Lab wichtig ist

Viele Wireshark-Analysen scheitern nicht am Protokollwissen, sondern daran, dass man die relevanten Pakete nicht sauber isoliert.

Display Filter sind dafür zentral.

AHA:

> Ein guter Filter beantwortet eine konkrete Analysefrage.
