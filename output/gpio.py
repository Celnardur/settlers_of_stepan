from smbus2 import SMBus
import time

def test(address):
    start = time.time()
    while True:
        with SMBus(1) as bus:
            read = bus.read_byte_data(address, 0)
        if read != 0:
            return (200, read)
        time.sleep(0.1)
        if time.time() - start > 15:
            return (400, "You need to press a button within 15 seconds")

    return (500, "Something went seriously wrong if your getting this response")
