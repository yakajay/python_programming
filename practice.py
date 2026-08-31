# Variables


a = 10

name = "ajay"

b = 20

print(a + b)
print(name)

# Data Types
#1. Numeric Data Types(int, float, complex)

# int

nums = 200

print(type(nums))

# float

nums_new = 233.3454

print(type(nums_new))

# complex

new_num = 1 +1j

print(type(new_num))

# sequence data types(list, tuple, range)

# list

list_list = ["ajay", "kumar", 23, 23344.455, {"fruit":"orange"}]

print(list_list[0])
print(list_list)
print(list_list[2])
print(list_list[3])
print(list_list[4])
print(type(list_list))

list_list[2] = "hello world" # where the values inside the list are replacable

print(list_list)

# tuple

list_tup = ("ajay", "kumar", 23, 23344.455, {"fruit":"orange"})

print(list_tup[0])
print(list_tup[1])
print(list_tup[2])
print(list_tup[3])
print(list_tup[4])
print(type(list_tup))

# list_tup[2] = "hello world" where the values inside a tuple cannot be changes

# print(list_tup)

# range

list_range = list(range(0, 200, 10))

print(list_range)

# negative values printing witht help of dictionary we can able to print the negative values as well

list_tup = ("ajay", "kumar", 23, 23344.455, {"fruit":"orange"})


print(list_tup[-1])

print(list(range(-20, 0)))

# Mapping Data type = dict

dict_data = {
    "username": "Ajay",
    "email": "ajay@gmail.com",
    "number": "12345679",
    "city": "Hyderabad"
}

print(dict_data) # to print all the values
print(dict_data["username"]) # to print the value inside a dictonary by passing an key.
print(type(dict_data))

# set data types(set, frozenset)

#set

fruits = {"banana", "orange", "mango", 55, False, 55, 55, False} # if we are passing the mutliple same value but when we print the repated value will print only once.

fruits.remove(55) # it will remove all the values where it matches the value that we are passing
fruits.add(100) # it will add the value to the data.

print(fruits)
print(type(fruits))

#frozenset

fruits_fro = frozenset({"banana", "orange", "mango", 55, False, 55, 55, False})

# fruits_fro.add(100) # we cannon add or remove in values in frozenset data.
# fruits_fro.remove(100)

print(fruits_fro)
print(type(fruits_fro))

#boolean data type (bool)

# bool this will print true/false when we pass any condition or number.

print(bool(99))

x = 10
y = 20
print(x<y)

#bytearry

sam_byt = bytearray([100, 200, 30, 40])

sam_byt[2] = 253

print(sam_byt)
print(type(sam_byt))

# none data type

# none

val = None

print(val)
print(type(val))

