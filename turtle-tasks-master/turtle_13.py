import turtle

turtle.shape('turtle')
turtle.speed(100)

def draw_circle(step):
    for i in range(180):
        turtle.forward(step)
        turtle.right(1)

turtle.left(90)
while True:
    draw_circle(1)
    draw_circle(0.2)

