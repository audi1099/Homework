# Описание задачи

## Задача

Создайте генератор `random_numbers(start, end)`, который будет возвращать случайные числа в заданном диапазоне от `start` до `end`.

## Пример использования

```python
from solution import random_numbers

# Пример
gen = random_numbers(1, 100)
print(next(gen))  # Выводится случайное число в диапазоне от 1 до 100
print(next(gen))  # Выводится следующее случайное число
print(next(gen))  # И так далее
