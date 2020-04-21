#кривая Дракона

import turtle as tr

tr.shape('turtle')
tr.speed('fastest')
tr.penup()
tr.goto(-300, 300)
tr.pendown()

def dragon_curve(sideLength, depth, angle_sign = 1):
    if depth == 0:
        tr.forward(sideLength)
        return
    else: 
        sideLength /= 1.56
        tr.left(45 * angle_sign)
        dragon_curve(sideLength, depth - 1, 1)
        tr.right(90 * angle_sign)
        dragon_curve(sideLength, depth - 1, -1)
        tr.left(45 * angle_sign)

    
length = 20000

dragon_curve(length, 20)


