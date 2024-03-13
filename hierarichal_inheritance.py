class A:
    def getA(self,a):
        self.a=a
    def putA(self):
        print("A : ", self.a) 
class B(A):
    def getB(self,b):
        self.b=b 
    def putB(self):
        print("B : ",self.b)
class C(A):
    def getC(self,c):
        self.c=c 
    def putC(self):
        print("C : ",self.c)

b1 = B()
c1 = C()

b1.getA(10)
b1.getB(20)
c1.getA(30)
c1.getC(40)
b1.putA()
b1.putB()
c1.putA()
c1.putC()
