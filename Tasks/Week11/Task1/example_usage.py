from solution import squares_of_even_divisible_by_5

# Запрашиваем у пользователя натуральное число
n = int(input("Введите натуральное число: "))

# Используем функцию для создания списка квадратов четных чисел, делящихся на 5
result = squares_of_even_divisible_by_5(n)

# Выводим результат
print(f"Список квадратов четных чисел, делящихся на 5 от 1 до {n}:")
print(result)
