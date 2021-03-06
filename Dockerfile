FROM ubuntu:18.04

LABEL maintainer="hichtakk@gmail.com"
LABEL version="0.1.1"
LABEL description="Prometheus exporter for Inkbird IBS-TH1 bluetooth temperature and humidity sensor."

COPY dist/inkbird-*.tar.gz /tmp/
RUN apt update && \
	apt -y install bluez python3-pip libglib2.0-dev && \
	pip3 install /tmp/inkbird-*.tar.gz && \
	apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV INKBIRD_DEVICE=""
ENV HANDLE=""
ENV PORT=0
#EXPOSE 18000

CMD ["sh", "-c", "/usr/local/bin/inkbird-exporter --handle $HANDLE --port $PORT $INKBIRD_DEVICE"]