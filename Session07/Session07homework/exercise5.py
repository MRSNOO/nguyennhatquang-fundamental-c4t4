from turtle import *
def draw_star(x,y,length):

    speed(-1)
    color("red")
    penup()
    goto(x,y)
    pendown()

    for i in range(5):
        forward(length)
        right(145)

draw_star(5,5,100)
mainloop()