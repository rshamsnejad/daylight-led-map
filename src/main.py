# Dummy library for testing purposes
from customprint import customprint
customprint("Importing libraries works!")

# https://docs.micropython.org/en/latest/esp8266/tutorial/neopixel.html
import machine
import neopixel
import time
import ntptime

NUM_LEDS = 24
GPIO_DIN = 2
SUNLIGHT_RGB = (244, 233, 155)

np = neopixel.NeoPixel(machine.Pin(GPIO_DIN), NUM_LEDS)

import wokwi_wifi

try:
    ntptime.settime()
except:
    print("Unable to retrieve NTP time!")

print(f"Current local time: {time.localtime()}")

for i in range(NUM_LEDS-1, -1, -1):
    # print(f"Lighting up LED {i}")
    np[i] = SUNLIGHT_RGB
    np.write()
    time.sleep(0.1)
