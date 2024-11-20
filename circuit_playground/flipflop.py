# We first need to import board specific tools
# Every project for this board will need this statement
from adafruit_circuitplayground import cp
import time
# when the program finishes, the board enters a "waiting" state
# -> flashes all green then off
# we do not want the program to ever end
# Thats why we put our work in a while TRUE, because while true runs forever

while True:

    if cp.switch:
        
        
        
        for i in range(5,10):

            cp.pixels[i] = (0,0,5)

        for x in range(0,5):

            cp.pixels[x] = (0,0,0)




    else:

        for b in range(0,5):

            cp.pixels[b] = (0,0,5)

        for y in range(5,10):

            cp.pixels[y] = (0,0,0)