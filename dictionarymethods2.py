# pop
# takes a single argument corresponding to a key and removes that key value pair from the dictionary. Returns the value corresponding to the key that was removed


instructor = {
    "name": "griffin",
    "owns_dog": True,
    "age": 29
    }

instructor.pop("owns_dog")
# now instructor will be instructor = {
    # "name": "griffin",
    # "age": 29
    # }


# popitem
# removes a random item
instructor.popitem()
# removes a random key-value pair

# update
# updates keys and values in a dictionary with another set of key value pairs
instructor = {
    "name": "griffin",
    "owns_dog": True,
    "age": 29
    }

instructor2 = {
    "name": "jon",
    "owns_dog": False,
    "age": 31
    }

instructor.update(instructor2)


# -------------------------------------------------------------------------------------------
inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1} #DON'T CHANGE THIS LINE!
# Make a copy of inventory and save it to a variable called stock_list
stock_list = inventory.copy()
# add the value 18 to stock_list under the key "cookie"
stock_list['cookie'] = 18
# remove 'cake' from stock_list
stock_list.pop('cake')