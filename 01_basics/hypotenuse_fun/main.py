import math

def hypotenuse(x: int, y: int):
    z2 = x * x + y * y
    z = math.sqrt(z2)
    return z

a: int = int(input("Введите длину первого катета: "))
b: int = int(input("Введите длину второго катета: "))

c: int = hypotenuse(x=a, y=b)
k = hypotenuse(x=3, y=4)

print(k)