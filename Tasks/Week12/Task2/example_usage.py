from solution import find_shortest_word

# Запрашиваем у пользователя строку
input_string = input("Введите строку: ")

# Используем функцию для нахождения самого короткого слова
shortest_word = find_shortest_word(input_string)

# Выводим результат
print(f"Самое короткое слово в строке: {shortest_word}")
