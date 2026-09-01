# Scopes
# Global Variables

apple = "red in color" # global variable where we can use in any place in this file

def fruit():
    return "This is fruit output", apple

print(fruit())

def mango():
    return "This is mango function", apple

print(mango())

# Local Variable

def local_var():
    username = "ajay" # local variable
    return "This is local variable output", username

local_var()

print(apple)
# print(username)

# Global Keyword

x = 10

def glo_nums():
    global x # we have declare like this to utlize globbal keyword in a function
    x = x + 5
    print(x)

glo_nums()

# nonlocal keyword

def outer_function():
    x = 10

    def inner_function():
        nonlocal x # when we declare a variable from outer function to inner function we have declare like "nonlocal"
        x += 5
        print("Inner Function, X:", x)

    inner_function()
    print("Outer functionm, X:", x)

# locals() -> function

def frnd():
    name = "sures"
    age = 30
    devel = True
    city = "Hyderabad"

    print(locals()) # when call "locals()" it will print the values inside a function as dictionary
    print(len(locals())) # to get the count, we have to pass it as "len()"
frnd()

# global() -> function
