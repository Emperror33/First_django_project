class Person():
    def __init__(self, fname,lname):
        self.fname=fname
        self.lname=lname
    
    def report(self):
        print(f"I am {self.fname} {self.lname}")

class Company(Person):

    def reveal(self, c_name):
        if c_name=="IBM":
            print('I am an empolyee of IBM')
        else:
            print(self.report())

x= Company("Prashanta", "Deuja")
x.report()
x.reveal("IBM")
