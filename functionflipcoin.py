from random import random

def flip_coin():
    #generate a number from 0-1
    r = random()
    if r > 0.5:
        return "heads"
    else:
        return "tails"

print(flip_coin())


#Generating evens using a list comprehension:

# def generate_evens():
#     return [x for x in range(1,50) if x%2 == 0]
# #Generating evens using a loop:

def generate_evens():
    result = []
    for x in range(1,50):
        if x % 2 == 0:
            result.append(x)
    return result