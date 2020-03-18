# Create a list called instructors
instructors = []
# Add the following strings to the instructors list 
    # "Colt"
    # "Blue"
    # "Lisa"
 
instructors.append("Colt")
instructors.append("Blue")
instructors.append("Lisa")



# Create a list called instructors
instructors = []
# Add the following strings to the instructors list 
    # "Colt"
    # "Blue"
    # "Lisa"
# Use any of the list methods we've seen to accomplish this:
instructors.extend(["Colt", "Blue", "Lisa"])


## Deleting things from a list
# Clear - removes everything from the list
# Pop - removes last item, if you provide an index it removes that item from where it is in the index
# Remove - removes the first instance of the item that you specify to remove, throws an error if not found

#index - returns the index of the specified item in the list
#count - returns the number of times x appears in the list
#reverse - reverses the elements of the list (in-place)
#sort - sorts the items of the list (in-place)
#join - technically a string method that takes an interable argument and concatenates(combines) a copy of the base string between each item of the list
# Create a list called instructors
instructors = []
 
# Add the following strings to the instructors list 
    # "Colt"
    # "Blue"
    # "Lisa"
instructors.extend(["Colt", "Blue", "Lisa"])
 
# Remove the last value in the list
instructors.pop()
 
# Remove the first value in the list
instructors.pop(0)
 
# Add the string "Done" to the beginning of the list
instructors.insert(0, 'Done')