def create_tuple_and_print_descending_order():
    # Создаем кортеж с квадратами чисел от 1 до 15
    a = tuple(i ** 2 for i in range(1, 16))

    # Выводим элементы кортежа в порядке убывания
    for element in reversed(a):
        print(element)
