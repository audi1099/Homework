from solution import count_words_with_more_than_three_vowels


def main():
    input_string = input("Введите строку: ")
    result = count_words_with_more_than_three_vowels(input_string)
    print(f"Количество слов с более чем тремя гласными: {result}")


if __name__ == "__main__":
    main()
