# Paket 31: Advanced Lab – Performanceanalyse

Dieses Paket ergänzt den Lab-Bereich um ein Advanced-Lab zur Performanceanalyse.

## Enthaltene Dateien

```text
mkdocs.yml
docs/40-labs-und-uebungen/index.md
docs/40-labs-und-uebungen/advanced-performance-analyse.md
labs/advanced/lab-advanced-030-performance-analyse/README.md
labs/advanced/lab-advanced-030-performance-analyse/scenario.md
labs/advanced/lab-advanced-030-performance-analyse/tasks.md
labs/advanced/lab-advanced-030-performance-analyse/hints.md
labs/advanced/lab-advanced-030-performance-analyse/solution.md
labs/advanced/lab-advanced-030-performance-analyse/metadata.yml
labs/advanced/lab-advanced-030-performance-analyse/check_tshark.sh
```

## Ziel

Dieses Lab trainiert Performanceanalyse mit Wireshark:

- DNS-, TCP- und HTTP-Zeitabschnitte trennen
- schnellen und langsamen Webserver vergleichen
- Zeitspalten und Time Reference nutzen
- Conversations und Protocol Hierarchy einsetzen
- I/O Graphs sinnvoll verwenden
- TShark-Ausgaben für Zeitmessungen erzeugen
- vorsichtig bewerten, wo die Wartezeit entsteht

Das Lab nutzt das vorhandene Docker-Lab `lab-basic-dns-http`.
