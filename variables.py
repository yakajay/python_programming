message = "Hello World!"

print(message)


# declaing a variable sin python "to comment a line in python use the "#" "

username = "Ajay"

print(username)

# Data types

# Text Type = str Strinf

username = "Ajay"

print(type(username)) # String Data Type


phone_number = 9505959888

print(type(phone_number)) # Integer Data Type

cities = '''Hyderabad, 
Secunderabad, 
Vijayawada''' # if we want the print the statement in multiple lines we have to pass like ''' / """ this to print the stament in multi lines

print(cities)

countries = """India,
China,
USA"""

print(countries)

# Numeric Data types = int, float, complex

x = 5   # Int
y = -10.56 # when ever it has a decimal number it consider as float data type.
z = 53465876845636

print(type(x))
print(type(x))
print(type(z))

complex_example = 3+4j # Complex data type example

print(type(complex_example))

# Sequence Data type = list, tuple, range

my_data = [11, "banana", 55.345, True, {"city": "Hyderabad"}]    # this is list data types

print(my_data[4])

my_data[2] = "Ajay Kumar"  # by assigning this new value the value in the dictionary can be replaced. and we can change the any value which mutable

print(my_data[2])

print(type(my_data))

# Tuple. what ever the values inside a tuple object those values cannot be changable

example_tuple = (11, "banana", 55.345, True, {"city": "Hyderabad"})

print("This is the output from tuple", example_tuple[4])

# example_tuple[3] = False

# print("This is the output from tuple", example_tuple[3])

# Range is called a function which can be used in loops

numberofseq = list(range(0,199, 4))   #we should list a mandatory to generate the sequence of numbers by giving the last numner it will divide that number and generate the sequence list.

print(numberofseq)

print(range(200, 213))

my_data = [11, "banana", 55.345, True, {"city": "Hyderabad"}]
my_tupledata = (11, "banana", 55.345, True, {"city": "Hyderabad"})

print("This is the negative output", my_data[-2]) # to print the value based on the negative order
print("This is the negative output", my_tupledata[-3]) 

# Mapping Data Type = dict

data_new = {
    "username": "Ajay Kumar",
    "city": "Hyderabad",
    "phone": 950595888,
    "male": True
}

print("this is the dictonary data type example", data_new["username"])
print("this is the dictonary data type example", data_new["phone"])

# Set Data Type = set, frozenset

# set the values are mutable where the values can be added and removed.

fruits = {"banana", "orange", "mango", 55, False, 55, 55, False} # as these values are not in a order so we cannot fetch the values using order and if the data has a duplicate values but when we print the values it will print only one so it will filter the duplicate values

fruits.add("grapes")    # by using add function to add the values to data. 

fruits.remove(55)   # by using remove function we can able to remove the values in data.

print(fruits) 

# frozenset the values are immutable where the values cannot be added or removed

new_fruits = frozenset({True, 44, 12, "pears", "ajay"})

# new_fruits.add("kumar")
# new_fruits.remove("pears")

print(type(new_fruits))

# Boolean Data Type = bool

print(bool(99))

x = 10

y = 20

print(x<y)  

# Binary Data Type = bytes, bytearray, memoryview

# bytes     the bytes datatype in python represents a sequence of integer, where each integer is in the range 0-255, It cannot directly store strings as its element, but it can store the byte-encoded representation of a string.

sample_bytes = bytes([22, 23, 24, 25]) + b"Ajay" # by mentioning the b and "value", the values cannot be changed once it was defined.

print(type(sample_bytes))
print(sample_bytes[4])

# bytearray             the value can be changed

sam_byt = bytearray([100, 200, 30, 40])

sam_byt[2] = 253

print(sam_byt)
print(type(sam_byt))

# memoryview  is a built in-class that provided a way to access the memory of an object without copying the data. 

# This is particularly useful when working with large datasets.

# the data can be shared to datset 1 to datset 2 for the memory efficiency

# None Data Type = NoneType

abc = None # variable doesnt have a value called a None data type

print(abc)
print(type(abc))

# Operators in Python are special symbools or keywords used to perform operations on variable or values.

# Arthmetic Operators

# Addition(+), Subtraction(-), Multiplication(*), Division(/), Modulus(%), Exponentiation(**), Floor Division(//)

x = 10
y = 20

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y) # "x" value to the power of "y" value
print(x // y) # it is will give the lease value

# Comparison Operators

x = 10
y = 20
 # (==) Equla to returns True is two operands are equal.

print(x==y)

 # (!=) Not Equal to returns True id two operands are not equal.

print(x!=y)

 # (>) Greather Than returns True if left operand is greather than right operand.

print(x>y)

 # (<) Less Than returns True is left operand is smaller than right operand.

print(x<y)

 # (>=) Greater Than or Equal To returns True if left operand is greater than or equal to right operand.

print(x>=y)

 # (<=) Less Than or Equal To retuns Trye if left operand is smaller than or equal to right operand.

print(x<=y)

# Assignment Operators

x = 5 # Basic Assignment operator

a = 10

a = a+20  # addition the value to the variable

a +=30

a = a-1 # to substract the value to the variable

a*=2

a/=2 # Equivalane the value to the variable

print(a) # Multiplication the value to the variable

# Logical Operators
l = True
m = False
# and if both the values are true the the output is true but if any one value was and another was false then the output is false and if bothe values are false then the output is false.

print(l and m)

# or

print(l or y)

# not

print(not y) # to make the flase value to true by using not operator.

# Bitwise Operators

# the value will be stored in bits.

# 0 = 0
# 1 = 1
# 2 = 10
# 3 = 11
# 4 = 100
# 5 = 101
# 6 = 110
# 7 = 111
# 8 = 1000
# 9 = 1001
# 10 = 1010

# Number to Binary

print(bin(0))
print(bin(1))
print(bin(2))
print(bin(3))
print(bin(4))
print(bin(5))
print(bin(6))
print(bin(7))
print(bin(8))
print(bin(9))
print(bin(10))

# Conditional Statements

# if

if 10<20:
    print("yes 10 is less than 20")

# if-else

if 10<20:
    print("true")
else:
    print("false")

#if-elif-else

if 10>20:
    print("Hello World")
elif 45<30:
    print("This is Ajay")
elif 30>40:
    print("This is Yakkali")
else:
    print("This is Kumar")

age = 18

if (age <=18) and (age!=19):
    print("You are not allowed here")

if(age < 18) or (age!=19):
    print("You will be allowed")

if not (age != 19):
    print("This is the place you belongs")
else:
    print("Your are 19 years old")

# Loops         initilization, condition, increment/decrement

# While loop

a = 10

while a < 200:
    print(a)
    a += 10

while a > -20:
    print(a)
    a-= 1

# break

marks = 360

while marks <= 475:
    print(marks)
    if marks == 400:
        break
    marks +=10

# continue  where we can skip the value

nums = 1

while nums < 20:
    nums+=1
    if nums == 12:
        continue
    print(nums)

# for loop

# for var in sequence

city = "hyderabad"

for i in city:
    print(i)

# list

fruitss = ["apple", "banana", "orange", "grapes", 55]

for fruit in fruitss:
    print(fruit)

# tuple

colour = ("red", "blue", "green", "yellow")

for col in colour:
    print(col)

# range

for item in range(5):
    print(item)

# Nested Loop

rows = 10

for i in range(1, rows+1):
    for j in range(1, i+1):
        print("*", end=" ")
    print()

for i in range(rows, 0, -1):
    for j in range(1, i+1):
        print("*", end=" ")
    print()