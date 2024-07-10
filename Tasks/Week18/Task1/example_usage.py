from solution import special_number


def main():
    number = input("Введите число: ")
    if special_number(number):
        print(f"Число {number} является специальным.")
    else:
        print(f"Число {number} не является специальным.")


if __name__ == "__main__":
    main()
