import turtle as tr

tr.shape('turtle')
tr.speed('fastest')
tr.penup()
tr.goto(-300, 300)
tr.pendown()

def canter_set(x, y, lineLength):
    if lineLength > 1:
        tr.penup()
        tr.goto(x, y)
        tr.pendown()
        tr.forward(lineLength)
        y -=15
        canter_set(x, y, lineLength / 3)
        canter_set(x + lineLength * 2 / 3, y, lineLength / 3)

length = 300
canter_set(-300, 300, length)

tr.penup()
tr.goto(0, 0)
tr.pendown()
