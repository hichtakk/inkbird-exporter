import argparse

from inkbird.ble import InkbirdReader

parser = argparse.ArgumentParser(description="")
parser.add_argument("device",  help="mac address of peripheral device")
parser.add_argument("--handle",  help="handle value to read characteristic", default=0x002d)

def main():
    args = parser.parse_args()
    inkbird = InkbirdReader(args.device, int(args.handle, 16))
    (temperature, humidity) = inkbird.read(0)
    print("Temperature: {} C".format(temperature))
    print("Humidity:    {} %".format(humidity))

if __name__ == "__main__":
    main()