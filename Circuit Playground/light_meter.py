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
    
    if cp.light == 30:
        cp.pixels[0] = (0,0,5)
    if cp.light == 27:
        cp.pixels[0] = (0,0,5)
        cp.pixels[1] = (0,0,5)
