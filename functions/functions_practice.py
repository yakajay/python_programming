def data_details (a, b):
    print(a + b)

data_details(250, 350)

data_details(250 456)

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
