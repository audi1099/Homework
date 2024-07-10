from solution import calculate_squares


def main():
    a = int(input("Введите значение a: "))
    b = int(input("Введите значение b: "))
    squares = calculate_squares(a, b)
    print("Список квадратов чисел от 'a' до 'b':", squares)


if __name__ == "__main__":
    main()
