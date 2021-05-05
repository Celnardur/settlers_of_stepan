from rpi_ws281x import *

# LED strip configuration:
LED_COUNT      = 119      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 10     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

def lightLED(strip, color, i):
    strip.setPixelColor(i, color)
    strip.show()

def roadSolver(n):
    return [7*n+2, 7*n+3, 7*n+4]

def citySolver(n):
    if(n == 0):
        return [12, 13, 14, 15]
    elif(n == 1):
        return [26, 27, 28, 29]
    elif(n == 2):
        return [40, 41, 42, 43]
    elif(n == 3):
        return [5, 6, 7, 8]
    elif(n == 4):
        return [19, 20, 21, 22]
    elif(n == 5):
        return [33, 34, 35, 36]
    elif(n == 6):
        return [47, 48, 49, 50]
    elif(n == 7):
        return [0, 1, 96, 97, 98, 99]
    elif(n == 8):
        return [82, 83, 84, 85]
    elif(n == 9):
        return [68, 69, 70, 71]
    elif(n == 10):
        return [54, 55, 56, 57]
    elif(n == 11):
        return [110, 111, 112, 113]
    else:
        return [120]

def settlementSolver(n):
    if(n == 0):
        return [13, 14]
    elif(n == 1):
        return [27, 28]
    elif(n == 2):
        return [41, 42]
    elif(n == 3):
        return [6, 7]
    elif(n == 4):
        return [20, 21]
    elif(n == 5):
        return [34, 35]
    elif(n == 6):
        return [48, 49]
    elif(n == 7):
        return [0, 97, 98]
    elif(n == 8):
        return [83, 84]
    elif(n == 9):
        return [69, 70]
    elif(n == 10):
        return [55, 56]
    elif(n == 11):
        return [111, 112]
    else:
        return [120]

def test():
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()
    lightLED(strip, Color(255, 0, 0), 3)

def set(state):
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)    
    strip.begin()
    for player in state['players']:
        c = player['color']
        for roads in player['roads']:
            for vals in roadSolver(roads):
                lightLED(strip, Color(c[0], c[1], c[2]), vals)
        for settlements in player['settlements']:
            for vals in settlementSolver(settlements):
                lightLED(strip, Color(c[0], c[1], c[2]), vals)
        for cities in player['cities']:
            for vals in citySolver(cities):
                lightLED(strip, Color(c[0], c[1], c[2]), vals)
