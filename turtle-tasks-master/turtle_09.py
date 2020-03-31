import turtle
import math

turtle.shape('turtle')


def regular_polygon(sides, side_length):
    for i in range(0, sides, 1):
        turtle.left(360/sides)
        turtle.forward(side_length)


def move_next(angle):
    turtle.right(angle)
    turtle.penup()
    turtle.forward(8)
    turtle.pendown()


radius=10
for i in range(3, 13, 1):
    side_len=2*radius*math.sin(math.pi/i)
    angle=(180-360/i)/2
    turtle.left(angle)

    regular_polygon(i, side_len)
    move_next(angle)
    radius+=8

        
