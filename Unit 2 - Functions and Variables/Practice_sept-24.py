my_variable_one = "cat"    
my_variable_two = 20 * my_variable_one  
print(my_variable_two)

favorite_animal = "dog"
print("My favorite animal is " + favorite_animal)  #concatenation
#Parameters and arguments go in the parenthesis of a functions
input #pauses program until the user gives me a response
favorite_color = input("What is your favorite color?\n>") #\n = new line, you can also add a greater than symbol
print("your favorite color is " + favorite_color)
num = input("Enter a number?\n>")
num = int(num) #however you can convert it with int
print(num * 10) #this code will give you 10101010101010101010 instead of 100, because input always gives a string
#if some hooligan types ten, it will error