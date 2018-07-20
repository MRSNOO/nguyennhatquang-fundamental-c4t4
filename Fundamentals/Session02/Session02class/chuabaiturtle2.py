from turtle import *
color("green")
shape("turtle")
speed(-1)
for i in range(10):
    for _ in range(4):
        forward(100+i*10)
        left(90)
    left(20)
    forward(10) 

mainloop()       