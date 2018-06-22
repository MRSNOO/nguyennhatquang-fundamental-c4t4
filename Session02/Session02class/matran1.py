m=int(input("so hang"))
n=int(input("so cot"))
for i in range(0,m+n,1):
    for i in range (0,m,2):
        for j in range(1,n,2):
            print("*", end=" ")
    print() 
    for i in range(0,n,2):
        for j in range(1,m,2):
            print("o",end=" ")
    print() 
