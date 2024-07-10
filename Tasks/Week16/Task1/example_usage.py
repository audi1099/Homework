from solution import check_leap_year


def main():
    year = int(input("Введите год для проверки: "))
    if check_leap_year(year):
        print(f"{year} - это год высокосный")
    else:
        print(f"{year} - это не год высокосный")


if __name__ == "__main__":
    main()
