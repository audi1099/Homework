# Описание задачи

## Задача

Напишите программу, которая запрашивает у пользователя два целых числа `a` и `b`, находит все четные числа в диапазоне от `a` до `b` (включительно) и выводит их список.

## Функция в solution.py

### Функция find_even_numbers

```python
def find_even_numbers(a, b):
    even_numbers = [i for i in range(a, b + 1) if i % 2 == 0]
    return even_numbers
