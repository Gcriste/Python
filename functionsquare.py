def square_of_7():
    return 7**2

result = square_of_7()
print(result)


#set a default for power = 2 (if none is provided), but you can ovveride it by specificing the power
def exponent(num,power=2):
    return num ** power

print(exponent(2,3)) #8
print(exponent(3,4)) #81
print(exponent(7)) #49