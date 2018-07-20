from random import *
numb= randint(1,100)
count=0
while count<7 :
    guess =int(input("Guess my number 1-100?"))
    if guess > numb:
        print("Too large") 
        count +=1
    elif guess < numb:
        print("Too small") 
        count+=1
    else :
        print("Bingo")

if count==7 :
    print("You Lose")

        

