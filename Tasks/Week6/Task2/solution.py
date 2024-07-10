def new_list(list_1, list_2):
    if len(list_1) != len(list_2):
        raise ValueError("Длина списков должна быть одинаковой")
    return [x + y for x, y in zip(list_1, list_2)]
