import machine
import neopixel
import time
import math
import ntptime
from wifi import connect_wifi
from neopixel_matrix import xy_to_index, xy_to_lonlat
from sun_math import sun_position, is_daytime

try:
    connect_wifi('Wokwi-GUEST', '')
    # connect_wifi(home_wifi['ssid'], home_wifi['password'])
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

DAY =  	(255,249,121)
NIGHT = (81,72,178)

# Get current UTC timestamp
utc_now = time.time()
# Calculate sun position
delta, lambda_s = sun_position(utc_now)

np = neopixel.NeoPixel(machine.Pin(GPIO_DIN), NUM_LEDS)

for y in range(HEIGHT):
    for x in range(WIDTH):
        lon, lat = xy_to_lonlat(x, y, width=WIDTH, height=HEIGHT)
        index = xy_to_index(x, y, zigzag=False, flip_y=True, square_split_x=True)
        
        if is_daytime(lon, math.radians(lat), delta, lambda_s):
            np[index] = DAY
        else:
            np[index] = NIGHT

        np.write()