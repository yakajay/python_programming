def data_details (a, b):
    print(a + b)

data_details(250, 350)

data_details(250, 456)

pwd = "ajay@123"

attempts = 0

max_ats = 5

while attempts < max_ats:
    user_password = input("pls enter your password")

    if user_password == pwd:
        print("welcome to the page")
    else:
        print("In Correct password")
        attempts += 1

    if attempts == max_ats:
        print("Max attempts completed for a day")

def pri_ret():
    print("This is Return statement output")
    return "This is print output"

pri_ret()
print(pri_ret())

def data_s():
    print("This is the correcy value")

data_s()

def sum_data(a, b):
    print( a + b)

sum_data(2345, 2345)

def new_data(a, b, c):
    print((a +b)-c)

new_data(200, 300, 100)


data_dict = [
    {
        "id": 1,
        "title": "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
        "price": 109.95,
        "description": "Your perfect pack for everyday use and walks in the forest. Stash your laptop (up to 15 inches) in the padded sleeve, your everyday",
        "category": "men's clothing",
        "image": "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_t.png",
        "rating": {
        "rate": 3.9,
        "count": 120
        }
    },
    {
        "id": 2,
        "title": "Mens Casual Premium Slim Fit T-Shirts ",
        "price": 22.3,
        "description": "Slim-fitting style, contrast raglan long sleeve, three-button henley placket, light weight & soft fabric for breathable and comfortable wearing. And Solid stitched shirts with round neck made for durability and a great fit for casual fashion wear and diehard baseball fans. The Henley style round neckline includes a three-button placket.",
        "category": "men's clothing",
        "image": "https://fakestoreapi.com/img/71-3HjGNDUL._AC_SY879._SX._UX._SY._UY_t.png",
        "rating": {
        "rate": 4.1,
        "count": 259
        }
    }
]

print(data_dict["title"])