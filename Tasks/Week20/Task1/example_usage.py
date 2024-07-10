from solution import random_number_generator


def main():
    gen = random_number_generator(0, 10)
    for number in gen:
        print(number)


if __name__ == "__main__":
    main()
