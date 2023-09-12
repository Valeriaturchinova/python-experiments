# Пользователь вводит имя валюты (USD or EUR)
# USD = 100 EUR = 110
# П. вводит кол-во рублей
# Взависимости от имени валюты используем USD или EUR для конвертации
# print("По курсу " + str(exchange_rate) + " на " + str(rubles) + " вы купите " + USD EUR))

def from_rubles(exchange_rate: float, rubles: int) -> float:
    euros: float = rubles / exchange_rate
    return euros

euros: int = 101.75
dollars: int = 94.85
yens: int = 0.64
pounds: int = 118.35
tenge: int = 0.2

currency: str = input("Введите валюту: ")
rubles: int = int(input("Введите сумму в рублях: "))

if currency == "EUR":
    result: float = from_rubles(exchange_rate = euros, rubles=rubles)
    print("По курсу " + str(euros) + " на " + str(rubles) + " вы купите " + str(result) + "EUR")

elif currency == "USD":
    result: float = from_rubles(exchange_rate = dollars, rubles=rubles)
    print("По курсу " + str(dollars) + " на " + str(rubles) + " вы купите " + str(result) + "USD")
    print("IN GOD WE TRUST")
elif currency == "YEN":
    result: float = from_rubles(exchange_rate = yens, rubles=rubles)
    print("По курсу " + str(yens) + " на " + str(rubles) + " вы купите " + str(result) + "YEN")

elif currency == "GBP":
    result: float = from_rubles(exchange_rate = pounds, rubles=rubles)
    print("По курсу " + str(pounds) + " на " + str(rubles) + " вы купите " + str(result) + "GBP")
elif currency == "KZT":
    result: float = from_rubles(exchange_rate = tenge, rubles=rubles)
    print("Валюта Казахстана")
    print("По курсу " + str(tenge) + " на " + str(rubles) + " вы купите " + str(result) + "KZT")
else:
    print("Валюта неизвестна")
   
print("Программа завершена")
# добавить йену и фунт
# курс актуальный

