# Advanced Lab 010: TCP Retransmission

Dieses Lab erzeugt kontrollierten TCP-Datenverkehr mit absichtlichem Paketverlust.

Du analysierst anschließend, wie Wireshark TCP Retransmissions, Duplicate ACKs und verwandte Analysehinweise darstellt.

## Lab-Pfad

```text
labs/advanced/lab-advanced-010-tcp-retransmission/
```

## Docker-Pfad

```text
docker/compose/lab-advanced-tcp-loss/
```

## Ziel

Du übst:

- TCP-Datenstrom mit größerer Übertragung zu erzeugen
- Paketverlust im Lab kontrolliert einzubauen
- TCP Retransmissions zu finden
- Duplicate ACKs und Fast Retransmit einzuordnen
- einen TCP Stream zu isolieren
- Analysefelder von Wireshark richtig zu bewerten
- vorsichtige Aussagen über Paketverlust zu formulieren

## Ergebnisdatei

Lokal erzeugter Capture:

```text
pcaps/generated/lab-advanced-010-tcp-retransmission.pcapng
```

Diese Datei ist lokal und wird nicht committed.

## WCA-Bezug

Dieses Lab trainiert:

- TCP-Analyse
- TCP Sequence / ACK
- Retransmissions
- Duplicate ACK
- Fast Retransmit
- Capture-Punkt und Belegbarkeit
- TShark-Auswertung
- Performance- und Troubleshooting-Methodik
