# the if statement has two buddies
# the first little buddy is the else statement

x = 10

if x > 0:   # not an every if needs an else
    print("x is a positive number")

# the second buddy is the elif statement, which is short for else if.
    
elif x < 0:
    print("x is a negative number")

else:       # else always needs an if
    print("x is zero")


light = input("What color is the light?\n")

if light.lower() == "green":
    print("GO")

elif light.lower() == "yellow":
    print("STOP IF IT IS SAFE TO DO SO")

elif light.lower() == "red":
    print("STOP")

else:
    print("YIELD")

x = 10

if x > 5:
    print("x is greater than 5")

if x > 8:
    print("x is greater than 8")
    
# this prints both, that is why we need elif statements, removed redundancy.
    
