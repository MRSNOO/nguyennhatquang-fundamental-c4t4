low =0
high=100
mid=int((low+high)/2)
sobannghi=70
guess=input("Is {0} your number?".format(50))
loop=True
while loop:
    if guess=="s" :
        high=mid
        mid=int((low+high)/2)
        guess=input("Is{0} your number?".format(mid))
    elif guess=="l":
        low=mid
        mid=int((low+high)/2)
        guess=input("Is{0} your number?".format(mid))
    if guess=="c":
        loop=False
print("I knew it ") 
        
    


        
    
        
