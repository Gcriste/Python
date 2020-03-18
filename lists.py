# Define my_stuff
my_stuff = [1, 2, 3, 4, "Camera", 2.5]
# Define nums
nums = list(range(1,100))


# DON'T TOUCH THIS PLEASE!
people = ["Hanna","Louisa","Claudia", "Angela","Geoffrey", "aparna"]
# DON'T TOUCH THIS PLEASE!
#Change "Hanna" to "Hanna"
people[0] = "Hannah"
#Change "Geoffrey" to "Jeffrey"
people[4] = "Jeffrey"
#Change "aparna" to "Aparna" (capitalize it)
people[-1] = "Aparna"

sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
# Define your code below:
result = ''
for s in sounds:
    result += s.upper()