#кривая Леви

import turtle as tr

tr.shape('turtle')
tr.speed('fastest')
tr.penup()
tr.goto(-150, -50)
tr.pendown()


def levi_curve(sideLength, depth):
    if depth == 0:
        tr.forward(sideLength)
        return
    sideLength /= 1.7
    tr.left(45)
    levi_curve(sideLength, depth - 1)
    tr.right(90)
    levi_curve(sideLength, depth - 1)
    tr.left(45)



    
length = 1000

levi_curve(length, 10)
