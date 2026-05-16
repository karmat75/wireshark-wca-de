# Challenge 006: Performance Triage

Diese Challenge nutzt das vorhandene Docker-Lab `lab-basic-dns-http`.

Du erzeugst einen Capture und untersuchst, warum `web-slow.lab.local` langsamer wirkt als `web-ok.lab.local`.

## Challenge-Pfad

```text
challenges/challenge-006-performance-triage/
```

## Benötigtes Docker-Lab

```text
docker/compose/lab-basic-dns-http/compose.yml
```

## Ergebnis-PCAP

```text
pcaps/generated/challenge-006-performance-triage.pcapng
```

Diese Datei wird lokal erzeugt und nicht committed.

## Ziel

Du sollst herausfinden:

- ob DNS sichtbar langsam ist
- ob TCP-Verbindungsaufbau sichtbar langsam ist
- ob die Wartezeit zwischen HTTP Request und HTTP Response entsteht
- welcher Server langsamer antwortet
- welche Frame-Nummern die Aussage belegen
- welche Aussage durch den Capture belegbar ist
- welche Aussagen zu stark wären

## WCA-Bezug

Diese Challenge trainiert:

- Performanceanalyse
- DNS
- TCP
- HTTP
- Conversations
- Time Display
- I/O Graphs
- TShark
- Fehleranalyse-Methodik
