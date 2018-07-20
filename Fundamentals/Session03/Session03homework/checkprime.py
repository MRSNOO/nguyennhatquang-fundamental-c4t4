n=int(input("So nhap vao la"))
k=int(n**0.5)
check=0
if n<2:
    print("n is not a prime number")
elif n==2 or n==3 :
    print("n is a prime number")
else:
    for i in range (2,k+1,1):
        if n%i==0:
            print("n is not a prime number")
            check+=1
            break
    if check ==0 :
        print("n is a prime number")

        
        