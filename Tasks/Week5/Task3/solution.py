def get_final_coordinate(directions):
    x, y = 0, 0
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
