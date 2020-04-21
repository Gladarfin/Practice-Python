#снежинка Коха

import turtle as tr

tr.shape('turtle')
tr.speed('fastest')
tr.penup()
tr.goto(-200, 100)
tr.pendown()

def koch_curve(sideLength, depth):
    if depth == 0:
        tr.forward(sideLength)
        return
    sideLength /=3.0
    koch_curve(sideLength, depth-1)
    tr.left(60)
    koch_curve(sideLength, depth-1)
    tr.right(120)
    koch_curve(sideLength, depth-1)
    tr.left(60)
    koch_curve(sideLength, depth-1)

length = 400

for i in range(3):
    koch_curve(length, 4)
    tr.right(120)
