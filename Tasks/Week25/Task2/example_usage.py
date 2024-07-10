from solution import extract_vowel_strings


def main():
    array = input("Введите строку: ")
    vowels_array = extract_vowel_strings(array)
    print("Список строк содержащих только гласные буквы:", vowels_array)


if __name__ == "__main__":
    main()
