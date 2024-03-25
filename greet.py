from Exercise_1 import greet

#Function Header
def name_input():
    '''My first user-interactive program in Python! first function requests a name
    and makes use of the greet function I already wrote.
    Function body prompts for name, calls greet function'''

    name = input('What is your name?\n')
    greet(name)
    return name

name_input();



