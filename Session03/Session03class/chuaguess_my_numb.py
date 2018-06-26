from random import *
count = 0 
numb = randint(1,100)
playing=True
while playing:
    guess = int(input("Guess my number 1-100"))
    if guess>numb:
        print("Too large ")
    elif guess<numb:
        print("Too small")
    else:
        print("Bingo")
        break
    count +=1
    if count==7 :
        print("You Lose")
        playing=False
