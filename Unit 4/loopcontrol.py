# Loop control statements
# Allow you to change how loops operate
# They do things like quit the loop early, skip the current loop, or even do nothing at all
# break, continue, pass


# Break
# exits a loop prematurely, before it was supposed to end
# happens immediately when ran
# program continues where the loop ended

# example

bag_of_fruit = ["Apple", "Orange", "Bug", "Strawberry", "Kiwi", "Watermelon", "Mango",]

for fruit in bag_of_fruit:
    if fruit == "Bug":
        print("You found a nasty bug...")
        break # Exits loop immediately and continues on
    else:
        print("You ate a " + fruit)

print("All done!")

# Continue
# Skips the current loop
# It does not exit the entire loop just moves on to the next iteration


orders = [15, 30, 35, 23, 100, 3, 10, 22]

# Discount applying program
# Only apply the discolunt to orders above $20

for order in orders:
    if order < 20:
        continue
    print("$" + str(order) + " order discounted 5% to $" + str(order * 0.95))

# Pass
# does nothing!!!!
    # usually used as a placeholder while writing code
# TEXT-ADVENTURE PROJECT
    
if True:
    pass

def enter_forest():
    pass

def swim_river():
    pass

def eat_icecream():
    pass