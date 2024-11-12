# There are a couple types of Loops in python
# The for loop lets you iterate through a list
# -Great for looping a set sumber of times
# BUT WHAT IF we need to loop an uncertain number of times???
# ex. Entering your password
# You could get it right the first time
# It could take you a million tries
# Or anything in between


real_pass = "ninjalowtaper"
entered_pass = ""
counter = 0

while entered_pass != real_pass:
    #ASk for the password
    entered_pass = input("Please enter the password\n>")
    counter = counter + 1

    #Check if password is correct
    if entered_pass == real_pass:
        print("ACCESS GRANTED")
    else:
        print("ACCESS DENIED")
        print("Try again")
        print("You have " + str(5 - (int(counter))) + " attempts left")
       
        
    

print("Welcome!")


# With while loops, you need to be carefulfor infinite loops
# When you put your computer into rest mode, it has nightmares about infinite loops /joke
# An infinite loop happens when you enter a loop that can never be escaped
# Like black hole
# Don't create a black hole
# Let's create a black hole


user_input = ""

while user_input != "exit":
    user_input = input("Enter something!")
    print("type 'exit' to quit")
    print("You typed " + user_input)

print("All done!")





