from rpi_ws281x import *

# LED strip configuration:
LED_COUNT      = 504      # Number of LED pixels.
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
        return [103, 104, 105, 106]
    elif(n == 12):
        return [89, 90, 91, 92, 378, 379]
    elif(n == 13):
        return [75, 76, 77, 78, 432, 433]
    elif(n == 14):
        return [61, 62, 63, 64, 448, 449]
    elif(n == 15):
        return [495, 496, 497, 498]
    elif(n == 16):
        return [110, 111, 112, 113, 376, 377]
    elif(n == 17):
        return [124, 125, 126, 127, 383, 384]
    elif(n == 18):
        return [138, 139, 140, 141, 427, 428]
    elif(n == 19):
        return [152, 153, 154, 155, 453, 454]
    elif(n == 20):
        return [166, 167, 168, 169, 490, 491]
    elif(n == 21):
        return [369, 370, 371, 372]
    elif(n == 22):
        return [117, 118, 119, 120, 385, 386]
    elif(n == 23):
        return [131, 132, 133, 134, 425, 426]
    elif(n == 24):
        return [145, 146, 147, 148, 455, 456]
    elif(n == 25):
        return [159, 160, 161, 162, 488, 489]
    elif(n == 26):
        return [173, 174, 175, 176]
    elif(n == 27):
        return [362, 363, 364, 365]
    elif(n == 28):
        return [236, 237, 238, 239, 390, 391]
    elif(n == 29):
        return [222, 223, 224, 225, 420, 421]
    elif(n == 30):
        return [208, 209, 210, 211, 460, 461]
    elif(n == 31):
        return [194, 195, 196, 197, 483, 484]
    elif(n == 32):
        return [180, 181, 182, 183]
    elif(n == 33):
        return [243, 244, 245, 246, 357, 358]
    elif(n == 34):
        return [229, 230, 231, 232, 392, 393]
    elif(n == 35):
        return [215, 216, 217, 218, 418, 419]
    elif(n == 36):
        return [201, 202, 203, 204, 462, 463]
    elif(n == 37):
        return [187, 188, 189, 190, 481, 482]
    elif(n == 38):
        return [250, 251, 252, 253]
    elif(n == 39):
        return [264, 265, 266, 267, 397, 398]
    elif(n == 40):
        return [278, 279, 280, 281, 413, 414]
    elif(n == 41):
        return [292, 293, 294, 295, 467, 468]
    elif(n == 42):
        return [474, 475, 476, 477]
    elif(n == 43):
        return [257, 258, 259, 260, 355, 356]
    elif(n == 44):
        return [271, 272, 273, 274, 399, 400]
    elif(n == 45):
        return [285, 286, 287, 288, 411, 412]
    elif(n == 46):
        return [299, 300, 301, 302, 469, 470]
    elif(n == 47):
        return [348, 349, 350, 351]
    elif(n == 48):
        return [334, 335, 336, 337, 404, 405]
    elif(n == 49):
        return [320, 321, 322, 323, 406, 407]
    elif(n == 50):
        return [306, 307, 308, 309]
    elif(n == 51):
        return [341, 342, 343, 344]
    elif(n == 52):
        return [327, 328, 329, 330]
    elif(n == 53):
        return [313, 314, 315, 316]

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
        return [20, 21, 440]
    elif(n == 5):
        return [34, 35, 441]
    elif(n == 6):
        return [48, 49]
    elif(n == 7):
        return [0, 97, 98]
    elif(n == 8):
        return [83, 84, 434]
    elif(n == 9):
        return [69, 70, 447]
    elif(n == 10):
        return [55, 56, 503]
    elif(n == 11):
        return [104, 105]
    elif(n == 12):
        return [90, 91, 378]
    elif(n == 13):
        return [76, 77, 433]
    elif(n == 14):
        return [62, 63, 448]
    elif(n == 15):
        return [496, 497]
    elif(n == 16):
        return [111, 112, 377]
    elif(n == 17):
        return [125, 126, 384]
    elif(n == 18):
        return [139, 140, 427]
    elif(n == 19):
        return [153, 154, 454]
    elif(n == 20):
        return [167, 168, 490]
    elif(n == 21):
        return [370, 371]
    elif(n == 22):
        return [118, 119, 385]
    elif(n == 23):
        return [132, 133, 426]
    elif(n == 24):
        return [146, 147, 455]
    elif(n == 25):
        return [160, 161, 489]
    elif(n == 26):
        return [174, 175]
    elif(n == 27):
        return [363, 364]
    elif(n == 28):
        return [237, 238, 391]
    elif(n == 29):
        return [223, 224, 420]
    elif(n == 30):
        return [209, 210, 461]
    elif(n == 31):
        return [195, 196, 483]
    elif(n == 32):
        return [181, 182]
    elif(n == 33):
        return [244, 245, 357]
    elif(n == 34):
        return [230, 231, 392]
    elif(n == 35):
        return [216, 217, 419]
    elif(n == 36):
        return [202, 203, 462]
    elif(n == 37):
        return [188, 189, 482]
    elif(n == 38):
        return [251, 252]
    elif(n == 39):
        return [265, 266, 398]
    elif(n == 40):
        return [279, 280, 413]
    elif(n == 41):
        return [293, 294, 468]
    elif(n == 42):
        return [475, 476]
    elif(n == 43):
        return [258, 259, 356]
    elif(n == 44):
        return [272, 273, 399]
    elif(n == 45):
        return [286, 287, 412]
    elif(n == 46):
        return [300, 301, 469]
    elif(n == 47):
        return [349, 350]
    elif(n == 48):
        return [335, 336, 405]
    elif(n == 49):
        return [321, 322, 406]
    elif(n == 50):
        return [307, 308]
    elif(n == 51):
        return [342, 343]
    elif(n == 52):
        return [328, 329]
    elif(n == 53):
        return [314, 315]

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

def startupAnimation():
    for i in range(904):
        if i<504:
            lightLED(strip, [0, 104, 132], i)
        if i>=20 and i<524:
            lightLED(strip, [137, 219, 236], i-20)
        if i>=40 and i<544:
            lightLED(strip, [250, 157, 0], i-40)
        if i>=60 and i<564:
            lightLED(strip, [50, 100, 0], i-60)
        if i>=80 and i<584:
            lightLED(strip, [110, 0, 108], i-80)
        if i>=100 and i<604:
            lightLED(strip, [246, 131, 112], i-100)
        if i>=120 and i<624:
            lightLED(strip, [115, 235, 174], i-120)
        if i>=140 and i<644:
            lightLED(strip, [140, 101, 211], i-140)
        if i>=160 and i<664:
            lightLED(strip, [243, 135, 47], i-160)
        if i>=180 and i<684:
            lightLED(strip, [76, 146, 177], i-180)
        if i>=200 and i<704:
            lightLED(strip, [168, 200, 121], i-200)
        if i>=220 and i<724:
            lightLED(strip, [173, 167, 89], i-220)
        if i>=240 and i<744:
            lightLED(strip, [255, 0, 51], i-240)
        if i>=260 and i<764:
            lightLED(strip, [84, 39, 143], i-260)
        if i>=280 and i<784:
            lightLED(strip, [247, 25, 1], i-280)
        if i>=300 and i<804:
            lightLED(strip, [235, 225, 223], i-300)
        if i>=320 and i<824:
            lightLED(strip, [108, 79, 60], i-320)
        if i>=340 and i<844:
            lightLED(strip, [108, 160, 220], i-340)
        if i>=360 and i<864:
            lightLED(strip, [236, 219, 83], i-360)
        if i>=380 and i<884:
            lightLED(strip, [227, 65, 50], i-380)
        if i>=400 and i<904:
            lightLED(strip, [0, 0, 0], i-400)
