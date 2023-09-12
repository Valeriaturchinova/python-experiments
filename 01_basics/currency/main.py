def from_rubles(exchange_rate: float, rubles: int) -> float:
    euros: float = rubles / exchange_rate
    return euros

exchange_rate: float = float(input("Введите курс: "))
rubles: int = int(input("Введите сумму в рублях: "))

euros: float = from_rubles(exchange_rate = exchange_rate, rubles=rubles)
print("По курсу " + str(exchange_rate) + " на " + str(rubles) + " вы купите " + str(euros))

