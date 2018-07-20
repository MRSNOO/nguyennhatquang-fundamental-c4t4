
def staircase(sohang):
    n = sohang - 1
    count=1
    for i in range(1, sohang):
        if i==(sohang-count):
            print("*")
        print()
        count+=1
    


n1=int(input("so nhap vao "))
for i in range (n1):
    print("*",end=" ")
staircase(n1)