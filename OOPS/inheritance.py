# Inheritance in Python OOP lets one class(child) use features of another class(parent). The child class gets access to the parent's methods and properties, so we can resue code and add new features and it helps organize and aviod repeating code

# Parent can use the child class but child class cannot used by parent class


class Maruti:

    def __init__(self):
        self.model = "Sedan AT"
        self.tyres = "4 wheel drive"
        self.seats = "4"
        self.price = "5 Lakhs"

    def  car_model(self):
        print(f"The model of the car is {self.model}, with {self.tyres} tyres, "
              f"{self.seats} seats and the price of the car is {self.price}")

# car1 = Maruti()
# car1.car_model()

#inheritance

class WagnoR(Maruti): # to use the parent to child

    def __init__(self, color):
        Maruti.__init__(self) # calling because we have to the parent class values to child class
        self.color = color

    def car_color(self):
        print(f"The model of the car is {self.model}, with {self.tyres} tyres, "
              f"{self.seats} seats, the price of the car is {self.price} and the colour is {self.color}")

# new_car = WagnoR()
# new_car.car_model()

new_wagon = WagnoR("green")
new_wagon.car_color()

# Super Method()

class WagnoR(Maruti): # to use the parent to child

    def __init__(self, color):
        super().__init__() # with the help of super we can use the parent to child
        self.color = color

    def car_color(self):
        print(f"The model of the car is {self.model}, with {self.tyres} tyres, "
              f"{self.seats} seats, the price of the car is {self.price} and the colour is {self.color}") 


new_wagon = WagnoR("green")
new_wagon.car_color()