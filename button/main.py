import neopixel
import time
from machine import Pin


NUM_LEDS = 32
# Color settings at 100 not 255 because it's really bright!
GREEN = (0, 100, 0)
RED = (100, 0, 0)


def is_pressed(button):
    # Debounce button value over 100ms
    first = button.value()
    time.sleep(0.1)
    second = button.value()
    if first and not second:
        return True
    elif second and not first:
        return False


def color_leds(color):
    # Set leds to a RGB tuple
    for i in range(NUM_LEDS):
        leds[i] = color
    leds.write()


button_pressed = False

if __name__ == '__main__':
    leds = neopixel.NeoPixel(Pin(12, Pin.OUT), NUM_LEDS, timing=True)
    button = Pin(22, Pin.IN, Pin.PULL_UP)
    color_leds((50, 50, 50))

    while True:
        if not button_pressed and is_pressed(button):
            button_pressed = True
            # Send request to toggle
            print ("Send!")
        elif button_pressed and not is_pressed(button):
            button_pressed = False
