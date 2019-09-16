# polymorphism types 1. duck typing 2. operator overloading 3. method overloading 4. method overriding
class Pycharm:
    def execute(self):
        print('Compiling')
        print('Running')

class MyEditor:
    def execute(self):
        print('spell check')
        print('Compiling')
        print('Running')


class Laptop:
    def code(self,ide):
        ide.execute()

p1 = Pycharm()
m1 = MyEditor()
l1 = Laptop()
l1.code(p1)
l1.code(m1)