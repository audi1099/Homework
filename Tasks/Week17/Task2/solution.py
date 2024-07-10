def count_words_with_more_than_three_vowels(input_string):
    vowels = "aeiouAEIOU"
    word_count = 0
    words = input_string.split()
    for word in words:
        vowel_count = sum(1 for char in word if char in vowels)
        if vowel_count > 3:
            word_count += 1
    return word_count
