def coordinate(start_x, start_y, directions):
    if not isinstance(start_x, int) or not isinstance(start_y, int):
        raise ValueError("Начальные координаты должны быть целыми числами")
    if not isinstance(directions, str):
        raise ValueError("Направления должны быть представлены строкой")

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
