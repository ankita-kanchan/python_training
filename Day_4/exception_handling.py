import sys
try:
    print("str"+5)
except:
    print(sys.exc_info()[0])
    print("you did something wrong!")

print("hello executed code outside try except")

import sys
try:
    print("str"+5)
except Exception as e:
    print(e.__class__)
    print("you did something wrong!")

print("hello executed code outside try except")

#write except for specific exceptions

try:
    #some code
except ValueError:
    #print msg for value error

except (TypeError,NameError):
    #print msg for multiple error

except:
    #print msg for other errors


#try except with else clause

try:
    a=int(input("enter number:"))
    print(a**2)
    #some code
except:
    print("Please enter valid number!")
    #print msg for  error

else:
    print("in else block")
    print(a**3)
    #some code

#try  with Finally 

try:
    a=int(input("enter number:"))
    print(a**2)
    #some code
except:
    print("Please enter valid number!")
    #print msg for  error

finally:
    print("in Finally block")
    
    #some code
