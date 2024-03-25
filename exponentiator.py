def exponentiate(num1: int, num2: int) -> int:
    '''This function takes two integers and returns the value of num 1 raised to the power of num 2'''
    return num1 ** num2

square = lambda num: exponentiate(num, 2)
cube = lambda num: exponentiate(num, 3)

def  raise_to_the_fourth_power(num: int) -> int:
    '''This function raises the provided int to the fourth power.'''
    return exponentiate(num, 4)


print(square(2))
print(cube(2))
print(raise_to_the_fourth_power(2))
