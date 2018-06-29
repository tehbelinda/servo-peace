# This file is automatically run on boot

def connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        # Update this to your wifi network
        sta_if.connect('TRI Guest WiFi', 'tri welcomes you')
        counter = 0
        while not sta_if.isconnected():
            counter += 1
            if counter < 100:
                pass
    print('network config:', sta_if.ifconfig())

connect()
