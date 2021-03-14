import struct
import time

## Important Registers
MODE1 = 0x00
MODE2 = 0x01

class PCA9685:
    def __init__(self, bus, addr = 0x40):
        self.bus = bus
        self.addr = addr

    def begin(self):
        self.writeByte(MODE1, 0x20)
        time.sleep(.1)

    def setPin(self, pin, dutyCycle=0, delay=0):
        onCount = max(int(4096 * delay) - 1, 0)
        offCount = max((int(dutyCycle * 4096) + onCount - 1), 0) & 0x0FFF
        print(onCount, offCount)
        self.write_pin(pin, True, onCount)
        self.write_pin(pin, False, offCount)

    def write_pin(self, pin, on, count):
        #TODO: indicate error if writing to non-existant pin
        if on:
            l = 6 + pin * 4
            h = 7 + pin * 4
        else:
            l = 8 + pin * 4
            h = 9 + pin * 4

        self.writeByte(h, (count & 0xFF00) >> 8)
        self.writeByte(l, count & 0x00FF)

    def writeByte(self, reg, byte):
        self.bus.write_byte_data(self.addr, reg, byte)

    def readByte(self, reg):
        return self.bus.read_byte_data(self.addr, reg)


