'''My first user-interactive program in Python! first function requests a name
and makes use of the greet function I already wrote. Wanted to call it from the other file,
but didn't have time to fight with it. I feel like I'm slower at this than everyone else.
Every line is a struggle so far'''

#Function Header
def name_input():
#Function body prompts for name, calls greet function
    name = input('What is your name?\n')
    greet(name)
    return name

#greet recieves the name from name_input and prints it with a greeting
def greet(name):
    print("Hi " + name + ", you're the best!")
    return

name_input();
