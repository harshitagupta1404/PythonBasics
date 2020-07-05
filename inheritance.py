"""class A:
    def __init__(self):
        print("In init A")
    def feat1(self):
        print("In f1A")
    def feat2(self):
        print("In f2A")

class B:
    def feat1(self):
        print("In f1B")
    def __init__(self):
        print("In init B")

class C(A,B):
    print("In C")

c=C()"""

class A:
    def __init__(self):
        print("In init A")
    def feat1(self):
        print("In f1A")
    def feat2(self):
        print("In f2A")

class B(A):
    def feat1(self):
        print("In f1B")
    def __init__(self):
        print("In init B")

class C(B):
    def feat1(self):
        print("In f1C")
    def __init__(self):
        super().__init__()
        print("In init C")

class D(C):
    print("In D")

d=D()