from random import *  
import evaluate
count = 0
playing = True
while playing:
    x = randint(1,10)
    y = randint(1,10)
    op = ["+","-","*","/"]
    ran_op = choice(op)
    error = [-1,0,1,0,0]
    ran_error = choice(error)
    # error = choice([-1,0,1])

        
    res = evaluate.calc(x,y,ran_op)
    # if ran_op == "+":
    #     res = x + y
    # elif ran_op == "-":
    #     res = x - y
    # elif ran_op == "*":
    #     res = x * y
    # elif ran_op == "/":
    #     res = x / y

    display = res + ran_error

    print("* "*10)
    print("{0} {1} {2} = {3}".format(x,ran_op,y,display))
    print("* "*10)

    ask = input("Y/N? : ").upper()

    if ran_error == 0:
        if ask == "Y":
            print("Yay")
            count += 1
        elif ask == "N":
            playing = False 
            print("You are wrong")
            print("Your Score :", count)
    else:
        if ask == "N":
            print("Yay")
            count += 1
        elif ask == "Y":
            playing = False 
            print("You are wrong")
            print("Your Score :", count)

