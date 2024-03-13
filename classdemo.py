class student:
    def getData(self,fname,lname):
        self.f = fname
        self.l = lname
    def putData(self):
        print("First Name : ", self.f)
        print("Last Name : ", self.l)

s1 = student()
s1.getData("Abc", "Xyz")
s1.putData()
