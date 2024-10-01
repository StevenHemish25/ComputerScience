x = 5 #GLOBAL variable

def my_function():
    x = 10                #Local Variable
    print(x)             #Print local variable x

my_function()            #run my_function
print(x)                 #Print Global variable         #Scope is the context of which a variable is made.

def add(x, y):
    print(x + y)
    return "catdog"    # with return it puts out 15 15, takes value after return back to where it came from, Line below looks like answer = "catdog"
    
answer = add(5, 10)
print(answer)               #results with 15, and None, because we wrote add function without return