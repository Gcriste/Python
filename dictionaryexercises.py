list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]
 
answer = {list1[i]: list2[i] for i in range(0,3)}
list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]
 
answer = {list1[i]: list2[i] for i in range(0,3)}


list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]
 
dict(zip(list1,list2))  

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = {thing[0]: thing[1] for thing in person}

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = {k:v for k,v in person}

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = dict(person)

answer = {char:0 for char in 'aeiou'} 

answer = dict.fromkeys("aeiou", 0) 