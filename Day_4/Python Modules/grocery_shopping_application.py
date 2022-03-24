#Application
#product: price

import mymodule as mm # import 

shop={"milk":25,"sugar":36,"rice":46,"bread":25}

ch=0
while(ch<5):
    print("-------------- \n",shop)
    print("1.Add Item \n2.Remove Item \n3.Display Bag \n4.Print Bill")
    print("-------------- \n")
    ch= int(input("Enter the Choice:"))
    
    if(ch==1):
        item= input("Enter item to Add in Cart:")
        bag=mm.add(item)
        print("your cart is :",bag)
    elif(ch==2):
        item= input("Enter item to Remove from Cart:")
        bag=mm.remove(item)
        print("your cart is :",bag)
    elif(ch==3):
        bag=mm.display()
        print("your cart is :",bag)
    elif(ch==4):
        mm.bill()
    else:
        print("Invalid Choice")

