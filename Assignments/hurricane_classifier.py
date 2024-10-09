#cat 1 < 96, 2 <111, 3 < 130, 4 < 157, 5>=157

windspeed = int(input("What speed is the wind speed of your storm in MPH? \n"))


if windspeed < 74:
        print("There is a tropical storm outside")
elif windspeed < 96:
        print("There is a category 1 hurricane outside")
elif windspeed < 111:
        print("There is a category 2 hurricane outside")
elif windspeed < 130:
        print("There is a category 3 hurricane outside")
elif windspeed < 157:
        print("There is a category 4 hurricane outside")
elif windspeed >= 157:
        print("There is a category 5 hurricane outside")
else:
        print("Good luck")

