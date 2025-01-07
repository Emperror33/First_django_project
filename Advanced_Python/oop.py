# Allws programmers to create their own objs that have methods and attributes


# As for much larger scripts of python code , functions /methods  by themselves are not enough for organizationa and repeatability.

# Syntax:

class NameOfClass(): # make use of Camelcase
    def _init_ (self,p1,p2): # self keyword is used to assign these parametrs p1 and p2 to the instance of the calss

        self.p1=p1
        self.p2=p2

    def some_method(self):
        #perform some action
        print(self.p1)    