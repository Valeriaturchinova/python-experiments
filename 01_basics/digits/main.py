a: str = input("Введите число: ")
b: int = int(a)
print(b)
c1 = b // 1000
print(c1)
r1 = b % 1000
print(r1)
c2 = r1 // 100
print(c2)
r2 = r1 % 100
print(r2)
c3 = r2 // 10
print(c3)
c4 = r2 % 10
print(c4)
result = c1 + c2 + c3 + c4
print("Сумма цифр равна " + str(result))

