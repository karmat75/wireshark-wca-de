# Umgebung prüfen

In diesem Schritt prüfen wir, ob die Lern- und Übungsumgebung einsatzbereit ist.

Diese Prüfung ist bewusst einfach gehalten. Sie soll sicherstellen, dass die wichtigsten Werkzeuge vorhanden sind und das Kurs-Repository lokal gebaut werden kann.

## Systeminformationen

```bash
hostnamectl
cat /etc/os-release
```

## Basiswerkzeuge

```bash
git --version
curl --version
python3 --version
python -m pip --version
```

Wenn `python -m pip --version` nicht funktioniert, zuerst die virtuelle Umgebung aktivieren:

```bash
source .venv/bin/activate
python -m pip --version
```

## Netzwerkwerkzeuge

```bash
ip address show
ip route show
dig example.org
traceroute example.org
```

## Docker prüfen

```bash
docker version
docker compose version
docker run --rm hello-world
```

Wenn Docker nur mit `sudo` funktioniert, wurde der Benutzer entweder noch nicht zur Gruppe `docker` hinzugefügt oder die Sitzung wurde nach der Gruppenänderung noch nicht neu gestartet.

Prüfen:

```bash
groups
```

## Wireshark und TShark prüfen

```bash
wireshark --version
tshark --version
tshark -D
```

Kurzer Capture-Test:

```bash
tshark -a duration:5 -w /tmp/wwca-test.pcapng
capinfos /tmp/wwca-test.pcapng
```

## Kursdokumentation prüfen

Im Root-Verzeichnis des Repositories:

```bash
source .venv/bin/activate
mkdocs build
```

Lokale Vorschau starten:

```bash
mkdocs serve
```

Im Browser öffnen:

```text
http://127.0.0.1:8000
```

## Erwarteter Zielzustand

Die Umgebung gilt als bereit, wenn folgende Punkte erfüllt sind:

- `git` funktioniert
- Python-venv funktioniert
- MkDocs baut die Dokumentation ohne Fehler
- Docker funktioniert ohne `sudo`
- Docker Compose ist vorhanden
- Wireshark startet
- TShark zeigt Interfaces an
- ein kurzer Capture kann erstellt werden

## Checkliste

- [ ] Betriebssystem aktualisiert
- [ ] Basispakete installiert
- [ ] VSCode installiert
- [ ] empfohlene VSCode-Erweiterungen installiert
- [ ] Docker installiert
- [ ] Benutzer ist Mitglied der Gruppe `docker`
- [ ] Wireshark installiert
- [ ] Benutzer ist Mitglied der Gruppe `wireshark`
- [ ] `mkdocs build` erfolgreich
- [ ] `mkdocs serve` erfolgreich

## Typische Probleme

### `mkdocs: command not found`

Meistens ist die virtuelle Umgebung nicht aktiviert oder MkDocs wurde noch nicht installiert.

```bash
source .venv/bin/activate
python -m pip install -r requirements.txt
mkdocs build
```

### Docker funktioniert nur mit `sudo`

```bash
sudo usermod -aG docker "$USER"
```

Danach vollständig abmelden und wieder anmelden.

### TShark darf nicht mitschneiden

```bash
sudo dpkg-reconfigure wireshark-common
sudo usermod -aG wireshark "$USER"
```

Danach vollständig abmelden und wieder anmelden.
