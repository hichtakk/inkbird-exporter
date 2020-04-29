import argparse

from inkbird.ble import InkbirdReader

parser = argparse.ArgumentParser(description="")
parser.add_argument("device",  help="mac address of peripheral device")

def main():
    args = parser.parse_args()
    inkbird = InkbirdReader(args.device)
    (temperature, humidity) = inkbird.read(0)
    print("Temperature: {} C".format(temperature))
    print("Humidity:    {} %".format(humidity))

if __name__ == "__main__":
    main()