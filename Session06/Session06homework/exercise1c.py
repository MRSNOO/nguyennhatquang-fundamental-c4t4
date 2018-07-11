from turtle import *
speed(-1)

for i in range (4) :
    forward(100)
    left(90)
left(90)
forward(100)
right(90)

begin_fill()
color("red")
for i in range (3):
    forward(100)
    left(120)
end_fill()

penup()
right(90)
forward(100)
left(90)
forward(20)
pendown()

begin_fill()
color("blue")
for i in range (2):
    forward(30)
    left(90)
    forward(50)
    left(90)


end_fill()
penup()
forward(50)
left(90)
forward(75)
pendown()
begin_fill()
color("yellow")
for i in range(4):
    forward(20)
    left(90)
end_fill()
mainloop()

