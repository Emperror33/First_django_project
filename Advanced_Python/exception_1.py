try:
    print('hello')
except:
    print('error!')    # prints hello as there is no any kind of error

    # but 

try:
    print('hello'+10)
except:
    print('error!') # this throws TypeError 