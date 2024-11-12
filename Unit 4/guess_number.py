import random

number = random.randint(0,101)


user_input = ""
   
while user_input != number:
     user_input = int(input("Enter a number: "))
     if user_input == number:
          print('You guessed correct')
     elif user_input > number:
          print("Lower!")
     elif user_input < number:
          print("Higher")
     else:
          print("Try Again")

print("Complete")
               
        













            


