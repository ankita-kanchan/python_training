#range => generates sequence

#range(start,stop,step_size)

print(list(range(10))) # stop

print(list(range(1,6))) #=> 1 2 3 4 5

print(list(range(1,15,2)))

#10 1 reverse range

print(list(range(10,0,-1)))

##even no. seq 2-10
print(list(range(0,11,2)))
##odd no. seq  1-9
print(list(range(1,10,2)))
##reverse odd no. seq
print(list(range(9,0,-2)))
##reverse even no. seq
print(list(range(10,0,-2)))

#break statement
for i in range(5):
    if(i==3):
        print("3 is found")
        break
    print(i)

#continue statement
for i in range(5):
    if(i==3):
        print("3 is found")
        continue
    print(i)

#Nested Loop

for i in range(3):
    print("outer i is :",i,"*")
    for j in range(2):
        print("inner j is:",j)
#Pattern 1
n=4
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()

#pattern 2 
#type 1
n=4
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()
#type 2
n = 4
for i in range(4, 0, -1):
    for j in range(0, i):
        print("* ", end=" ")
    print()

#While Loop
#intialize 
#while(condition):
    #body of while
    #incre

 

i=0
while(i<5):
    print("i is :",i)
    i+=1

#Nested While Loop
i=0
while(i<5):
    print("i is :",i," *")
    j=0
    while(j<2):
        print("j is :",j)
        j+=1
    i+=1
#Break Statement with While Loop
i=0
while(i<5):
    if(i==3):
        print("3 is found")
        break
    print("i is :",i)
    i+=1

#Continue Statement with While Loop
while(i<5):
    if(i==3):
        print("3 is found")
        i+=1
        continue
    print("i is :",i)
    i+=1
