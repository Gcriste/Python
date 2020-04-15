
def fav_colors(**kwargs):
    for person, color in kwargs.items():
        print(f"{person}'s favorite color is {color}")


fav_colors(griffin="blue", hallie="red", tyler="green")


def special_greeting(**kwargs):
    if "david" in kwargs and kwargs["david"] == "special":
        return "you are the special guest david!"
    elif "david" in kwargs:
        return f"{kwargs['david']} david!"
    return "not sure who this is"

print(special_greeting(david="hello"))
print(special_greeting(Bob="hello"))
print(special_greeting(david="special"))


def combine_words(word,**kwargs):
    if 'prefix' in kwargs:
        return kwargs['prefix'] + word
    elif 'suffix' in kwargs:
        return word + kwargs['suffix']
    return word


def display_info(a,b, *args, instructor = "Griffin", **kwargs):
    return[a,b, args, instructor, kwargs]

print(display_info(1,2,3, last_name="Criste", job="Coder"))

#a - 1
#b - 2
#args (3)
#instructor - griffin
#kwargs - {'last_name': "Criste", "job": "Coder"}


### parameter ordering
# 1. parameter
# 2. *args
# 3. default parameters
# 4. **kwargs