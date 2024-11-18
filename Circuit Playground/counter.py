from adafruit_circuitplayground import cp
import time
import random
# when the program finishes, the board enters a "waiting" state
# -> flashes all green then off
# we do not want the program to ever end
# Thats why we put our work in a while TRUE, because while true runs forever

count = 0


    
    

while True:
    
    
    if cp.button_a:
        while cp.button_a:
             pass
        if count == 10:
            count == 10

            cp.pixels[-1 + count] = (0,0,5)
        
        else:
            count += 1

        

            cp.pixels[-1 + count] = (0,0,5)

    elif cp.button_b:
        while cp.button_b:
            pass
        if count == 0:
            count == 0

            cp.pixels[0] = (0,0,0)

        else:
            count -= 1

            cp.pixels[0+ count] = (0,0,0)