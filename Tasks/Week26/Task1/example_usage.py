from solution import find_even_numbers


def main():
    a = int(input("Введите значение a: "))
    b = int(input("Введите значение b: "))
    even_numbers = find_even_numbers(a, b)
    print("Список четных чисел от 'a' до 'b':", even_numbers)


if __name__ == "__main__":
    main()
