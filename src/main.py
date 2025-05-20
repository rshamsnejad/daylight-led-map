# https://docs.micropython.org/en/latest/esp8266/tutorial/neopixel.html
import machine
import neopixel
import time
import ntptime
from suntimes import get_suntime
from wokwi_wifi import connect_wokwi_wifi



NUM_LEDS = 24
GPIO_DIN = 2
SUNLIGHT_RGB = (244, 233, 155)

np = neopixel.NeoPixel(machine.Pin(GPIO_DIN), NUM_LEDS)

try:
    connect_wokwi_wifi()
except:
    print("Unable to connect to internet!")

try:
    ntptime.settime()
except:
    print("Unable to retrieve NTP time!")

print(f"Current local time: {time.localtime()}")
print(get_suntime(lat='36.7201600', lon='-4.4203400', date='05-20-2025'))

for i in range(NUM_LEDS-1, -1, -1):
    # print(f"Lighting up LED {i}")
    np[i] = SUNLIGHT_RGB
    np.write()
    time.sleep(0.1)
