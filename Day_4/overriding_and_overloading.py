class a:
    def myfunc(self):
        print('function of class A')
        
class b(a):
    def myfunc(self,x):
        print('function of class B')   

obj = b()

obj.myfunc()
