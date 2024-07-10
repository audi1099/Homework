from solution import even_number_generator


def main():
    gen = even_number_generator(1, 31)
    for number in gen:
        print(number)


if __name__ == "__main__":
    main()
