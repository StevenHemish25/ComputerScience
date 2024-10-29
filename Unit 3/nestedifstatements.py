# Nested if statements


prime = True
cost = 20
age = 17
consent = False

if prime:
    if age >= 18:
        print ("FREE SHIPPING APPLIED!")
    elif consent:
        print("FREE SHIPPING APPLIED!")
    else:
        print("No free shipping")

elif cost >= 25:
    if age >= 18:
        print ("FREE SHIPPING APPLIED!")
    elif consent:
        print("FREE SHIPPING APPLIED!")
    else:
        print("No free shipping")

else:
    print("No free shipping")



# Decide if we need an umbrella
# You need an umbrella if its raining AND you are going outside that day.
    

raining = input("Is it raining outside?\n")

if raining.lower() == "yes":   # If first decision matters on second question
    outside = input("Do you plan on going outside?\n")

    if outside.lower("yes"):
        print("BRING AN UMBRELLA")
    else:
        print("NO UMBRELLA")
else:
    print("NO UMBRELLA")