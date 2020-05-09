inkbird-exporter
================

[![container repository](https://img.shields.io/badge/docker-0.1.1-blue)](https://hub.docker.com/r/hichtakk/inkbird-exporter)  

Prometheus exporter for Inkbird IBS-TH1 Bluetooth LE temperature and humidity sensor.  
https://www.ink-bird.com/products-smart-sensor.html

# Usage

# Run with Docker container
To access hci from docker container, `--net=host` and `--privileged` options are required.

```
$ docker run -d --net=host --privileged -e INKBIRD_DEVICE=XX:XX:XX:XX:XX:XX -e HANDLE 0x0028 -e PORT 18000 hichtakk/inkbird-exporter:0.1.0
```

inkbird-exporter reports temperature and humidity at that time.

```
# HELP inkbird_temperature current temperature
# TYPE inkbird_temperature gauge
inkbird_temperature{device="XX:XX:XX:XX:XX:XX"} 25.22
# HELP inkbird_humidity current humidity
# TYPE inkbird_humidity gauge
inkbird_humidity{device="XX:XX:XX:XX:XX:XX"} 56.27
```
