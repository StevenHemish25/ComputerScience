from adafruit_circuitplayground import cp
import time
# when the program finishes, the board enters a "waiting" state
# -> flashes all green then off
# we do not want the program to ever end
# Thats why we put our work in a while TRUE, because while true runs forever



while True:

    cp.pixels.fill((0,0,25))
    cp.play_tone(500, .5)
    time.sleep(.500)
    cp.pixels.fill((25,0,0))
    cp.play_tone(900, .5)
    time.sleep(.5)
    