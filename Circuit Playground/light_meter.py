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
    
    while cp.light == 30:
        cp.pixels[0] = (0,0,5)
    while cp.light == 27:
        cp.pixels[0] = (0,0,5)
        cp.pixels[1] = (0,0,5)
    while cp.light == 24:
        cp.pixels[0] = (0,0,5)
        cp.pixels[1] = (0,0,5)
        cp.pixels[2] = (0,0,5)
    while cp.light == 21:
        
        for m in range(0,4):
            
            cp.pixels[m] = (0,0,5)

    while cp.light == 18:

        for l in range(0,5):
            
            cp.pixels[l] = (0,0,5)

    while cp.light == 18:

        for l in range(0,5):
            
            cp.pixels[l] = (0,0,5)
        
    while cp.light == 18:

        for l in range(0,5):
            
            cp.pixels[l] = (0,0,5)

    while cp.light == 18:

        for l in range(0,5):
            
            cp.pixels[l] = (0,0,5)
    
    while cp.light == 15:

        for l in range(0,6):

            cp.pixels[l] = (0,0,5)

    while cp.light == 12:

        for l in range(0,7):

            cp.pixels[l] = (0,0,5)

    while cp.light == 9:

        for l in range(0,8):

            cp.pixels[l] = (0,0,5)

    while cp.light == 6:

        for l in range(0,9):

            cp.pixels[l] = (0,0,5)

    while cp.light == 3:

        for l in range(0,10):

            cp.pixels[l] = (0,0,5)










    

    
