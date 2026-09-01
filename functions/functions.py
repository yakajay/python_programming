# Function  "def" before any function is a mandatory, while declaring a function numbers are special characters are now allowed in starting.

def fruits():
    print("Hi, Wlecome to the python")

fruits()


# Built in Functions
# abs(), all(), any(), basestring(), bin(), bool(), bytearray(), callable(), chr(), classmethod(), cmp(), compile(), complex(), delattr(), dict(), dir(), divmod(), enumerate(), eval(), execfile(), file(), filter(), float(), format(), forzenset(), getattr(), globals(), hasattr(), hash(), help(), hex(), id(), input(), int(), isinstance(), issubclass(), iter(), len(), list(), locals(), long(), map(), max(), memoryview(), min(), max(), next(), memoryview(), min(), next(), object(), oct(), open(), ord(), pow(), print(), property(), range(), raw_input(), reduce(), reload(), repr(), reversed(), round(), set(), serattr(), slice(), sorted(), staticmethod(), str(), sum(), super(), tuple(), type(), unichr(), unicode(), vars(), xrange(), zip(), __import__() # these are the default functions in python. 


# Functions with parameteres and aurgements.

def adding_numbers(a, b, c=1, d=10): # values in a function paranthesis is called parameters, it could any number of parametres
    print((a + b)-(c + d)) # it is called an arguments.

adding_numbers(245, 345)
adding_numbers(24, 45)
adding_numbers(8445, 4589, 4563, 4789)

# Return statements in functions

def sample_return():
    print("This is checking")
    return "This is return statement"   # when we write "Return" the execution will stop to that specific line

print(sample_return())
sample_return()

# Arbitary Arguments

# * unpacking operator or splat operator

def see_args(*args):
    print(args)
    print(args[0])
    # args[0] = 55
    print(type(args))

see_args("red", 185, True, {"Mango": "yellow"})


# ** kwargs = keyword arguments

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

def api_func(**kwargs):
    print(kwargs)

for record in data_dict:
    api_func(**record)
    print("This is a message from records", record["title"])