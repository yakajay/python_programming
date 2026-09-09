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

# call bacl function => callback functions in python are functions passed as arguments to other functions They are executed when the operation of the function completes.

products = ("mobiles", "laptops", "tablets")

print(products)

def mobile_price():
    print("price of mobile is 15000")

def process_selection(selected_item, product_price):
    if selected_item == "mobiles":
        product_price()

def select_product():
    selected_item = input("select your product: ")
    process_selection(selected_item, mobile_price)
select_product()