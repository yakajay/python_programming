# input function with while loop

crt_pwd = "secret123"

attempts = 0

max_attempts = 3

while attempts < max_attempts:
    user_password = input("Enter your password")

    if user_password == crt_pwd:
        print("You are welcome to the page")
    else:
        print("incorrect password")
        attempts += 1

    if attempts == max_attempts:
        print("You have tried max attempts, Please reset your password")
