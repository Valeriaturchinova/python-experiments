# Пользователь вводит какое-то число, и если число четное, то его нужно вывести.
# Если число нечетное, то нужно найти ближайшее четное число

number: int = int(input("Введите число: "))
result: int = number % 2
if result == 0 :
    print("Введенное число " + str(number) + " - четное")
else:
    print("Число - нечетное")
    print("Введенное число " + str(number))
    print("Ближайшее четное число: " + str(number + 1))
print("Программа завершена")

