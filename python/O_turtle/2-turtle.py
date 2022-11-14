# Draw rainbow Benze
# https://www.geeksforgeeks.org/turtle-programming-python/

from turtle import *
import turtle as tr
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = tr.Pen()
tr.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x//100 + 1)
    t.forward(x)
    t.left(59)
done()