# Напишите функцию, которая принимает на вход строку и возвращает количество
# слов в этой строке, в которых есть более 3-х гласных (a, e, i, o, u)
def count_words_with_more_than_three_vowels(input_string):
    vowels = "aeiou"
    word_count = 0
    words = input_string.split()
    for word in words:
        vowel_count = sum(1 for char in word if char.lower() in vowels)
        if vowel_count > 3:
            word_count += 1
    return word_count


input_string = "rrrrrr ttttt aaayyy  mmmmm bbbbb eeeeee uuuuu"
result = count_words_with_more_than_three_vowels(input_string)
print(f"Слова, более чем с тремя гласными: ", result)

