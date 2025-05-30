import machine
import neopixel
from neopixel_matrix import xy_to_index

NUM_LEDS = 512
GPIO_DIN = 2

np = neopixel.NeoPixel(machine.Pin(GPIO_DIN), NUM_LEDS)

for i in range(NUM_LEDS):
    np[i] = (0, 0, 255)
np.write()

np[xy_to_index(2, -5, zigzag=False)] = (255, 0, 0)
np.write()