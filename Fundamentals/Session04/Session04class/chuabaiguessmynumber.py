print("Guess my number game")
print("Now think of a number(0-100),then press Enter")



print("""
All you have to do is to answer my guess
"c" if my guess is Correct
"s" if my guess is Smaller than your number 
"l" if my guess is larger than your number 




""")
low=0 
high=100
playing =True 


while playing :
    mid=int((low+high)/2)
    ans = input("Is {0} your number?".format(mid).upper())
    if ans =="C":
        print("I knew it")
    elif ans=="S":
        low=mid
    elif ans =="L":
        high=mid
    else:
        playing=False 


