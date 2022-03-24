shop={"milk":{"price":25,"discount":5},"sugar":{"price":36,"discount":5}
      ,"rice":{"price":46,"discount":2},"bread":{"price":25,"discount":3}}
bag={}
def add(item):
    if item in shop.keys():
        bag[item]={"price":shop[item]["price"],"discount":shop[item]["discount"]} #shop["milk"] => 25 :  bag["milk"]=25
        print("Item Found and added in bag!")
    else:
        print("item not found")
    return bag

def remove(item):
    if item in bag.keys():
        bag.pop(item)
        print("Item is Removed!")
    else:
        print("Item not Found in Bag!")
    return bag

def display():
    print(bag)
    
def bill():
    total=0
    for i in bag.keys():
        total=total+(bag[i]["price"]-bag[i]["discount"])
    print("Your Bill is :",total)
    
