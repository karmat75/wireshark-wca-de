# Paket 29: Advanced Lab – TCP Retransmission

Dieses Paket ergänzt den Lab-Bereich um ein erstes Advanced-Lab zu TCP Retransmissions.

## Enthaltene Dateien

```text
mkdocs.yml
docs/40-labs-und-uebungen/index.md
docs/40-labs-und-uebungen/advanced-tcp-retransmission.md
docker/compose/lab-advanced-tcp-loss/README.md
docker/compose/lab-advanced-tcp-loss/compose.yml
docker/compose/lab-advanced-tcp-loss/web-loss/Dockerfile
docker/compose/lab-advanced-tcp-loss/web-loss/entrypoint.sh
docker/compose/lab-advanced-tcp-loss/web-loss/nginx.conf
docker/compose/lab-advanced-tcp-loss/web-loss/index.html
labs/advanced/lab-advanced-010-tcp-retransmission/README.md
labs/advanced/lab-advanced-010-tcp-retransmission/scenario.md
labs/advanced/lab-advanced-010-tcp-retransmission/tasks.md
labs/advanced/lab-advanced-010-tcp-retransmission/hints.md
labs/advanced/lab-advanced-010-tcp-retransmission/solution.md
labs/advanced/lab-advanced-010-tcp-retransmission/metadata.yml
labs/advanced/lab-advanced-010-tcp-retransmission/check_tshark.sh
```

## Ziel

Dieses Lab trainiert eine zentrale Advanced-/WCA-nahe TCP-Fähigkeit:

- kontrollierten TCP-Datenverkehr erzeugen
- absichtlichen Paketverlust im Lab einbauen
- TCP Retransmissions erkennen
- Duplicate ACKs und Fast Retransmit einordnen
- TCP Stream isolieren
- Wireshark-generierte Analysefelder richtig bewerten
- nicht vorschnell „das Netzwerk ist schuld“ sagen
- TShark für reproduzierbare Auswertung verwenden

Das Lab baut ein eigenes Docker-Netz `172.28.60.0/24` auf.
