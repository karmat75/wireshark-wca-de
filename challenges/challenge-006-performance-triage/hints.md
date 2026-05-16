# Hinweise

## Hinweis 1: IP-Adressen

```text
web-ok.lab.local   -> 172.28.50.10
web-slow.lab.local -> 172.28.50.20
lab-client         -> 172.28.50.100
lab-dns            -> 172.28.50.53
```

## Hinweis 2: erst grob, dann genau

Beginne mit:

```text
http
```

Dann trenne:

```text
ip.addr == 172.28.50.10 and http
```

und:

```text
ip.addr == 172.28.50.20 and http
```

## Hinweis 3: Zeitdarstellung

Hilfreich ist:

```text
View > Time Display Format > Seconds Since Beginning of Capture
```

oder:

```text
Seconds Since Previous Displayed Packet
```

## Hinweis 4: DNS nicht vorschnell beschuldigen

Wenn DNS Query und DNS Response schnell nacheinander kommen, ist DNS vermutlich nicht die sichtbare Hauptwartezeit.

## Hinweis 5: TCP nicht vorschnell beschuldigen

Wenn SYN und SYN/ACK schnell nacheinander kommen, ist der TCP-Verbindungsaufbau vermutlich nicht die sichtbare Hauptwartezeit.

## Hinweis 6: HTTP Request/Response vergleichen

Beim langsamen Server liegt die auffällige Wartezeit typischerweise zwischen:

```text
HTTP Request
```

und:

```text
HTTP Response
```

## Hinweis 7: vorsichtig formulieren

Nicht sauber:

```text
Das Netzwerk ist langsam.
```

Besser:

```text
Im Capture ist die auffällige Wartezeit zwischen HTTP Request und HTTP Response zu web-slow.lab.local sichtbar.
```
