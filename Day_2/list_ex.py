#List

l=[1,2.3,"demo",[5,6,7],("a","b","c")]
print(l)

#Access
print(l[2])
#Nested Indexing
print(l[4][2])
#Negative Indexing
print(l[-1])
#slicing
#val[start:stop:step]
print(l[2::2])

#List Operations

l=[1,2,3]
print(l)

#add element
#list.append(element)
l.append(4)

print(l)

#remove element
#list.remove(element)

l.remove(2)
print(l)

l=["a","b","d"]
print(l)

#insert element
#list.insert(pos,elem)

l.insert(2,"c")
print(l)

#Pop 
print(l.pop()) #removes last element
print(l)

print(l.pop(1)) #removes element at index 1
print(l)

[12:13] Ankita Kanchan
    
l=["a","b","d"]
#update values in list
print(l)


#list[index]=new_val
l[2]="c"
print(l)
 
#list[index]=new_val
l[1:]=["x","y"]
print(l)

#List methods
l=["a","b","d"]

#removing all elements from list
l.clear()
print(l)

#count the frequency
l=["a","b","d"]
print(l.count("b"))

#reverse
l.reverse()
print(l)

#sorting list
l.sort()
print(l)

#Generating a Dynamic List
l=[]
n=int(input("Enter no. elements:"))
for i in range(n):
    elem=input("enter element:")
    l.append(elem)
print(l)


