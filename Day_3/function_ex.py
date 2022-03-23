def myFunc():
    print("Hello User!") #Defination
myFunc() #call

# Function with parameters
def add(a,b):
    print(a+b)
    

add(5,6) #call

# Function with Default parameters

def add(a=0,b=0):
    print(a+b) # 5+0
    

add(5) #call

# Function with Return Statement

def add(a=0,b=0):
    print(a+b) # 5+0
    

add(b=1) #call

#Lambda Function

 

# lambda arg : expression

 

#addition 
x = lambda a,b : a+b

 

print(x(5,6))

 

#lamda function to get square of number

 

sq= lambda x: x**2

 

print(sq(23))


#Filter
#filter(function,list)

l=[1,2,3,4,5,6,7,8,9,10]

#filter even values

even_list = filter(lambda x: x%2==0,l)
print(list(even_list))

def check(x):
    if x%2==0:
        return True
    else:
        return False
    
even_list = filter(check,l)
print(list(even_list))

#map
#map(function and list)

l=[1,2,3,4,5,6,7,8,9,10]
op_list = map(lambda x: x**2,l)
print(list(op_list))

def sqrt(x):
    return x**2

op_list = map(sqrt,l)
print(list(op_list))


#Recursive Function

def factorial(x):
    if x==1:
        return x
    else:
        return (x * factorial(x-1))


print(factorial(3)) #3*2*1
