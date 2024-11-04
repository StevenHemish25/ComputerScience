#For loops
#This is a BIG deal
#For loops allow the programer to REPEAT, or what we call LOOP

#Write a program that prints the numbers 1 through 10
#Each on a new line

fav_foods = ["Eggs Bennedict", "Fried Chicken", "Mac n Cheese"]

#for <var> in <list>:

for i in range(90,101): #Range creates a list
    print(i)

for food in fav_foods:
    print(food)
    #Runs all of the lines inside for the loop
    #When it reaches the bottom of the list, it runs again
    #And moves on to the next item in the list
    #It ends when there are no list items left.
    #Run item, done, next item done, next item done, 



#Print a countdwon: Create a countdown from 10 to 1 using a loop
    
for i in range(10,0,-1): #START,STOP,STEP, STEP: How does the number change between?
    print(i)

var_sum = [1,2,3,4,5]
total=0
for e in var_sum:
    total += e
print(total)





nums = [68, 79, 419, 421, 665]
sum = 0
for n in nums:
    sum = sum + n
print(sum)


#Square


ints = [3,2,5,4,1]
newlist= []

for o in ints:
    newlist.append(o*o)
print(newlist)

#Characar Count

stringy = input("Please enter a string\n>")
numvowels = 0
for s in stringy:
    if s.lower() in ["a", "e", "i", "o", "u"]:
        numvowels = numvowels + 1
print(numvowels)

#print multiplication Table
try:
    multi = int(input("Gimme an int yo!"))
except:
    print("womp womp")


for l in range(0,multi+1):
    print(str(multi) + "x" + str(l) + " = " + str(multi*l))


#List of Names
    
names = ["Peter", "John", "Paul", "Luke"]

for name in names:
    print("Hello, " + name + "!")