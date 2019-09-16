
## types of inheritance 1. simple inheritance 2. multi level inheritance 3. multiple inheritance

class A:
    def feature1(self):
        print("Feature 1 working")

class B:
    def feature2(self):
        print("Feature 2 working")

class C(B):
    def feature3(self):
        print("Feature 3 working")

class D(A,B):
    def feature4(self):
        print("Feature 4 working")

a1 = A()
b1 = B()
c1 = C()
d1 = D()

print(a1.feature1())
print(b1.feature2())
#print(c1.feature1())
print(d1.feature1())
