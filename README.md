# Servo Peace

esp32 code for interacting with a simple servo to block an annoying door sensor

One esp32 is required for the servo, see servo/main.py

One esp32 is required for the button, see button/main.py

The button esp32 can make requests to the webservice, and also reflects the current status via LEDs.
The servo esp32 responds to the webservice and does the action of covering up the sensor

## Board set up
 * Run on boards with the esp wroom32 chip, eg the Adafruit Huzzah
 * Very similar steps to setting up a esp8266:
  https://learn.adafruit.com/micropython-basics-how-to-load-micropython-on-a-board/esp8266
 * You'll need to download the latest ESP32 bin to flash the board:
  sudo esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 ../esp32-20180524-v1.9.4-85-gdf9b7e8f.bin
 * Install ampy for interacting with the obard:
  https://learn.adafruit.com/micropython-basics-load-files-and-run-code/install-ampy

## Assuming ampy is installed upload code:
export AMPY_PORT=/dev/ttyUSB0
 * Try it:
   ampy run main.py
 * Upload it:
   ampy put main.py
The environment variable doesn't always seem to work, and you may need sudo, if so, try:
  sudo ampy -p /dev/ttyUSB0 put main.py
  
For servo-peace in particular

* Both esp32s:
  sudo ampy -p /dev/ttyUSB0 put boot.py
* Servo esp32:
  sudo ampy -p /dev/ttyUSB0 put servo/main.py
* Button esp32:
  sudo ampy -p /dev/ttyUSB0 put servo/main.py
  
### To get on:
screen $AMPY_PORT 115200
