# Docker installieren

Docker wird im Kurs für reproduzierbare Lab-Umgebungen verwendet.

Wireshark selbst läuft dabei auf dem Host-System. Docker wird genutzt, um kontrollierten Netzwerkverkehr zu erzeugen, kleine Testdienste bereitzustellen und spätere Labs reproduzierbar zu machen.

## Warum Docker?

Mit Docker können wir Labs so bauen, dass Lernende nicht mühsam eigene Server vorbereiten müssen.

Beispiele:

- Webserver für HTTP-Labs
- DNS-Server für DNS-Labs
- Clients, die definierte Anfragen erzeugen
- fehlerhafte Dienste für Troubleshooting-Szenarien
- kontrollierte Umgebungen für TCP- und Performanceübungen

## Installation über das offizielle Docker-Repository

Zuerst benötigte Pakete installieren:

```bash
sudo apt update
sudo apt install -y ca-certificates curl gnupg
```

Keyring-Verzeichnis anlegen:

```bash
sudo install -m 0755 -d /etc/apt/keyrings
```

Docker-GPG-Schlüssel importieren:

```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg   | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

sudo chmod a+r /etc/apt/keyrings/docker.gpg
```

Ubuntu-Codename ermitteln:

```bash
. /etc/os-release
echo "VERSION_CODENAME=${VERSION_CODENAME}"
echo "UBUNTU_CODENAME=${UBUNTU_CODENAME}"
```

Docker-Paketquelle einrichten:

```bash
. /etc/os-release
DOCKER_CODENAME="${UBUNTU_CODENAME:-$VERSION_CODENAME}"

echo   "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu ${DOCKER_CODENAME} stable"   | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

Docker installieren:

```bash
sudo apt update
sudo apt install -y   docker-ce   docker-ce-cli   containerd.io   docker-buildx-plugin   docker-compose-plugin
```

## Docker-Dienst prüfen

```bash
sudo systemctl status docker --no-pager
```

Testcontainer ausführen:

```bash
sudo docker run hello-world
```

## Docker ohne `sudo` verwenden

Für die Kursarbeit ist es komfortabler, Docker ohne `sudo` ausführen zu können.

Benutzer zur Gruppe `docker` hinzufügen:

```bash
sudo usermod -aG docker "$USER"
```

Danach einmal vollständig abmelden und wieder anmelden.

Nach dem erneuten Login prüfen:

```bash
groups
docker run hello-world
```

!!! warning "Sicherheitshinweis"
    Mitglieder der Gruppe `docker` haben sehr weitreichende Rechte auf dem lokalen System. Auf einem persönlichen Lernsystem ist das praktisch. Auf produktiven oder gemeinsam genutzten Systemen sollte diese Entscheidung bewusst getroffen werden.

## Docker Compose prüfen

```bash
docker compose version
```

## Zielzustand

Docker ist für den Kurs bereit, wenn folgende Befehle ohne Fehler laufen:

```bash
docker version
docker compose version
docker run hello-world
```
