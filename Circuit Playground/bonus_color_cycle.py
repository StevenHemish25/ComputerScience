# We first need to import board specific tools
# Every project for this board will need this statement
from adafruit_circuitplayground import cp
import time
import random
# when the program finishes, the board enters a "waiting" state
# -> flashes all green then off
# we do not want the program to ever end
# Thats why we put our work in a while TRUE, because while true runs forever

presses = 0

def button_press():
    
    if presses == 1:
            
        cp.pixels.fill((10,5,0))

    elif presses == 2:

        cp.pixels.fill((5,5,0))

    elif presses == 3:

        cp.pixels.fill((0,5,0))

    elif presses == 4:

        cp.pixels.fill((0,0,5))

    elif presses == 5:

        cp.pixels.fill((3,0,5))

    elif presses == 6:

        cp.pixels.fill((5,0,5))
    elif presses ==7:

        cp.pixels.fill((5,0,0))

        presses = 0 

        if cp.button_a:
            
            presses += 1

            button_press()

            
while True:
    
    if cp.button_a:
           
           presses += 1

           button_press()