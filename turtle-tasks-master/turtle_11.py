import turtle

turtle.shape('turtle')
turtle.speed(100)

def draw_circle(direction, step):
    angle=2*direction
    for i in range(180):
        turtle.forward(step)
        turtle.left(angle)
        
step=2.0
turtle.left(90)
for i in range(0, 10, 1):
    draw_circle(1, step)
    draw_circle(-1, step)
    step+=0.3
