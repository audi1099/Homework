from solution import count_even_digits

# Запрашиваем у пользователя целое положительное число
number = int(input("Введите любое целое число: "))

# Используем функцию для подсчета четных цифр и их суммы
count_even, sum_even = count_even_digits(number)

# Выводим результаты
print(f"Количество четных цифр: {count_even}")
print(f"Сумма четных цифр: {sum_even}")
