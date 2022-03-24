#Multiple Inheritance
class Parent1:
    data1="parent1"
    def func1(self):
        print("This is a parent 1 class")

class Parent2:
    data2="parent2"
    def func2(self):
        print("This is a parent 2 class")

class child(Parent1,Parent2):
    data3="child"
    def func3(self):
        print("This is a child class")

#object of child class
c=child()
print(c.data1)
print(c.data2)
print(c.data3)
c.func1()
c.func2()
c.func3()

#Hierarchical Inheritance
class Parent:
    data1="parent1"
    def func1(self):
        print("This is a parent 1 class")

class child1(Parent):
    data2="child1"
    def func2(self):
        print("This is a child 1 class")

class child2(Parent):
    data3="child2"
    def func3(self):
        print("This is a child 2 class")

#object of child class
c1=child1()
print(c1.data1)
print(c1.data2)
c2=child2()
print(c2.data1)
print(c2.data3)

#Hybrid Inheritance
class Parent:
    data1="parent1"
    def func1(self):
        print("This is a parent 1 class")

class child1(Parent):
    data2="child1"
    def func2(self):
        print("This is a child 1 class")

class child2(Parent):
    data3="child2"
    def func3(self):
        print("This is a child 2 class")
        
class hybridChild(child1,child2):
    data4="child2"
    def func4(self):
        print("This is a child 2 class")      

#object of child class
c1=child1()
print(c1.data1)
print(c1.data2)
c2=child2()
print(c2.data1)
print(c2.data3)

hc=hybridChild()
print(hc.data1)
print(hc.data2)
print(hc.data3)
print(hc.data4)
