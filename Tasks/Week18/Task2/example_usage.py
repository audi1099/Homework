from solution import random_numbers


def main():
    gen = random_numbers(1, 100)
    print(next(gen))
    print(next(gen))
    print(next(gen))


if __name__ == "__main__":
    main()
