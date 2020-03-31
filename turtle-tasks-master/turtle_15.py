import turtle

turtle.shape('turtle')


def draw_star(vertices):
    angle=vertices // 2 * 360 / vertices
    for i in range(0, vertices, 1):
        turtle.forward(200)
        turtle.right(-angle)

        
turtle.left(180)
draw_star(5)
turtle.penup()
turtle.forward(-210)
turtle.pendown()
draw_star(11)
