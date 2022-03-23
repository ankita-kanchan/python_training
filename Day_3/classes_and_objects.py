#Class

class myClass:
    data="class1"
    def myFunc(self):
        print("Welcome to my class")

#obj_name=class_name()
obj=myClass()

print(obj.data) #using object accessing the variable of class

obj.myFunc()#using object accessing the method of class

#Class with constructor

class myClass:
    data="class1"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myData(self):
        print("my name is {} and i am {} years old! ".format(self.name,self.age))
    def myFunc(self):
        print("Welcome to my class")

p1= myClass("Jae",24) #obj = class(name,age) => class(obj,name,age)

p1.myData() #=> myData(p1)

p2= myClass("Max",27)

p2.myData()

#Class example without constructor

class myClass:
    data="class1"
    def myData(self,name,age):
        self.data="demo"
        print(self.data)
        print("my name is {} and i am {} years old! ".format(name,age))
    def myFunc(self,num):
        print("Welcome to my class",num)

 

p1= myClass() #obj = class(name,age) => class(obj,name,age)

 

p1.myData("Max",27) #=> myData(p1)
p1.myFunc(13)
p2= myClass()
p2.myFunc(16)
p2.myData("Jae",24)

#Single Inheritance
class parent:
    data1="parent class"
    def fuc1(self):
        print("Hello this is parent class")
        print(self.__class__)

class child(parent):
    data2="child class"
    def fuc2(self):
        print("Hello this is child class")
        print(self.__class__)
        
#object of parent class
p=parent()
print(p.data1)
p.fuc1()

#object of child class
c=child()
print(c.data1)
c.fuc1()
print(c.data2)
c.fuc2()

#Multi Level Inheritance
class parent:
    data1="parent class"
    def fuc1(self):
        print("Hello this is parent class")
        print(self.__class__)

class child(parent):
    data2="child class"
    def fuc2(self):
        print("Hello this is child class")
        print(self.__class__)

class finalChild(child):
    data3="Final child class"
    def fuc3(self):
        print("Hello this is Final child class")
        print(self.__class__)

#object of parent class
p=parent()
print(p.data1)
p.fuc1()

#object of child class
c=child()
print(c.data1)
c.fuc1()
print(c.data2)
c.fuc2()


#object of Final child class
f=finalChild()
print(f.data1)
f.fuc1()
print(f.data2)
f.fuc2()
print(f.data3)
f.fuc3()
