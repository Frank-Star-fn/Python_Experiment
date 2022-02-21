import turtle as t
import math

t.pensize(2)
t.right(90)
t.penup()
t.forward(200)
t.pendown()
t.left(90)

r=200
t.circle(r)

len=r*math.sqrt(3)
t.left(60)
t.forward(len)
t.left(120)
t.forward(len)
t.left(120)
t.forward(len)
