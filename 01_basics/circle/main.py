# функция
def area(r: int):
    radius2:int = r * r# r^2
    area = 3.14 * radius2
    return area

def circle_length(rad: int):
    diameter:int = 2 * rad
    circ = 3.14 * diameter
    return circ

radius: int = int(input("Введите радиус:"))

if not(radius > 0):
    print("Некорректный ввод")
    exit(0)


value = area(radius)
length = circle_length(radius)
length2 = circle_length(radius * 2)
print("area: " + str(value))
print("circumeverance: " + str(length))
print("длина окружности двойного радиуса: " + str(length2))