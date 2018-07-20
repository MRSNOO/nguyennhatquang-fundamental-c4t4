from random import choice
from random import *
playing = True
wordlist = ["germany","argentina","spain","portugal"]
while playing :
    word = choice(wordlist)
    letters = list(word)

    loop = True
    while loop:
        rand_char = choice(letters)
        print(rand_char,end="  ")
        letters.remove(rand_char)
        if len(letters) == 0 :
            loop = False
    print()
    ans = input("Your Answer? :")
    if ans == word:
        print("Hura")
        wordlist.remove(word)
    else :
        guess = True
        while guess:
            againans = input("Try Again:")
            if againans == word:
                print("Hura!!!")
                wordlist.remove(word)
                guess = False

    if len(wordlist) == 0 or ans == "out" :
        playing = False
        break

