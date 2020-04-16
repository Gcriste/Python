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




def add_and_multiply(a,b,c, **kargs):
    print (a+b * c)
    print('OTHER STuff...')
    print(kargs)

data = dict(a=1,b=2,c=3, d="55", name="Griffin")

add_and_multiply(**data)
add_and_multiply(**data, cat ="blue")


def calculate(**kwargs):
    operation_lookup = {
        'add': kwargs.get('first', 0) + kwargs.get('second', 0),
        'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
        'divide': kwargs.get('first', 0) / kwargs.get('second', 0),
        'multiply': kwargs.get('first', 0) * kwargs.get('second', 0)
    }
    is_float = kwargs.get('make_float', False)
    operation_value = operation_lookup[kwargs.get('operation', '')]
    if is_float:
        final = "{} {}".format(kwargs.get('message','The result is'), float(operation_value))
    else:
        final = "{} {}".format(kwargs.get('message','The result is'), int(operation_value))
    return final

