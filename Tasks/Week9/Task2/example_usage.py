from solution import number_operations

# Запрашиваем у пользователя число
num = float(input("Введите число: "))

# Вызываем функцию для выполнения операций с числом
result = number_operations(num)

# Выводим результат
print(f"Введенное число: {result['original']}, "
      f"число меньше на 5: {result['minus_5']}, "
      f"число большее на 12.5: {result['plus_12.5']}")
