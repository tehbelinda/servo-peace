import machine
from machine import Pin

MIN_DUTY = 27
MAX_DUTY = 136

PEACE_DUTY = 33
ANNOYING_DUTY = 128

cur_duty = PEACE_DUTY
button_pressed = False

if __name__ == '__main__':
    servo = machine.PWM(Pin(12), freq=50)
    servo.duty(cur_duty)
    button = Pin(27, Pin.IN, Pin.PULL_UP)

    while True:
        if not button_pressed and button.value() == 0:
            button_pressed = True
            cur_duty = ANNOYING_DUTY if cur_duty == PEACE_DUTY else PEACE_DUTY
            servo.duty(cur_duty)
        elif button_pressed and button.value() == 1:
            button_pressed = False
