# Szenario

Ein Monitoring-System meldet auf mehreren Switch-Interfaces steigende Counter.

Die Meldungen kommen nicht dauerhaft, sondern in einzelnen Zeitfenstern.

## Monitoring-Auszug

| Zeitfenster | Gerät | Interface | Counter | Richtung | Beobachtung |
|---|---|---|---|---|---|
| 10:14-10:18 | sw-core-01 | uplink-01 | discards | out | deutlicher Anstieg während hoher Auslastung |
| 11:03-11:07 | sw-access-12 | port-24 | errors | in | CRC/FCS steigt langsam, Last unauffällig |
| 13:22-13:26 | sw-access-07 | port-10 | discards | out | kurze Peaks, gleichzeitig Benutzerbeschwerden |
| 15:40-15:45 | sw-dist-02 | trunk-03 | errors | in | Giants und input errors steigen |

## Vereinfachte Topologie

```text
Clients ---- Access Switches ---- Distribution ---- Core ---- Servernetz
```

## Zusatzinformationen

- `sw-core-01 uplink-01` ist ein Uplink vom Distribution-Layer zum Core.
- `sw-access-12 port-24` ist ein Access-Port zu einem Access Point.
- `sw-access-07 port-10` ist ein Access-Port zu einem Server.
- `sw-dist-02 trunk-03` ist ein Trunk mit mehreren VLANs.
- Das Monitoring-System zeigt keine Paketdetails.
- Es gibt noch keinen Capture.
- Es gibt noch keine direkten Switch-CLI-Auszüge.
- Es gibt keine bestätigte Applikationsstörung, nur mehrere Benutzerhinweise.

## Aufgabe

Erstelle eine Triage.

Du sollst nicht sofort „die Ursache“ finden.

Du sollst entscheiden:

- welche Counter ernst sind
- welche Fragen offen sind
- welche Prüfungen zuerst kommen
- wann Wireshark sinnvoll ist
- wo Wireshark wahrscheinlich nicht reicht
