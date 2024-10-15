# Create a function called free_shipping
# That tells you if you qualify for free shipping or not
# You only get free shipping if
# You are a Prime member OR order is at least $25
# You are at least 18 years old and prime, OR have parent consent.
# prime (bool) cost (float) age (int) consent (bool)
# HUGE HINT!
# you can use more than one logical operator in a conditional
# Use parenthesis to group if needed)
prime = True
age = 18
consent = False
cost = 15


def free_shipping(prime,cost,age,consent):
    if prime == True and (age >= 18 or consent == True) or cost >= 25:
        print("You have free shipping")
    else:
        print("You do not have free shipping")

free_shipping(prime,cost,age,consent)