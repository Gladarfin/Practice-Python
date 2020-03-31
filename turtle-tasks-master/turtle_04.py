import turtle

turtle.shape('turtle')
i = 1
for i in range(11):
    turtle.pendown()
    for j in range(4):
        turtle.forward(i*30)
        turtle.left(90)
        j += 1
    turtle.penup()
    turtle.right(90)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(15)
    turtle.left(180)
    i += 1
