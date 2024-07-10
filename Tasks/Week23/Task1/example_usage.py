from solution import russian_english_dict


def main():
    word = input("Введите русское слово: ").strip().capitalize()
    translation = russian_english_dict.get(word)
    if translation:
        print(f"{word} переводится как: {translation}")
    else:
        print("Слово не найдено в словаре.")


if __name__ == "__main__":
    main()
