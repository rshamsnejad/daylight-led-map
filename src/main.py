import machine
import neopixel
import time
import math
import ntptime
from wifi import connect_wifi
from neopixel_matrix import xy_to_index, xy_to_lonlat
from sun_math import sun_position, is_daytime
from tm1637 import TM1637

# MODE = "hardware"
MODE = "simulation"

if MODE == "hardware":
    from secrets.home_wifi import home_wifi
    SSID = home_wifi['ssid']
    PASSWORD = home_wifi['password']
    ZIGZAG = True
    FLIP_X = True
    FLIP_Y = True
else:
    SSID = 'Wokwi-GUEST'
    PASSWORD = ''
    ZIGZAG = False
    FLIP_X = False
    FLIP_Y = False


try:
    connect_wifi(SSID, PASSWORD)
except Exception as e:
    print("Unable to connect to internet!")
    print(e)

try:
    ntptime.settime()
except Exception as e:
    print("Unable to retrieve NTP time!")
    print(e)

WIDTH = 32
HEIGHT = 16
NUM_LEDS = WIDTH * HEIGHT
GPIO_DIN = 2

if MODE == "hardware":
    DAY   = (183, 177, 49)
    NIGHT = (9, 0, 106)
else:
    DAY =  	(255,249,121)
    NIGHT = (81,72,178)

# Get current UTC timestamp
utc_now = time.time()
print(time.gmtime(utc_now))
print(time.localtime(utc_now))

# Display time on TM1637 clock
tm = TM1637(clk=machine.Pin(4), dio=machine.Pin(5))
tm.numbers(time.gmtime(utc_now)[3], time.gmtime(utc_now)[4])

# Calculate sun position
delta, lambda_s = sun_position(utc_now)

np = neopixel.NeoPixel(machine.Pin(GPIO_DIN), NUM_LEDS)

for y in range(HEIGHT):
    for x in range(WIDTH):
        lon, lat = xy_to_lonlat(x, y, width=WIDTH, height=HEIGHT)
        index = xy_to_index(x, y, zigzag=ZIGZAG, flip_x=FLIP_X, flip_y=FLIP_Y, square_split_x=True)
        
        if is_daytime(lon, math.radians(lat), delta, lambda_s):
            np[index] = DAY
        else:
            np[index] = NIGHT

        np.write()