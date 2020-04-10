#Using string concatenation:

def yell(word):
    return word.upper() + "!"




#Using the string format() method:

def yell2(word):
    return "{}!".format(word.upper())



#Using an f-string. My personal favorite, but only works in python 3.6 or later.  Udemy exercises don't support it currently :(

def yell3(word):
    return f"{word.upper()}!"