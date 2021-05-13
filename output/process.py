from output import led_strip
from output import gpio
from output.pwm import PCA9685

def process(state):
    try:
        led_strip.set(state)
    except:
        pass

    for i, tile in enumerate(state['hexes']):
        try:
            set_tile_type(tile['address'], tile['tile_type'])
            set_num(tile['address'], tile['roll_number'])
            set_robber(tile['address'], i, state['robber'])
        except:
            pass

def set_tile_type(address, tile_type):
    address = 0x40 | address
    pwm = PCA9685(address)
    pwm.begin()
    brightness = 0.7
    pin = 0
    if tile_type == 'Forest':
        pin = 0
    elif tile_type == 'Desert':
        pin = 1
    elif tile_type == 'Hills':
        pin = 2
    elif tile_type == 'Mountains':
        pin = 3
    elif tile_type == 'Pasture':
        pin = 5
    elif tile_type == 'Fields':
        pin = 6

    pins = [0,1,2,3,5,6]
    for i in pins:
        if i == pin:
            pwm.setPin(i, brightness)
        else:
            pwm.setPin(i, 0)

def set_num(address, value):
    address = address | 0x40
    pwm = PCA9685(address)
    pwm.begin()
    pins = []
    if value == 2:
        pins = [8,9,12,13,15]
    elif value == 3:
        pins = [9,10,12,13,15]
    elif value == 4:
        pins = [10,12,14,15]
    elif value == 5:
        pins = [9,10,13,14,15]
    elif value == 6:
        pins = [8,9,10,11,13,14,15]
    elif value == 8:
        pins = [8,9,10,12,13,14,15]
    elif value == 9:
        pins = [9,10,11,12,13,14,15]
    elif value == 10:
        pins = [8,10,12,13,14,15]
    elif value == 11:
        pins = [8,9,10,11,14,15]
    elif value == 12:
        pins = [8,9,13,14]

    for i in range(8, 16):
        if i in pins:
            pwm.setPin(i, 1)
        else:
            pwm.setPin(i, 0)

def set_robber(address, tile_id, robber):
    address = address | 0x40
    pwm = PCA9685(address)
    pwm.begin()
    if tile_id == robber:
        pwm.setPin(4, 0.7)
    else:
        pwm.setPin(4, 0)


