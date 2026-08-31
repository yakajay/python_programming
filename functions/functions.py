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