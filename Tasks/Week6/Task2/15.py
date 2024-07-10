# Написать функцию, которая принимает на вход два списка чисел одинаковой длины и возвращает
# овый список, содержащий суммы соответствующих элементов этих списков.
def new_list(list_1, list_2):
    if len(list_1) != len(list_2):
        raise ValueError("Длинна списков должна быть одинакова: ")
    return [x + y for x, y in zip(list_1, list_2)]


list_1 = [7, 2, 8]
list_2 = [2, 5, 9]
result = new_list(list_1, list_2)
print(result)
