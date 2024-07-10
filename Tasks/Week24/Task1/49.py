def extract_digit(word):
    for char in word:
        if char.isdigit():
            return int(char)


def sort_words_with_hidden_digit(input_str):
    words = input_string.split()
    sorted_words = sorted(words, key=extract_digit)
    sorted_string = ' '.join(sorted_words)

    return sorted_string


input_string = "adf0dsf sdf1df wer5ew 3vv di1ef"
result = sort_words_with_hidden_digit(input_string)
print(result)







