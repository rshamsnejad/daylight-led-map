import machine
import neopixel
import time
from neopixel_matrix import xy_to_index
from sys import argv

MODE = "hardware"
# MODE = "simulation"
WIDTH = 32
HEIGHT = 16
SQUARE_SPLIT = True
NUM_LEDS = WIDTH * HEIGHT
GPIO_DIN = 2

if MODE == "hardware":
    zigzag = True
    flip_x = True
    # flip_x = False
    intensity = 10
else:
    zigzag = False
    flip_x = False
    # flip_x = True
    intensity = 255

np = neopixel.NeoPixel(machine.Pin(GPIO_DIN), NUM_LEDS)

np.fill((0, 0, 0))
np.write()

for i in range(NUM_LEDS):
    np[i] = (0, 0, intensity)
    # time.sleep(0.1)
    # np.write()
np.write()

red_dots = [
    (0, 0),
    (0, 1),
    (2, 1),
    (15, 15),
    (16, 5),
    (31, 15)
]

for dot in red_dots:
    index = xy_to_index(
            dot[0], dot[1],
            width=WIDTH,
            height=HEIGHT,
            zigzag=zigzag,
            flip_x=flip_x,
            square_split_x=SQUARE_SPLIT
        )

    print(f"index = {index}")

    np[index] = (intensity, 0, 0)

    np.write()