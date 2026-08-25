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
