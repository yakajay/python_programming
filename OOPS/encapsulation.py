# Encapsulation

# Encapsulation is the prrocess of restricting access to certain details of an object and exposing only the necessary parts it helps achieve data hiding, ensuring that the internal reperesenataion of an object is hiddedn from the outside world and can only accessed through controlled interfaces.

# Without Encapsulation
# class Bank:

#     account_balance = "15000"

# user = Bank()

# print(user.account_balance)

# Encapsulation

class Bank:

    __account_balance = "55000" # whenever we "__" before the variable the value cannot be accessable

    def __user_account(self):
        print(f"Account balance is {self.__account_balance}")
    def show_balance(self):
        self.__user_account()


b1 = Bank()

# print(b1.__account_balance)

b1.show_balance()
