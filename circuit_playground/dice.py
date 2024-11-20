# We first need to import board specific tools
# Every project for this board will need this statement
from adafruit_circuitplayground import cp
import time
import random
# when the program finishes, the board enters a "waiting" state
# -> flashes all green then off
# we do not want the program to ever end
# Thats why we put our work in a while TRUE, because while true runs forever
def dice_roll():

    roll = random.randint(0,10)

    for m in range(roll):
        cp.pixels[m] = (0,0,25)

while True:
    

    if cp.button_a:
        dice_roll()

    elif cp.button_b:

        cp.pixels.fill((0,0,0))