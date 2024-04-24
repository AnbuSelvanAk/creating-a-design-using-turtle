from turtle import *
colors=["red","blue","green","yellow"]
t=Pen()
for x in range(360):
    t.pencolor(colors[x%4])
    t.width(x//100+1)
    t.forward(x)
    t.left(59)