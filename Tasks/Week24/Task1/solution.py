def extract_digit(word):
    for char in word:
        if char.isdigit():
            return int(char)
    return 0  # Если цифра не найдена, возвращаем 0


def sort_words_with_hidden_digit(input_str):
    words = input_str.split()
    sorted_words = sorted(words, key=extract_digit)
    sorted_string = ' '.join(sorted_words)
    return sorted_string
