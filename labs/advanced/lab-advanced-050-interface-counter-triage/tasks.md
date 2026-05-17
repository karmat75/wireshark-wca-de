# Aufgaben

## Aufgabe 1: Counter klassifizieren

Ordne jeden Eintrag aus dem Monitoring-Auszug ein.

Tabelle:

```text
Interface | Counter | Erste Einordnung | Wireshark hilfreich? | Nächster Schritt
```

Nutze dabei:

- Error oder Discard?
- In oder Out?
- Access-Port oder Uplink?
- Lastabhängig oder nicht?
- potenziell physikalisch?
- potenziell Queue/Buffer/QoS?
- potenziell VLAN/MTU/Policy?

## Aufgabe 2: Wireshark-Eignung bewerten

Bewerte für jeden Fall:

```text
Wireshark als erster Schritt sinnvoll?
Wireshark später sinnvoll?
Wireshark wahrscheinlich wenig hilfreich?
```

Begründe kurz.

Achte besonders auf:

- CRC/FCS
- Giants
- OutDiscards
- Uplink vs. Access-Port
- Benutzerbeschwerden
- Zeitfenster

## Aufgabe 3: Fragen an das Monitoring-System

Formuliere mindestens zehn Fragen, die du aus dem Monitoring heraus beantwortet haben möchtest.

Beispiele:

```text
Steigt der Counter dauerhaft oder nur in Peaks?
```

```text
Gibt es zeitgleich hohe Interface-Auslastung?
```

```text
Sind beide Richtungen betroffen?
```

## Aufgabe 4: Fragen an den Switch oder Router

Formuliere mindestens zehn Geräteprüfungen.

Beispiele:

```text
show interface <port>
```

```text
show interface counters errors
```

```text
show queue / qos counters
```

Beschreibe jeweils, was du damit prüfen möchtest.

## Aufgabe 5: Capture-Strategie

Wähle für zwei Fälle einen sinnvollen Capture-Ansatz.

Mögliche Capture-Punkte:

- Host-Capture
- SPAN/Mirror-Port
- TAP
- beidseitiger Capture
- Capture am Server
- Capture am Client
- Capture vor und nach einem Segment

Beantworte:

- Wo würdest du capturen?
- Warum dort?
- Was erwartest du zu sehen?
- Was kann dieser Capture nicht beweisen?

## Aufgabe 6: Berichtssprache verbessern

Formuliere diese Sätze vorsichtiger:

```text
Der Switch ist kaputt.
```

```text
Das Netzwerk verliert Pakete.
```

```text
Die Firewall blockt.
```

```text
Wireshark zeigt nichts, also gibt es kein Problem.
```

```text
Der Server ist schuld.
```

## Aufgabe 7: Kurzbericht schreiben

Schreibe eine kurze Triage:

```text
Ausgangslage:
<Monitoring-Symptom>

Einordnung:
<Errors/Discards, Richtung, Interface-Rolle>

Wireshark:
<wo hilfreich, wo nicht>

Nächste Schritte:
<Geräteprüfungen, Messfenster, Capture-Punkte>

Bewertung:
<was ist belegt?>

Einschränkungen:
<was ist nicht belegt?>
```
