# list comprehension technique
answer = [person[0] for person in ["Ellie", "John", "Griffin"] ]
answer2 = [val for val in [1,2,3,4,5,6] if val %2 == 0]


# good ole loops
answer = []
for person in ["Ellie", "John", "Griffin"]:
    answer.append(person[0])

answer2 = []
for num in [1,2,3,4,5,6]:
    if num %2 == 0:
        answer2.append(num)
