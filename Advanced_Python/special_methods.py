# python has special built-in pre-defined functions also called dunder methods
class Book:
    def __init__(self,bname,bauthor,bpage):
        self.bname=bname
        self.bauthor=bauthor
        self.bpage=bpage

    def __str__(self):
        return f"{self.bname} is written by {self.bauthor}"
    def __len__(self):
        return self.bpage

    
mybook= Book( "Advanced Python! ", " Sunil Sharma", 208)
print(len(mybook))

