# Logical Operators
# Arithmetic Operators + - * / // ** %
# Comparison Operators > < >= <= ==
# Logical Operators and or !
# AND means that BOTH conditions must be true
# Or means that at least one condition must be true
# ! (not) means the inverse, ex. != (not equal)


def check_eligibility(age,experience):
    if age >= 18 and experience >=1: # AND Both conditions must be true, "or"  atleast one of the conditions must be true
        print("you are eligible!")

    else:
        print("You are not eligible...")

check_eligibility()

