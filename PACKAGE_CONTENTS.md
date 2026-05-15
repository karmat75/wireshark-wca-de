# Paket 19: Docker-Lab DNS/HTTP

Dieses Paket ergänzt den Kurs um das erste reproduzierbare Docker-basierte Lab.

## Enthaltene Dateien

```text
.gitignore
mkdocs.yml
docs/40-labs-und-uebungen/index.md
docs/40-labs-und-uebungen/basic-dns-http-docker.md
docker/compose/lab-basic-dns-http/README.md
docker/compose/lab-basic-dns-http/compose.yml
docker/compose/lab-basic-dns-http/dns/Corefile
docker/compose/lab-basic-dns-http/dns/db.lab.local
docker/compose/lab-basic-dns-http/web-ok/index.html
docker/compose/lab-basic-dns-http/web-slow/app.py
labs/basic/lab-basic-020-dns-http-docker/README.md
labs/basic/lab-basic-020-dns-http-docker/scenario.md
labs/basic/lab-basic-020-dns-http-docker/tasks.md
labs/basic/lab-basic-020-dns-http-docker/hints.md
labs/basic/lab-basic-020-dns-http-docker/solution.md
labs/basic/lab-basic-020-dns-http-docker/metadata.yml
pcaps/generated/.gitkeep
```

## Ziel

Dieses Paket macht Docker erstmals praktisch nutzbar:

- eigenes isoliertes Lab-Netz
- eigener DNS-Server mit `lab.local`
- normaler Webserver
- langsamer Webserver
- Client-Container für `dig` und `curl`
- Host-Capture mit Wireshark oder TShark
- Analyse von DNS, NXDOMAIN, HTTP und einfacher Wartezeit

Lokal erzeugte PCAP-Dateien werden über `.gitignore` vom Commit ausgeschlossen.
