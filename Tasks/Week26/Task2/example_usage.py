from solution import even_number_generator


def main():
    start = int(input("Введите начало диапазона: "))
    end = int(input("Введите конец диапазона: "))

    print(f"Четные числа от {start} до {end}:")
    for number in even_number_generator(start, end):
        print(number)


if __name__ == "__main__":
    main()
