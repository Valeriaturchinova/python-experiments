import math
a: int = int(input("Введите длину первого катета:"))
b: int = int(input("Введите длину второго катета:"))
a2 = a * a
b2 = b * b
c2 = a2 + b2
print(c2)
c = math.sqrt(c2)
print(c)
print("Длина гипотенузы " + str(c))

# графически изобразить