# source: https://medium.com/xster-tech/using-luxafor-with-linux-53381093a40f

import argparse
import usb.core
def main():
    parser = argparse.ArgumentParser(description='Change Luxafor color')

    parser.add_argument('color', choices=['green', 'yellow', 'red', 'blue', 'white', 'off'], help='color to change to')

    args = parser.parse_args()

    color_codes = {'green': 71, 'yellow': 89, 'red': 82, 'blue':66, 'white': 87, 'off': 79}

    dev = usb.core.find(idVendor=0x04d8, idProduct=0xf372)

    if dev is None:
        print('Not connected')
        return

    try:
        dev.detach_kernel_driver(0)
    except usb.core.USBError:
        pass

    try:
        dev.set_configuration()
    except usb.core.USBError:
        print(usb.core.USBError)
        print("Did you give Luxafor USB permission to your user?")
        return

    dev.set_configuration()
    dev.write(1, [0, 0])
    dev.write(1, [0, color_codes[args.color]])

if __name__ == '__main__':
    main()
