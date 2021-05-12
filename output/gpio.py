from smbus2 import SMBus
import time

def wait_tile(state):
    start = time.time()
    while True:
        tiles = get_tiles(state)
        if len(tiles) > 0:
            return (200, tiles[0])

        time.sleep(0.05)
        if time.time() - start > 20:
            return (400, "You need to press a button within 20 seconds")


def wait_intersection(state):
    start = time.time()
    while True:
        roads = get_roads(state)
        if len(roads) > 1:
            if roads[0] != roads[1]:
                for intersection in state['roads'][roads[0]]['settlements']:
                    if intersection in state['roads'][roads[1]]['settlements']:
                        return (200, intersection)

        time.sleep(0.05)
        if time.time() - start > 20:
            return (400, "You need to press a button within 20 seconds")

def wait_road(state):
    start = time.time()
    while True:
        roads = get_roads(state)
        if len(roads) > 0:
            return (200, roads[0])

        time.sleep(0.05)
        if time.time() - start > 20:
            return (400, "You need to press a button within 20 seconds")

def get_tiles(state):
    tiles = []
    for i, tile in enumerate(state['hexes']):
        btns = get_buttons(tile['address'])
        if len(btns) > 0:
            tiles.append(i)
    return tiles 

# all buttons are next to roads so they will go by their road id
def get_roads(state):
    roads = []
    for i, tile in enumerate(state['hexes']):
        btns = get_buttons(tile['address'])
        for btn in btns:
            roads.append(tile['roads'][btn])
    return roads

def get_buttons(address):
    address = 0x20 | address
    io = 0
    with SMBus(1) as bus:
        io = bus.read_byte_data(address, 0)

    buttons = []
    if io & 0x01 != 0:
        buttons.append(1)
    if io & 0x02 != 0:
        buttons.append(2)
    if io & 0x04 != 0:
        buttons.append(0)
    if io & 0x08 != 0:
        buttons.append(5)
    if io & 0x10 != 0:
        buttons.append(4)
    if io & 0x20 != 0:
        buttons.append(3)

    return buttons

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
