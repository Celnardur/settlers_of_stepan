#!/usr/bin/env python3

from smbus2 import SMBus
from time import sleep

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please specify the i2c address")
        print("Example:")
        print("    ./test_gpio.py 0x28")

    addr = int(sys.argv[1], 0)

    last = 0
    while True:
        now = last
        with SMBus(1) as bus:
            now = bus.read_byte_data(addr, 0)
        if now != last:
            print(hex(now))

        sleep(0.1)

