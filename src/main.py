# Dummy library for testing purposes
from customprint import customprint
customprint("Importing libraries works!")

# https://docs.micropython.org/en/latest/esp8266/tutorial/neopixel.html
import machine, neopixel, time, ntptime

NUM_LEDS = 24
GPIO_DIN = 2

np = neopixel.NeoPixel(machine.Pin(GPIO_DIN), NUM_LEDS)

try:
    ntptime.settime()
except:
    print("Unable to retrieve NTP time!")

print(f"Current local time: {time.localtime()}")

for i in range(NUM_LEDS-1, -1, -1):
    # print(f"Lighting up LED {i}")
    np[i] = (244, 233, 155)
    np.write()
    time.sleep(0.1)
