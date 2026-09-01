def data_details (a, b):
    print(a + b)

data_details(250, 350)


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

