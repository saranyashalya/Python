
class Student:
    def __init__(self):
        self.name = 'Ram'
        self.age = 3
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.age)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.ram = 8

        def show(self):
            print(self.brand, self.ram)


s1 = Student()
s2 = Student()

print(s1.show())
print(s1.lap.brand)

lap1 = s1.lap
lap2 = s2.lap
print(id(lap1))
print(id(lap2))

lap3 = Student.Laptop()
print(lap3.show())