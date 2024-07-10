# Описание задачи

## Задача

Написать программу, которая сортирует слова в строке по первой найденной в слове цифре.

## Функции в solution.py

### Функция extract_digit

```python
def extract_digit(word):
    for char in word:
        if char.isdigit():
            return int(char)
    return 0  # Если цифра не найдена, возвращаем 0
