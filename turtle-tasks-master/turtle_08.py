import turtle
from math import pi, cos, sin

turtle.shape('turtle')


def regular_polygon(angles):
    for j in range(0, angles, 1):
        turtle.left(360 / angles)
        turtle.forward(10 * angles)


def move_back():
    turtle.penup()
    turtle.forward(5)
    turtle.right(90)
    turtle.forward(5)
    turtle.left(90)
    turtle.pendown()


for i in range(3, 13, 1):
    regular_polygon(i)
    move_back()
