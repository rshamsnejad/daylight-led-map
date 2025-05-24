# https://docs.micropython.org/en/latest/esp8266/tutorial/neopixel.html
import machine
import neopixel
import time
import ntptime
from suntimes import get_suntime
from wifi import connect_wifi
from secrets.home_wifi import home_wifi
from timedate import Timedate



NUM_LEDS = 24
GPIO_DIN = 2
SUNLIGHT_RGB = {
    "dawn":      (20,50,255,0),
    "morning":   (255,100,0,0),
    "afternoon": (255,50,0,0),
    "dusk":      (200,20,120,0),
    "night":     (0,0,255,0)                
}
SUNLIGHT_RGB = {
    "dawn":      (2,5,25,0),
    "morning":   (25,5,0,0),
    "afternoon": (25,7,0,0),
    "dusk":      (20,2,12,0),
    "night":     (5,0,25,0)                
}
TIMEZONE_OFFSETS = list(range(-11, 13))
TIMEZONE_LONGITUDES = [i * (360/NUM_LEDS) for i in TIMEZONE_OFFSETS]
UTC_INDEX = TIMEZONE_OFFSETS.index(0)

np = neopixel.NeoPixel(machine.Pin(GPIO_DIN), NUM_LEDS, bpp=4)

try:
    # connect_wifi('Wokwi-GUEST', '')
    connect_wifi(home_wifi['ssid'], home_wifi['password'])
except Exception as e:
    print("Unable to connect to internet!")
    print(e)

try:
    ntptime.settime()
except Exception as e:
    print("Unable to retrieve NTP time!")
    print(e)

utc_tuple = time.gmtime()
utc_time = Timedate()
utc_time.set_timedate_ints(utc_tuple[0], utc_tuple[1], utc_tuple[2], utc_tuple[3], utc_tuple[4], utc_tuple[5])

today_us_format = f"{utc_time.get_date_ints()[1]:0>2}-{utc_time.get_date_ints()[2]:0>2}-{utc_time.get_date_ints()[0]}"
suntime_api_response = get_suntime(lat='0', lon='0', date=today_us_format)

suntime = {
    "dawn":    Timedate(),
    "sunrise": Timedate(),
    "noon":    Timedate(),
    "dusk":    Timedate(),
    "sunset":  Timedate(),
    "night":   Timedate()
}

suntime['dawn'].set_timedate_string(suntime_api_response['data']['dawn'])
suntime['sunrise'].set_timedate_string(suntime_api_response['data']['sunrise'])
suntime['noon'].set_timedate_string(suntime_api_response['data']['solarNoon'])
suntime['dusk'].set_timedate_string(suntime_api_response['data']['dusk'])
suntime['sunset'].set_timedate_string(suntime_api_response['data']['sunset'])
suntime['night'].set_timedate_string(suntime_api_response['data']['night'])

i = 0
for offset in TIMEZONE_OFFSETS:
       
    current_time = utc_time.add_hour(offset)

    if   suntime['dawn'] <= current_time and current_time < suntime['sunrise']:
        np[i] = SUNLIGHT_RGB['dawn']
    elif suntime['sunrise'] <= current_time and current_time < suntime['noon']:
        np[i] = SUNLIGHT_RGB['morning']
    elif suntime['noon'] <= current_time and current_time < suntime['dusk']:
        np[i] = SUNLIGHT_RGB['afternoon']
    elif suntime['dusk'] <= current_time and current_time < suntime['sunset']:
        np[i] = SUNLIGHT_RGB['dusk']
    else:
        np[i] = SUNLIGHT_RGB['night']
    
    np.write()

    i += 1
