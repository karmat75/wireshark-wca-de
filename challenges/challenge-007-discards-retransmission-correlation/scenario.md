# Szenario

Ein Monitoring-System meldet:

```text
10:14:00-10:18:00
Gerät: sw-access-07
Interface: port-10
Counter: OutDiscards
Beobachtung: deutlicher Anstieg während eines Benutzerbeschwerde-Zeitfensters
```

Gleichzeitig meldet ein Benutzer:

```text
Der Download vom internen Webserver ist langsam und wirkt unruhig.
```

Du erhältst oder erzeugst einen Capture aus dem betroffenen Zeitraum.

## Lab-Netz

```text
172.28.60.0/24
```

## Systeme

| System | IP | Rolle |
|---|---:|---|
| `lab-client` | `172.28.60.100` | Client |
| `lab-web-loss` | `172.28.60.10` | Webserver mit absichtlichem Paketverlust |

## Monitoring-Kontext

Das Monitoring zeigt nur Counter.

Es zeigt nicht:

- welche Pakete verworfen wurden
- welche Flows betroffen waren
- ob der Drop im Capture sichtbar ist
- ob der Switch sicher die Ursache ist

## Deine Aufgabe

Erstelle eine Triage, die beides zusammenbringt:

```text
Monitoring-Zeitfenster + PCAP-Beobachtung
```

Aber formuliere vorsichtig.

Gesucht ist nicht:

```text
Der Switch ist schuld.
```

Gesucht ist:

```text
Im Zeitraum der gemeldeten OutDiscards zeigt der Capture TCP-Symptome, die zu Paketverlust oder fehlenden Segmenten passen. Der genaue Drop-Ort ist noch nicht bewiesen.
```
