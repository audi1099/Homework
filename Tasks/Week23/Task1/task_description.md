# Описание задачи

## Задача

Создать Русско-Английский словарь, содержащий 10 слов с переводом.

## Реализация

### Файл solution.py

```python
russian_words = ['Дом', 'машина', 'яблоко', 'кот', 'школа', 'солнце', 'молоко', 'книга', 'вода', 'собака']
english_words = ['House', 'car', 'apple', 'cat', 'school', 'sun', 'milk', 'book', 'water', 'dog']

russian_english_dict = dict(zip(russian_words, english_words))
