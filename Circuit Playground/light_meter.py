# We first need to import board specific tools
# Every project for this board will need this statement
from adafruit_circuitplayground import cp
import time
import random
# when the program finishes, the board enters a "waiting" state
# -> flashes all green then off
# we do not want the program to ever end
# Thats why we put our work in a while TRUE, because while true runs forever

light = 0

if cp.light <= 30:
    light = 1
elif cp.light <= 27:
    light = 2
elif cp.light <= 24:
    light = 3
elif cp.light <= 21:
    light = 4
elif cp.light <= 18:
    light = 5
elif cp.light <= 15:
    light = 6
elif cp.light <= 12:
    light = 7
elif cp.light <= 9:
    light = 8
elif cp.light <= 6:
    light = 9
elif cp.light <= 3:
    light =10



while True:

    while light == 1:
        cp.pixels[-1+light] = (0,0,5)
        cp.pixels[range(1,9)] = (5,5,0)
    while light == 2:
        cp.pixels[-1+light] = (0,0,5)
        cp.pixels[range(0,-2+light)] = (0,0,5)
        cp.pixels[range(2,9)] = (5,5,0)
    while light ==3:
        cp.pixels[-1+light] = (0,0,5)
        cp.pixels[range(0,-2+light)]= (0,0,5)
        cp.pixels[range(3,9)] = (5,5,0)
    while light == 4:
        cp.pixels[-1+light] = (0,0,5)
        cp.pixels[range(0,-2+light)] = (0,0,5)
        cp.pixels[range(4,9)] = (5,5,0)
    while light == 5:
        cp.pixels[-1+light] = (0,0,5)
        cp.pixels[range(0,-2+light)] = (0,0,5)
        cp.pixels[range(5,9)] = (5,5,0)
    while light == 6:
        cp.pixels[-1+light] = (0,0,5)
        cp.pixels[range(0,-2+light)] = (0,0,5)
        cp.pixels[range(6,9)] = (5,5,0)
    while light == 7:
        cp.pixels[-1+light] = (0,0,5)
        cp.pixels[range(0,-2+light)] = (0,0,5)
        cp.pixels[range(7,9)] = (5,5,0)
    while light == 8:
        cp.pixels[-1+light] = (0,0,5)
        cp.pixels[range(0,-2+light)] = (0,0,5)
        cp.pixels[range(8,9)] = (5,5,0)
    while light == 9:
        cp.pixels[-1+light] = (0,0,5)
        cp.pixels[range(0,-2+light)] = (0,0,5)
        cp.pixels[9] = (5,5,0)
    while light == 10:
        cp.pixels[-1+light] = (0,0,5)
        cp.pixels[range(0,-2+light)] = (0,0,5)










    

    
