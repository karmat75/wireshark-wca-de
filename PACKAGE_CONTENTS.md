# Paket 28: Basic Lab – Display Filter

Dieses Paket ergänzt den Lab-Bereich um ein gezieltes Display-Filter-Lab.

## Enthaltene Dateien

```text
mkdocs.yml
docs/40-labs-und-uebungen/index.md
docs/40-labs-und-uebungen/basic-display-filter.md
labs/basic/lab-basic-010-display-filter/README.md
labs/basic/lab-basic-010-display-filter/scenario.md
labs/basic/lab-basic-010-display-filter/tasks.md
labs/basic/lab-basic-010-display-filter/hints.md
labs/basic/lab-basic-010-display-filter/solution.md
labs/basic/lab-basic-010-display-filter/metadata.yml
labs/basic/lab-basic-010-display-filter/check_tshark.sh
```

## Ziel

Dieses Lab trainiert Display Filter systematisch:

- einfache Protokollfilter
- IP-, Port- und Hostfilter
- DNS Query/Response Filter
- DNS Response Codes
- HTTP Request/Response Filter
- TCP Stream Filter
- logische Operatoren
- Klammern
- `contains`
- Negation
- Unterschied zwischen Display Filter und Capture Filter
- Filter dokumentieren und mit TShark gegenprüfen

Das Lab nutzt eine vorhandene oder neu erzeugte PCAP aus dem Docker-DNS/HTTP-Lab.
