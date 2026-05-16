FROM alpine:3.20

RUN apk add --no-cache nginx iproute2 coreutils \
    && mkdir -p /run/nginx /usr/share/nginx/html \
    && dd if=/dev/urandom of=/usr/share/nginx/html/bigfile.bin bs=1M count=12 status=none

COPY nginx.conf /etc/nginx/nginx.conf
COPY index.html /usr/share/nginx/html/index.html
COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

EXPOSE 80

CMD ["/entrypoint.sh"]
