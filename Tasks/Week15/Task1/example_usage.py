from solution import print_numbers_while


def main():
    number = int(input("Введите целое положительное число: "))
    print("Числа от 0 до", number)
    print_numbers_while(number)


if __name__ == "__main__":
    main()
