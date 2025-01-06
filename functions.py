# Description: This file contains the functions that will be used in the main.py file

def display_info(name):
    return f"Hello World {name}"
r=display_info("Joseph")
print(r) 

def compare_num(num):
    if num>10:
        return print("Greater")
    elif num<10:
        return print("Lesser")
    else:
        return print( "Equal")
compare_num(10)