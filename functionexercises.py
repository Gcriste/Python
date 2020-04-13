#RETURN_DAY
#Check to make sure num isn't < 0 or  > 6.  
#Return the corresponding day. Use days[num-1] because return_day(1) should return 0th item in list.
def return_day(num):
    days = ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"]
    # Check to see if num valid
    if num > 0 and num <= len(days):
        # use num - 1 because lists start at 0 
        return days[num-1]
    return None
#BONUS ADVANCED VERSION:

#Here's a more advanced solution that involves error handling, which we have not covered yet.  It eliminates the need to check to see if num is a valid index in the list. We cover this in the debugging section, but I thought you may want to see if now.

def return_day(num):
    try:
        return ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"][num-1]
    except IndexError as e:
        return None


#LAST_ELEMENT
#First check to see if the list exists (if it has data in it).  If it does, return the -1 item (last item).  Otherwise, return None.

def last_element(l):
    if l:
        return l[-1]
    return None


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


#IS_PALINDROME
#Here's the simpler version that doesn't ignore whitespace.  I reverse the string using a slice [::-1] and compare that to the original string, which returns True or False.  

def is_palindrome(string):
    return string == string[::-1]
#The Bonus Version:
#For the more advanced version that ignores whitespace, I first remove all whitespace from the input string using a string method called replace() . What I'm actually doing is replacing all spaces(" ") with empty strings ("").  I save the result to a new variable I call stripped .  Then, I simply check if stripped is a palindrome, using the same logic I did in the previous solution.

def is_palindrome(string):
    stripped = string.replace(" ", "")
    return stripped == stripped[::-1]


#FREQUENCY
#using the built-in count() method, this is really nice and easy:

def frequency(collection, searchTerm):
    return collection.count(searchTerm)