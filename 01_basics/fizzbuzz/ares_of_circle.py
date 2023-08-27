# Пользователь вводит радиус окружности. Радиус должен быть больше нуля.
# Необходимо вычислить длину окружности (2 * PI * радиус)
# Необходимо вычислить площадь круга (PI * (радиус * радиус))
# Проверить, что площадь круга меньше длины окружности
# 	(Площадь круга больше длины окружности)
# Если площадь круга больше длины окружности и радиус больше 10, то напечатать "белый", иначе "черный"

a: int = int(input("Введите радиус окружности: "))
PI = 3,14
circumference = 2 * PI * a
area_of_circle = PI * a * a
if area_of_circle > circumference:
    print("Площадь круга больше длины окружности")
elif area_of_circle < circumference:
    print("Площадь круга меньше длины окружности")
else:
    print("Площадь круга равна длины окружности")
    
if area_of_circle > circumference and a > 10: 
    print("белый")
else:
    print("черный")