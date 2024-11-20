# We first need to import board specific tools
# Every project for this board will need this statement
from adafruit_circuitplayground import cp
import time
import random
# when the program finishes, the board enters a "waiting" state
# -> flashes all green then off
# we do not want the program to ever end
# Thats why we put our work in a while TRUE, because while true runs forever



while True:
    
    x, y, z = cp.acceleration

    if abs(z) > 25:

        for i in range(0,10):

            cp.pixels[i] = (random.randint(0,10),random.randint(0,10),random.randint(0,10))

      