# Dummy library for testing purposes
from customprint import customprint
customprint("Importing libraries works!")

# https://docs.micropython.org/en/latest/esp8266/tutorial/neopixel.html
import machine, neopixel, time

NUM_LEDS = 24
GPIO_DIN = 2

np = neopixel.NeoPixel(machine.Pin(GPIO_DIN), NUM_LEDS)

for i in range(NUM_LEDS-1, -1, -1):
    print(f"Lighting up LED {i}")
    np[i] = (255, 0, 0)
    np.write()
    time.sleep(0.5)