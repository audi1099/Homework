# Напишите генератор, который будет возвращать строки из списка слов, разделенных пробелами
def gen(words):
    for word in words:
        yield word
        yield " "


words = 'dhgf', 'ggjhg', 'yguyiuh', 'rytuguyg', 'ghfjhgkj'
for word in gen(words):
    print(word, end="")


