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

    if cp.light >= 30:
        cp.pixels[1] = (0,0,5)
    elif cp.light < 27 and cp.light > 24:
        for i in range(0,1):
            cp.pixels[i] = (0,0,5)
        for i in range(2,9):
            cp.pixels[i] = (0,0,0)
    elif cp.light < 24 and cp.light > 21:
        for i in range(0,2):
            cp.pixels[i] = (0,0,5)
        for i in range(3,9):
            cp.pixels[i] = (0,0,0)
    elif cp.light < 21 and cp.light > 18:
        for i in range(0,3):
            cp.pixels[i]= (0,0,5)
        for i in range(4,9):
            cp.pixels[i] = (0,0,0)
    elif cp.light < 18 and cp.light > 15:
        for i in range(0,4):
            cp.pixels[i]= (0,0,5)
        for i in range(5,9):
            cp.pixels[i] = (0,0,0)
    elif cp.light < 15 and cp.light > 12:
        for i in range(0,5):
            cp.pixels[i]= (0,0,5)
        for i in range(6,9):
            cp.pixels[i] = (0,0,0)
    elif cp.light < 12 and cp.light > 9:
        for i in range(0,6):
            cp.pixels[i]= (0,0,5)
        for i in range(7,9):
            cp.pixels[i] = (0,0,0)
    elif cp.light < 9 and cp.light > 6:
        for i in range(0,7):
            cp.pixels[i]= (0,0,5)
        for i in range(8,9):
            cp.pixels[i] = (0,0,0)
    elif cp.light < 6 and cp.light > 3:
        for i in range(0,8):
            cp.pixels[i]= (0,0,5)
            cp.pixels[9] = (0,0,0)
    elif cp.light < 3:
        for i in range(0,9):
            cp.pixels[i] = (0,0,5)










    

    
