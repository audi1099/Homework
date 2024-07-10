from solution import sum_min_max


def main():
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    c = int(input("Введите третье число: "))
    result = sum_min_max(a, b, c)
    print(f"Сумма наибольшего и наименьшего чисел: {result}")


if __name__ == "__main__":
    main()
