
#3 types : 1. Instance methods(works on objects) 2, Class methods(works for entire class) 3. static methods (common methods - not specific to class or objects)
#Instance methods 2 types 1. Accessor/get methods 2. mutator/set methods

class Student:

    school = 'PSGR'
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    @classmethod
    def get_school(cls):
        return cls.school

    @staticmethod
    def get_info():
        return 'This is general info'


s1 = Student(30,40,50)
s2 = Student(50,60,70)

print(s1.avg())
print(s2.avg())

print(Student.get_school())

print(Student.get_info())