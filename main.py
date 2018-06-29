import machine


if __name__ == '__main__':
    servo = machine.PWM(machine.Pin(12), freq=50)
    servo.duty(77)
