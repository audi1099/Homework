# Написать функцию,  которая будет принимать строку из букв "SWEN" в любом порядке
# и количестве, например: "SNNNWEESENSWWWW". Каждая из букв означает направление движения на единичный отрезок по
# координатной прямой (S - вниз, N - вверх, W - влево, E - вправо). За начальную
# координату примите (0,0). При строке равной "SSWE" конечная координата будет равна (0, -2). Функция должна вернуть эту
# координату в виде кортежа.
def coordinate(directions):
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


directions = "SSWE"
coordinate = coordinate(directions)
print("Координата :", coordinate)

