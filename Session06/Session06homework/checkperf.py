numb_in = int(input("Enter your number:"))
s= 0 
for i in range(1,numb_in,1):
    if numb_in %i == 0 :
        s=s+i
if numb_in == s and numb_in > 0 :
    print("{0} is a perfect number".format(numb_in))
else :
    print("{0} is not a perfect number".format(numb_in))


