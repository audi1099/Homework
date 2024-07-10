# Описание задачи

## Задача

Напишите программу, которая запрашивает у пользователя два целых числа `a` и `b`, вычисляет квадраты всех чисел от `a` до `b` (включительно), и выводит список этих квадратов.

## Функция в solution.py

### Функция calculate_squares

```python
def calculate_squares(a, b):
    squares = [i ** 2 for i in range(a, b + 1)]
    return squares
