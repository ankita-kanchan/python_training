#Polymorphism
#Operator Overloading

#overload comparison op 
class myClass:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self): #print object of class
        return "({} , {})".format(self.x,self.y)
    def __add__(self,other): #self => o1 and other => o2
        x = self.x + other.x 
        y = self.y + other.y
        return myClass(x,y)
    def __gt__(self,other):
        a=self.x+self.y
        b=other.x+other.y
        return a > b


o1=myClass(1,3)
o2=myClass(4,2)
print(o1 + o2)
print(o1 > o2)

#+ => __add__
#- => __sub__
#* => __mul__
#/ => __truediv__
#// => __floordiv__
#% => __mod__
#** => __pow__

