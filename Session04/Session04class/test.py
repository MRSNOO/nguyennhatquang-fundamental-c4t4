# food1 = "pizza"
# food2 = "mi"
# food3 = "hamburger"
# food4 = "com"

# list/ array

# menu = ["pizza","mi","hamburger","com","xoi ga"]
# #create

# menu.append("tra sua")
# menu[0]="thit cho"
# print(*menu,sep=",")
# #update
# # print(*menu,sep=", ")   #print ra cac phan tu va co dau phay la seperator
# # print(len(menu))

# food = menu[-1]
# print(food)
for i in range (len(menu)):
     print(menu[i])

# for index, item in enumerate(menu):
#     print(index,item)
# for item in menu:
#     print(item)
menu=["death note", "netflix","teaching","cooking","eating","sleeping"]
# print("*"*50)
 for index,item in enumerate(menu):
     print(index+1,item,sep=". ")
# print("*"*50)
# vitri=int(input("Position want to replace"))
# fav= input("Your favorite replace:")
# menu[vitri-1]=fav
# print("*"*50)
 for index,item in enumerate(menu):
     print(index+1,item,sep=". ")
# print("*"*50)      
# menu.remove("death note")
# a = menu.pop(1)
# print(a)
# del menu[1]
# menu.pop(0)
# menu.remove("cooking ")
from random import*
numbers=[randint(0,1000),randint(0,1000),randint(0,1000),randint(0,1000),randint(0,1000),randint(0,1000)]
sortedlist=[]
while len(numbers)!=0:
    min_num=min(numbers)
    sortedlist.append(min_num)
    numbers.remove(min_num)
print(sortedlist,sep=",")






