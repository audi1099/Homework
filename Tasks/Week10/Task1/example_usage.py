from solution import process_string

# Запрашиваем у пользователя строку
input_string = input("Введите строку на английском: ")

# Обрабатываем строку с помощью функции
result_list = process_string(input_string)

# Выводим результат
print("Исходная строка в виде списка:", result_list)
