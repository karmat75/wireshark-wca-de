# Hinweise

## Hinweis 1: Beginne mit DNS

Nutze zuerst:

```text
dns
```

Dann trenne Anfragen und Antworten:

```text
dns.flags.response == 0
```

```text
dns.flags.response == 1
```

## Hinweis 2: Suche DNS-Fehler

NXDOMAIN ist ein DNS Response Code.

Filter:

```text
dns.flags.rcode == 3
```

## Hinweis 3: Prüfe HTTP separat

Nutze:

```text
http
```

Dann:

```text
http.request
```

und:

```text
http.response
```

## Hinweis 4: Langsamkeit ist Zeitabstand

Filtere auf den langsamen Server:

```text
ip.addr == 172.28.50.20 and http
```

Prüfe den Zeitabstand zwischen Request und Response.

## Hinweis 5: Nicht zu viel behaupten

Wenn DNS und HTTP sichtbar funktionieren, aber eine Response verzögert kommt, ist das nicht automatisch ein Netzwerkproblem.

Formuliere:

```text
Im Capture liegt die Wartezeit zwischen HTTP Request und HTTP Response.
```

Nicht:

```text
Das Netzwerk ist kaputt.
```
