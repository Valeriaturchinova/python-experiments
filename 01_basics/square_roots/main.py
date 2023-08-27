# D = 4
# D_sqrt - это квадратный корень из D
# D_sqrt = math.sqrt(D)

import math
a: int = int(input("Введите a: "))
print(a)
b: int = int(input("Введите b: "))
print(b)
c: int = int(input("Введите c: "))
print(c)

D = b * b - 4 * a * c
print(D)
if D < 0:
    print("Корней нет")
elif D == 0:  
    print("Корень один")
    x = -b / 2 * a
    print("x = " + str(x))
else:
    print("Два корня")
    x1 = (-b + math.sqrt(D)) / 2 * a
    x2 = (-b - math.sqrt(D)) / 2 * a
    print("x1 = " + str(x1))
    print("x2 = " + str(x2))


