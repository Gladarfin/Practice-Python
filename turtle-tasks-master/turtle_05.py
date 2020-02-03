import turtle

turtle.shape('turtle')
print("Введите количество лапок:",end=' ')
paws=int(input())
i=0
for i in range(paws):
    turtle.forward(120)
    turtle.stamp()
    turtle.left(180)
    turtle.forward(120)
    turtle.left(180)
    turtle.right(360/paws)
print("Ваш паучок готов!")

