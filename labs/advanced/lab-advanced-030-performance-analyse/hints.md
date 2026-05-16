# Hinweise

## Hinweis 1: HTTP Request/Response ist der Schlüssel

Beginne mit:

```text
http
```

Dann isoliere:

```text
ip.addr == 172.28.50.10 and http
```

und:

```text
ip.addr == 172.28.50.20 and http
```

## Hinweis 2: langsamer Server

Der langsame Server ist:

```text
172.28.50.20
```

Der schnelle Server ist:

```text
172.28.50.10
```

## Hinweis 3: Zeitabstand sichtbar machen

Hilfreich ist:

```text
View > Time Display Format > Seconds Since Previous Displayed Packet
```

Wenn du vorher auf einen einzelnen HTTP-Stream oder Server filterst, ist der Abstand zwischen Request und Response leichter lesbar.

## Hinweis 4: DNS ist nicht automatisch schuld

Nur weil ein Benutzer „Webseite langsam“ meldet, ist DNS nicht automatisch die Ursache.

Prüfe:

- DNS Query bis Response
- TCP SYN bis SYN/ACK
- HTTP Request bis Response

## Hinweis 5: I/O Graphs sind Orientierung

I/O Graphs zeigen Muster.

Sie beweisen nicht allein die Ursache.

Nutze sie als Einstieg und prüfe danach die relevanten Frames.

## Hinweis 6: vorsichtig formulieren

Gut:

```text
Im Capture liegt die sichtbare Wartezeit zwischen HTTP Request und HTTP Response.
```

Zu stark:

```text
Der Server ist kaputt.
```

Besser:

```text
Das Muster passt zu serverseitiger oder anwendungsseitiger Verarbeitung. Im Lab ist die Verzögerung absichtlich serverseitig eingebaut.
```
