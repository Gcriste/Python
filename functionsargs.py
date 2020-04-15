def sum_all_nums(num1, num2, num3):
    return num1+num2+num3

print(sum_all_nums(4,6,9))


def sum_nums(*args):
    total = 0
    for num in args:
        total+= num
    return total

print(sum_nums(3,4,51,0))
print(sum_nums(4,-3,5,6))



def contains_purple(*args):
    if "purple" in args: return True
    return False


def sum_all_numbers(*args):
    total = 0
    for num in args:
        total+= num
    print(total)

nums = (1,2,3,4,5,6)
sum_all_numbers(*nums)
