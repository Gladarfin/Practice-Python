#кривая Минковского

import turtle as tr

tr.shape('turtle')
tr.speed('fastest')
tr.penup()
tr.goto(-200, 100)
tr.pendown()

def minkowski_curve(sideLength, depth):
    if depth == 0:
        tr.forward(sideLength)
        return
    sideLength /= 4.0
    minkowski_curve(sideLength, depth-1)
    tr.left(90)
    minkowski_curve(sideLength, depth-1)
    tr.right(90)
    minkowski_curve(sideLength, depth-1)
    tr.right(90)
    minkowski_curve(sideLength, depth-1)
    minkowski_curve(sideLength, depth-1)
    tr.left(90)
    minkowski_curve(sideLength, depth-1)
    tr.left(90)
    minkowski_curve(sideLength, depth-1)
    tr.right(90)
    minkowski_curve(sideLength, depth-1)

     
length = 700

minkowski_curve(length, 4)
