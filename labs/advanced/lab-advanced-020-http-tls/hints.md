# Hinweise

## Hinweis 1: Kein HTTP sichtbar

Prüfe, ob du wirklich HTTP verwendet hast:

```text
http://172.28.70.10/
```

Nicht:

```text
https://...
```

HTTP ist auf Port 80.

## Hinweis 2: Kein SNI sichtbar

SNI wird sichtbar, wenn der Client einen Hostnamen für TLS verwendet.

Im Lab passiert das durch:

```bash
--resolve secure.lab.local:443:172.28.70.10
```

und:

```text
https://secure.lab.local/
```

Wenn du nur `https://172.28.70.10/` verwendest, ist SNI möglicherweise nicht wie erwartet sichtbar.

## Hinweis 3: Zertifikatsfehler ist erwartet

Das Zertifikat ist selbstsigniert.

Mit `-k` akzeptiert curl das Zertifikat trotzdem.

Ohne `-k` sollte ein Zertifikatsfehler entstehen.

Das kann im Capture zu einem TLS Alert führen.

## Hinweis 4: ALPN nicht immer sichtbar

Je nach Client und TLS-Version kann ALPN sichtbar sein oder nicht.

Filter:

```text
tls.handshake.extensions_alpn_str
```

Wenn nichts sichtbar ist, ist das nicht automatisch ein Fehler.

## Hinweis 5: TLS Application Data

Bei HTTPS ist der HTTP-Inhalt normalerweise nicht als `http` sichtbar.

Stattdessen siehst du TLS-Pakete, zum Beispiel:

```text
tls.app_data
```

oder in der Info-Spalte:

```text
Application Data
```

## Hinweis 6: Nicht überinterpretieren

Sauber:

```text
Der HTTP-Inhalt ist im Klartext sichtbar. Bei HTTPS sind TLS-Metadaten sichtbar, der HTTP-Inhalt aber nicht im Klartext.
```

Zu stark:

```text
Bei HTTPS sieht man gar nichts.
```

Das stimmt nicht. Metadaten bleiben sichtbar.
