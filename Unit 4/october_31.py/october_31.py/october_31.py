import random
# Pyhton has four types of collections
#Tuple
#Set
#>List
#>Dictionary

#Today, were going to focus of lists
# A list is a way to store more than one value in a single variable
#The values in the list are called ITEMS
# Items can be accessed by their INDEX (Position in the list)
#INDEX                             0                1              2                3                 4
best_elden_ring_weapons = ["Blasphemous Blade", "Moonveil", "Rivers of Blood", "Iron Ball", "Bloodhound's Fang"]
best_years = [1776, 1985, 1994, 1957, 2016]

print(best_years[4])  # Print best years at index 0
#YOU CAN GET AN INDEXERROR: OUT OF RANGE

myint = 3

print(best_years[myint])   
print(best_elden_ring_weapons[0]) # Print the first item
print(best_elden_ring_weapons[4]) # Print the 4th item, not "LAST"

print(len(best_elden_ring_weapons))
# LENGTH, TELLS US THE AMMOUNT OF ITEMS


# If you want your code to print the last, and be able to change your rankings, the code won't break

print(best_elden_ring_weapons[0])                              # Print the first item
print(best_elden_ring_weapons[len(best_elden_ring_weapons)-1]) # PRINT THE LAST ITEM


# LIST OF ITEMS CAN BE CHANGED!

best_elden_ring_weapons[3] = "Spiked Fist"
print(best_elden_ring_weapons)

#List functions!
#.pop()
# Removes an item at a given position
best_elden_ring_weapons.pop(1) # Remmoves moonviel

#.remove()
# Removes an item by value- removes the first instance of the value
best_elden_ring_weapons.remove("Blasphemous Blade") #If the value doesn't exist, it erros :(, SO YOU SHOULD PUT IT IN A TRy>ACCEPT)


#.append()
# Adds the value as a new item to the end of the list
best_elden_ring_weapons.append("Death's Poker")


numbers = [random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100),]
print(numbers)
#.sort()
# Sorts the numbers from samllest to largest
numbers.sort()
print(numbers)

#max()
# Prints the larget number in the list
print(max(numbers))

#min()
#Prints the smallest number in the list
print(min(numbers))

#Strings ..... are just... lists of characters :O  
print("Osowski"[2])
print(len("Osowski")) # Finds how many characters are in osowski

