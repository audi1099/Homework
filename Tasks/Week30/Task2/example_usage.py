from solution import Square


def main():
    square_1 = Square(side_length=9, color="красный")
    print(f"Квадрат со стороной {square_1.side_length} и цветом {square_1.color}")

    perimeter = square_1.calculate_perimeter()
    print("Периметр квадрата =", perimeter)

    area = square_1.calculate_area()
    print("Площадь квадрата =", area)

    print("------------------------------------------------------------------------------------")


if __name__ == "__main__":
    main()
