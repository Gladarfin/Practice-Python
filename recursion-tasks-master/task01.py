import sys

rec_depth = 0

def fac(n):
     global rec_depth
     if n == 0:
         return 1
     rec_depth += 1
     return n * fac(n - 1)

        
print(fac(5))
print("Глубина рекурсии: " + str(rec_depth-1))
print("Глубина рекурсии по getrecursionlimit: "+str(sys.getrecursionlimit()))
