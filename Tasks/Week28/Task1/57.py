# 2. Теперь эта функция может принимать любые начальные координаты. Измените решение и добавьте проверку
# входных данных, отловите возможные ошибки.
def coordinate(start_x, start_y, directions):
    if not isinstance(start_x, int) or not isinstance(start_y, int):
        raise ValueError("Начальные координаты должны быть целыми числами")
    if not isinstance(directions, str):
        raise ValueError("Начальные данные для направлений должны быть строкой")
    x, y = start_x, start_y
    for direction in directions:
        if direction == 'S':
            y -= 1
        elif direction == 'N':
            y += 1
        elif direction == 'W':
            x -= 1
        elif direction == 'E':
            x += 1
    return x, y


try:
    start_x = 0
    start_y = 0
    directions = "SSWE"
    result_coordinate = coordinate(start_x, start_y, directions)
    print("Координата: ", result_coordinate)
except ValueError as ve:
    print("Ошибка:", ve)
except Exception as e:
    print("Произошла ошибка:", e)

