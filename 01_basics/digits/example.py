# 4 - (1+2) * 2   второе число - сумма 2х последних чисел и умножить на 2
# 54321

example: int = int(input("Введите число:"))
m1 = example // 10000
print(m1)
n1 = example % 10000
print(n1)
m2 = n1 // 1000
print(m2)
n2 = n1 % 1000
print(n2)
m3 = n2 // 100
print(m3)
n3 = n2 % 100
print (n3)
m4 = n3 // 10
print(m4)
m5 = n3 % 10
print(m5)
result = m2 - (m4 + m5) * 2
print("Итоговый результат: " + str(result))