def extract_vowel_strings(input_string):
    vowels = "AEIOUaeiou"
    vowel_strings = [i for i in input_string if i in vowels]
    return vowel_strings
