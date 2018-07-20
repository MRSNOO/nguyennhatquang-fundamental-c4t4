def staircase(sohang):
    n = sohang - 1
    for i in range(1, sohang):
        print (" " *2* n,("*"+" ")*i,end=" ")
        n -= 1
        print()
    



n1=int(input("so nhap vao "))
staircase(n1)