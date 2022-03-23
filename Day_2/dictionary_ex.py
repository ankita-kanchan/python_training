#Dictionary

#elem => key : value

d={1:"alex",2:"max",3:"jae"}
print(d)
print(type(d))


#Access
#d[key]
print(d[1])

print(d.get(3))

#remove
print(d.pop(2))
print(d)

#popitem
print(d.popitem())
print(d)

#clear
d.clear()


#Keys => returns list of keys
print(d.keys())

for i in d.keys():
    print(d[i])

#items() => returns list of (key,value)
print(d.items())

for key,val in d.items():
    print(key ,":",val)

d={1:"alex",2:"max",3:"jae"}
print(d)
#update value
d[3]="demo"
print(d)

#add new key: val pair
d[4]="kit"
print(d)

# Dynamic dictionary

d={}
n=int(input("Enter no. of values:"))
for i in range(n):
    rol=int(input("Enter Roll no."))
    name=input("Enter name:")
    d[rol]=name
print(d)
