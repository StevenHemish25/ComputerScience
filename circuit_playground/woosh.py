# We first need to import board specific tools
# Every project for this board will need this statement
from adafruit_circuitplayground import cp
import time
# when the program finishes, the board enters a "waiting" state
# -> flashes all green then off
# we do not want the program to ever end
# Thats why we put our work in a while TRUE, because while true runs forever

while True:

    if cp.button_a:
        for i in range(0,10):
        
            cp.pixels[i] = (0,5,0)
            time.sleep (.1)
            cp.pixels[i] = (0,0,0)
            