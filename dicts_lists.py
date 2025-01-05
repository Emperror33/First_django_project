#make use of lists and dictionaries at once , together

stock_prices ={ "META": [200,210,220], "MS":[20,120,300]}


history=stock_prices["META"]
print(f"first day price is:{history}")
print(f"first day initial price is:{history[2]}")  

#nested_dictionaries
mydict= {'OUTER': {'INNER':100}}
print(mydict['OUTER']['INNER'])
 
 # acceesing dict. itmes with methods
mydict1= { 'key1':100, 'key2':200,'key3':400}
print(mydict1.keys())
print(mydict1.values())
print(mydict1.items()) # items make use of  python tuples tuple , as first value is key and 2nd is value , we cant change them
mydict1['key1']=231 # updating items
mydict1['key4']=256 # adding new items

print(mydict1['key1']) #indexing notations 


 