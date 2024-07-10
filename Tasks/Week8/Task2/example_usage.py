from solution import gen

# Список слов
words = ['dhgf', 'ggjhg', 'yguyiuh', 'rytuguyg', 'ghfjhgkj']

# Использование генератора для получения строк, разделенных пробелами
for word in gen(words):
    print(word, end="")
