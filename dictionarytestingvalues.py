instructor = {
    "name": "griffin",
    "owns_dog": True,
    "age": 29
    }

instructor.clear()
    # will clear the dictionary

instructor.copy()
    # makes a copy of the dictionary


new_user = {}.fromkeys(['name', 'score', 'email', 'profile bio'], 'unknown')

# will create {'name': 'unknown', 'score':'unknown', etc}
{}.fromkeys()
    # creates key-value pairs from comma sepearted values


instructor = {
    "name": "griffin",
    "owns_dog": True,
    "age": 29
    }
instructor.get("name")
    # returns griffin
# retrieves a key in an object and return None instead of a KeyError if the key does not exist


# ----------------------------------------------------------------------

# This code picks a random food item:
from random import choice #DON'T CHANGE!
food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!
 
#DON'T CHANGE THIS DICTIONARY EITHER!
bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

if food in bakery_stock:
    print("{} left".format(bakery_stock[food]))
else:
    print("We don't make that")


quantity = bakery_stock.get(food)
if quantity:
    print("{} left".format(quantity))
else:
    print("we don't make that")