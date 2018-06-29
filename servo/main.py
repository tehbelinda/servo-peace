import machine
from machine import Pin


MIN_DUTY = 27
MAX_DUTY = 136

PEACEFUL_DUTY = 33
ANNOYING_DUTY = 128


serve_peace = False

if __name__ == '__main__':
    servo = machine.PWM(Pin(12), freq=50)
    servo.duty(PEACEFUL_DUTY if serve_peace else ANNOYING_DUTY)

    peaceful = True # Get from socket
    while True:
        if peaceful and not serve_peace:
            serve_peace = True
            servo.duty(PEACEFUL_DUTY)
        elif not peaceful and serve_peace:
            serve_peace = False
            servo.duty(ANNOYING_DUTY)
