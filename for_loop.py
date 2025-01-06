#  control flow: for loops
#  for loop is used to iterate over a sequence (list, tuple, string) or other iterable objects.
#  Iterating over a sequence is called traversal.
#  Syntax:

a=[1,2,3,4,5]
for i in a:
    print(i) #prints each element of the list a

 # works similarly in tuples and strings

 #working in dictionaries

employees= {'ceo':'John','cfo':'Doe','rm':'Jane'}
for i in employees:
        print(f"The {i} is held by {employees[i]}") #prints each key of the dictionary employees

        # tuples unpacking

        mylist=[(1,2),(3,4),(5,6)] #list of tuples
        for a,b in mylist:
            print(a)
            print(b)