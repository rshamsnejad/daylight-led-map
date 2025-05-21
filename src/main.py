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
TIMEZONE_LONGITUDES = [i * (360/NUM_LEDS) for i in TIMEZONE_OFFSETS]
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

utc_tuple = time.gmtime()
utc_time = Timedate()
utc_time.set_timedate_ints(utc_tuple[0], utc_tuple[1], utc_tuple[2], utc_tuple[3], utc_tuple[4], utc_tuple[5])

print(f"Current UTC time: {utc_time}")

utc_date_us = f"{utc_time.get_date_ints()[1]:0>2}-{utc_time.get_date_ints()[2]:0>2}-{utc_time.get_date_ints()[0]}"
utc_suntime = get_suntime(lat='0', lon='0', date=utc_date_us)

utc_noon = Timedate()
utc_noon.set_timedate_string(utc_suntime['data']['solarNoon'])

print(f"UTC Solar Noon: {utc_noon}")

print(utc_time > utc_noon)

timezones = []
for offset in TIMEZONE_OFFSETS:
       
    timezones.append(utc_time.add_hour(offset))

    print(timezones[-1])


# for i in range(NUM_LEDS-1, -1, -1):
#     # print(f"Lighting up LED {i}")
#     np[i] = SUNLIGHT_RGB
#     np.write()
#     time.sleep(0.1)

