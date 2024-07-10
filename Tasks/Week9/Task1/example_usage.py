from solution import sum_even_numbers

# Запрашиваем у пользователя целое число N
N = int(input("Введите целое число N: "))

# Вызываем функцию для вычисления суммы четных чисел от 0 до N
result = sum_even_numbers(N)

# Выводим результат
print(f"Сумма всех четных чисел от 0 до {N} равна: {result}")
