from turtle import *
speed(-1)
colorx = ["blue","red"]

for i in range (4,10,1):
    for j in range (0,i,1):
        forward(100)
        left(360/i)
        color(colorx[j%2])


mainloop()


