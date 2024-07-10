from solution import bubble_sort


def main():
    numbers = list(map(int, input("Введите числа через пробел: ").split()))
    sorted_numbers = bubble_sort(numbers)
    print("Отсортированный список:", sorted_numbers)


if __name__ == "__main__":
    main()
