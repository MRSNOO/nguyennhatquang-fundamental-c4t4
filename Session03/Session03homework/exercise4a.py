def rev_sum(n):
    s=0
    for i in range (1,n+1,1):
        s=s+1/i
    return s



n=int(input("so nhap vao"))
print(rev_sum(n))    