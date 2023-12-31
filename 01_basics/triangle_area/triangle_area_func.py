# Реализовать вычисление площади треугольника через формулу Герона в функции
# Проверку существовании треугольника необходимо осуществить до вызова функции
# 1. вычислить полупериметр (p 14 строчка) 2. вычислить площадь по формуле (15 строчка)
# 3. значение площади вернуть из функции

import math

def calculate_area(x: int, y: int, z: int):
    p = 1/2 * (x+y+z)
    area = math.sqrt(p*(p-x)*(p-y)*(p-z))
    return area

a: int = int(input("Введите первую сторону: "))
b: int = int(input("Введите вторую сторону: "))
c: int = int(input("Введите третью сторону: "))

if (a + b > c) and (a + c > b) and (c + b > a):
    result = calculate_area(x=a,y=b,z=c)
    
    print("Площадь треугольника равна " + str(result))
else:
    print("Такого треугольника не существует")
