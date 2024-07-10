# Описание задачи

## Задача

Написать генератор, который будет возвращать случайные числа в заданном диапазоне.

## Функции в solution.py

### Генератор random_numbers

```python
import random

def random_numbers(start, end):
    while True:
        yield random.randint(start, end)
