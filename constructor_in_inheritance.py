class A:
    def __init__(self):
        print("in A init")
    def feature1(self):
        print("Feature 1 working")

class B:
    def __init__(self):
        super().__init__()
        print("in B init")

    def feature2(self):
        print("Feature 2 working")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("in C init")

#Method resolution order. In multiple inheritance, preference is given to the left class first while calling super() or any common function in both super classes
c1 = C()
c1.feature2()

