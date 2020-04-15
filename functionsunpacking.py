#First, call count_sevens  with the numbers: 1,4, and 7  (review)

result1 = count_sevens(1,4,7)
#Next, call count_sevens  with all the values from the nums  list, unpacked:

result2 = count_sevens(*nums)
#Adding that little *  makes a huge difference! Instead of passing in a single item (the list), we're now passing in 121 separate arguments.