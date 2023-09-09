# Реализовать вычисление корней квадратного уравнения через функции:
# 1. Дискриминант, который принимает на вход 3 параметра а,b,c(D = b * b - 4 * a * c)
# return D
# 2. Вычисление корня (x1 = (-b + math.sqrt(D)) / 2 * a) (return x1)
# 3. Вычисление корня (x2 = (-b - math.sqrt(D)) / 2 * a) (return x2)
# 4. Вычиление корня (x = -b / 2 * a) (return x)
# Вычисление корня(4) выполнять, когда D == 0
# Вычисление 2х корней (2,3), выполнять, когда D>0

import math

def calculate_D(a: int, b: int, c: int):
    D = b * b - 4 * a * c
    return D

def calculate_root1(a: int, b: int, D: int):
    x1 = (-b + math.sqrt(D)) / 2 * a
    return x1

def calculate_root2(a: int, b: int, D: int):
    x2 = (-b - math.sqrt(D)) / 2 * a
    return x2

a: int = int(input("Введите первую сторону: "))
b: int = int(input("Введите вторую сторону: "))
c: int = int(input("Введите третью сторону: "))

D = calculate_D(a=a, b=b, c=c)

if D == 0:
    result = calculate_root1(a=a, b=b, D=0)
    print("Корень равен " + str(result))
elif D > 0:
    result1 = calculate_root1(a=a, b=b, D=D)
    result2 = calculate_root2(a=a, b=b, D=D)
    print("x1 = " + str(result1))
    print("x2 = " + str(result2))
else:
    # D < 0 
    print("Корней нет")