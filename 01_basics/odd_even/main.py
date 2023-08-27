# N % 2 == 0 - четное
# N % 2 == 1 нечетное

n: int=int(input("Введите целое число: "))
result = n % 2 
print(result)
is_even = result == 0
print(is_even)

if is_even:
    print("Введенное число - четное")
else:
    print("Введенное число - нечетное")

# Программа запрашивает возраст пользователя и проверяет можно ли получить права в этом возрасте
# is_ even -true
# else - false