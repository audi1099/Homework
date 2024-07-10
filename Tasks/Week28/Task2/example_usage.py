from solution import print_and_count_numbers


def main():
    try:
        x = int(input("Введите число X: "))
        r = int(input("Введите число R (должно быть больше X): "))

        if r <= x:
            raise ValueError("Число R должно быть больше X")

        count = print_and_count_numbers(x, r)
        print("Количество чисел:", count)

    except ValueError as ve:
        print("Ошибка:", ve)
    except Exception as e:
        print("Произошла ошибка:", e)


if __name__ == "__main__":
    main()
