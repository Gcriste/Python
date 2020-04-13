#NUMBER COMPARE
def number_compare(a,b):
    if a > b:
        return "First is greater"
    elif b > a:
        return "Second is greater"
    return "Numbers are equal"


#SINGLE LETTER COUNT
#In my solution, I use the built-in count()  to count the number of times letter  appears in string .  I also downcase both string  and letter  to make it case-insensitive (you could also upcase both instead)

def single_letter_count(string,letter):
    return string.lower().count(letter.lower())


#MULTIPLE LETTER COUNT
#I used a dictionary comprehension. For each letter in the input string, I make the key the letter itself ("a" for example), and the corresponding value is the result of running count() of that letter in the string.

def multiple_letter_count(string):
    return {letter: string.count(letter) for letter in string}


#LIST_MANIPULATION
def list_manipulation(collection, command, location, value=None):
    if(command == "remove" and location == "end"):
        return collection.pop()
    elif(command == "remove" and location == "beginning"):
        return collection.pop(0)
    elif(command == "add" and location == "beginning"):
        collection.insert(0,value)
        return collection
    elif(command == "add" and location == "end"):
        collection.append(value)
        return collection