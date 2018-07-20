def giaithua(n):
    s=1
    for i in range(1,n+1,1):
        s=s*i
    return s    




def rev_sum_giaithua(n):
    s=0
    for i in range(1,n+1,1):
        s=s+i/giaithua(i)
    return s

n=int(input("So nhap vao "))
print(rev_sum_giaithua(n))


