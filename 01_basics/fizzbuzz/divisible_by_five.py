# Если число оканчивается на 0 или на 5, то оно делится на 5
# Пользователь вводит число. Необходимо проверить делится ли оно на 5 нацело.

a: int = int(input("Введите число: "))
if a % 10 == 0 or a % 10 == 5:
    print(str(a) + " делится на 5")
else:
    print(str(a) + " не делится на 5")


# Пользователь вводит радиус окружности. Радиус должен быть больше нуля.
# Необходимо вычислить длину окружности (2 * PI * радиус)
# Необходимо вычислить площадь круга (PI * (радиус * радиус))
# Проверить, что площадь круга меньше длины окружности
# 	(Площадь круга больше длины окружности)


# Если площадь круга больше длины окружности и радиус больше 10, то напечатать "белый", иначе "черный"