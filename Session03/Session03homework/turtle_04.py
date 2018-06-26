from turtle import *
shape("turtle")
speed(-1)
sidecolor = ("red","blue","brown","yellow","grey")
for i in range (3,8,1) :
    for j in range (0,i,1) :
        forward(100)
        left(360/i)
        color(sidecolor[i-3])
    
color("grey")
forward(100)

mainloop()
