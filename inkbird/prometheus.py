import argparse
import time

from prometheus_client import start_http_server, Gauge
from prometheus_client import REGISTRY, PROCESS_COLLECTOR, PLATFORM_COLLECTOR, GC_COLLECTOR

from inkbird.ble import InkbirdReader
from inkbird.logger import logger

REGISTRY.unregister(PROCESS_COLLECTOR)
REGISTRY.unregister(PLATFORM_COLLECTOR)
REGISTRY.unregister(GC_COLLECTOR)

parser = argparse.ArgumentParser(description="")
parser.add_argument("device",  help="mac address of peripheral device")
parser.add_argument("-p", "--port",  type=int, default=18000, help="server listen port")
parser.add_argument("-i", "--interval",  type=int, default=60, help="read interval in second")
parser.add_argument("--timeout",  type=int, default=10, help="read interval in second")
parser.add_argument("--handle",  help="handle value to read characteristic", default=0x002d)

TEMPERATURE = Gauge("inkbird_temperature", "current temperature", ["device"])
HUMIDITY = Gauge("inkbird_humidity", "current humidity", ["device"])


def set_value(device, temperature, humidity):
    TEMPERATURE.labels(device).set(temperature)
    HUMIDITY.labels(device).set(humidity)


def run_exporter():
    args = parser.parse_args()
    start_http_server(args.port)
    inkbird = InkbirdReader(args.device, int(args.handle, 16))
    while True:
        (temperature, humidity) = inkbird.read(0)
        if temperature is not None:
            set_value(args.device, temperature, humidity)
            logger.info("temperature: {} C, humidity: {} %".format(temperature, humidity))
        time.sleep(args.interval)


if __name__ == "__main__":
    run_exporter()