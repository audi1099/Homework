# Описание задачи

## Задача

Напишите генератор, который будет возвращать случайные числа в заданном диапазоне.

## Пример использования

```python
from solution import random_number_generator

# Пример использования генератора
gen = random_number_generator(0, 10)
for number in gen:
    print(number)
