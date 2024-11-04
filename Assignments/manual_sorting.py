import random
#GENERATE NUMBERS
numbers = [random.randint(0,101),random.randint(0,101),random.randint(0,101),random.randint(0,101),random.randint(0,101),]

#Print the list before it is started
print(numbers)

#define the function
def bubble_sort(n): #Take the list as the parameter n

#Create a local variable to record number of steps
    steps = 0

#Sort the list as many times as there are items in the list
    for j in range(0, len(n)-1):
    
      #Iterate through every item in the list
         for i in range(0, len(n)-1):

        #Check if the current list item is greater than the next list item
             if n[i] > n[i+1]:

        
            #swap their values
                 n[i], n[i+1] = n[i+1], n[i]

                 #Add a step
                 steps +=1

    #print the sorted list
    print(n)

    #Print the number of steps
    print(str(steps) + " Steps to complete")

bubble_sort(numbers)