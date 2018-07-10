import machine
import time

from machine import Pin
from urequests import get


MIN_DUTY = 27
MAX_DUTY = 136

PEACEFUL_DUTY = 33
ANNOYING_DUTY = 128

serve_peace = False

HOST = "http://robotic.ventures:3001"

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


if __name__ == "__main__":
    servo = machine.PWM(Pin(12), freq=50)
    servo.duty(PEACEFUL_DUTY if serve_peace else ANNOYING_DUTY)

    while True:
        # Poll for current status
        res = retrieve_url(HOST + '/peace')
        peaceful = res["peaceful"]

        # Move motor on status change
        if peaceful and not serve_peace:
            serve_peace = True
            servo.duty(PEACEFUL_DUTY)
            print("Peaceful duty")
        elif not peaceful and serve_peace:
            serve_peace = False
            servo.duty(ANNOYING_DUTY)
            print("Annoying duty")

        time.sleep(.3)
