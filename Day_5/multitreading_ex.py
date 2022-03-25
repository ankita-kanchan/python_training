import _thread
import time
def check_thread(name,delay):
    i=0
    while(i<=3):
        time.sleep(delay) # 1ms
        print("running thread is",name) #
        i+=1

    print(name," finished execution")

if __name__=="__main__":
    _thread.start_new_thread(check_thread,("first",1)) #thread 1
    _thread.start_new_thread(check_thread,("second",2)) #thread 2
    _thread.start_new_thread(check_thread,("third",3)) #thread 3



#Threading Module

# 1. define your cass which is extending thread class
#2 . override __init__
#3. override run() method

import time
import threading

class multithreading (threading.Thread):
    def __init__(self,id,name,delay):
        threading.Thread.__init__(self) # overriding 
        self.id=id 
        self.name=name
        self.delay=delay
        
    def run(self):
        check_thread(self.name,self.delay,5)
        print(self.name," has finished the execution!")
        
def check_thread(name,delay,i):
    while(i<=3):
        print(delay)
        time.sleep(delay) # 1ms
        print("running thread is",name) 
        i+=1

    print(name," finished execution")

if __name__=="__main__":
    thread1=multithreading(1,"first thread",1)
    thread2=multithreading(2,"second thread",2)
    thread3=multithreading(3,"third thread",3)

    #start method is going to start thread execution
    thread1.start()
    thread2.start()
    thread3.start()

    #join() will block all other code till the current activities
    thread1.join()
    thread2.join()
    thread3.join()


#synchronizing thread using lock objects
import threading
lock=threading.Lock()

def function1():
    for i in range(5):
        lock.acquire()
        print("lock aquired")
        print("Executing first function")
        lock.release()

def function2():
    for i in range(5):
        lock.acquire()
        print("lock aquired")
        print("Executing seccond function")
        lock.release()

if __name__ =="__main__":
    t1=threading.Thread(target=function1)
    t2=threading.Thread(target=function2)

    t1.start()
    t2.start()

    t1.join()
    t2.join()









    

