# Описание задачи

## Задача

Напишите функцию `count_words_with_more_than_three_vowels(input_string)`, которая принимает на вход строку и возвращает количество слов в этой строке, в которых есть более 3-х гласных (a, e, i, o, u).

## Пример использования

```python
from solution import count_words_with_more_than_three_vowels

# Пример
input_string = "This is a test string with some vowels like aaaeeeiiiioooouuuu"
result = count_words_with_more_than_three_vowels(input_string)
print(f"Количество слов с более чем тремя гласными: {result}")
