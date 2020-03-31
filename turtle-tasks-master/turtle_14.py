import turtle

turtle.shape('turtle')
turtle.speed(100)

def draw_circle(step, angle):
    for i in range(180):
        turtle.forward(step)
        turtle.left(angle)

#лицо     
turtle.begin_fill()
draw_circle(3, 2)
turtle.fillcolor('yellow') 
turtle.end_fill()
turtle.fillcolor('black')

#левый глаз
turtle.begin_fill()
turtle.penup()
turtle.goto(-40, 100)
turtle.pendown()
draw_circle(0.5, 2)
turtle.fillcolor('blue') 
turtle.end_fill()
turtle.fillcolor('black')

#правый глаз
turtle.begin_fill()
turtle.penup()
turtle.goto(40, 100)
turtle.pendown()
draw_circle(0.5, 2)
turtle.fillcolor('blue') 
turtle.end_fill()
turtle.fillcolor('black')

#нос
turtle.penup()
turtle.goto(0, 100)
turtle.pendown()
turtle.width(10)
turtle.right(90)
turtle.forward(30)

#рот
turtle.color('red')
turtle.penup()
turtle.goto(45, 70)
turtle.pendown()
draw_circle(0.8, -1)






