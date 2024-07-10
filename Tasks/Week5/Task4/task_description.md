# Описание задачи

## Задача

Написать функцию, которая определяет, является ли переданное число простым.

## Пример использования

```python
from solution import is_prime

test_number = 17
if is_prime(test_number):
    print(f"{test_number} - простое число")
else:
    print(f"{test_number} - не простое число")
