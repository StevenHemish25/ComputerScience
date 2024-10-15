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

