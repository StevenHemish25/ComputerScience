
def start():
    print("The Year is 2032, and you have just been elected to the United States Senate, you are expected to work in the best interests of your constituents,\n But will you? \n A conglomerate called Phig Barma produces medical supplies and pharmaceuticals,\n They donated $750,000 to you during your political campaign, Now there is legislation regarding regulations in the Medical Inudstry")
    print("1. Vote in favor of stricter regulations,")
    print("2. Vote against, Phig Barma expects us to represent them")

    choice = input("> ")

    if choice =="1":
        favor()
    elif choice == "2":
        against()
    else:
        print("Invalid answer")
        start()



def favor():
    print("Thanks to your contribution, Bill no. >insert comedically large number< passed in the Upper House")
    favor_consequence()
def against():
    print("Thanks to your contribution, Bill no. >insert comedically large number< has failed.")
    against_consequence()



# END OF ENCOUNTER ONE
    

def favor_consequence():
    print("A spokesperson for Phig Barma LTD. has spoken against you in a media conference covered on the IDC News Network")
    print("1. Promise Phig Barma to vote a certain way on a future bill to regain funding")
    print("2. Call out the company for Immoral business practices")

    choice = input("> ")

    if choice =="1":
        promise()
    elif choice == "2":
        call_out()
    else:
        print("Invalid answer")
        favor_consequence()


    # END OF ENCOUNTER 2


def promise():
    print("You recieved an email from Phig Barma, saying that if you keep to your promise, they will endorse you")
    favor_promise()
def call_out():
    print("Phig Barma has cut all communications from you, and now endorses your political rival\n An aptley named O'ponnent")
    challenge()

def challenge():
    print("Irish Statesman O'ponnent has gained momentum in the re-election polls, how do you combat this?")
    print("1. Hire a hitman")
    print("2. Challenge him to a debate")

    choice = input("> ")

    if choice == "1":
        print("The PoPo found out. Game over")
    elif choice == "2":
        o_ponnent()
    else:
        print("Invalid answer")
        challenge()


        # UNIQUE ENDING 1
        #END OF ENCOUNTER 3


def o_ponnent():
    print("O'ponnent has spent hours studying numerous political topics in preparation for the debate. You might be cooked")
    print("1. Back down")
    print("2. How bad could this go?")

    choice = input("> ")

    if choice == "1":
        print("You are politically humiliated and lose re-election. \n Game Over")
    elif choice == "2":
        print(" Surprisingly you win against O'ponnent in a heated debate.")
        cease_harrassment_consequence()  # THIS FUNCTION TAKES PLAYER TO CHOICE OVER WHETHER TO RUN FOR PRESIDENT, FUNCTION NAME DERIVES FROM OVER PATHS
    else:
        print("Invalid Answer")
        o_ponnent()


# END OF ENCOUNTER 4


def against_consequence():
    print("Phig Barma has decided to raise prices on a medical product of theirs called Flintstone Gummies, \n Your constituents are displeased and post about their frustrations on Twitter/X")  
    print("1. Make a post online supporting your constituents and calling for change")
    print("2. Do nothing")

    choice = input("> ")

    if choice == "1":
        tweet()
    elif choice == "2":
        no_tweet()
    else:
        print("Invalid answer")
        against_consequence()

def tweet():
    print("You decided to post online about the issue and it was recieved very well from your constituents")
    tweet_consequence()
def no_tweet():
    print("You decided to stay silent on the issue, the people become frustrated")
    left_on_read()


    # END OF ENCOUNTER 5



def left_on_read():
    print("You lose support from your voters \n You lose your bid at re-election \n Game over\n \n \n Since you died so early would you like to try again?")
    print("1. Yes")
    print("2. No")

    choice = input("> ")

    if choice == ("1"):
        start()
    else:
        print("GG no RE")
   
   
    #GAME END NON UNIQUE



def tweet_consequence():
    print("Your tweet has garnered you a lot of attention online, you question the posibility of running for president")
    print("1. Run for president")
    print("2. continue job as senator")

    choice = input("> ")

    if choice == "1":
        president_run()
    elif choice == "2":
        boring()
    else:
        print("Invalid answer")
        tweet_consequence()


# END OF ENCOUNTER 6


def boring():
    print("Your life continues boringly as a carreer politician \n You die at the old age of 79") # UNIQUE GAME END 2
    
    

def favor_promise():
    print("Your email history was leaked to the public, your consituents are outraged at your financial connections to Phig Barma")
    print("1. Say the media is lying")
    print("2. Admit you made a immoral decision and that you will put your people first in the future")

    choice = input("> ")

    if choice == "1":
        fake_news()
    elif choice == "2":
        appology()
    else:
        print("Invalid answer")
        favor_promise()


# END OF ENCOUNTER 7


def fake_news():
    print("You have claimed in a recent conference that the accusations against you are false")
    f_promise_fake()
def appology():
    print("You have made a formal appology to your voters in a press conference")
    f_promise_appol()


def f_promise_fake():
    print("Most of the population of your district believes your claim. \n However, \n Some of these people are harrassing the leaker of the E-Mail")
    print("1. Tell your people to not harrass the whistleblower")
    print("2. Do nothing")

    choice = input("> ")

    if choice == "1":
        cease_harrassment()
    elif choice == "2":
        nothing()
    else:
        print("Invalid answer")
        f_promise_fake()


# END OF ENCOUNTER 8


def cease_harrassment():
    print("The situation boils over, your actions have appealed to a organization called the Anti-Cyberbullying Association which endorses you")
    cease_harrassment_consequence()
def nothing():
    print("The whistleblowers address has been released to the a public. \n an aptley named H.Acker Known as Hugo Acker, has been blamed. \n Hugo Acker has asked you to tell the people to back down as he fears he will be targeted online at Fortnite")
    humiliated_at_fortnite()



def humiliated_at_fortnite():
    print("Hugo acker has gone silent online after he lost a game of fortnite")
    print("Political rival, an irish statesman named O'ponnent has called you out on your actions")
    print("1. Challenge him to a debate")
    print("2. Ignore the issue")
        
    choice = input("> ")

    if choice == "1":
        debate()
    elif choice == "2":
        protests()
    else:
        print("Invalid answer")
        humiliated_at_fortnite()


# END OF ENCOUNTER 9
        

def debate():
    print("You have entered a debate with O'Ponnent, the topic of the debate is the overpopulation of cats")
    print("1. Argue in favor of sending the cats elsewhere")
    print("2. Argue in favor of creating a hotel for cats")

    choice = input("> ")

    if choice == "1":
        shipment()
    elif choice == "2":
        pursailles()
    else:
        print("Invalid answer")
        debate()

# END OF ENCOUNTER 10
    

def f_promise_appol():
    print("Most of your constituents accept your appology, \n Your political campaign has recieved a large sum of donations. \n What are you going to spend this money on?")
    print("1. DLC for your favorite steam game")
    print("2. A new waterfront property")
    print("3. Politcal advertisements")

    choice = input("> ")
                   
    if choice == "1":
        bad_purchase()
    elif choice == "2":
        waterfront()
    elif choice == "3":
        advertisement()
    else:
        print ("Invalid answer")
        f_promise_appol()

# END OF ENCOUNTER 11
        
def cease_harrassment_consequence():
    print("Your popularity has rose substantially over the past few months and people suggest you run for president")
    print("1. Run for president")
    print("2. Stay content as a Senator")

    choice = input("> ")

    if choice == "1":
        president_run()
    elif choice == "2":
        re_election()
    else:
        print("Invalid answer")
        cease_harrassment_consequence()

# END OF ENCOUNTER 12
        
def bad_purchase():
    print("You have decided to spend funds on a new game instead of focusing on your people. \n They want answers")
    print("1. Say Hearts of Iron 4 no step back DLC is a perfecly acceptable purchase")
    print("2. Admit wrongdoing")

    choice = input("> ")

    if choice == ("1"):
        print("You lose support for re-election. Game over")  #GAME END NON UNIQUE
    if choice == ("2"):
        wrong_doing()
    else:
        print("Invalid answer")
        bad_purchase()

# END OF ENCOUNTER 13
        
def waterfront():
    print("Voters have found out you spent money on a luxurious waterfront property. \n Your character dies in a vehicular accident on their way to the new propert. \n Rest in peace Player1 \n Click here to add text \n Game over")
#UNIQUE GAME-END 3
    
def president_run():
    print("Now that you have entered the presidential race you have been invited to a debate \n Oh boy. \n The telepromter asks,\n If you were elected president what would you do about the rising cost of clothespins?")
    print("1. Create a law creating a pricecap on clothespins")
    print("2. Rising prices are a natural process in the economy, \n We can't undercut the rights of private companies")

    choice = input("> ")

    if choice == "1":
        president()
    elif choice == "2":
        print("Your response was recieved poorly. \n The only state you win in the election is Idaho. \n Game Over")
        # UNIQUE GAME ENDING 4
    else:
        print ("Invalid answer")
        president_run()


# END OF ENCOUNTER 14


def advertisement():
    print("With newly garnered funds, you decide to create a political campaign slogan to win re-election")
    print("1. VOTE PLAYER1 FOR SENATE")
    print("2. Skibidi")

    choice = input("> ")

    if choice == "1":
        print("Your slogan was very popular, \n You decide to step up your game and run for president")
        president_run
    elif choice == "2":
        print("Game over\n You were tricked by brainrot")
    else:
        print("Invalid answer")
        advertisement()
        
        
# UNIQUE GAME ENDING 5   
# END OF ENCOUNTER 15
        

def protests():
    print("Your lack of action has caused protests against you")
    print("1. Call in the national guard")
    print("2. Resign")

    choice = input("> ")

    if choice == "1":
        coup_d_etat()
    elif choice == "2":
        print("You resigned from your political position. \n Game over")
    else:
        print("Invalid answer")
        protests()


# END OF ENCOUNTER 16
        

def shipment():
    print("Your decision to ship cats nearby states is wildly unplopular amongst your neighbors \n Your cabinet coerces you to resign after the humiliation of the incident")


# NON UNIQUE GAME END


def pursailles():
    print("A large hotel has been created for the overflow of cats, what do you name it?")
    print("1. The Pallace of Purrsailles")
    print("2. Cats R us")

    choice = input("> ")

    if choice == "1":
       opportunity()
    elif choice == "2":
        print("Your decision was so terrible you were forced to resign")
    else:
        print("Invalid answer")
        pursailles()


# END OF ENCOUNTER 17
        

        
def opportunity():
    print("You decide to spend the rest of your life as a manager for a cat hotel. \n Happy Ending")


# NON UNIQUE GAME END


def re_election():
    print("The rest of your life is boring. \n If only you had the ambition! \n Game over")


# NON UNIQUE GAME END
    
    
def wrong_doing():
    print("The voters have no empathy for you. \n Welcome to the real world. \n Game Over")


# NON UNIQUE GAME END
    

def president():
    print("Congratulations Player1, you are now the President of the United States. \n Expectations of your preformance are high especially since there is a crisis growing overseas,\n" + 
           "Essentially, There's this guy in Argentina named Javier Milei, Who is President of Argentina. \n All of the Following is True, Javier owned an English Mastiff named Conan. \n Milei reffered to Conan as his closest friend, and claims to have Met Conan in a previous life as a roman gladiator. \n " +  
          "Conan died of spinal cancer in 2017, although Milei reffered to it as a physical dissapearance and that Conan was sitting with god to protect him. \n Milei thanked Conan's physical dissapearance for allowing him to talk with god. \n In 2018, Milei went to the U.S. to have the dog cloned for $50,000. \n Javier says he uses a mystic to talk to his dog and that Conan advises him on his political decisons. \n\n " + 
          "Because of this, Javier has sent Argentina at war with Paraguay because the dog said so.")
    print("1. Clearly Javier is very devoted to his dog and we should let him settle this")
    print("2. Nuke France")

    choice = input("> ")

    if choice == "1":
        argentina()
    elif choice == "2":
        world_war_3()
    else:
        print("Invalid Answer")
        president()


# END OF ENCOUNTER 18
        

def coup_d_etat():
    print("Several High ranking generals in the government are planning to coup the government to set up a Military dictatorship. \n Your deployment of the national guard has made your name known to these generals. \n They propose you act as dictator after the coup succeeds.")
    print("1. Decline, report this to the feds")
    print("2. I accept")

    choice = input("> ")

    if choice == "1":
        print("You died in a TrAgIc AcCiDeNt \n Game over")
    elif choice == "2":
        dictatorship()
    else:
        print("Invalid Answer")
        coup_d_etat()


# END OF ENCOUNTER 19
        

def argentina():
    print("Argentina annexed Paraguay. \n Your name is discredited in the American, Mexican, and Brazilian press. \n You lose popular support in the government and fail at re-election. \n Game Over")


#NON UNIQUE GAME ENDING
    

def world_war_3():
    print("You launch all of the United State's nuclear arsenal on the Fifth French Republic. \n The United States is kicked out of NATO and an international coalition forms to depose the U.S. Government." 
          + " Britain, Germany, Turkiye, Iran, China, Egypt, Russia, Australia, Brazil, Italy, and India declare war. \n Because you wasted the entire nuclear arsenal on France Nukes are not an option, What is your plan?")
    print("1. Surrender, it's not worth a world war")
    print("2. Bring it on, prepare for total war")

    choice = input("> ")

    if choice == "1":
        print("You have been sent to exile in Greenland. \n Game over")
    elif choice == "2":
        total_war()
    else:
        print("Invalid Answer")
        world_war_3()

# END OF ENCOUNTER 20
        
def dictatorship():
    print("You are president of the United States for life under a military dictatorship. \n Good for you, I can trust you wont cause too much trouble. \n The End")


# NON UNIQUE GAME END
    

def total_war():
    print("You prepare the country for complete conflict with the rest of the globe. \n Guam, Samoa, Midway, and Hawaii have already been occupied by China, The U.S. Navy was sunk by a combined Sino-Russian-British-Australian fleet. \n The West coast is completely vaulnerable. \n Minnesota and Alaska left to join Canada."
          + " Sanctions have caused the tech industry to go under. \n There are mass demonstrations and the whole situation is terrible")
    print("1. The country won't survive this war, surrender to the Coalition")
    print("2. Maybe If you personally lead battles the people will respect you")

    choice = input("> ")

    if choice == "1":
        peace_terms()
    elif choice == "2":
        print(" \n You get shot in battle. \n \n Game Over")
    else:
        print("Invalid Answer")
        total_war()


#GAME ENDS
# Not encounter because both choices end the game
        

def peace_terms():
    print(" You surrender to the allied coalition. \n You are exiled to Greenland where you spend the rest of your life. \n Game Over")



# KEEP AT BOTTOM
start()