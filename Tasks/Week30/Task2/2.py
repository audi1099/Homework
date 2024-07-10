# Создайте класс "Квадрат". У него должны быть атрибуты, такие как длина стороны и цвет.
# Также создайте метод "посчитать периметр" и "посчитать площадь".


class Square:
    def __init__(self, side_length, color):
        self.side_length = side_length
        self.color = color

    def calculate_perimeter(self):
        return 4 * self.side_length

    def calculate_area(self):
        return self.side_length ** 2


square_1 = Square(side_length=9, color="красный")
print(f"Квадрат со стороной {square_1.side_length} и цветом {square_1.color}")
perimeter = square_1.calculate_perimeter()
print("Периметр квадрата =", perimeter)
area = square_1.calculate_area()
print("Площадь квадрата =", area)
print("------------------------------------------------------------------------------------")
