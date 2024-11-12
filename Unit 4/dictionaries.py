# Dictionary is a type of collection like a list
# A list is a collecttion of items in a sequence
# A dictionary is different
# Dictionaries store data in key-value pair
# You can retreie ddta quicckly by using a  unique key
# instead of retreiving it by index

#Examples
#Lists use brackets [], Dictionaries use braces {}


steven = {
    "name": "Steven",
    "age": 18,
    "city": "St. Michael",
    "pets": 2,
    "height": 5.5
}

# Each key must be unique

# Retreiving values from a dictionary
print(steven["name"]) # prints the name
print(steven["age"]) # Prints the age

# This will error if you give a key that doesn't exist
# print(steven["country"]) # ERROR, NO COUNTRY KEY   #KEY ERROR

# .get allows you to retrieve a value without erroring
# when the key doesn't exist
# the second parameter is what is given if the value is not found, if not specified it will return NONE

print(steven.get("height"))
print(steven.get("country", "Country not found"))

# YOu can add new values to an existing dictionary
steven["country"] = "The United States of America"

# You can modify existing values
steven["age"] = 19

# YOU CAN REMOVE VALUES
steven.pop("pets")

# Iterate through a dictionary using a for loop!

for key, value  in steven.items():
    print(key + " = " + str(value))


# Dictionary Functions
    
print(steven.keys())
    # RETURNS ALL KEYS
print(steven.values()) # RETURNS ALL VALUES

print(steven.items()) # RETURNS ALL KEY VALUE PAIRS

print(steven.clear()) # REMOVES ALL ITEMS FROM DICTIONARY




students = {
    "Amy": "A",
    "Greg": "A-",
    "Friedrich": "C+",
    "Olaf": "B-",
    "Gunhilda": "B"
}

print(students.items())

    