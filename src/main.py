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
SUNLIGHT_RGB = {
    "dawn":      (102,150,186),
    "morning":   (226,227,139),
    "afternoon": (231,165,83),
    "dusk":      (126,75,104),
    "night":     (41,41,101)
}
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

utc_date_us = f"{utc_time.get_date_ints()[1]:0>2}-{utc_time.get_date_ints()[2]:0>2}-{utc_time.get_date_ints()[0]}"
utc_suntime = get_suntime(lat='0', lon='0', date=utc_date_us)

utc = {
    "dawn":    Timedate(),
    "sunrise": Timedate(),
    "noon":    Timedate(),
    "dusk":    Timedate(),
    "sunset":  Timedate(),
    "night":   Timedate()
}

utc['dawn'].set_timedate_string(utc_suntime['data']['dawn'])
utc['sunrise'].set_timedate_string(utc_suntime['data']['sunrise'])
utc['noon'].set_timedate_string(utc_suntime['data']['solarNoon'])
utc['dusk'].set_timedate_string(utc_suntime['data']['dusk'])
utc['sunset'].set_timedate_string(utc_suntime['data']['sunset'])
utc['night'].set_timedate_string(utc_suntime['data']['night'])


current_times = []
suntimes = []
colors = []
i = 0
for offset in TIMEZONE_OFFSETS:
       
    current_times.append(utc_time.add_hour(offset))

    if   utc['dawn'] <= current_times[-1] and current_times[-1] < utc['sunrise']:
        colors.append(SUNLIGHT_RGB['dawn'])
    elif utc['sunrise'] <= current_times[-1] and current_times[-1] < utc['noon']:
        colors.append(SUNLIGHT_RGB['morning'])
    elif utc['noon'] <= current_times[-1] and current_times[-1] < utc['dusk']:
        colors.append(SUNLIGHT_RGB['afternoon'])
    elif utc['dusk'] <= current_times[-1] and current_times[-1] < utc['sunset']:
        colors.append(SUNLIGHT_RGB['dusk'])
    else:
        colors.append(SUNLIGHT_RGB['night'])
    
    # print(current_times[-1])
    # print(colors[-1])
    np[i] = colors[-1]
    i += 1
    np.write()
