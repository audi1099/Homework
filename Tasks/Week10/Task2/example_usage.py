from solution import find_min_max

# Запрашиваем у пользователя два числа
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

# Используем функцию для определения наибольшего и наименьшего числа
min_number, max_number = find_min_max(a, b)

# Выводим результат
print(f"Наименьшее число: {min_number}")
print(f"Наибольшее число: {max_number}")