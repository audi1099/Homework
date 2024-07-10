def print_odd_index_elements(digits_string):
    digits_list = list(digits_string)
    print("Список цифр:", digits_list)
    odd_index_elements = digits_list[1::2]
    print("Элементы с нечетными индексами:", odd_index_elements)
