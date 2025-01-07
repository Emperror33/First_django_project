try:
    print('10+'+10) #VISIT a URL (MOdify Databases)

except TypeError:
    print('You are using wrong data type')
except IOError:
    print('You have I/O Error')    
    print('Did you check the file permissions')
except:
    # Report back to the user
    print("hey you got an error" )   

finally:  #finally is used to run else block even if it is there is na error or not

   # Take them to another page (Refresh)
    print(" Else  block ran")   
  

  # else can be used in place of finally if we dont want to run else kind of block when there is error 
