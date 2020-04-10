#sets are lists that have no specific order and you cannot use the index to find the thing in the set

s = set({1,2,3,4,5})

# no duplicates
s = set({1,2,3,4,5,5,5,5})
# would print
1,2,3,4,5


s.add({9})
#would print (always random order)
1,2,3,9,4,5


s.remove({3})
#would print . If you try to remove something that doesn't exist, you will get an error
1,2,9,4,5

s.discard({8})
#would print . If you try to remove something that doesn't exist, you won't get an error
1,2,9,4,5

s.copy()
# prints
1,2,3,9,4,5

s.clear()
#deletes the whole set

#set math
#math_students | biology_students = union, combines sets, but doesn't make duplicates
#math_students & biology_students = combines sets, does make duplicates


# 1 - Create a variable called numbers which is a tuple with the the values 1, 2, 3 and 4 inside.
numbers = (1,2,3,4)
 
# 2 - Create a variable called value which is a tuple with the the value 1 inside.
value = (1,)
 
# 3 - Given the following variable:
values = [10,20,30]
# Create a variable called static_values which is the result of the values variable converted to a tuple
static_values = tuple(values)
 
# 3 - Given the following variable
stuff = [1,3,1,5,2,5,1,2,5]
 
# Create a variable called unique_stuff which is a set of only the unique values in the stuff list
unique_stuff = set(stuff)