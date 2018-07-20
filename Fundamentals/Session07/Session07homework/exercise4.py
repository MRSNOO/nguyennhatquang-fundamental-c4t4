from turtle import *
def draw_square(length,color1): 
    color(color1)
    for i in range(4):
        left(90)
        forward(length)

speed(-1)
for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()

mainloop()