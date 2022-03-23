#Create tuple

t=(1,2,3,4,"str",(5,6,7))
print(t)
print(type(t))

t1=2,3,5,6
print(t1)
print(type(t1))

t=(1,2,3,4,5,(6,7,8))
print(t)
#Access

#indexing

print(t[0])
print(t[1])
print(t[2])

#Nested Index
print(t[5][1])
print(t[5][2])

#Negative index
print(t[-1])
print(t[-3])

#Slicing
#t[start:stop:step]
t=(1,2,3,4,5,6,7,8,9,10)
print(t[3:6])
print(t[:5])
print(t[3::3])

#even
print(t[1::2])
#odd
print(t[::2])

t=("a","b","c")
key=input("enter key to search :")
if key in t:
    print("key is found")
else:
    print("key is not found")

#reverse even
print(t[::-2])
#reverse odd
print(t[-2::-2])
