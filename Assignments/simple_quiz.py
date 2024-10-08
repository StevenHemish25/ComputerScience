answer1  = (int(input("What is 3+4? \n")))
answer2  = (int(input("What is 5+5? \n")))
answer3  = (int(input("What is 1+5? \n")))
answer4  = (int(input("What is 10-7? \n")))
answer5  = (int(input("What is 8-3? \n")))




def tally_score():
    tally = 0
    if answer1 == 7:
        tally = tally + 1
    if answer2 == 10:
        tally = tally + 1
    if answer3 == 6:
        tally = tally + 1
    if answer4 == 3:
        tally = tally + 1
    if answer5 == 5:
        tally = tally + 1
    print("You scored a " + str(tally) + " Out of 5")

tally_score()
   



