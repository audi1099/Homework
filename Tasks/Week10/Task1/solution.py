def process_string(input_string):
    # Преобразуем строку в список символов
    char_list = list(input_string)

    # Удаляем буквы 'a', 'e', 'u' из списка
    char_list = [char for char in char_list if char not in ['a', 'e', 'u']]

    return char_list
