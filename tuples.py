# tuples are list where the values are immutable i.e. cant be changed.
 # we dont manually define tuples , many functions return tuple when returning results.

mylist =[1,2,3]
mytuple =(1,2,3) # we use () parenthesis in tuples


mylist[0]= "yes"
print(mylist)
print(mytuple)

#but doing mytuples[0]="yes" gives error as tuples are immutable.

#indexing is as same in list.
print(mytuple[1])

# what we cannot do is just re-assignment.