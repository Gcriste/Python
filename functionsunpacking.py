#First, call count_sevens  with the numbers: 1,4, and 7  (review)

# result1 = count_sevens(1,4,7)
# #Next, call count_sevens  with all the values from the nums  list, unpacked:

# result2 = count_sevens(*nums)
#Adding that little *  makes a huge difference! Instead of passing in a single item (the list), we're now passing in 121 separate arguments.


def display_names(first, second):
    print(f"{first} says hello to {second}")

names = {"first": "Griffin", "second": "John"}

#display_names(first = "Charlie", second = "Sue")
display_names(**names)




def add_and_multiply(a,b,c):
    print (a+b * c)

data = dict(a=1,b=2,c=3)

add_and_multiply(**data)