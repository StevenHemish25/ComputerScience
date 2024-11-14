from adafruit_circuitplayground import cp
import time
import random
# when the program finishes, the board enters a "waiting" state
# -> flashes all green then off
# we do not want the program to ever end
# Thats why we put our work in a while TRUE, because while true runs forever



while True:
    count = 0
    def button():
        
        count == count+1
        cp.pixels[0 + count] = (0,0,5)
        

        
        
        
    if cp.button_a:
        button()