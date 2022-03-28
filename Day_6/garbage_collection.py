
a=9 #9 is int object

#reference for 9 becomes 0
a=3 # 3 is int object 

import gc

print(gc.get_threshold()) #700

# if number of allocations vs the no. of deallocation is greater than 700
#then automatic garbage collection will run

#invoke manaual garbage collector
collected=gc.collect()

print("garbage collector",collected)


import gc

i=0
def generate_cycle():
    x={} 
    x[i+1]=x 
    print(x)
    
collected=gc.collect()
print("garbage collecter: collected {} objects".format(collected))

print("generating cycle")
for i in range(4):
    generate_cycle()

collected=gc.collect()
print("garbage collecter: collected {} objects".format(collected))


