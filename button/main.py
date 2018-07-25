import neopixel
import utime

from machine import Pin
from urequests import get, post

HOST = "http://54.218.3.161:3001"

NUM_LEDS = 32
# Color settings not at 255 because it's really bright!
GREEN = (0, 40, 0)
RED = (40, 0, 0)

serve_peace = None

# Software loop poll debounce
# button_pressed = False
# def is_pressed(button):
#     # Debounce button value over 100ms
#     first = button.value()
#     time.sleep(0.1)
#     second = button.value()
#     if first and not second:
#         return True
#     elif second and not first:
#         return False


def color_leds(color):
    # Set leds to a RGB tuple
    for i in range(NUM_LEDS):
        leds[i] = color
    leds.write()


def retrieve_url(url):
    resp = None
    try:
        print("Getting url", url)
        resp = get(url)
        value = resp.json()
        print(value)
    except Exception as e: # Here it catches any error.
        if isinstance(e, OSError) and resp: # If the error is an OSError the socket has to be closed.
            resp.close()
        value = {"error": e}
    return value


last_button_irq_time = utime.ticks_ms()
def button_change(button):
    global last_button_irq_time
    if utime.ticks_diff(utime.ticks_ms(), last_button_irq_time) < 200:
        return

    global serve_peace
    # Only activate button once status is confirmed
    if serve_peace is not None:
        print ("Sending!")
        val = 0 if serve_peace else 1
        post(HOST + "/peace?peace=" + str(val))
        last_button_irq_time = utime.ticks_ms()


if __name__ == "__main__":
    leds = neopixel.NeoPixel(Pin(12, Pin.OUT), NUM_LEDS, timing=True)
    button = Pin(22, Pin.IN, Pin.PULL_UP)
    button.irq(trigger=Pin.IRQ_FALLING, handler=button_change)

    color_leds((20, 20, 20))

    start = utime.ticks_ms()
    while True:
        # Poll for current status
        if utime.ticks_diff(utime.ticks_ms(), start) > 600:
            res = retrieve_url(HOST + "/peace")
            if "error" in res:
                print("Error", res["error"])
                continue

            peaceful = res["peaceful"]
            if serve_peace is None:
                # Set initial state
                serve_peace = peaceful
                color_leds(RED if serve_peace else GREEN)

            # Update lights on status change
            if peaceful and not serve_peace:
                serve_peace = True
                color_leds(RED)
                print("Peaceful duty")
            elif not peaceful and serve_peace:
                serve_peace = False
                color_leds(GREEN)
                print("Annoying duty")

            start = utime.ticks_ms()
