import machine
import neopixel
import time
from neopixel_matrix import xy_to_index

NUM_LEDS = 512
GPIO_DIN = 2

np = neopixel.NeoPixel(machine.Pin(GPIO_DIN), NUM_LEDS)

np.fill((0, 0, 0))
np.write()

for i in range(NUM_LEDS):
    np[i] = (0, 0, 255)
np.write()

np[xy_to_index(0, 0, width=32, height=16, zigzag=False, square_split_x=True)] = (255, 0, 0)
np[xy_to_index(2, 1, width=32, height=16, zigzag=False, square_split_x=True)] = (255, 0, 0)
np[xy_to_index(16, 5, width=32, height=16, zigzag=False, square_split_x=True)] = (255, 0, 0)
np.write()