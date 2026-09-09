# Higher Order Functions

# filter()

# filter(function, collection)

collection = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def get_even(even):
    return even%2 == 0

# print("Checking for even number", get_even(2))

print_even = filter(get_even, collection)

secone_att = filter(get_even, collection)

print(set(print_even)) # filter function can be consumed only one time
print(list(secone_att))

# map()

# map(cbf, collection)

employees = [
    {"id": 1, "name": "Ajay", "department": "IT", "location": "hyderabad", "salary":25000},
    {"id": 2,"name": "Kumar", "department": "IT", "location": "hyderabad", "salary":35000},
    {"id": 3,"name": "Sravani", "department": "IT", "location": "hyderabad", "salary":45000},
    {"id": 4, "name": "Sai", "department": "IT", "location": "hyderabad", "salary":55000},
    {"id": 5, "name": "Lakshman", "department": "IT", "location": "hyderabad", "salary":6500}
]

def emp_data(item):
    return {"name of the employee": item["name"], "from": item["location"], "salary is": item["salary"]}

emp_output = map(emp_data, employees)

print(list(emp_output)) # once the data is consumed, cannot be consumes again like filter()
print(list(emp_output))