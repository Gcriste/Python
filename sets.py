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