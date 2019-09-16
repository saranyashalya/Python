#Two types of variables: 1. class/static variables 2. instance variables
# class variables are common for all objects
# instance variables are specific to each objects

class Car:
    wheels = 4

    def __init__(self):
        self.model ="BMW"
        self.mil = 10

c1 = Car()
c2 = Car()

print(c1.model, c1.mil, c1.wheels)
print(c2.model, c2.mil, c2.wheels)

# class variables or static variables is common for all objects. It can be accessed using class name or object name
Car.wheels = 5

print(c1.model, c1.mil, c1.wheels)
print(c2.model, c2.mil, c2.wheels)
