# Exception Handling
# Write a program that asks for two numbers and divides them.

#if = try
# elif = except with error type
#else = except
def divide_two_numbers():
    try:  # We always enter the try block, there is no condition
        x = int(input("What is the first number?\n"))
        y = int(input("What is the second number?\n"))
        print(x / y)

    except ZeroDivisionError:
        print("Cannont divid by zero, try again.")

    except ValueError:
        print("Please enter a numerical symbol, try again.")

    except: # If anything in the try block causes an error, the try block stops immediately.
        # then the except is ran instead
        # The rest of the try block never finishes running, it is skipped
        # If the try block executes without an error, the except is skipped
        # The only wa to get into the except is to "throw" an error
        print("IDK what you did, but you broke it... Try again.")
        divide_two_numbers() # Tell the function to run again

divide_two_numbers()