# Определить счастливый билетик. Пример: 123321 - счастливый билет,
# тк 1+2+3 - (3+2+1) = 0, а 123456 - несчастливый билетик.
# Пользователь вводит 6ти значное число и программа говорит счастливый или нет
# boolean
# bool
# 0 == 0
# a cумма первых трех и б сумма оставшихся трех сделать отдельный файл
# Билет счастливый: True

ticket_number: int = int(input("Введите номер билетика: "))
a1 = ticket_number // 100000
print(a1)
b1 = ticket_number % 100000
print(b1)
a2 = b1 // 10000
print(a2)
b2 = b1 % 10000
print(b2)
a3 = b2 // 1000
print(a3)
b3 = b2 % 1000
print(b3)
a4 = b3 // 100
print(a4)
b4 = b3 % 100
print(b4)
a5 = b4 // 10
print(a5)
a6 = b4 % 10
print(a6)
result = a1 + a2 + a3
print(result)
result2 = a4 + a5 + a6
print(result2)

print("Билет счастливый: " + str(result == result2))

# 4 - (1+2) * 2   второе число - сумма 2х последних чисел и умножить на 2
# 54321