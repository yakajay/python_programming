# 23-Aug-2026

name = "Ajay Kumar"

print(name)
print(type(name))

cities = """Hyderabad 
vijayawada
vizag"""

print(cities)
print(type(cities))

x = 10
y = 11.345
z = 3453453345

print(type(x))
print(type(y))
print(type(z))

data_list = [32, "Markapur", 19.92, {"study": "graduation"}]

print(data_list[3])

# Numerci Data Types
 # Int

mumbers = 200

print(mumbers)
print(type(mumbers))

 # Float

mumber = 1234.6465

print(mumber)
print(type(mumber))


 # Complex
mum  = 3+4j

print(mum)
print(type(mum))

# Sequence Data Types

# List - where as these value are mutuable means the values inside a list can be replacable

data_list = [11, True, 2345.67, {"name": "Ajay"}]

print(data_list[3])
print(type(data_list))

data_list[2] = "Sravani"

print(data_list[2])


# Tuple - These values are inmutuable and these value once declared cannot be replaced

new_data = (11, False, {"Captial": "Hyderabad"}, 24524.3536)

print(new_data[2])

# new_data[2] = "Vijayawada"

# Range

number = list(range(0, 999, 89))

print(number)