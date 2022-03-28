#f= open(file,mode)
#r=> open existing file for read operation
#w=> open existing file for write operation
#a => open existing file for append operation(does not override)
#r+ => read and write data => it will not override
#w+ => write and read => it will override
#a+ => to append and read data from file

    
#write operation
f= open("mydata.txt",'w')
f.write("Hello World")
f.write("Hi World")
f.close()


#append Operation
f=open("mydata.txt","a")
f.write("this is append operation")
f.close()

#read Operation
f=open("mydata.txt","r")
print(f.read())
f.close()


#writing file along with with()
with open("mydata.txt",'w') as file:
    file.write(" writing with with() func")

#reading file along with with()
with open("mydata.txt") as file:
    print(file.read())


# Split Function

f=open("mydata.txt",'r')
data=f.readlines()
print(data)
for line in data:
    words=line.split()
    print(words)

print(f.tell()) #get current file position

print(f.seek(0))# brings the cusor to the initial position
