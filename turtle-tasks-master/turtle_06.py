import turtle
from math import pi, cos, sin

turtle.shape('turtle')
i = 0
while True:
    new_coord = i/(2*pi)
    turtle.goto(new_coord*cos(new_coord), new_coord*sin(new_coord))
    i += 1
