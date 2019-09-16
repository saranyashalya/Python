#number and types of arguments changes operator overloading
# method overloading -> in a class , 2 methods with same name with different arguments
# method overriding -> in 2 class, 2 methods with same name with same parameters

class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a=None,b=None, c= None):
        s=0
        if a!=None and b!= None and c!=None:
            s = a+b+c
        elif a!= None and b!= None:
            s = a+b
        else:
            s = a
        return s

s1 = Student(9,10)

print(s1.sum(5,4,3))
print(s1.sum(5,4))
print(s1.sum())