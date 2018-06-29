available = True
shopitems = ["T-shirt","sweater"]
while available:
    action=input("Welcome to our shop, What do you want(C,R,U,D)?")
    if action == "R":
        print("Our items:",*shopitems,sep=",")
    elif action=="C":
        newitem=input("Enter new items:")
        shopitems.append(newitem)
        print("Our items:",*shopitems,sep=",")
    elif action=="U":
        updatepos=int(input("Update position:"))
        newitem2=input("New item?")
        if updatepos>len(shopitems) or updatepos<-len(shopitems) :
            print("Out of range")
        else:
            shopitems[updatepos-1]= newitem2
            print("Our items:",*shopitems,sep=",")
    elif action=="D":
        delpos=int(input("Delete Position:"))
        if delpos>len(shopitems) or delpos<-len(shopitems):
                print("Out of range")
        else:
                del shopitems[delpos-1]
                print("Our items:",*shopitems,sep=",")   
    if len(shopitems)==0 or action=="Out":
        available=False
        



