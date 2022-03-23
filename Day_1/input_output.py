# If else statement
age= int(input("Enter your age:"))

if(age>=18):
    print("You are Eligible")
else:
    print("Please Try after ",18-age," years")
    
# If elif else statement
#calculator
a=int(input("Enter number 1:"))
b=int(input("Enter number 2:"))
print("1.Add \n2.Sub \n3.Multiply \n4.Divide")
op=int(input("Enter the operation that you want to perform:"))
if(op==1):
    print(a+b)
elif(op==2):
    print(a-b)
elif(op==3):
    print(a*b)
elif(op==4):
    print(a/b)
else:
    print("Invalid Operation")

# If elif else statement with nested
#calculator
a=int(input("Enter number 1:"))
b=int(input("Enter number 2:"))
print("1.Add \n2.Sub \n3.Multiply \n4.Divide")
op=int(input("Enter the operation that you want to perform:"))
if(op==1):
    print(a+b)
elif(op==2):
    print(a-b)
elif(op==3):
    print(a*b)
elif(op==4):
    if(b==0):
        print("Please enter a non zero value")
    else:
        print(a/b)
else:
    print("Invalid Operation")

##Multiple Conditions
a=5

if(a>0 and a%2==0):
    print("both condition are true")
else:
    print("not true")
