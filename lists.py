#It is a data structure in python that can hold elementsin sequence defined by brackets and spaced out by a comma.
a="oman"
my_list= [1,2,3,4,5]

#slicing on the list with indexing
print(my_list) 

print(my_list[2:5])

#appending elements on to the list
my_list.append(a) 
print(my_list)

#inserting elements in particular index of the list
my_list.insert(0, a) # 2 arguments( index , variable)
print(my_list)

#remove item/s from the list
my_list.pop() # remove very last item of the list
my_list.pop(4)
my_list.pop(0)

my_list.reverse()#reverse the list
print(my_list)
my_list.sort() # sorting the list in ascending order
print(my_list)

 
 