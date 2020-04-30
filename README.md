inkbird-exporter
================

[![container repository](https://img.shields.io/badge/docker-0.1.0-blue)](https://hub.docker.com/r/hichtakk/inkbird-exporter)  

Prometheus exporter for Inkbird IBS-TH1 Bluetooth LE temperature and humidity sensor.  
https://www.ink-bird.com/products-smart-sensor.html

# Run with Docker container
To access hci from docker container, `--net=host` and `--privileged` options are required.

```
$ docker run -d --net=host --privileged -e INKBIRD_DEVICE=XX:XX:XX:XX:XX:XX inkbird-exporter:0.1.0
```