#Set
#unique elements
#every element should be immutable(cannot be changed)

#str int float bool tuple  -> set 

#set is mutable -> add and remove elements from set

#Empty set
s=set()
print(s)
print(type(s))

s={1,2,3,4,"abc",(5,6,7),3.14,1}
print(s)


#add values in set
#set.add(elem)
s.add(10)
print(s)

#update => add multiple elements

s.update([8,9],{10,11})
print(s)

#remove elements in set

#Discard
s.discard(100)
print(s)

#remove 
s.remove(10)
print(s)

#pop random element
print(s.pop())

#clear => removing all elements




#Set Operations

a={1,2,3,4,5}
b={4,5,6,7,8}

#Set Union

print(a.union(b))
print(a | b)

#Set Intersection
print(a.intersection(b))
print(a & b)

#Set Difference
print(a.difference(b))
print(a-b)

print(b.difference(a))
print(b-a)

#Set Symmetric Difference
print(a.symmetric_difference(b))
print(a ^ b)

#Frozen Set

fs=frozenset([1,2,3,4])
print(fs)

fs.add(4)



