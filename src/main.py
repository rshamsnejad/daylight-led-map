# https://docs.micropython.org/en/latest/esp8266/tutorial/neopixel.html
import machine
import neopixel
import time
import ntptime
from suntimes import get_suntime
from wokwi_wifi import connect_wokwi_wifi
from timedate import Timedate



NUM_LEDS = 24
GPIO_DIN = 2
SUNLIGHT_RGB = (244, 233, 155)
TIMEZONE_OFFSETS = list(range(-11, 13))
UTC_INDEX = TIMEZONE_OFFSETS.index(0)

np = neopixel.NeoPixel(machine.Pin(GPIO_DIN), NUM_LEDS)

try:
    connect_wokwi_wifi()
except:
    print("Unable to connect to internet!")

try:
    ntptime.settime()
except:
    print("Unable to retrieve NTP time!")

utc_time = time.gmtime()
utc_time_string = f"{utc_time[0]}-{utc_time[1]:0>2}-{utc_time[2]:0>2}T{utc_time[3]:0>2}:{utc_time[4]:0>2}:{utc_time[5]:0>2}"
print(f"Current UTC time: {utc_time_string}")

utc_date_us = f"{utc_time[1]:0>2}-{utc_time[2]:0>2}-{utc_time[0]}"
utc_suntime = get_suntime(lat='0', lon='0', date=utc_date_us)
utc_noon_string = utc_suntime['data']['solarNoon'].split('.')[0]
# print(suntime)
print(f"UTC Solar Noon: {utc_noon_string}")

utc_time = Timedate(utc_time_string)
utc_noon = Timedate(utc_noon_string)
print(utc_time > utc_noon)

# for i in range(NUM_LEDS-1, -1, -1):
#     # print(f"Lighting up LED {i}")
#     np[i] = SUNLIGHT_RGB
#     np.write()
#     time.sleep(0.1)

