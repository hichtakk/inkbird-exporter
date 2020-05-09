from bluepy.btle import Peripheral, ADDR_TYPE_PUBLIC, BTLEDisconnectError
from inkbird.logger import logger

HANDLE = 0x0028
RETRY = 3


class InkbirdReader(object):

    def __init__(self, device, handle):
        self.device = device
        self.handle = handle

    def read(self, retry):
        (temperature, humidity) = (None, None)
        try:
            peripheral = Peripheral(self.device, addrType=ADDR_TYPE_PUBLIC)
            characteristic = peripheral.readCharacteristic(self.handle)
            temperature = self.read_temperature(characteristic)
            humidity = self.read_humidity(characteristic)
        except BTLEDisconnectError as e:
            logger.info(e)
            if retry < RETRY:
                (temperature, humidity) = self.read(retry+1)
            else:
                logger.info("read retry error")
        return (temperature, humidity)

    def read_temperature(self, characteristic):
        return int.from_bytes(characteristic[0:2], "little") / 100

    def read_humidity(self, characteristic):
        return int.from_bytes(characteristic[2:4], "little") / 100
