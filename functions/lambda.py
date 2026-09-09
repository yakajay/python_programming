#fmt: off = to not to convert the functions from lmbda to normal

# Lamba functions called as anonmyous functions

def user_details(): # regular function types
    user_name = "Ajay"
    phone_number = "123456789"

    print(user_name)
    print(phone_number)
    return user_name + " " + phone_number

print(user_details())

# lambda function

greeting = lambda: "welcome to lambda"

print(greeting())

calc_la = lambda x, y: x + y # taking the arguments and giving a calculation.

print(calc_la(10, 20))

