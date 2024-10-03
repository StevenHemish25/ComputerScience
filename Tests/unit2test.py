randword = input("Enter a random word: ")  #part 1
randword2 = input("Enter another random word: ")
randword3 = input("Enter another random word: ")
print(randword + " " + randword2 + " " + randword3)
#part 2
def add_three(x, y, z):
    print(x + y + z)
int1 = (int(input("Give me a random number: ")))
int2 = (int(input("Give me a random number: ")))
int3 = (int(input("Give me a random number: ")))
add_three(int1, int2, int3)
#part 3
def data_three():
    word = input("Give me a word: ")
    integer = (int(input("give me an integer: ")))
    flo = (float(input("give me a number with a decimal: ")))
    (intflo) = float(integer) + flo
    print(str(intflo) + word)
data_three()

