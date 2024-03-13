import math
def exponentiate(num1, num2):
    return math.pow(num1, num2)

def  raise_to_the_fourth_power(given_number):
    return exponentiate(given_number, 4)

square = lambda num: math.pow(num, 2)

cube = lambda num: math.pow(num, 3)

print(square(2))
print(cube(2))
print(raise_to_the_fourth_power(2))


#4
#8
#16