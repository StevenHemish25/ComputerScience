






from adafruit_circuitplayground import cp
import time


while True:

        x, y, z = cp.acceleration
        
        
        
        

        if x > 5:

        #TILTED RIGHT, PIXELS 7 8 9
        

            for i in range(1,4):
                cp.pixels[i] = (0,0,5)

    

        elif x < -5:

        #TILTED LEFT, PIXELS 2,3,4
        

            for i in range(6,9):
                cp.pixels[i] = (0,0,5)


        else:

            cp.pixels.fill((0,0,0))