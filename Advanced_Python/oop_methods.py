class Circle():
    
    pi=3.14
    def __init__ (self ,r=7): # instantiation of class cirlle and r is an attribute of the class ciecle
      
        self.r=r
        
    def area(self):
        return self.r**2*Circle.pi  # self.pi also okay  
    
    def multiply_r(self,m):
        self.r=self.r*m
        print(f'Radius is now :{self.r}')
    

my_c = Circle(r=10)   # calling instance ofa circle
my_c.multiply_r(5)
print(my_c.area())
print(my_c.r)