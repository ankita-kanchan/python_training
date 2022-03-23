# Variable => temp storage

val1 = 5
print(val1)
print(type(val1))

val2=3.15
print(val2)
print(type(val2))

val3="Hello World"
print(val3)
print(type(val3))

val4 =True
print(val4)
print(type(val4))

#Data Type Conversion

#int(),float(),str(),bool()

#int to float
print(float(val1))

#float to int
print(int(val2))

#str to int
a=int('23')
print(a)
print(type(a))

#str to float
a=float('2.789')
print(a)
print(type(a))

#bool to int
print(int(False))

#int to Bool

print(bool(100)) # true
print(bool(34))  #true
print(bool(-1))  #true

print(bool(0)) # false

#implicit Type Conversion

a=23
b=4.5
print(a+b)


