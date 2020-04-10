def add(first,second):
    return first + second

print(add(3,4))


def multiply(a,b):
    return a * b

print(multiply(4,5))


#BE CAREFUL ABOUT INDENTING!!S
def sum_odd_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
    return total

print(sum_odd_numbers([1,2,3,4,5,6,7]))
#prints 16 (1 + 3 + 5 + 7)

# def sum_odd_numbers(numbers):
#     total = 0
#     for num in numbers:
#         if num % 2 != 0:
#             total += num
#         return total

# print(sum_odd_numbers([1,2,3,4,5,6,7]))
# #prints 1


# def is_odd_number(num):
#     if num % 2 != 0:
#         return True
#     else:
#         return False

# print(is_odd_number(4))
# #should print True
# print(is_odd_number(9))
# #should print False

#BUT WE DON'T NEED THE ELSE BECAUSE IF ITS NOT TRUE THEN IT HAS TO BE FALSE
def is_odd_number(num):
    if num % 2 != 0:
        return True
    return False

print(is_odd_number(4))
#should print True

print(is_odd_number(9))
#should print False