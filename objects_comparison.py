class Person:
    def __init__(self):
        self.name = 'Sara'
        self.age = 20

    def compare(self, other):
        if self.age == other.age:
            print("They are same")
        else:
            print("They are not same")


p1 = Person()
p2 = Person()

p1.compare(p2)

if p1.age == p2.age:
    print("Their ages are same")
else:
    print('Their ages are different')