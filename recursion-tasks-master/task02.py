def fib(n):
    if n in (1,2):
        return 1
    return fib(n-1)+fib(n-2)

print("Введите число до которого вычисляется ряд: ", end=''),
x = int(input())
print(str(x)+"-ое число Фибоначчи="+str(fib(x)))
