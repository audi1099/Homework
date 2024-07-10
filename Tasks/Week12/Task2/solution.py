def find_shortest_word(input_string):
    words = input_string.split()
    shortest_word = min(words, key=len)
    return shortest_word
