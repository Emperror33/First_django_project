#dictionaries  allowas us to store data in key-value pairs
#i.e. Matching a unique key to some sort of value

employees = { "chef" : "Deuja", "CEO":"Niraj","IT_man": 25 } # dictionary syntax ,key:value

#lookup info from the dictionary
print(employees["chef"])

# adding new key:value pair (position) on a dictionary
employees["Developer"]="Mishra"
print(employees)

#update key:value pair
print("new chef is")
employees["chef"] = "Adhikari"
print(employees["chef"].upper()) #this is also okay to use)
