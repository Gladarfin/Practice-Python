import turtle

turtle.shape('turtle')

def draw_circle(direction):
    step=2*direction
    for i in range(180):
        turtle.forward(2)
        turtle.left(step)

for i in range(0, 3, 1):
    draw_circle(1)
    draw_circle(-1)
    turtle.right(60)

