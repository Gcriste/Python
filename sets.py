s = set({1,2,3,4,5})

# no duplicates
s = set({1,2,3,4,5,5,5,5})
# would print
1,2,3,4,5


s.add({9})
#would print (always random order)
1,2,3,9,4,5


s.remove({3})
#would print 
1,2,9,4,5